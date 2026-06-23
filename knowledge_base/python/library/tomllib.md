# `!tomllib` \-\-- Parse TOML files

::: {.module synopsis="Parse TOML files."}
tomllib
:::

**Source code:** `Lib/tomllib`

This module provides an interface for parsing TOML 1.1.0 (Tom\'s Obvious
Minimal Language, [https://toml.io](https://toml.io/en/)). This module
does not support writing TOML.

::: versionadded
3.11 The module was added with support for TOML 1.0.0.
:::

::: versionchanged
3.15 Added TOML 1.1.0 support. See the
`What's New <whatsnew315-tomllib-1-1-0>`
for details.
:::

:::: warning
::: title
Warning
:::

Be cautious when parsing data from untrusted sources. A malicious TOML
string may cause the decoder to consume considerable CPU and memory
resources. Limiting the size of data to be parsed is recommended.
::::

::: seealso
The `Tomli-W package <tomli-w>` is a TOML
writer that can be used in conjunction with this module, providing a
write API familiar to users of the standard library
`marshal` and `pickle` modules.
:::

::: seealso
The `TOML Kit package <tomlkit>` is a
style-preserving TOML library with both read and write capability. It is
a recommended replacement for this module for editing already existing
TOML files.
:::

This module defines the following functions:

::: function
load(fp, /, \*, parse_float=float)

Read a TOML file. The first argument should be a readable and binary
file object. Return a `dict`. Convert
TOML types to Python using this
`conversion table <toml-to-py-table>`.

*parse_float* will be called with the string of every TOML float to be
decoded. By default, this is equivalent to `float(num_str)`. This can be
used to use another datatype or parser for TOML floats (e.g.
`decimal.Decimal`). The callable must
not return a `dict` or a
`list`, else a
`ValueError` is raised.

A `TOMLDecodeError` will be raised on an
invalid TOML document.
:::

::: function
loads(s, /, \*, parse_float=float)

Load TOML from a `str` object. Return a
`dict`. Convert TOML types to Python
using this `conversion table <toml-to-py-table>`. The *parse_float* argument has the same meaning as in
`load`.

A `TOMLDecodeError` will be raised on an
invalid TOML document.
:::

The following exceptions are available:

:::::::::: exception
TOMLDecodeError(msg, doc, pos)

Subclass of `ValueError` with the
following additional attributes:

::: attribute
msg

The unformatted error message.
:::

::: attribute
doc

The TOML document being parsed.
:::

::: attribute
pos

The index of *doc* where parsing failed.
:::

::: attribute
lineno

The line corresponding to *pos*.
:::

::: attribute
colno

The column corresponding to *pos*.
:::

::: versionchanged
3.14 Added the *msg*, *doc* and *pos* parameters. Added the
`msg`, `doc`, `pos`,
`lineno` and `colno` attributes.
:::

::: deprecated
3.14 Passing free-form positional arguments is deprecated.
:::
::::::::::

## Examples

Parsing a TOML file:

    import tomllib

    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)

Parsing a TOML string:

    import tomllib

    toml_str = """
    python-version = "3.11.0"
    python-implementation = "CPython"
    """

    data = tomllib.loads(toml_str)

## Conversion Table

::: {#toml-to-py-table}

  TOML         Python
  ------------ ----------------------------------------------------------
  TOML         dict
  document

  string       str

  integer      int

  float        float (configurable with *parse_float*)

  boolean      bool

  offset       datetime.datetime (`tzinfo` attribute set to an instance
  date-time    of `datetime.timezone`)

  local        datetime.datetime (`tzinfo` attribute set to `None`)
  date-time

  local date   datetime.date

  local time   datetime.time

  array        list

  table        dict

  inline table dict

  array of     list of dicts
  tables

:::