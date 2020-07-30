import re
from io import StringIO
from json import dumps, loads

from _gojsonnet import evaluate_snippet
from hypothesis import HealthCheck, assume, given, settings
from hypothesis_jsonschema import from_schema

from yaml2jsonnet.yaml2jsonnet import convert_yaml

unicode_re = re.compile(r"\\u[d-f]")
trailing_zero_re = re.compile(r"[.]0\b")
sci_number_re = re.compile(r"[1-9]e[+-][1-9]")
too_big_int_re = re.compile(r"[1-9][0-9]{16,}")


@settings(suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow])
@given(obj=from_schema({"type": ["object"]}))
def test_flow_round_trip_single_obj(obj):
    original_json = dumps(obj, sort_keys=True)
    # Jsonnet mangles "\ud800\udc00", so we'll skip some things
    assume(not unicode_re.search(original_json))
    # Python preserves 0.0 and 0, but Jsonnet does not. Transform float to int when it's free
    original_json = trailing_zero_re.sub("", original_json)
    # Python and Jsonnet have different ideas about rendering 1e16
    assume(not sci_number_re.search(original_json))
    # Very large ints aren't preserved by JSON since they become floats
    assume(not too_big_int_re.search(original_json))
    output = StringIO()
    convert_yaml(yaml_data=original_json, output=output, array=False)
    jsonnet_json = evaluate_snippet(src=output.getvalue(), filename="")
    rt_json = dumps(loads(jsonnet_json), sort_keys=True)
    assert original_json == rt_json


@settings(suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow])
@given(arr=from_schema({"type": ["array"]}))
def test_flow_round_trip_single_arr(arr):
    original_json = dumps(arr, sort_keys=True)
    # Jsonnet mangles "\ud800\udc00", so we'll skip some things
    assume(not unicode_re.search(original_json))
    # Python preserves 0.0 and 0, but Jsonnet does not. Transform float to int when it's free
    original_json = trailing_zero_re.sub("", original_json)
    # Python and Jsonnet have different ideas about rendering 1e16
    assume(not sci_number_re.search(original_json))
    # Very large ints aren't preserved by JSON since they become floats
    assume(not too_big_int_re.search(original_json))
    output = StringIO()
    convert_yaml(yaml_data=original_json, output=output, array=False)
    jsonnet_json = evaluate_snippet(src=output.getvalue(), filename="")
    rt_json = dumps(loads(jsonnet_json), sort_keys=True)
    assert original_json == rt_json
