# YAML2Jsonnet: Switch configuration languages

Converts YAML into Jsonnet (specifically targetting YAML for Kubernetes)

Suppose that you have some [YAML][] that you use for [Kubernetes][] (either hand-written or output by [Helm][]. Now you'd like to use
[Jsonnet][] instead, for its fancier templating capabilities. This is a pain, because while YAML->JSON converters are easy to find,
they produce ugly-looking (but valid!) Jsonnet.

YAML2Jsonnet makes the conversion a little easier: it transforms the YAML into *slightly* prettier Jsonnet, preserving
comments along the way.

## Example

A trivial YAML document:

```
---
# simple example
- hello: world
  one: 1
```

Convert it to Jsonnet:

```
$ yaml2jsonnet trivial.yaml | jsonnetfmt - -o trivial.jsonnet
```

(Note that we run the output of yaml2jsonnet through the jsonnet formatter `jsonnetfmt`. This is _strongly_ recommended, since the
raw output of yaml2jsonnet is quite ugly.)

The result:

```
[
  // simple example
  {
    hello: 'world',
    one: 1,
  },
]
```

# Installing

Yaml2Jsonnet expects Python 3.6 or above.

```
pip install yaml2jsonnet
```

Or, as this is meant as a stand-alone tool, you may prefer

```
pipx install yaml2jsonnet
```

## Development

* Install [Poetry]
* Install [Pre-commit]
* Run `poetry install` to install dependencies
* Run `poetry run python -m yaml2jsonnet /path/to/yaml` to convert a file
* Probably, run `jsonnetfmt` on the output, since the only whitespace I provide is newlines


[YAML]: https://yaml.org/
[Helm]: https://helm.sh/
[Jsonnet]: https://jsonnet.org/
[Kubernetes]: https://kubernetes.io/
[Poetry]: https://python-poetry.org/
[Pre-commit]: https://pre-commit.com/
