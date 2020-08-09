=================
yaml2jsonnet
=================


Converts YAML into Jsonnet (specifically targetting YAML for Kubernetes)

Suppose that you have some `YAML`_ that you use for `Kubernetes`_ (either hand-written or output by `Helm`_. Now you'd like to use
`Jsonnet`_ instead, for its fancier templating capabilities. This is a pain, because while YAML->JSON converters are easy to find,
they produce ugly-looking (but valid!) Jsonnet.

The goal of this project is to make the conversion a little easier: transform the YAML into *slightly* prettier Jsonnet, preserving
comments along the way.


------------------
Development Setup
------------------


* Install `Poetry`_
* Install `Pre-commit`_
* Run ``poetry install`` to install dependencies
* Run ``poetry run python -m yaml2jsonnet /path/to/yaml`` to convert a file
* Probably, run ``jsonnetfmt`` on the output, since the only whitespace I provide is newlines



.. _YAML: https://yaml.org/
.. _Helm: https://helm.sh/
.. _Jsonnet: https://jsonnet.org/
.. _Kubernetes: https://kubernetes.io/
.. _Poetry: https://python-poetry.org/
.. _Pre-commit: https://pre-commit.com/
