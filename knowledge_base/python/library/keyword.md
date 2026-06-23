# `!keyword` \-\-- Testing for Python keywords

::: {.module synopsis="Test whether a string is a keyword in Python."}
keyword
:::

**Source code:** `Lib/keyword.py`

This module allows a Python program to determine if a string is a
`keyword <keywords>` or
`soft keyword <soft-keywords>`.

::: function
iskeyword(s)

Return `True` if *s* is a Python `keyword <keywords>`.
:::

::: data
kwlist

Sequence containing all the `keywords <keywords>` defined for the interpreter. If any keywords are defined to
only be active when particular `__future__` statements are in effect, these will be included as well.
:::

:::: function
issoftkeyword(s)

Return `True` if *s* is a Python
`soft keyword <soft-keywords>`.

::: versionadded
3.9
:::
::::

:::: data
softkwlist

Sequence containing all the
`soft keywords <soft-keywords>` defined
for the interpreter. If any soft keywords are defined to only be active
when particular `__future__` statements
are in effect, these will be included as well.

::: versionadded
3.9
:::
::::