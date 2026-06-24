::: {#basics}
{{ header }}
:::

# Essential basic functionality

Here we discuss a lot of the essential functionality common to the
pandas data structures. To begin, let\'s create some example objects
like we did in the `10 minutes to pandas <10min>` section:

::: ipython
python

index = pd.date_range(\"1/1/2000\", periods=8) s =
pd.Series(np.random.randn(5), index=\[\"a\", \"b\", \"c\", \"d\",
\"e\"\]) df = pd.DataFrame(np.random.randn(8, 3), index=index,
columns=\[\"A\", \"B\", \"C\"\])
:::

## Head and tail {#basics.head_tail}

To view a small sample of a Series or DataFrame object, use the
`~DataFrame.head` and
`~DataFrame.tail` methods. The default
number of elements to display is five, but you may pass a custom number.

::: ipython
python

long_series = pd.Series(np.random.randn(1000)) long_series.head()
long_series.tail(3)
:::

## Attributes and underlying data {#basics.attrs}

pandas objects have a number of attributes enabling you to access the
metadata.

- **shape**: gives the axis dimensions of the object, consistent with
  ndarray

-

  Axis labels

  : - **Series**: *index* (only axis)
    - **DataFrame**: *index* (rows) and *columns*

Note, **these attributes can be safely assigned to**!

::: ipython
python

df\[:2\] df.columns = \[x.lower() for x in df.columns\] df
:::

pandas objects (`Index`,
`Series`, `DataFrame`) can be thought of as containers for arrays, which hold
the actual data and do the actual computation. For many types, the
underlying array is a `numpy.ndarray`.
However, pandas and 3rd party libraries may *extend* NumPy\'s type
system to add support for custom arrays (see
`basics.dtypes`).

To get the actual data inside a `Index`
or `Series`, use the `.array` property.

::: ipython
python

s.array s.index.array
:::

`~Series.array` will always be an
`~pandas.api.extensions.ExtensionArray`.
The exact details of what an
`~pandas.api.extensions.ExtensionArray`
is and why pandas uses them are a bit beyond the scope of this
introduction. See `basics.dtypes` for
more.

If you know you need a NumPy array, use
`~Series.to_numpy` or
`numpy.asarray`.

::: ipython
python

s.to_numpy() np.asarray(s)
:::

When the Series or Index is backed by an
`~pandas.api.extensions.ExtensionArray`,
`~Series.to_numpy` may involve copying
data and coercing values. See `basics.dtypes` for more.

`~Series.to_numpy` gives some control
over the `dtype` of the resulting `numpy.ndarray`. For example, consider datetimes with timezones. NumPy
doesn\'t have a dtype to represent timezone-aware datetimes, so there
are two possibly useful representations:

1.  An object-dtype `numpy.ndarray` with
    `Timestamp` objects, each with the
    correct `tz`.
2.  A `datetime64[ns]` -dtype `numpy.ndarray`, where the values have been converted to UTC and the
    timezone discarded.

Timezones may be preserved with `dtype=object`:

::: ipython
python

ser = pd.Series(pd.date_range(\"2000\", periods=2, tz=\"CET\"))
ser.to_numpy(dtype=object)
:::

Or thrown away with `dtype='datetime64[ns]'`:

::: ipython
python

ser.to_numpy(dtype=\"datetime64\[ns\]\")
:::

Getting the \"raw data\" inside a `DataFrame` is possibly a bit more complex. When your `DataFrame` only
has a single data type for all the columns,
`DataFrame.to_numpy` will return the
underlying data:

::: ipython
python

df.to_numpy()
:::

If a DataFrame contains homogeneously-typed data, the ndarray can
actually be modified in-place, and the changes will be reflected in the
data structure. For heterogeneous data (e.g. some of the DataFrame\'s
columns are not all the same dtype), this will not be the case. The
values attribute itself, unlike the axis labels, cannot be assigned to.

:::: note
::: title
Note
:::

When working with heterogeneous data, the dtype of the resulting ndarray
will be chosen to accommodate all of the data involved. For example, if
strings are involved, the result will be of object dtype. If there are
only floats and integers, the resulting array will be of float dtype.
::::

In the past, pandas recommended `Series.values` or `DataFrame.values` for
extracting the data from a Series or DataFrame. You\'ll still find
references to these in old code bases and online. Going forward, we
recommend avoiding `.values` and using `.array` or `.to_numpy()`.
`.values` has the following drawbacks:

1.  When your Series contains an
    `extension type <extending.extension-types>`, it\'s unclear whether `Series.values` returns a NumPy array or the extension array.
    `Series.array` will always return an
    `~pandas.api.extensions.ExtensionArray`, and will never copy data.
    `Series.to_numpy` will always return
    a NumPy array, potentially at the cost of copying / coercing values.
2.  When your DataFrame contains a mixture of data types,
    `DataFrame.values` may involve
    copying data and coercing values to a common dtype, a relatively
    expensive operation. `DataFrame.to_numpy`, being a method, makes it clearer that the returned
    NumPy array may not be a view on the same data in the DataFrame.

## Accelerated operations {#basics.accelerate}

pandas has support for accelerating certain types of binary numerical
and boolean operations using the `numexpr` library and the `bottleneck`
libraries.

These libraries are especially useful when dealing with large data sets,
and provide large speedups. `numexpr` uses smart chunking, caching, and
multiple cores. `bottleneck` is a set of specialized cython routines
that are especially fast when dealing with arrays that have `nans`.

You are highly encouraged to install both libraries. See the section
`Recommended Dependencies <install.recommended_dependencies>` for more installation info.

These are both enabled to be used by default, you can control this by
setting the options:

``` python
pd.set_option("compute.use_bottleneck", False)
pd.set_option("compute.use_numexpr", False)
```

## Flexible binary operations {#basics.binop}

With binary operations between pandas data structures, there are two key
points of interest:

- Broadcasting behavior between higher- (e.g. DataFrame) and
  lower-dimensional (e.g. Series) objects.
- Missing data in computations.

We will demonstrate how to manage these issues independently, though
they can be handled simultaneously.

### Matching / broadcasting behavior

DataFrame has the methods `~DataFrame.add`, `~DataFrame.sub`,
`~DataFrame.mul`,
`~DataFrame.div` and related functions
`~DataFrame.radd`,
`~DataFrame.rsub`, \... for carrying out
binary operations. For broadcasting behavior, Series input is of primary
interest. Using these functions, you can use to either match on the
*index* or *columns* via the **axis** keyword:

::: ipython
python

df = pd.DataFrame(

:

  {

  : \"one\": pd.Series(np.random.randn(3), index=\[\"a\", \"b\",
    \"c\"\]), \"two\": pd.Series(np.random.randn(4), index=\[\"a\",
    \"b\", \"c\", \"d\"\]), \"three\": pd.Series(np.random.randn(3),
    index=\[\"b\", \"c\", \"d\"\]),

  }

) df row = df.iloc\[1\] column = df\[\"two\"\]

df.sub(row, axis=\"columns\") df.sub(row, axis=1)

df.sub(column, axis=\"index\") df.sub(column, axis=0)
:::

Furthermore you can align a level of a MultiIndexed DataFrame with a
Series.

::: ipython
python

dfmi = df.copy() dfmi.index = pd.MultiIndex.from_tuples( \[(1, \"a\"),
(1, \"b\"), (1, \"c\"), (2, \"a\")\], names=\[\"first\", \"second\"\] )
dfmi.sub(column, axis=0, level=\"second\")
:::

When operating with a plain Python list, pandas aligns it to the
**columns** of the DataFrame (not the rows); to broadcast row-wise, pass
`axis=0` to the explicit method, e.g. `df.add([1, 2, 3], axis=0)`.

Series and Index also support the `divmod` builtin. This function takes the floor division and modulo
operation at the same time returning a two-tuple of the same type as the
left hand side. For example:

::: ipython
python

s = pd.Series(np.arange(10)) s div, rem = divmod(s, 3) div rem

idx = pd.Index(np.arange(10)) idx div, rem = divmod(idx, 3) div rem
:::

We can also do elementwise `divmod`:

::: ipython
python

div, rem = divmod(s, \[2, 2, 3, 3, 4, 4, 5, 5, 6, 6\]) div rem
:::

### Missing data / operations with fill values

In Series and DataFrame, the arithmetic functions have the option of
inputting a *fill_value*, namely a value to substitute when at most one
of the values at a location are missing. For example, when adding two
DataFrame objects, you may wish to treat NaN as 0 unless both DataFrames
are missing that value, in which case the result will be NaN (you can
later replace NaN with some other value using `fillna` if you wish).

::: ipython
python

df2 = df.copy() df2.loc\[\"a\", \"three\"\] = 1.0 df df2 df + df2
df.add(df2, fill_value=0)
:::

### Flexible comparisons {#basics.compare}

Series and DataFrame have the binary comparison methods `eq`, `ne`,
`lt`, `gt`, `le`, and `ge` whose behavior is analogous to the binary
arithmetic operations described above:

::: ipython
python

df.gt(df2) df2.ne(df)
:::

These operations produce a pandas object of the same type as the
left-hand-side input that is of dtype `bool`. These `boolean` objects
can be used in indexing operations, see the section on
`Boolean indexing<indexing.boolean>`.

### Boolean reductions {#basics.reductions}

You can apply the reductions: `~DataFrame.empty`, `~DataFrame.any`,
`~DataFrame.all`.

::: ipython
python

(df \> 0).all() (df \> 0).any()
:::

You can reduce to a final boolean value.

::: ipython
python

(df \> 0).any().any()
:::

You can test if a pandas object is empty, via the
`~DataFrame.empty` property.

::: ipython
python

df.empty pd.DataFrame(columns=list(\"ABC\")).empty
:::

:::::: warning
::: title
Warning
:::

Asserting the truthiness of a pandas object will raise an error, as the
testing of the emptiness or values is ambiguous.

::: {.ipython okexcept=""}
python

if df:

: print(True)
:::

::: {.ipython okexcept=""}
python

df and df2
:::

See `gotchas<gotchas.truth>` for a more
detailed discussion.
::::::

### Comparing if objects are equivalent {#basics.equals}

Often you may find that there is more than one way to compute the same
result. As a simple example, consider `df + df` and `df * 2`. To test
that these two computations produce the same result, given the tools
shown above, you might imagine using `(df + df == df * 2).all()`. But in
fact, this expression is False:

::: ipython
python

df + df == df \* 2 (df + df == df \* 2).all()
:::

Notice that the boolean DataFrame `df + df == df * 2` contains some
False values! This is because NaNs do not compare as equals:

::: ipython
python

np.nan == np.nan
:::

So, NDFrames (such as Series and DataFrames) have an
`~DataFrame.equals` method for testing
equality, with NaNs in corresponding locations treated as equal.

::: ipython
python

(df + df).equals(df \* 2)
:::

Note that the Series or DataFrame index needs to be in the same order
for equality to be True:

::: ipython
python

df1 = pd.DataFrame({\"col\": \[\"foo\", 0, np.nan\]}) df2 =
pd.DataFrame({\"col\": \[np.nan, 0, \"foo\"\]}, index=\[2, 1, 0\])
df1.equals(df2) df1.equals(df2.sort_index())
:::

### Comparing array-like objects

You can conveniently perform element-wise comparisons when comparing a
pandas data structure with a scalar value:

::: ipython
python

pd.Series(\[\"foo\", \"bar\", \"baz\"\]) == \"foo\" pd.Index(\[\"foo\",
\"bar\", \"baz\"\]) == \"foo\"
:::

pandas also handles element-wise comparisons between different
array-like objects of the same length:

::: ipython
python

pd.Series(\[\"foo\", \"bar\", \"baz\"\]) == pd.Index(\[\"foo\", \"bar\",
\"qux\"\]) pd.Series(\[\"foo\", \"bar\", \"baz\"\]) ==
np.array(\[\"foo\", \"bar\", \"qux\"\])
:::

Trying to compare `Index` or `Series` objects of different lengths will
raise a ValueError:

::: {.ipython okexcept=""}
python

pd.Series(\[\'foo\', \'bar\', \'baz\'\]) == pd.Series(\[\'foo\',
\'bar\'\])

pd.Series(\[\'foo\', \'bar\', \'baz\'\]) == pd.Series(\[\'foo\'\])
:::

### Combining overlapping data sets

A problem occasionally arising is the combination of two similar data
sets where values in one are preferred over the other. An example would
be two data series representing a particular economic indicator where
one is considered to be of \"higher quality\". However, the lower
quality series might extend further back in history or have more
complete data coverage. As such, we would like to combine two DataFrame
objects where missing values in one DataFrame are conditionally filled
with like-labeled values from the other DataFrame. The function
implementing this operation is
`~DataFrame.combine_first`, which we
illustrate:

::: ipython
python

df1 = pd.DataFrame(

: {\"A\": \[1.0, np.nan, 3.0, 5.0, np.nan\], \"B\": \[np.nan, 2.0, 3.0,
  np.nan, 6.0\]}

) df2 = pd.DataFrame( { \"A\": \[5.0, 2.0, 4.0, np.nan, 3.0, 7.0\],
\"B\": \[np.nan, np.nan, 3.0, 4.0, 6.0, 8.0\], } ) df1 df2
df1.combine_first(df2)
:::

### General DataFrame combine

The `~DataFrame.combine_first` method
above calls the more general `DataFrame.combine`. This method takes another DataFrame and a combiner
function, aligns the input DataFrame and then passes the combiner
function pairs of Series (i.e., columns whose names are the same).

So, for instance, to reproduce
`~DataFrame.combine_first` as above:

::: ipython
python

def combiner(x, y):

: return np.where(pd.isna(x), y, x)

df1.combine(df2, combiner)
:::

## Descriptive statistics {#basics.stats}

There exists a large number of methods for computing descriptive
statistics and other related operations on
`Series <api.series.stats>`, `DataFrame
<api.dataframe.stats>`. Most of these are
aggregations (hence producing a lower-dimensional result) like
`~DataFrame.sum`,
`~DataFrame.mean`, and
`~DataFrame.quantile`, but some of them,
like `~DataFrame.cumsum` and
`~DataFrame.cumprod`, produce an object
of the same size. Generally speaking, these methods take an **axis**
argument, just like *ndarray.{sum, std, \...}*, but the axis can be
specified by name or integer:

- **Series**: no axis argument needed
- **DataFrame**: \"index\" (axis=0, default), \"columns\" (axis=1)

For example:

::: ipython
python

df df.mean(axis=0) df.mean(axis=1)
:::

All such methods have a `skipna` option signaling whether to exclude
missing data (`True` by default):

::: ipython
python

df.sum(axis=0, skipna=False) df.sum(axis=1, skipna=True)
:::

Combined with the broadcasting / arithmetic behavior, one can describe
various statistical procedures, like standardization (rendering data
zero mean and standard deviation of 1), very concisely:

::: ipython
python

ts_stand = (df - df.mean()) / df.std() ts_stand.std() xs_stand =
df.sub(df.mean(axis=1), axis=0).div(df.std(axis=1), axis=0)
xs_stand.std(axis=1)
:::

Note that methods like `~DataFrame.cumsum` and `~DataFrame.cumprod`
preserve the location of `NaN` values. This is somewhat different from
`~DataFrame.expanding` and
`~DataFrame.rolling` since `NaN` behavior
is furthermore dictated by a `min_periods` parameter.

::: ipython
python

df.cumsum()
:::

Here is a quick reference summary table of common functions. Each also
takes an optional `level` parameter which applies only if the object has
a `hierarchical index<advanced.hierarchical>`.

  Function       Description
  -------------- --------------------------------------------------------
  `count`        Number of non-NA observations

  `sum`          Sum of values

  `mean`         Mean of values

  `median`       Arithmetic median of values

  `min`          Minimum

  `max`          Maximum

  `mode`         Mode

  `abs`          Absolute Value

  `prod`         Product of values

  `std`          Bessel-corrected sample standard deviation

  `var`          Unbiased variance

  `sem`          Standard error of the mean

  `skew`         Sample skewness (3rd moment)

  `kurt`         Sample kurtosis (4th moment)

  `quantile`     Sample quantile (value at %)

  `cumsum`       Cumulative sum

  `cumprod`      Cumulative product

  `cummax`       Cumulative maximum

  `cummin`       Cumulative minimum

Note that by chance some NumPy methods, like `mean`, `std`, and `sum`,
will exclude NAs on Series input by default:

::: ipython
python

np.mean(df\[\"one\"\]) np.mean(df\[\"one\"\].to_numpy())
:::

`Series.nunique` will return the number
of unique non-NA values in a Series:

::: ipython
python

series = pd.Series(np.random.randn(500)) series\[20:500\] = np.nan
series\[10:20\] = 5 series.nunique()
:::

### Summarizing data: describe {#basics.describe}

There is a convenient `~DataFrame.describe` function which computes a variety of summary statistics
about a Series or the columns of a DataFrame (excluding NAs of course):

::: ipython
python

series = pd.Series(np.random.randn(1000)) series\[::2\] = np.nan
series.describe() frame = pd.DataFrame(np.random.randn(1000, 5),
columns=\[\"a\", \"b\", \"c\", \"d\", \"e\"\]) frame.iloc\[::2\] =
np.nan frame.describe()
:::

You can select specific percentiles to include in the output:

::: ipython
python

series.describe(percentiles=\[0.05, 0.25, 0.75, 0.95\])
:::

By default, the median is always included.

For a non-numerical Series object, `~Series.describe` will give a simple summary of the number of unique values
and most frequently occurring values:

::: ipython
python

s = pd.Series(\[\"a\", \"a\", \"b\", \"b\", \"a\", \"a\", np.nan, \"c\",
\"d\", \"a\"\]) s.describe()
:::

Note that on a mixed-type DataFrame object,
`~DataFrame.describe` will restrict the
summary to include only numerical columns or, if none are, only
categorical columns:

::: ipython
python

frame = pd.DataFrame({\"a\": \[\"Yes\", \"Yes\", \"No\", \"No\"\],
\"b\": range(4)}) frame.describe()
:::

This behavior can be controlled by providing a list of types as
`include`/`exclude` arguments. The special value `all` can also be used:

::: ipython
python

frame.describe(include=\[\"str\"\])
frame.describe(include=\[\"number\"\]) frame.describe(include=\"all\")
:::

That feature relies on
`select_dtypes <basics.selectdtypes>`.
Refer to there for details about accepted inputs.

### Index of min/max values {#basics.idxmin}

The `~DataFrame.idxmin` and
`~DataFrame.idxmax` functions on Series
and DataFrame compute the index labels with the minimum and maximum
corresponding values:

::: ipython
python

s1 = pd.Series(np.random.randn(5)) s1 s1.idxmin(), s1.idxmax()

df1 = pd.DataFrame(np.random.randn(5, 3), columns=\[\"A\", \"B\",
\"C\"\]) df1 df1.idxmin(axis=0) df1.idxmax(axis=1)
:::

When there are multiple rows (or columns) matching the minimum or
maximum value, `~DataFrame.idxmin` and
`~DataFrame.idxmax` return the first
matching index:

::: ipython
python

df3 = pd.DataFrame(\[2, 1, 1, 3, np.nan\], columns=\[\"A\"\],
index=list(\"edcba\")) df3 df3\[\"A\"\].idxmin()
:::

:::: note
::: title
Note
:::

`idxmin` and `idxmax` are called `argmin` and `argmax` in NumPy.
::::

### Value counts (histogramming) / mode {#basics.discretization}

The `~Series.value_counts` Series method
computes a histogram of a 1D array of values. It can also be used as a
function on regular arrays:

::: ipython
python

data = np.random.randint(0, 7, size=50) data s = pd.Series(data)
s.value_counts()
:::

The `~DataFrame.value_counts` method can
be used to count combinations across multiple columns. By default all
columns are used but a subset can be selected using the `subset`
argument.

::: ipython
python

data = {\"a\": \[1, 2, 3, 4\], \"b\": \[\"x\", \"x\", \"y\", \"y\"\]}
frame = pd.DataFrame(data) frame.value_counts()
:::

Similarly, you can get the most frequently occurring value(s), i.e. the
mode, of the values in a Series or DataFrame:

::: ipython
python

s5 = pd.Series(\[1, 1, 3, 3, 3, 5, 5, 7, 7, 7\]) s5.mode() df5 =
pd.DataFrame( { \"A\": np.random.randint(0, 7, size=50), \"B\":
np.random.randint(-10, 15, size=50), } ) df5.mode()
:::

### Discretization and quantiling

Continuous values can be discretized using the `cut` (bins based on values) and `qcut` (bins based on sample quantiles) functions:

::: ipython
python

arr = np.random.randn(20) factor = pd.cut(arr, 4) factor

factor = pd.cut(arr, \[-5, -1, 0, 1, 5\]) factor
:::

`qcut` computes sample quantiles. For
example, we could slice up some normally distributed data into
equal-size quartiles like so:

::: ipython
python

arr = np.random.randn(30) factor = pd.qcut(arr, \[0, 0.25, 0.5, 0.75,
1\]) factor
:::

We can also pass infinite values to define the bins:

::: ipython
python

arr = np.random.randn(20) factor = pd.cut(arr, \[-np.inf, 0, np.inf\])
factor
:::

## Function application {#basics.apply}

To apply your own or another library\'s functions to pandas objects, you
should be aware of the three methods below. The appropriate method to
use depends on whether your function expects to operate on an entire
`DataFrame` or `Series`, row- or column-wise, or elementwise.

1.  Tablewise Function Application:
    `~DataFrame.pipe`
2.  Row or Column-wise Function
    Application:
    `~DataFrame.apply`
3.  Aggregation API:
    `~DataFrame.agg` and
    `~DataFrame.transform`
4.  Applying Elementwise Functions:
    `~DataFrame.map`

### Tablewise function application {#basics.pipe}

`DataFrames` and `Series` can be passed into functions. However, if the
function needs to be called in a chain, consider using the
`~DataFrame.pipe` method.

First some setup:

::: ipython
python

def extract_city_name(df):

: \"\"\" Chicago, IL -\> Chicago for city_name column \"\"\"
  df\[\"city_name\"\] =
  df\[\"city_and_code\"\].str.split(\",\").str.get(0) return df

def add_country_name(df, country_name=None):

: \"\"\" Chicago -\> Chicago-US for city_name column \"\"\" col =
  \"city_name\" df\[\"city_and_country\"\] = df\[col\] + country_name
  return df

df_p = pd.DataFrame({\"city_and_code\": \[\"Chicago, IL\"\]})
:::

`extract_city_name` and `add_country_name` are functions taking and
returning `DataFrames`.

Now compare the following:

::: ipython
python

add_country_name(extract_city_name(df_p), country_name=\"US\")
:::

Is equivalent to:

::: ipython
python

df_p.pipe(extract_city_name).pipe(add_country_name, country_name=\"US\")
:::

pandas encourages the second style, which is known as method chaining.
`pipe` makes it easy to use your own or another library\'s functions in
method chains, alongside pandas\' methods.

In the example above, the functions `extract_city_name` and
`add_country_name` each expected a `DataFrame` as the first positional
argument. What if the function you wish to apply takes its data as, say,
the second argument? In this case, provide `pipe` with a tuple of
`(callable, data_keyword)`. `.pipe` will route the `DataFrame` to the
argument specified in the tuple.

For example, we can fit a regression using statsmodels. Their API
expects a formula first and a `DataFrame` as the second argument,
`data`. We pass in the function, keyword pair `(sm.ols, 'data')` to
`pipe`:

``` ipython
In [147]: import statsmodels.formula.api as sm

In [148]: bb = pd.read_csv("data/baseball.csv", index_col="id")

In [149]: (
   .....:     bb.query("h > 0")
   .....:     .assign(ln_h=lambda df: np.log(df.h))
   .....:     .pipe((sm.ols, "data"), "hr ~ ln_h + year + g + C(lg)")
   .....:     .fit()
   .....:     .summary()
   .....: )
   .....:
Out[149]:
<class 'statsmodels.iolib.summary.Summary'>
"""
                           OLS Regression Results
==============================================================================
Dep. Variable:                     hr   R-squared:                       0.685
Model:                            OLS   Adj. R-squared:                  0.665
Method:                 Least Squares   F-statistic:                     34.28
Date:                Tue, 22 Nov 2022   Prob (F-statistic):           3.48e-15
Time:                        05:34:17   Log-Likelihood:                -205.92
No. Observations:                  68   AIC:                             421.8
Df Residuals:                      63   BIC:                             432.9
Df Model:                           4
Covariance Type:            nonrobust
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]

Intercept   -8484.7720   4664.146     -1.819      0.074   -1.78e+04     835.780
C(lg)[T.NL]    -2.2736      1.325     -1.716      0.091      -4.922       0.375
ln_h           -1.3542      0.875     -1.547      0.127      -3.103       0.395
year            4.2277      2.324      1.819      0.074      -0.417       8.872
g               0.1841      0.029      6.258      0.000       0.125       0.243
==============================================================================
Omnibus:                       10.875   Durbin-Watson:                   1.999
Prob(Omnibus):                  0.004   Jarque-Bera (JB):               17.298
Skew:                           0.537   Prob(JB):                     0.000175
Kurtosis:                       5.225   Cond. No.                     1.49e+07
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.49e+07. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
```

The pipe method is inspired by unix pipes and more recently
[dplyr](https://github.com/tidyverse/dplyr) and
[magrittr](https://github.com/tidyverse/magrittr), which have introduced
the popular `(%>%)` (read pipe) operator for
[R](https://www.r-project.org). The implementation of `pipe` here is
quite clean and feels right at home in Python. We encourage you to view
the source code of `~DataFrame.pipe`.

### Row or column-wise function application

Arbitrary functions can be applied along the axes of a DataFrame using
the `~DataFrame.apply` method, which,
like the descriptive statistics methods, takes an optional `axis`
argument:

::: ipython
python

df.apply(lambda x: np.mean(x)) df.apply(lambda x: np.mean(x), axis=1)
df.apply(lambda x: x.max() - x.min()) df.apply(np.cumsum)
df.apply(np.exp)
:::

The `~DataFrame.apply` method will also
dispatch on a string method name.

::: ipython
python

df.apply(\"mean\") df.apply(\"mean\", axis=1)
:::

The return type of the function passed to
`~DataFrame.apply` affects the type of
the final output from `DataFrame.apply` for the default behaviour:

- If the applied function returns a `Series`, the final output is a
  `DataFrame`. The columns match the index of the `Series` returned by
  the applied function.
- If the applied function returns any other type, the final output is a
  `Series`.

This default behaviour can be overridden using the `result_type`, which
accepts three options: `reduce`, `broadcast`, and `expand`. These will
determine how list-likes return values expand (or not) to a `DataFrame`.

`~DataFrame.apply` combined with some
cleverness can be used to answer many questions about a data set. For
example, suppose we wanted to extract the date where the maximum value
for each column occurred:

::: ipython
python

tsdf = pd.DataFrame(

: np.random.randn(1000, 3), columns=\[\"A\", \"B\", \"C\"\],
  index=pd.date_range(\"1/1/2000\", periods=1000),

) tsdf.apply(lambda x: x.idxmax())
:::

You may also pass additional arguments and keyword arguments to the
`~DataFrame.apply` method.

::: ipython
python

def subtract_and_divide(x, sub, divide=1):

: return (x - sub) / divide

df_udf = pd.DataFrame(np.ones((2, 2))) df_udf.apply(subtract_and_divide,
args=(5,), divide=3)
:::

Another useful feature is the ability to pass Series methods to carry
out some Series operation on each column or row:

::: ipython
python

tsdf = pd.DataFrame(

: np.random.randn(10, 3), columns=\[\"A\", \"B\", \"C\"\],
  index=pd.date_range(\"1/1/2000\", periods=10),

) tsdf.iloc\[3:7\] = np.nan tsdf tsdf.apply(pd.Series.interpolate)
:::

Finally, `~DataFrame.apply` takes an
argument `raw` which is False by default, which converts each row or
column into a Series before applying the function. When set to True, the
passed function will instead receive an ndarray object, which has
positive performance implications if you do not need the indexing
functionality.

### Aggregation API {#basics.aggregate}

The aggregation API allows one to express possibly multiple aggregation
operations in a single concise way. This API is similar across pandas
objects, see `groupby API <groupby.aggregate>`, the `window API <window.overview>`, and the
`resample API <timeseries.aggregate>`. The
entry point for aggregation is `DataFrame.aggregate`, or the alias `DataFrame.agg`.

We will use a similar starting frame from above:

::: ipython
python

tsdf = pd.DataFrame(

: np.random.randn(10, 3), columns=\[\"A\", \"B\", \"C\"\],
  index=pd.date_range(\"1/1/2000\", periods=10),

) tsdf.iloc\[3:7\] = np.nan tsdf
:::

Using a single function is equivalent to
`~DataFrame.apply`. You can also pass
named methods as strings. These will return a `Series` of the aggregated
output:

::: ipython
python

tsdf.agg(lambda x: np.sum(x))

tsdf.agg(\"sum\")

\# these are equivalent to a `.sum()` because we are aggregating \# on a
single function tsdf.sum()
:::

Single aggregations on a `Series` this will return a scalar value:

::: ipython
python

tsdf\[\"A\"\].agg(\"sum\")
:::

#### Aggregating with multiple functions

You can pass multiple aggregation arguments as a list. The results of
each of the passed functions will be a row in the resulting `DataFrame`.
These are naturally named from the aggregation function.

::: ipython
python

tsdf.agg(\[\"sum\"\])
:::

Multiple functions yield multiple rows:

::: ipython
python

tsdf.agg(\[\"sum\", \"mean\"\])
:::

On a `Series`, multiple functions return a `Series`, indexed by the
function names:

::: ipython
python

tsdf\[\"A\"\].agg(\[\"sum\", \"mean\"\])
:::

Passing a `lambda` function will yield a `<lambda>` named row:

::: ipython
python

tsdf\[\"A\"\].agg(\[\"sum\", lambda x: x.mean()\])
:::

Passing a named function will yield that name for the row:

::: ipython
python

def mymean(x):

: return x.mean()

tsdf\[\"A\"\].agg(\[\"sum\", mymean\])
:::

#### Aggregating with a dict

Passing a dictionary of column names to a scalar or a list of scalars,
to `DataFrame.agg` allows you to customize which functions are applied
to which columns. Note that the results are not in any particular order,
you can use an `OrderedDict` instead to guarantee ordering.

::: ipython
python

tsdf.agg({\"A\": \"mean\", \"B\": \"sum\"})
:::

Passing a list-like will generate a `DataFrame` output. You will get a
matrix-like output of all of the aggregators. The output will consist of
all unique functions. Those that are not noted for a particular column
will be `NaN`:

::: ipython
python

tsdf.agg({\"A\": \[\"mean\", \"min\"\], \"B\": \"sum\"})
:::

#### Custom describe {#basics.aggregation.custom_describe}

With `.agg()` it is possible to easily create a custom describe
function, similar to the built in
`describe function <basics.describe>`.

::: ipython
python

from functools import partial

q_25 = partial(pd.Series.quantile, q=0.25) q_25.\_\_name\_\_ = \"25%\"
q_75 = partial(pd.Series.quantile, q=0.75) q_75.\_\_name\_\_ = \"75%\"

tsdf.agg(\[\"count\", \"mean\", \"std\", \"min\", q_25, \"median\",
q_75, \"max\"\])
:::

### Transform API {#basics.transform}

The `~DataFrame.transform` method returns
an object that is indexed the same (same size) as the original. This API
allows you to provide *multiple* operations at the same time rather than
one-by-one. Its API is quite similar to the `.agg` API.

We create a frame similar to the one used in the above sections.

::: ipython
python

tsdf = pd.DataFrame(

: np.random.randn(10, 3), columns=\[\"A\", \"B\", \"C\"\],
  index=pd.date_range(\"1/1/2000\", periods=10),

) tsdf.iloc\[3:7\] = np.nan tsdf
:::

Transform the entire frame. `.transform()` allows input functions as: a
NumPy function, a string function name or a user defined function.

::: {.ipython okwarning=""}
python

tsdf.transform(np.abs) tsdf.transform(\"abs\") tsdf.transform(lambda x:
x.abs())
:::

Here `~DataFrame.transform` received a
single function; this is equivalent to a
[ufunc](https://numpy.org/doc/stable/reference/ufuncs.html) application.

::: ipython
python

np.abs(tsdf)
:::

Passing a single function to `.transform()` with a `Series` will yield a
single `Series` in return.

::: ipython
python

tsdf\[\"A\"\].transform(np.abs)
:::

#### Transform with multiple functions

Passing multiple functions will yield a column MultiIndexed DataFrame.
The first level will be the original frame column names; the second
level will be the names of the transforming functions.

::: ipython
python

tsdf.transform(\[np.abs, lambda x: x + 1\])
:::

Passing multiple functions to a Series will yield a DataFrame. The
resulting column names will be the transforming functions.

::: ipython
python

tsdf\[\"A\"\].transform(\[np.abs, lambda x: x + 1\])
:::

#### Transforming with a dict

Passing a dict of functions will allow selective transforming per
column.

::: ipython
python

tsdf.transform({\"A\": np.abs, \"B\": lambda x: x + 1})
:::

Passing a dict of lists will generate a MultiIndexed DataFrame with
these selective transforms.

::: {.ipython okwarning=""}
python

tsdf.transform({\"A\": np.abs, \"B\": \[lambda x: x + 1, \"sqrt\"\]})
:::

### Applying elementwise functions {#basics.elementwise}

Since not all functions can be vectorized (accept NumPy arrays and
return another array or value), the methods
`~DataFrame.map` on DataFrame and
analogously `~Series.map` on Series
accept any Python function taking a single value and returning a single
value. For example:

::: ipython
python

df4 = df.copy() df4

def f(x):

: return len(str(x))

df4\[\"one\"\].map(f) df4.map(f)
:::

`Series.map` has an additional feature;
it can be used to easily \"link\" or \"map\" values defined by a
secondary series. This is closely related to
`merging/joining functionality <merging>`:

::: ipython
python

s = pd.Series(

: \[\"six\", \"seven\", \"six\", \"seven\", \"six\"\], index=\[\"a\",
  \"b\", \"c\", \"d\", \"e\"\]

) t = pd.Series({\"six\": 6.0, \"seven\": 7.0}) s s.map(t)
:::

## Reindexing and altering labels {#basics.reindexing}

`~Series.reindex` is the fundamental data
alignment method in pandas. It is used to implement nearly all other
features relying on label-alignment functionality. To *reindex* means to
conform the data to match a given set of labels along a particular axis.
This accomplishes several things:

- Reorders the existing data to match a new set of labels
- Inserts missing value (NA) markers in label locations where no data
  for that label existed
- If specified, **fill** data for missing labels using logic (highly
  relevant to working with time series data)

Here is a simple example:

::: ipython
python

s = pd.Series(np.random.randn(5), index=\[\"a\", \"b\", \"c\", \"d\",
\"e\"\]) s s.reindex(\[\"e\", \"b\", \"f\", \"d\"\])
:::

Here, the `f` label was not contained in the Series and hence appears as
`NaN` in the result.

With a DataFrame, you can simultaneously reindex the index and columns:

::: ipython
python

df df.reindex(index=\[\"c\", \"f\", \"b\"\], columns=\[\"three\",
\"two\", \"one\"\])
:::

Note that the `Index` objects containing the actual axis labels can be
**shared** between objects. So if we have a Series and a DataFrame, the
following can be done:

::: ipython
python

rs = s.reindex(df.index) rs rs.index is df.index
:::

This means that the reindexed Series\'s index is the same Python object
as the DataFrame\'s index.

`DataFrame.reindex` also supports an
\"axis-style\" calling convention, where you specify a single `labels`
argument and the `axis` it applies to.

::: ipython
python

df.reindex(\[\"c\", \"f\", \"b\"\], axis=\"index\")
df.reindex(\[\"three\", \"two\", \"one\"\], axis=\"columns\")
:::

::: seealso
`MultiIndex / Advanced Indexing <advanced>` is an even more concise way of doing reindexing.
:::

:::: note
::: title
Note
:::

When writing performance-sensitive code, there is a good reason to spend
some time becoming a reindexing ninja: **many operations are faster on
pre-aligned data**. Adding two unaligned DataFrames internally triggers
a reindexing step. For exploratory analysis you will hardly notice the
difference (because `reindex` has been heavily optimized), but when CPU
cycles matter sprinkling a few explicit `reindex` calls here and there
can have an impact.
::::

### Reindexing to align with another object {#basics.reindex_like}

You may wish to take an object and reindex its axes to be labeled the
same as another object. While the syntax for this is straightforward
albeit verbose, it is a common enough operation that the
`~DataFrame.reindex_like` method is
available to make this simpler:

::: ipython
python

df2 = df.reindex(\[\"a\", \"b\", \"c\"\], columns=\[\"one\", \"two\"\])
df3 = df2 - df2.mean() df2 df3 df.reindex_like(df2)
:::

### Aligning objects with each other with `align` {#basics.align}

The `~Series.align` method is the fastest
way to simultaneously align two objects. It supports a `join` argument
(related to `joining and merging <merging>`):

> - `join='outer'`: take the union of the indexes (default)
> - `join='left'`: use the calling object\'s index
> - `join='right'`: use the passed object\'s index
> - `join='inner'`: intersect the indexes

It returns a tuple with both of the reindexed Series:

::: ipython
python

s = pd.Series(np.random.randn(5), index=\[\"a\", \"b\", \"c\", \"d\",
\"e\"\]) s1 = s\[:4\] s2 = s\[1:\] s1.align(s2) s1.align(s2,
join=\"inner\") s1.align(s2, join=\"left\")
:::

::: {#basics.df_join}
For DataFrames, the join method will be applied to both the index and
the columns by default:
:::

::: ipython
python

df.align(df2, join=\"inner\")
:::

You can also pass an `axis` option to only align on the specified axis:

::: ipython
python

df.align(df2, join=\"inner\", axis=0)
:::

::: {#basics.align.frame.series}
If you pass a Series to `DataFrame.align`, you can choose to align both objects either on the
DataFrame\'s index or columns using the `axis` argument:
:::

::: ipython
python

df.align(df2.iloc\[0\], axis=1)
:::

### Filling while reindexing {#basics.reindex_fill}

`~Series.reindex` takes an optional
parameter `method` which is a filling method chosen from the following
table:

  Method                     Action
  -------------------------- --------------------------------------------
  ffill                      Fill values forward

  bfill                      Fill values backward

  nearest                    Fill from the nearest index value

We illustrate these fill methods on a simple Series:

::: ipython
python

rng = pd.date_range(\"1/3/2000\", periods=8) ts =
pd.Series(np.random.randn(8), index=rng) ts2 = ts.iloc\[\[0, 3, 6\]\] ts
ts2

ts2.reindex(ts.index) ts2.reindex(ts.index, method=\"ffill\")
ts2.reindex(ts.index, method=\"bfill\") ts2.reindex(ts.index,
method=\"nearest\")
:::

These methods require that the indexes are **ordered** increasing or
decreasing.

Note that the same result could have been achieved using
`ffill <missing_data.fillna>` (except for
`method='nearest'`) or
`interpolate <missing_data.interpolate>`:

::: ipython
python

ts2.reindex(ts.index).ffill()
:::

`~Series.reindex` will raise a ValueError
if the index is not monotonically increasing or decreasing.
`~Series.fillna` and
`~Series.interpolate` will not perform
any checks on the order of the index.

### Limits on filling while reindexing {#basics.limits_on_reindex_fill}

The `limit` and `tolerance` arguments provide additional control over
filling while reindexing. Limit specifies the maximum count of
consecutive matches:

::: ipython
python

ts2.reindex(ts.index, method=\"ffill\", limit=1)
:::

In contrast, tolerance specifies the maximum distance between the index
and indexer values:

::: ipython
python

ts2.reindex(ts.index, method=\"ffill\", tolerance=\"1 day\")
:::

Notice that when used on a `DatetimeIndex`, `TimedeltaIndex` or
`PeriodIndex`, `tolerance` will coerced into a `Timedelta` if possible.
This allows you to specify tolerance with appropriate strings.

### Dropping labels from an axis {#basics.drop}

A method closely related to `reindex` is the
`~DataFrame.drop` function. It removes a
set of labels from an axis:

::: ipython
python

df df.drop(\[\"a\", \"d\"\], axis=0) df.drop(\[\"one\"\], axis=1)
:::

Note that the following also works, but is a bit less obvious / clean:

::: ipython
python

df.reindex(df.index.difference(\[\"a\", \"d\"\]))
:::

### Renaming / mapping labels {#basics.rename}

The `~DataFrame.rename` method allows you
to relabel an axis based on some mapping (a dict or Series) or an
arbitrary function.

::: ipython
python

s s.rename(str.upper)
:::

If you pass a function, it must return a value when called with any of
the labels (and must produce a set of unique values). A dict or Series
can also be used:

::: ipython
python

df.rename(

: columns={\"one\": \"foo\", \"two\": \"bar\"}, index={\"a\": \"apple\",
  \"b\": \"banana\", \"d\": \"durian\"},

)
:::

If the mapping doesn\'t include a column/index label, it isn\'t renamed.
Note that extra labels in the mapping don\'t throw an error.

`DataFrame.rename` also supports an
\"axis-style\" calling convention, where you specify a single `mapper`
and the `axis` to apply that mapping to.

::: ipython
python

df.rename({\"one\": \"foo\", \"two\": \"bar\"}, axis=\"columns\")
df.rename({\"a\": \"apple\", \"b\": \"banana\", \"d\": \"durian\"},
axis=\"index\")
:::

Finally, `~Series.rename` also accepts a
scalar or list-like for altering the `Series.name` attribute.

::: ipython
python

s.rename(\"scalar-name\")
:::

::: {#basics.rename_axis}
The methods `DataFrame.rename_axis` and
`Series.rename_axis` allow specific names
of a `MultiIndex` to be changed (as opposed to the labels).
:::

::: ipython
python

df = pd.DataFrame(

: {\"x\": \[1, 2, 3, 4, 5, 6\], \"y\": \[10, 20, 30, 40, 50, 60\]},
  index=pd.MultiIndex.from_product( \[\[\"a\", \"b\", \"c\"\], \[1,
  2\]\], names=\[\"let\", \"num\"\] ),

) df df.rename_axis(index={\"let\": \"abc\"})
df.rename_axis(index=str.upper)
:::

## Iteration {#basics.iteration}

The behavior of basic iteration over pandas objects depends on the type.
When iterating over a Series, it is regarded as array-like, and basic
iteration produces the values. DataFrames follow the dict-like
convention of iterating over the \"keys\" of the objects.

In short, basic iteration (`for i in object`) produces:

- **Series**: values
- **DataFrame**: column labels

Thus, for example, iterating over a DataFrame gives you the column
names:

::: ipython
python

df = pd.DataFrame(

: {\"col1\": np.random.randn(3), \"col2\": np.random.randn(3)},
  index=\[\"a\", \"b\", \"c\"\]

)

for col in df:

: print(col)
:::

pandas objects also have the dict-like
`~DataFrame.items` method to iterate over
the (key, value) pairs.

To iterate over the rows of a DataFrame, you can use the following
methods:

- `~DataFrame.iterrows`: Iterate over the
  rows of a DataFrame as (index, Series) pairs. This converts the rows
  to Series objects, which can change the dtypes and has some
  performance implications.
- `~DataFrame.itertuples`: Iterate over
  the rows of a DataFrame as namedtuples of the values. This is a lot
  faster than `~DataFrame.iterrows`, and
  is in most cases preferable to use to iterate over the values of a
  DataFrame.

:::: warning
::: title
Warning
:::

Iterating through pandas objects is generally **slow**. In many cases,
iterating manually over the rows is not needed and can be avoided with
one of the following approaches:

- Look for a *vectorized* solution: many operations can be performed
  using built-in methods or NumPy functions, (boolean) indexing, \...
- When you have a function that cannot work on the full DataFrame/Series
  at once, it is better to use `~DataFrame.apply` instead of iterating over the values. See the docs on
  `function application <basics.apply>`.
- If you need to do iterative manipulations on the values but
  performance is important, consider writing the inner loop with cython
  or numba. See the
  `enhancing performance <enhancingperf>`
  section for some examples of this approach.
::::

::::: warning
::: title
Warning
:::

You should **never modify** something you are iterating over. This is
not guaranteed to work in all cases. Depending on the data types, the
iterator returns a copy and not a view, and writing to it will have no
effect!

For example, in the following case setting the value has no effect:

::: ipython
python

df = pd.DataFrame({\"a\": \[1, 2, 3\], \"b\": \[\"a\", \"b\", \"c\"\]})

for index, row in df.iterrows():

: row\[\"a\"\] = 10

df
:::
:::::

### items

Consistent with the dict-like interface,
`~DataFrame.items` iterates through
key-value pairs:

- **Series**: (index, scalar value) pairs
- **DataFrame**: (column, Series) pairs

For example:

::: ipython
python

for label, ser in df.items():

: print(label) print(ser)
:::

### iterrows {#basics.iterrows}

`~DataFrame.iterrows` allows you to
iterate through the rows of a DataFrame as Series objects. It returns an
iterator yielding each index value along with a Series containing the
data in each row:

::: ipython
python

for row_index, row in df.iterrows():

: print(row_index, row, sep=\"n\")
:::

:::::: note
::: title
Note
:::

Because `~DataFrame.iterrows` returns a
Series for each row, it does **not** preserve dtypes across the rows
(dtypes are preserved across columns for DataFrames). For example,

::: ipython
python

df_orig = pd.DataFrame(\[\[1, 1.5\]\], columns=\[\"int\", \"float\"\])
df_orig.dtypes row = next(df_orig.iterrows())\[1\] row
:::

All values in `row`, returned as a Series, are now upcasted to floats,
also the original integer value in column `x`:

::: ipython
python

row\[\"int\"\].dtype df_orig\[\"int\"\].dtype
:::

To preserve dtypes while iterating over the rows, it is better to use
`~DataFrame.itertuples` which returns
namedtuples of the values and which is generally much faster than
`~DataFrame.iterrows`.
::::::

For instance, a contrived way to transpose the DataFrame would be:

::: ipython
python

df2 = pd.DataFrame({\"x\": \[1, 2, 3\], \"y\": \[4, 5, 6\]}) print(df2)
print(df2.T)

df2_t = pd.DataFrame({idx: values for idx, values in df2.iterrows()})
print(df2_t)
:::

### itertuples

The `~DataFrame.itertuples` method will
return an iterator yielding a namedtuple for each row in the DataFrame.
The first element of the tuple will be the row\'s corresponding index
value, while the remaining values are the row values.

For instance:

::: ipython
python

for row in df.itertuples():

: print(row)
:::

This method does not convert the row to a Series object; it merely
returns the values inside a namedtuple. Therefore,
`~DataFrame.itertuples` preserves the
data type of the values and is generally faster than
`~DataFrame.iterrows`.

:::: note
::: title
Note
:::

The column names will be renamed to positional names if they are invalid
Python identifiers, repeated, or start with an underscore. With a large
number of columns (\>255), regular tuples are returned.
::::

## .dt accessor {#basics.dt_accessors}

`Series` has an accessor to succinctly return datetime like properties
for the *values* of the Series, if it is a datetime/period like Series.
This will return a Series, indexed like the existing Series.

::: ipython
python

\# datetime s = pd.Series(pd.date_range(\"20130101 09:10:12\",
periods=4)) s s.dt.hour s.dt.second s.dt.day
:::

This enables nice expressions like this:

::: ipython
python

s\[s.dt.day == 2\]
:::

You can easily produce tz aware transformations:

::: ipython
python

stz = s.dt.tz_localize(\"US/Eastern\") stz stz.dt.tz
:::

You can also chain these types of operations:

::: ipython
python

s.dt.tz_localize(\"UTC\").dt.tz_convert(\"US/Eastern\")
:::

You can also format datetime values as strings with
`Series.dt.strftime` which supports the
same format as the standard
`~datetime.datetime.strftime`.

::: ipython
python

\# DatetimeIndex s = pd.Series(pd.date_range(\"20130101\", periods=4)) s
s.dt.strftime(\"%Y/%m/%d\")
:::

::: ipython
python

\# PeriodIndex s = pd.Series(pd.period_range(\"20130101\", periods=4)) s
s.dt.strftime(\"%Y/%m/%d\")
:::

The `.dt` accessor works for period and timedelta dtypes.

::: ipython
python

\# period s = pd.Series(pd.period_range(\"20130101\", periods=4,
freq=\"D\")) s s.dt.year s.dt.day
:::

::: ipython
python

\# timedelta s = pd.Series(pd.timedelta_range(\"1 day 00:00:05\",
periods=4, freq=\"s\")) s s.dt.days s.dt.seconds s.dt.components
:::

:::: note
::: title
Note
:::

`Series.dt` will raise a `TypeError` if you access with a
non-datetime-like values.
::::

## Vectorized string methods

Series is equipped with a set of string processing methods that make it
easy to operate on each element of the array. Perhaps most importantly,
these methods exclude missing/NA values automatically. These are
accessed via the Series\'s `str` attribute and generally have names
matching the equivalent (scalar) built-in string methods. For example:

> ::: ipython
> python
>
> s = pd.Series(
>
> : \[\"A\", \"B\", \"C\", \"Aaba\", \"Baca\", np.nan, \"CABA\",
>   \"dog\", \"cat\"\], dtype=\"string\"
>
> ) s.str.lower()
> :::

Powerful pattern-matching methods are provided as well, but note that
pattern-matching generally uses [regular
expressions](https://docs.python.org/3/library/re.html) by default (and
in some cases always uses them).

:::: note
::: title
Note
:::

Prior to pandas 1.0, string methods were only available on `object`
-dtype `Series`. pandas 1.0 added the `StringDtype` which is dedicated to strings. See
`text.types` for more.
::::

Please see
`Vectorized String Methods <text.string_methods>` for a complete description.

## Sorting {#basics.sorting}

pandas supports three kinds of sorting: sorting by index labels, sorting
by column values, and sorting by a combination of both.

### By index {#basics.sort_index}

The `Series.sort_index` and
`DataFrame.sort_index` methods are used
to sort a pandas object by its index levels.

::: ipython
python

df = pd.DataFrame(

:

  {

  : \"one\": pd.Series(np.random.randn(3), index=\[\"a\", \"b\",
    \"c\"\]), \"two\": pd.Series(np.random.randn(4), index=\[\"a\",
    \"b\", \"c\", \"d\"\]), \"three\": pd.Series(np.random.randn(3),
    index=\[\"b\", \"c\", \"d\"\]),

  }

)

unsorted_df = df.reindex(

: index=\[\"a\", \"d\", \"c\", \"b\"\], columns=\[\"three\", \"two\",
  \"one\"\]

) unsorted_df

\# DataFrame unsorted_df.sort_index()
unsorted_df.sort_index(ascending=False) unsorted_df.sort_index(axis=1)

\# Series unsorted_df\[\"three\"\].sort_index()
:::

::: {#basics.sort_index_key}
Sorting by index also supports a `key` parameter that takes a callable
function to apply to the index being sorted. For `MultiIndex` objects,
the key is applied per-level to the levels specified by `level`.
:::

::: ipython
python

s1 = pd.DataFrame({\"a\": \[\"B\", \"a\", \"C\"\], \"b\": \[1, 2, 3\], \"c\": \[2, 3, 4\]}).set_index(

: list(\"ab\")

) s1
:::

::: ipython
python

s1.sort_index(level=\"a\") s1.sort_index(level=\"a\", key=lambda idx:
idx.str.lower())
:::

For information on key sorting by value, see `value sorting
<basics.sort_value_key>`.

### By values {#basics.sort_values}

The `Series.sort_values` method is used
to sort a `Series` by its values. The
`DataFrame.sort_values` method is used to
sort a `DataFrame` by its column or row values. The optional `by`
parameter to `DataFrame.sort_values` may
used to specify one or more columns to use to determine the sorted
order.

::: ipython
python

df1 = pd.DataFrame(

: {\"one\": \[2, 1, 1, 1\], \"two\": \[1, 3, 2, 4\], \"three\": \[5, 4,
  3, 2\]}

) df1.sort_values(by=\"two\")
:::

The `by` parameter can take a list of column names, e.g.:

::: ipython
python

df1\[\[\"one\", \"two\", \"three\"\]\].sort_values(by=\[\"one\",
\"two\"\])
:::

These methods have special treatment of NA values via the `na_position`
argument:

::: ipython
python

s\[2\] = np.nan s.sort_values() s.sort_values(na_position=\"first\")
:::

::: {#basics.sort_value_key}
Sorting also supports a `key` parameter that takes a callable function
to apply to the values being sorted.
:::

::: ipython
python

s1 = pd.Series(\[\"B\", \"a\", \"C\"\])
:::

::: ipython
python

s1.sort_values() s1.sort_values(key=lambda x: x.str.lower())
:::

`key` will be given the `Series` of
values and should return a `Series` or array of the same shape with the
transformed values. For `DataFrame` objects, the key is applied per
column, so the key should still expect a Series and return a Series,
e.g.

::: ipython
python

df = pd.DataFrame({\"a\": \[\"B\", \"a\", \"C\"\], \"b\": \[1, 2, 3\]})
:::

::: ipython
python

df.sort_values(by=\"a\") df.sort_values(by=\"a\", key=lambda col:
col.str.lower())
:::

The name or type of each column can be used to apply different functions
to different columns.

### By indexes and values {#basics.sort_indexes_and_values}

Strings passed as the `by` parameter to
`DataFrame.sort_values` may refer to
either columns or index level names.

::: ipython
python

\# Build MultiIndex idx = pd.MultiIndex.from_tuples( \[(\"a\", 1),
(\"a\", 2), (\"a\", 2), (\"b\", 2), (\"b\", 1), (\"b\", 1)\] ) idx.names
= \[\"first\", \"second\"\]

\# Build DataFrame df_multi = pd.DataFrame({\"A\": np.arange(6, 0, -1)},
index=idx) df_multi
:::

Sort by \'second\' (index) and \'A\' (column)

::: ipython
python

df_multi.sort_values(by=\[\"second\", \"A\"\])
:::

:::: note
::: title
Note
:::

If a string matches both a column name and an index level name then a
warning is issued and the column takes precedence. This will result in
an ambiguity error in a future version.
::::

### searchsorted {#basics.searchsorted}

Series has the `~Series.searchsorted`
method, which works similarly to
`numpy.ndarray.searchsorted`.

::: ipython
python

ser = pd.Series(\[1, 2, 3\]) ser.searchsorted(\[0, 3\])
ser.searchsorted(\[0, 4\]) ser.searchsorted(\[1, 3\], side=\"right\")
ser.searchsorted(\[1, 3\], side=\"left\") ser = pd.Series(\[3, 1, 2\])
ser.searchsorted(\[0, 3\], sorter=np.argsort(ser))
:::

### smallest / largest values {#basics.nsorted}

`Series` has the `~Series.nsmallest` and
`~Series.nlargest` methods which return
the smallest or largest $n$ values. For a large `Series` this can be
much faster than sorting the entire Series and calling `head(n)` on the
result.

::: ipython
python

s = pd.Series(np.random.permutation(10)) s s.sort_values()
s.nsmallest(3) s.nlargest(3)
:::

`DataFrame` also has the `nlargest` and `nsmallest` methods.

::: ipython
python

df = pd.DataFrame(

:

  {

  : \"a\": \[-2, -1, 1, 10, 8, 11, -1\], \"b\": list(\"abdceff\"),
    \"c\": \[1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0\],

  }

) df.nlargest(3, \"a\") df.nlargest(5, \[\"a\", \"c\"\]) df.nsmallest(3,
\"a\") df.nsmallest(5, \[\"a\", \"c\"\])
:::

### Sorting by a MultiIndex column {#basics.multiindex_sorting}

You must be explicit about sorting when the column is a MultiIndex, and
fully specify all levels to `by`.

::: ipython
python

df1.columns = pd.MultiIndex.from_tuples(

: \[(\"a\", \"one\"), (\"a\", \"two\"), (\"b\", \"three\")\]

) df1.sort_values(by=(\"a\", \"two\"))
:::

## Copying

The `~DataFrame.copy` method on pandas
objects copies the underlying data (though not the axis indexes, since
they are immutable) and returns a new object. Note that **it is seldom
necessary to copy objects**. For example, there are only a handful of
ways to alter a DataFrame *in-place*:

- Inserting, deleting, or modifying a column.
- Assigning to the `index` or `columns` attributes.
- For homogeneous data, directly modifying the values via the `values`
  attribute or advanced indexing.

To be clear, no pandas method has the side effect of modifying your
data; almost every method returns a new object, leaving the original
object untouched. If the data is modified, it is because you did so
explicitly.

## dtypes {#basics.dtypes}

For the most part, pandas uses NumPy arrays and dtypes for Series or
individual columns of a DataFrame. NumPy provides support for `float`,
`int`, `bool`, `timedelta64[ns]` and `datetime64[ns]` (note that NumPy
does not support timezone-aware datetimes).

pandas and third-party libraries *extend* NumPy\'s type system in a few
places. This section describes the extensions pandas has made
internally. See `extending.extension-types` for how to write your own extension that works with pandas.
See [the ecosystem
page](https://pandas.pydata.org/community/ecosystem.html) for a list of
third-party libraries that have implemented an extension.

The following table lists all of pandas extension types. For methods
requiring `dtype` arguments, strings can be specified as indicated. See
the respective documentation sections for more on each type.

+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| Kind of Data                                                 | Data Type                               | Scalar                            | Array                                    | String Aliases                      |
+==============================================================+=========================================+===================================+==========================================+=====================================+
| `tz-aware datetime <timeseries.timezone>`                                                  | role="class"}                           | role="class"}                     | role="class"}                            |                                     |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `Categorical <categorical>`    | `CategoricalDtype`                           |                                   | role="class"}                            |                                     |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `period (time spans) <timeseries.periods>`                                                  | role="class"}                           | role="class"}                     | role="class"} `'Period[<freq>]'`         |                                     |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `sparse <sparse>`              | `SparseDtype`                           |                                   | role="class"}                            | `'Sparse[float]'`                   |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `intervals <advanced.intervalindex>`                                                  | role="class"}                           | role="class"}                     | role="class"}                            | `'Interval[<numpy_dtype>]'`,        |
|                                                              |                                         |                                   |                                          | `'Interval[datetime64[ns, <tz>]]'`, |
|                                                              |                                         |                                   |                                          | `'Interval[timedelta64[<freq>]]'`   |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `nullable integer <integer_na>`                                                  | role="class"}, \...                     |                                   | role="class"}                            | `'Int64'`, `'UInt8'`, `'UInt16'`,   |
|                                                              |                                         |                                   |                                          | `'UInt32'`, `'UInt64'`              |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `nullable float <api.arrays.float_na>`                                                  | role="class"}, \...                     |                                   | role="class"}                            |                                     |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `Strings <text>`               | `StringDtype`                           | role="class"}                     | role="class"}                            |                                     |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+
| `Boolean (with NA) <api.arrays.bool>`                                                  | role="class"}                           | role="class"}                     | role="class"}                            |                                     |
+--------------------------------------------------------------+-----------------------------------------+-----------------------------------+------------------------------------------+-------------------------------------+

pandas has two ways to store strings.

1.  `object` dtype, which can hold any Python object, including strings.
2.  `StringDtype`, which is dedicated to
    strings.

Generally, we recommend using `StringDtype`. See `text.types` for more.

Finally, arbitrary objects may be stored using the `object` dtype, but
should be avoided to the extent possible (for performance and
interoperability with other libraries and methods. See
`basics.object_conversion`).

A convenient `~DataFrame.dtypes`
attribute for DataFrame returns a Series with the data type of each
column.

::: ipython
python

dft = pd.DataFrame(

:

  {

  : \"A\": np.random.rand(3), \"B\": 1, \"C\": \"foo\", \"D\":
    pd.Timestamp(\"20010102\"), \"E\": pd.Series(\[1.0\] \*
    3).astype(\"float32\"), \"F\": False, \"G\": pd.Series(\[1\] \* 3,
    dtype=\"int8\"),

  }

) dft dft.dtypes
:::

On a `Series` object, use the `~Series.dtype` attribute.

::: ipython
python

dft\[\"A\"\].dtype
:::

If a pandas object contains data with multiple dtypes *in a single
column*, the dtype of the column will be chosen to accommodate all of
the data types (`object` is the most general).

::: ipython
python

\# these ints are coerced to floats pd.Series(\[1, 2, 3, 4, 5, 6.0\])

\# string data forces an `object` dtype pd.Series(\[1, 2, 3, 6.0,
\"foo\"\])
:::

The number of columns of each type in a `DataFrame` can be found by
calling `DataFrame.dtypes.value_counts()`.

::: ipython
python

dft.dtypes.value_counts()
:::

Numeric dtypes will propagate and can coexist in DataFrames. If a dtype
is passed (either directly via the `dtype` keyword, a passed `ndarray`,
or a passed `Series`), then it will be preserved in DataFrame
operations. Furthermore, different numeric dtypes will **NOT** be
combined. The following example will give you a taste.

::: ipython
python

df1 = pd.DataFrame(np.random.randn(8, 1), columns=\[\"A\"\],
dtype=\"float64\") df1 df1.dtypes df2 = pd.DataFrame( { \"A\":
pd.Series(np.random.randn(8), dtype=\"float32\"), \"B\":
pd.Series(np.random.randn(8)), \"C\": pd.Series(np.random.randint(0,
255, size=8), dtype=\"uint8\"), \# \[0,255\] (range of uint8) } ) df2
df2.dtypes
:::

### defaults

By default integer types are `int64` and float types are `float64`,
*regardless* of platform (32-bit or 64-bit). The following will all
result in `int64` dtypes.

::: ipython
python

pd.DataFrame(\[1, 2\], columns=\[\"a\"\]).dtypes pd.DataFrame({\"a\":
\[1, 2\]}).dtypes pd.DataFrame({\"a\": 1}, index=list(range(2))).dtypes
:::

Note that Numpy will choose *platform-dependent* types when creating
arrays. The following **WILL** result in `int32` on 32-bit platform.

::: ipython
python

frame = pd.DataFrame(np.array(\[1, 2\]))
:::

### upcasting

Types can potentially be *upcasted* when combined with other types,
meaning they are promoted from the current type (e.g. `int` to `float`).

::: ipython
python

df3 = df1.reindex_like(df2).fillna(value=0.0) + df2 df3 df3.dtypes
:::

`DataFrame.to_numpy` will return the
*lower-common-denominator* of the dtypes, meaning the dtype that can
accommodate **ALL** of the types in the resulting homogeneous dtyped
NumPy array. This can force some *upcasting*.

::: ipython
python

df3.to_numpy().dtype
:::

### astype

::: {#basics.cast}
You can use the `~DataFrame.astype`
method to explicitly convert dtypes from one to another. These will by
default return a copy, even if the dtype was unchanged (pass
`copy=False` to change this behavior). In addition, they will raise an
exception if the astype operation is invalid.
:::

Upcasting is always according to the **NumPy** rules. If two different
dtypes are involved in an operation, then the more *general* one will be
used as the result of the operation.

::: ipython
python

df3 df3.dtypes

\# conversion of dtypes df3.astype(\"float32\").dtypes
:::

Convert a subset of columns to a specified type using
`~DataFrame.astype`.

::: ipython
python

dft = pd.DataFrame({\"a\": \[1, 2, 3\], \"b\": \[4, 5, 6\], \"c\": \[7,
8, 9\]}) dft\[\[\"a\", \"b\"\]\] = dft\[\[\"a\",
\"b\"\]\].astype(np.uint8) dft dft.dtypes
:::

Convert certain columns to a specific dtype by passing a dict to
`~DataFrame.astype`.

::: ipython
python

dft1 = pd.DataFrame({\"a\": \[1, 0, 1\], \"b\": \[4, 5, 6\], \"c\": \[7,
8, 9\]}) dft1 = dft1.astype({\"a\": [np.bool](), \"c\": np.float64})
dft1 dft1.dtypes
:::

::::: note
::: title
Note
:::

When trying to convert a subset of columns to a specified type using
`~DataFrame.astype` and
`~DataFrame.loc`, upcasting occurs.

`~DataFrame.loc` tries to fit in what we
are assigning to the current dtypes, while `[]` will overwrite them
taking the dtype from the right hand side. Therefore the following piece
of code produces the unintended result.

::: ipython
python

dft = pd.DataFrame({\"a\": \[1, 2, 3\], \"b\": \[4, 5, 6\], \"c\": \[7,
8, 9\]}) dft.loc\[:, \[\"a\", \"b\"\]\].astype(np.uint8).dtypes
dft.loc\[:, \[\"a\", \"b\"\]\] = dft.loc\[:, \[\"a\",
\"b\"\]\].astype(np.uint8) dft.dtypes
:::
:::::

### object conversion {#basics.object_conversion}

pandas offers various functions to try to force conversion of types from
the `object` dtype to other types. In cases where the data is already of
the correct type, but stored in an `object` array, the
`DataFrame.infer_objects` and
`Series.infer_objects` methods can be
used to soft convert to the correct type.

> ::: ipython
> python
>
> import datetime
>
> df = pd.DataFrame(
>
> :
>
>   \[
>
>   : \[1, 2\], \[\"a\", \"b\"\], \[datetime.datetime(2016, 3, 2),
>     datetime.datetime(2016, 3, 2)\],
>
>   \]
>
> ) df = df.T df df.dtypes
> :::

Because the data was transposed the original inference stored all
columns as object, which `infer_objects` will correct.

> ::: ipython
> python
>
> df.infer_objects().dtypes
> :::

The following functions are available for one dimensional object arrays
or scalars to perform hard conversion of objects to a specified type:

- `~pandas.to_numeric` (conversion to
  numeric dtypes)

  ::: ipython
  python

  m = \[\"1.1\", 2, 3\] pd.to_numeric(m)
  :::

- `~pandas.to_datetime` (conversion to
  datetime objects)

  ::: ipython
  python

  import datetime

  m = \[\"2016-07-09\", datetime.datetime(2016, 3, 2)\]
  pd.to_datetime(m)
  :::

- `~pandas.to_timedelta` (conversion to
  timedelta objects)

  ::: ipython
  python

  m = \[\"5us\", pd.Timedelta(\"1day\")\] pd.to_timedelta(m)
  :::

To force a conversion, we can pass in an `errors` argument, which
specifies how pandas should deal with elements that cannot be converted
to desired dtype or object. By default, `errors='raise'`, meaning that
any errors encountered will be raised during the conversion process.
However, if `errors='coerce'`, these errors will be ignored and pandas
will convert problematic elements to `pd.NaT` (for datetime and
timedelta) or `np.nan` (for numeric). This might be useful if you are
reading in data which is mostly of the desired dtype (e.g. numeric,
datetime), but occasionally has non-conforming elements intermixed that
you want to represent as missing:

::: {.ipython okwarning=""}
python

import datetime

m = \[\"apple\", datetime.datetime(2016, 3, 2)\] pd.to_datetime(m,
errors=\"coerce\")

m = \[\"apple\", 2, 3\] pd.to_numeric(m, errors=\"coerce\")

m = \[\"apple\", pd.Timedelta(\"1day\")\] pd.to_timedelta(m,
errors=\"coerce\")
:::

In addition to object conversion, `~pandas.to_numeric` provides another argument `downcast`, which gives the
option of downcasting the newly (or already) numeric data to a smaller
dtype, which can conserve memory:

::: ipython
python

m = \[\"1\", 2, 3\] pd.to_numeric(m, downcast=\"integer\") \# smallest
signed int dtype pd.to_numeric(m, downcast=\"signed\") \# same as
\'integer\' pd.to_numeric(m, downcast=\"unsigned\") \# smallest unsigned
int dtype pd.to_numeric(m, downcast=\"float\") \# smallest float dtype
:::

As these methods apply only to one-dimensional arrays, lists or scalars;
they cannot be used directly on multi-dimensional objects such as
DataFrames. However, with `~pandas.DataFrame.apply`, we can \"apply\" the function over each column
efficiently:

::: ipython
python

import datetime

df = pd.DataFrame(\[\[\"2016-07-09\", datetime.datetime(2016, 3, 2)\]\]
\* 2, dtype=\"O\") df df.apply(pd.to_datetime)

df = pd.DataFrame(\[\[\"1.1\", 2, 3\]\] \* 2, dtype=\"O\") df
df.apply(pd.to_numeric)

df = pd.DataFrame(\[\[\"5us\", pd.Timedelta(\"1day\")\]\] \* 2,
dtype=\"O\") df df.apply(pd.to_timedelta)
:::

### gotchas

Performing selection operations on `integer` type data can easily upcast
the data to `floating`. The dtype of the input data will be preserved in
cases where `nans` are not introduced. See also
`Support for integer NA <gotchas.intna>`.

::: ipython
python

dfi = df3.astype(\"int32\") dfi\[\"E\"\] = 1 dfi dfi.dtypes

casted = dfi\[dfi \> 0\] casted casted.dtypes
:::

While float dtypes are unchanged.

::: ipython
python

dfa = df3.copy() dfa\[\"A\"\] = dfa\[\"A\"\].astype(\"float32\")
dfa.dtypes

casted = dfa\[df2 \> 0\] casted casted.dtypes
:::

## Selecting columns based on `dtype`

::: {#basics.selectdtypes}
The `~DataFrame.select_dtypes` method
implements subsetting of columns based on their `dtype`.
:::

First, let\'s create a `DataFrame` with
a slew of different dtypes:

::: ipython
python

df = pd.DataFrame(

:

  {

  : \"string\": list(\"abc\"), \"int64\": list(range(1, 4)), \"uint8\":
    np.arange(3, 6).astype(\"u1\"), \"float64\": np.arange(4.0, 7.0),
    \"bool1\": \[True, False, True\], \"bool2\": \[False, True, False\],
    \"dates\": pd.date_range(\"now\", periods=3), \"category\":
    pd.Series(list(\"ABC\")).astype(\"category\"),

  }

) df\[\"tdeltas\"\] = df.dates.diff() df\[\"uint64\"\] = np.arange(3,
6).astype(\"u8\") df\[\"other_dates\"\] = pd.date_range(\"20130101\",
periods=3) df\[\"tz_aware_dates\"\] = pd.date_range(\"20130101\",
periods=3, tz=\"US/Eastern\") df
:::

And the dtypes:

::: ipython
python

df.dtypes
:::

`~DataFrame.select_dtypes` has two
parameters `include` and `exclude` that allow you to say \"give me the
columns *with* these dtypes\" (`include`) and/or \"give the columns
*without* these dtypes\" (`exclude`).

For example, to select `bool` columns:

::: ipython
python

df.select_dtypes(include=\[bool\])
:::

You can also pass the name of a dtype in the [NumPy dtype
hierarchy](https://numpy.org/doc/stable/reference/arrays.scalars.html):

::: ipython
python

df.select_dtypes(include=\[\"bool\"\])
:::

`~pandas.DataFrame.select_dtypes` also
works with generic dtypes as well.

For example, to select all numeric and boolean columns while excluding
unsigned integers:

::: ipython
python

df.select_dtypes(include=\[\"number\", \"bool\"\],
exclude=\[\"unsignedinteger\"\])
:::

To select string columns include `str`:

::: ipython
python

df.select_dtypes(include=\[str\])
:::

:::: note
::: title
Note
:::

This is a change in pandas 3.0. Previously strings were stored in
`object` dtype columns, so would be selected with `include=[object]`.
See
`the migration guide <string_migration.select_dtypes>` for details on how to write code that works with both
versions.
::::

To see all the child dtypes of a generic `dtype` like `numpy.number` you
can define a function that returns a tree of child dtypes:

::: ipython
python

def subdtypes(dtype):

: subs = dtype.\_\_subclasses\_\_() if not subs: return dtype return
  \[dtype, \[subdtypes(dt) for dt in subs\]\]
:::

All NumPy dtypes are subclasses of `numpy.generic`:

::: ipython
python

subdtypes(np.generic)
:::

:::: note
::: title
Note
:::

pandas also defines the types `category`, and `datetime64[ns, tz]`,
which are not integrated into the normal NumPy hierarchy and won\'t show
up with the above function.
::::