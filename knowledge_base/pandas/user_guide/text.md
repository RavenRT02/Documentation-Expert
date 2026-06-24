::: {#text}
{{ header }}
:::

# Working with text data

::: versionchanged
3.0 The inference and behavior of strings changed significantly in
pandas 3.0. See the `string_migration_guide`.
:::

## Text data types {#text.types}

There are two ways to store text data in pandas:

1.  `StringDtype` extension type.
2.  NumPy `object` dtype.

We recommend using `StringDtype` to
store text data via the alias `dtype="str"` (the default when dtype of
strings is inferred), see below for more details.

Prior to pandas 1.0, `object` dtype was the only option. This was
unfortunate for many reasons:

1.  You can accidentally store a *mixture* of strings and non-strings in
    an `object` dtype array. It\'s better to have a dedicated dtype.
2.  `object` dtype breaks dtype-specific operations like
    `DataFrame.select_dtypes`. There
    isn\'t a clear way to select *just* text while excluding non-text
    but still object-dtype columns.
3.  When reading code, the contents of an `object` dtype array is less
    clear than `'string'`.

When using `StringDtype` with PyArrow as
the storage (see below), users will see large performance improvements
in memory as well as time for certain operations when compared to
`object` dtype arrays. When not using PyArrow as the storage, the
performance of `StringDtype` is about
the same as that of `object`. We expect future enhancements to
significantly increase the performance and lower the memory overhead of
`StringDtype` in this case.

::: versionchanged
3.0

The default when pandas infers the dtype of a collection of strings is
to use `dtype='str'`. This will use `np.nan` as its NA value and be
backed by a PyArrow string array when PyArrow is installed, or backed by
NumPy `object` array when PyArrow is not installed.
:::

::: ipython
python

pd.Series(\[\"a\", \"b\", \"c\"\])
:::

## Specifying `StringDtype` explicitly

When it is desired to explicitly specify the dtype, we generally
recommend using the alias `dtype="str"` if you desire to have `np.nan`
as the NA value or the alias `dtype="string"` if you desire to have
`pd.NA` as the NA value.

::: ipython
python

pd.Series(\[\"a\", \"b\", None\], dtype=\"str\") pd.Series(\[\"a\",
\"b\", None\], dtype=\"string\")
:::

Specifying either alias will also convert non-string data to strings:

::: ipython
python

s = pd.Series(\[\"a\", 2, np.nan\], dtype=\"str\") s type(s\[1\])
:::

or convert from existing pandas data:

::: ipython
python

s1 = pd.Series(\[1, 2, pd.NA\], dtype=\"Int64\") s1 s2 =
s1.astype(\"string\") s2 type(s2\[0\])
:::

However there are four distinct `StringDtype` variants that may be utilized. See
`text.four_string_variants` section below
for details.

## String methods {#text.string_methods}

Series and Index are equipped with a set of string processing methods
that make it easy to operate on each element of the array. Perhaps most
importantly, these methods exclude missing/NA values automatically.
These are accessed via the `str` attribute and generally have names
matching the equivalent (scalar) built-in string methods:

::: ipython
python

s = pd.Series(

: \[\"A\", \"B\", \"C\", \"Aaba\", np.nan, \"dog\", \"cat\"\],
  dtype=\"str\",

) s.str.lower() s.str.upper() s.str.len()
:::

::: ipython
python

idx = pd.Index(\[\" jack\", \"jill \", \" jesse \", \"frank\"\])
idx.str.strip() idx.str.lstrip() idx.str.rstrip()
:::

The string methods on Index are especially useful for cleaning up or
transforming DataFrame columns. For instance, you may have columns with
leading or trailing whitespace:

::: ipython
python

df = pd.DataFrame(

: np.random.randn(3, 2), columns=\[\" Column A \", \" Column B \"\],
  index=range(3),

) df
:::

Since `df.columns` is an Index object, we can use the `.str` accessor

::: ipython
python

df.columns.str.strip() df.columns.str.lower()
:::

These string methods can then be used to clean up the columns as needed.
Here we are removing leading and trailing whitespaces, lower casing all
names, and replacing any remaining whitespaces with underscores:

::: ipython
python

df.columns = df.columns.str.strip().str.lower().str.replace(\" \",
\"\_\") df
:::

:::: note
::: title
Note
:::

If you have a `Series` where lots of elements are repeated (i.e. the
number of unique elements in the `Series` is a lot smaller than the
length of the `Series`), it can be faster to convert the original
`Series` to one of type `category` and then use `.str.<method>` or
`.dt.<property>` on that. The performance difference comes from the fact
that, for `Series` of type `category`, the string operations are done on
the `.categories` and not on each element of the `Series`.

Please note that a `Series` of type `category` with string `.categories`
has some limitations in comparison to `Series` of type string (e.g. you
can\'t add strings to each other: `s + " " + s` won\'t work if `s` is a
`Series` of type `category`). Also, `.str` methods which operate on
elements of type `list` are not available on such a `Series`.
::::

::::: {#text.warn_types}
:::: warning
::: title
Warning
:::

The type of the Series is inferred and is one among the allowed types
(i.e. strings).

Generally speaking, the `.str` accessor is intended to work only on
strings. With very few exceptions, other uses are not supported, and may
be disabled at a later point.
::::
:::::

## Splitting and replacing strings {#text.split}

Methods like `split` return a Series of lists:

::: ipython
python

s2 = pd.Series(\[\"a_b_c\", \"c_d_e\", np.nan, \"f_g_h\"\],
dtype=\"str\") s2.str.split(\"\_\")
:::

Elements in the split lists can be accessed using `get` or `[]`
notation:

::: ipython
python

s2.str.split(\"\_\").str.get(1) s2.str.split(\"\_\").str\[1\]
:::

It is easy to expand this to return a DataFrame using `expand`.

::: ipython
python

s2.str.split(\"\_\", expand=True)
:::

When original `Series` has `StringDtype`, the output columns will all be
`StringDtype` as well.

It is also possible to limit the number of splits:

::: ipython
python

s2.str.split(\"\_\", expand=True, n=1)
:::

`rsplit` is similar to `split` except it works in the reverse direction,
i.e., from the end of the string to the beginning of the string:

::: ipython
python

s2.str.rsplit(\"\_\", expand=True, n=1)
:::

`replace` optionally uses [regular
expressions](https://docs.python.org/3/library/re.html):

::: ipython
python

s3 = pd.Series(

: \[\"A\", \"B\", \"C\", \"Aaba\", \"Baca\", \"\", np.nan, \"CABA\",
  \"dog\", \"cat\"\], dtype=\"str\",

) s3 s3.str.replace(\"\^.a\|dog\", \"XX-XX \", case=False, regex=True)
:::

::: versionchanged
2.0 Single character pattern with `regex=True` will also be treated as
regular expressions:
:::

::: ipython
python

s4 = pd.Series(\[\"a.b\", \".\", \"b\", np.nan, \"\"\], dtype=\"str\")
s4 s4.str.replace(\".\", \"a\", regex=True)
:::

If you want literal replacement of a string (equivalent to
`str.replace`), you can set the optional
`regex` parameter to `False`, rather than escaping each character. In
this case both `pat` and `repl` must be strings:

::: ipython
python

dollars = pd.Series(\[\"12\", \"-\$10\", \"\$10,000\"\], dtype=\"str\")

\# These lines are equivalent dollars.str.replace(r\"-\$\", \"-\",
regex=True) dollars.str.replace(\"-\$\", \"-\", regex=False)
:::

The `replace` method can also take a callable as replacement. It is
called on every `pat` using `re.sub`. The
callable should expect one positional argument (a regex object) and
return a string.

::: ipython
python

\# Reverse every lowercase alphabetic word pat = r\"\[a-z\]+\"

def repl(m):

: return m.group(0)\[::-1\]

pd.Series(\[\"foo 123\", \"bar baz\", np.nan\], dtype=\"str\").str.replace(

: pat, repl, regex=True

)

\# Using regex groups pat = r\"(?P\<one\>w+) (?P\<two\>w+)
(?P\<three\>w+)\"

def repl(m):

: return m.group(\"two\").swapcase()

pd.Series(\[\"Foo Bar Baz\", np.nan\], dtype=\"str\").str.replace(

: pat, repl, regex=True

)
:::

The `replace` method also accepts a compiled regular expression object
from `re.compile` as a pattern. All flags
should be included in the compiled regular expression object.

::: ipython
python

import re

regex_pat = re.compile(r\"\^.a\|dog\", flags=re.IGNORECASE)
s3.str.replace(regex_pat, \"XX-XX \", regex=True)
:::

Including a `flags` argument when calling `replace` with a compiled
regular expression object will raise a `ValueError`.

::: ipython
\@verbatim In \[1\]: s3.str.replace(regex_pat, \'XX-XX \',
flags=re.IGNORECASE)
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
ValueError: case and flags cannot be set when pat is a compiled regex
:::

`removeprefix` and `removesuffix` have the same effect as
`str.removeprefix` and `str.removesuffix` added in [Python
3.9](https://docs.python.org/3/library/stdtypes.html#str.removeprefix):

::: ipython
python

s = pd.Series(\[\"str_foo\", \"str_bar\", \"no_prefix\"\])
s.str.removeprefix(\"str\_\")

s = pd.Series(\[\"foo_str\", \"bar_str\", \"no_suffix\"\])
s.str.removesuffix(\"\_str\")
:::

## Concatenation {#text.concatenate}

There are several ways to concatenate a `Series` or `Index`, either with
itself or others, all based on `~Series.str.cat`, resp. `Index.str.cat`.

### Concatenating a single Series into a string

The content of a `Series` (or `Index`) can be concatenated:

::: ipython
python

s = pd.Series(\[\"a\", \"b\", \"c\", \"d\"\], dtype=\"str\")
s.str.cat(sep=\",\")
:::

If not specified, the keyword `sep` for the separator defaults to the
empty string, `sep=''`:

::: ipython
python

s.str.cat()
:::

By default, missing values are ignored. Using `na_rep`, they can be
given a representation:

::: ipython
python

t = pd.Series(\[\"a\", \"b\", np.nan, \"d\"\], dtype=\"str\")
t.str.cat(sep=\",\") t.str.cat(sep=\",\", na_rep=\"-\")
:::

### Concatenating a Series and something list-like into a Series

The first argument to `~Series.str.cat`
can be a list-like object, provided that it matches the length of the
calling `Series` (or `Index`).

::: ipython
python

s.str.cat(\[\"A\", \"B\", \"C\", \"D\"\])
:::

Missing values on either side will result in missing values in the
result as well, *unless* `na_rep` is specified:

::: ipython
python

s.str.cat(t) s.str.cat(t, na_rep=\"-\")
:::

### Concatenating a Series and something array-like into a Series

The parameter `others` can also be two-dimensional. In this case, the
number of rows must match the lengths of the calling `Series` (or
`Index`).

::: ipython
python

d = pd.concat(\[t, s\], axis=1) s d s.str.cat(d, na_rep=\"-\")
:::

### Concatenating a Series and an indexed object into a Series, with alignment

For concatenation with a `Series` or `DataFrame`, it is possible to
align the indexes before concatenation by setting the `join`-keyword.

::: {.ipython okwarning=""}
python

u = pd.Series(\[\"b\", \"d\", \"a\", \"c\"\], index=\[1, 3, 0, 2\],
dtype=\"str\") s u s.str.cat(u) s.str.cat(u, join=\"left\")
:::

The usual options are available for `join` (one of
`'left', 'outer', 'inner', 'right'`). In particular, alignment also
means that the different lengths do not need to coincide anymore.

::: ipython
python

v = pd.Series(\[\"z\", \"a\", \"b\", \"d\", \"e\"\], index=\[-1, 0, 1,
3, 4\], dtype=\"str\") s v s.str.cat(v, join=\"left\", na_rep=\"-\")
s.str.cat(v, join=\"outer\", na_rep=\"-\")
:::

The same alignment can be used when `others` is a `DataFrame`:

::: ipython
python

f = d.loc\[\[3, 2, 1, 0\], :\] s f s.str.cat(f, join=\"left\",
na_rep=\"-\")
:::

### Concatenating a Series and many objects into a Series

Several array-like items (specifically: `Series`, `Index`, and
1-dimensional variants of `np.ndarray`) can be combined in a list-like
container (including iterators, `dict`-views, etc.).

::: ipython
python

s u s.str.cat(\[u, u.to_numpy()\], join=\"left\")
:::

All elements without an index (e.g. `np.ndarray`) within the passed
list-like must match in length to the calling `Series` (or `Index`), but
`Series` and `Index` may have arbitrary length (as long as alignment is
not disabled with `join=None`):

::: ipython
python

v s.str.cat(\[v, u, u.to_numpy()\], join=\"outer\", na_rep=\"-\")
:::

If using `join='right'` on a list-like of `others` that contains
different indexes, the union of these indexes will be used as the basis
for the final concatenation:

::: ipython
python

u.loc\[\[3\]\] v.loc\[\[-1, 0\]\] s.str.cat(\[u.loc\[\[3\]\],
v.loc\[\[-1, 0\]\]\], join=\"right\", na_rep=\"-\")
:::

## Indexing with `.str`

::: {#text.indexing}
You can use `[]` notation to directly index by position locations. If
you index past the end of the string, the result will be a `NaN`.
:::

::: ipython
python

s = pd.Series(

: \[\"A\", \"B\", \"C\", \"Aaba\", \"Baca\", np.nan, \"CABA\", \"dog\",
  \"cat\"\], dtype=\"str\"

)

s.str\[0\] s.str\[1\]
:::

## Extracting substrings

### Extract first match in each subject (extract) {#text.extract}

The `extract` method accepts a [regular
expression](https://docs.python.org/3/library/re.html) with at least one
capture group.

Extracting a regular expression with more than one group returns a
DataFrame with one column per group.

::: ipython
python

pd.Series(

: \[\"a1\", \"b2\", \"c3\"\], dtype=\"str\",

).str.extract(r\"(\[ab\])(d)\", expand=False)
:::

Elements that do not match return a row filled with `NaN`. Thus, a
Series of messy strings can be \"converted\" into a like-indexed Series
or DataFrame of cleaned-up or more useful strings, without necessitating
`get()` to access tuples or `re.match` objects. The dtype of the result
is always object, even if no match is found and the result only contains
`NaN`.

Named groups like

::: ipython
python

pd.Series(\[\"a1\", \"b2\", \"c3\"\], dtype=\"str\").str.extract(

: r\"(?P\<letter\>\[ab\])(?P\<digit\>d)\", expand=False

)
:::

and optional groups like

::: ipython
python

pd.Series(

: \[\"a1\", \"b2\", \"3\"\], dtype=\"str\",

).str.extract(r\"(\[ab\])?(d)\", expand=False)
:::

can also be used. Note that any capture group names in the regular
expression will be used for column names; otherwise capture group
numbers will be used.

Extracting a regular expression with one group returns a `DataFrame`
with one column if `expand=True`.

::: ipython
python

pd.Series(\[\"a1\", \"b2\", \"c3\"\],
dtype=\"str\").str.extract(r\"\[ab\](d)\", expand=True)
:::

It returns a Series if `expand=False`.

::: ipython
python

pd.Series(\[\"a1\", \"b2\", \"c3\"\],
dtype=\"str\").str.extract(r\"\[ab\](d)\", expand=False)
:::

Calling on an `Index` with a regex with exactly one capture group
returns a `DataFrame` with one column if `expand=True`.

::: ipython
python

s = pd.Series(\[\"a1\", \"b2\", \"c3\"\], \[\"A11\", \"B22\", \"C33\"\],
dtype=\"str\") s s.index.str.extract(\"(?P\<letter\>\[a-zA-Z\])\",
expand=True)
:::

It returns an `Index` if `expand=False`.

::: ipython
python

s.index.str.extract(\"(?P\<letter\>\[a-zA-Z\])\", expand=False)
:::

Calling on an `Index` with a regex with more than one capture group
returns a `DataFrame` if `expand=True`.

::: ipython
python

s.index.str.extract(\"(?P\<letter\>\[a-zA-Z\])(\[0-9\]+)\", expand=True)
:::

It raises `ValueError` if `expand=False`.

::: {.ipython okexcept=""}
python

s.index.str.extract(\"(?P\<letter\>\[a-zA-Z\])(\[0-9\]+)\",
expand=False)
:::

The table below summarizes the behavior of `extract(expand=False)`
(input subject in first column, number of groups in regex in first row)

  -------- --------- ------------
           1 group   \>1 group

  Index    Index     ValueError

  Series   Series    DataFrame
  -------- --------- ------------

### Extract all matches in each subject (extractall)

::: {#text.extractall}
Unlike `extract` (which returns only the first match),
:::

::: ipython
python

s = pd.Series(\[\"a1a2\", \"b1\", \"c1\"\], index=\[\"A\", \"B\",
\"C\"\], dtype=\"str\") s two_groups =
\"(?P\<letter\>\[a-z\])(?P\<digit\>\[0-9\])\" s.str.extract(two_groups,
expand=True)
:::

the `extractall` method returns every match. The result of `extractall`
is always a `DataFrame` with a `MultiIndex` on its rows. The last level
of the `MultiIndex` is named `match` and indicates the order in the
subject.

::: ipython
python

s.str.extractall(two_groups)
:::

When each subject string in the Series has exactly one match,

::: ipython
python

s = pd.Series(\[\"a3\", \"b3\", \"c2\"\], dtype=\"str\") s
:::

then `extractall(pat).xs(0, level='match')` gives the same result as
`extract(pat)`.

::: ipython
python

extract_result = s.str.extract(two_groups, expand=True) extract_result
extractall_result = s.str.extractall(two_groups) extractall_result
extractall_result.xs(0, level=\"match\")
:::

`Index` also supports `.str.extractall`. It returns a `DataFrame` which
has the same result as a `Series.str.extractall` with a default index
(starts from 0).

::: ipython
python

pd.Index(\[\"a1a2\", \"b1\", \"c1\"\]).str.extractall(two_groups)

pd.Series(\[\"a1a2\", \"b1\", \"c1\"\],
dtype=\"str\").str.extractall(two_groups)
:::

## Testing for strings that match or contain a pattern

You can check whether elements contain a pattern:

::: ipython
python

pattern = r\"\[0-9\]\[a-z\]\" pd.Series( \[\"1\", \"2\", \"3a\", \"3b\",
\"03c\", \"4dx\"\], dtype=\"str\", ).str.contains(pattern)
:::

Or whether elements match a pattern:

::: ipython
python

pd.Series(

: \[\"1\", \"2\", \"3a\", \"3b\", \"03c\", \"4dx\"\], dtype=\"str\",

).str.match(pattern)
:::

::: ipython
python

pd.Series(

: \[\"1\", \"2\", \"3a\", \"3b\", \"03c\", \"4dx\"\], dtype=\"str\",

).str.fullmatch(pattern)
:::

:::: note
::: title
Note
:::

The distinction between `match`, `fullmatch`, and `contains` is
strictness: `fullmatch` tests whether the entire string matches the
regular expression; `match` tests whether there is a match of the
regular expression that begins at the first character of the string; and
`contains` tests whether there is a match of the regular expression at
any position within the string.

The corresponding functions in the `re` package for these three match
modes are
[re.fullmatch](https://docs.python.org/3/library/re.html#re.fullmatch),
[re.match](https://docs.python.org/3/library/re.html#re.match), and
[re.search](https://docs.python.org/3/library/re.html#re.search),
respectively.
::::

Methods like `match`, `fullmatch`, `contains`, `startswith`, and
`endswith` take an extra `na` argument so missing values can be
considered True or False:

::: ipython
python

s4 = pd.Series(

: \[\"A\", \"B\", \"C\", \"Aaba\", \"Baca\", np.nan, \"CABA\", \"dog\",
  \"cat\"\], dtype=\"str\"

) s4.str.contains(\"A\", na=False)
:::

## Creating indicator variables {#text.indicator}

You can extract dummy variables from string columns. For example if they
are separated by a `'|'`:

::: ipython
python

s = pd.Series(\\"a\", \"a[\|b\", np.nan,
\"a\|c\"\], dtype=\"str\")
s.str.get_dummies(sep=\"\|\")
:::

String `Index` also supports `get_dummies` which returns a `MultiIndex`.

::: ipython
python

idx = pd.Index(\\"a\", \"a[\|b\", np.nan,
\"a\|c\"\]) idx.str.get_dummies(sep=\"\|\")
:::

See also `~pandas.get_dummies`.

## Behavior differences {#text.differences}

Differences in behavior will be primarily due to the kind of NA value.

### `StringDtype` with `np.nan` NA values

1.  Like `dtype="object"`,
    `string accessor methods<api.series.str>` that return **integer** output will return a NumPy array
    that is either dtype int or float depending on the presence of NA
    values. Methods returning **boolean** output will return a NumPy
    array that is dtype bool, with the value `False` when an NA value is
    encountered.

    ::: ipython
    python

    s = pd.Series(\[\"a\", None, \"b\"\], dtype=\"str\") s
    s.str.count(\"a\") s.dropna().str.count(\"a\")
    :::

    When NA values are present, the output dtype is float64. However
    **boolean** output results in `False` for the NA values.

    ::: ipython
    python

    s.str.isdigit() s.str.match(\"a\")
    :::

2.  Some string methods, like `Series.str.decode`, are not available because the underlying array can
    only contain strings, not bytes.

3.  Comparison operations will return a NumPy array with dtype bool.
    Missing values will always compare as unequal just as
    `np.nan` does.

### `StringDtype` with `pd.NA` NA values

1.  `String accessor methods<api.series.str>` that return **integer** output will always return a
    nullable integer dtype, rather than either int or float dtype
    (depending on the presence of NA values). Methods returning
    **boolean** output will return a nullable boolean dtype.

    ::: ipython
    python

    s = pd.Series(\[\"a\", None, \"b\"\], dtype=\"string\") s
    s.str.count(\"a\") s.dropna().str.count(\"a\")
    :::

    Both outputs are `Int64` dtype. Similarly for methods returning
    boolean values.

    ::: ipython
    python

    s.str.isdigit() s.str.match(\"a\")
    :::

2.  Some string methods, like `Series.str.decode` because the underlying array can only contain strings,
    not bytes.

3.  Comparison operations will return an object with
    `BooleanDtype`, rather than a `bool`
    dtype object. Missing values will propagate in comparison
    operations, rather than always comparing unequal like
    `numpy.nan`.

:::: important
::: title
Important
:::

Everything else that follows in the rest of this document applies
equally to `'str'`, `'string'`, and `object` dtype.
::::

## The four `StringDtype` variants {#text.four_string_variants}

There are four `StringDtype` variants
that are available to users, controlled by the `storage` and `na_value`
parameters of `StringDtype`. At runtime,
these can be checked via the `StringDtype.storage` and `StringDtype.na_value`
attributes.

### Python storage with `np.nan` values

:::: note
::: title
Note
:::

This is the same as `dtype='str'` *when PyArrow is not installed*.
::::

The implementation uses a NumPy object array, which directly stores the
Python string objects, hence why the storage here is called `'python'`.
NA values in this array are represented and behave as `np.nan`.

::: ipython
python

pd.Series(

: \[\"a\", \"b\", None, np.nan, pd.NA\],
  dtype=pd.StringDtype(storage=\"python\", na_value=np.nan)

)
:::

Notice that the last three values are all inferred by pandas as being NA
values, and hence stored as `np.nan`.

### PyArrow storage with `np.nan` values

:::: note
::: title
Note
:::

This is the same as `dtype='str'` *when PyArrow is installed*.
::::

The implementation uses a PyArrow array, however NA values in this array
are represented and behave as `np.nan`.

::: ipython
python

pd.Series(

: \[\"a\", \"b\", None, np.nan, pd.NA\],
  dtype=pd.StringDtype(storage=\"pyarrow\", na_value=np.nan)

)
:::

Notice that the last three values are all inferred by pandas as being NA
values, and hence stored as `np.nan`.

### Python storage with `pd.NA` values

:::: note
::: title
Note
:::

This is the same as `dtype='string'` *when PyArrow is not installed*.
::::

The implementation uses a NumPy object array, which directly stores the
Python string objects, hence why the storage here is called `'python'`.
NA values in this array are represented and behave as `np.nan`.

::: ipython
python

pd.Series(

: \[\"a\", \"b\", None, np.nan, pd.NA\],
  dtype=pd.StringDtype(storage=\"python\", na_value=pd.NA)

)
:::

Notice that the last three values are all inferred by pandas as being NA
values, and hence stored as `pd.NA`.

### PyArrow storage with `pd.NA` values

:::: note
::: title
Note
:::

This is the same as `dtype='string'` *when PyArrow is installed*.
::::

The implementation uses a PyArrow array. NA values in this array are
represented and behave as `pd.NA`.

::: ipython
python

pd.Series(

: \[\"a\", \"b\", None, np.nan, pd.NA\],
  dtype=pd.StringDtype(storage=\"python\", na_value=pd.NA)

)
:::

Notice that the last three values are all inferred by pandas as being NA
values, and hence stored as `pd.NA`.

## Method summary

::: {#text.summary}

  Method                                          Description
  ----------------------------------------------- --------------------------------------------------------
  `~Series.str.cat`

  `~Series.str.split`

  `~Series.str.rsplit`                                    string

  `~Series.str.get`

  `~Series.str.join`                                    separator

  `~Series.str.get_dummies`                                    dummy variables

  `~Series.str.contains`                                    pattern/regex

  `~Series.str.replace`                                    other string or the return value of a callable given the
                                                  occurrence

  `~Series.str.removeprefix`                                    starts with prefix.

  `~Series.str.removesuffix`                                    ends with suffix.

  `~Series.str.repeat`                                    `x * 3`)

  `~Series.str.pad`

  `~Series.str.center`

  `~Series.str.ljust`

  `~Series.str.rjust`

  `~Series.str.zfill`

  `~Series.str.wrap`                                    given width

  `~Series.str.slice`

  `~Series.str.slice_replace`

  `~Series.str.count`

  `~Series.str.startswith`

  `~Series.str.endswith`

  `~Series.str.findall`                                    each string

  `~Series.str.match`                                    as list

  `~Series.str.extract`                                    with one row for each element and one column for each
                                                  regex capture group

  `~Series.str.extractall`                                    with one row for each match and one column for each
                                                  regex capture group

  `~Series.str.len`

  `~Series.str.strip`

  `~Series.str.rstrip`

  `~Series.str.lstrip`

  `~Series.str.partition`

  `~Series.str.rpartition`

  `~Series.str.lower`

  `~Series.str.casefold`

  `~Series.str.upper`

  `~Series.str.find`

  `~Series.str.rfind`

  `~Series.str.index`

  `~Series.str.rindex`

  `~Series.str.capitalize`

  `~Series.str.swapcase`

  `~Series.str.normalize`                                    `unicodedata.normalize`

  `~Series.str.translate`

  `~Series.str.isalnum`

  `~Series.str.isalpha`

  `~Series.str.isdigit`

  `~Series.str.isspace`

  `~Series.str.islower`

  `~Series.str.isupper`

  `~Series.str.istitle`

  `~Series.str.isnumeric`

  `~Series.str.isdecimal`

:::