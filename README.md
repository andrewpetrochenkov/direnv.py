<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/direnv.svg?longCache=True)](https://pypi.org/project/direnv/)
[![](https://img.shields.io/pypi/v/direnv.svg?maxAge=3600)](https://pypi.org/project/direnv/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/direnv.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/direnv.py/)

#### Installation
```bash
$ [sudo] pip install direnv
```

#### Functions
function|`__doc__`
-|-
`direnv.load(path=None)` |load environment variables depending on the current directory
`direnv.read(path=None)` |return a dictionary with environment variables depending on the current directory

#### Examples
`path/to/parent-folder/current-folder/.envrc`

`path/to/parent-folder/.envrc`

```python
>>> import direnv
>>> direnv.load()
```

#### Links
+   [direnv.net](https://direnv.net/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>