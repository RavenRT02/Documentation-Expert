{{ header }}

# pandas arrays, scalars, and data types {#api.arrays}

## Objects

::: currentmodule
pandas
:::

For most data types, pandas uses NumPy arrays as the concrete objects
contained with a `Index`,
`Series`, or
`DataFrame`.

For some data types, pandas extends NumPy\'s type system. String aliases
for these types can be found at `basics.dtypes`.

  Kind of Data          pandas Data Type                                       Scalar                                                   Array
  --------------------- ------------------------------------------------------ -------------------------------------------------------- --------------------------------------------------------
  TZ-aware datetime     `DatetimeTZDtype`      `Timestamp`              `api.arrays.datetime`
  Timedeltas            (none)                                                 `Timedelta`              `api.arrays.timedelta`
  Period (time spans)   `PeriodDtype`          `Period`                 `api.arrays.period`
  Intervals             `IntervalDtype`        `Interval`               `api.arrays.interval`
  Nullable Integer      `Int64Dtype`, \...     (none)                                                   `api.arrays.integer_na`
  Nullable Float        `Float64Dtype`, \...   (none)                                                   `api.arrays.float_na`
  Categorical           `CategoricalDtype`     (none)                                                   `api.arrays.categorical`
  Sparse                `SparseDtype`          (none)                                                   `api.arrays.sparse`
  Strings               `StringDtype`          `str`                    `api.arrays.string`
  Nullable Boolean      `BooleanDtype`         `bool`                   `api.arrays.bool`
  PyArrow               `ArrowDtype`           Python Scalars or `NA`   `api.arrays.arrow`

pandas and third-party libraries can extend NumPy\'s type system (see
`extending.extension-types`). The
top-level `array` method can be used to
create a new array, which may be stored in a `Series`, `Index`, or as a column
in a `DataFrame`.

::: {.autosummary toctree="api/"}
array
:::

### PyArrow {#api.arrays.arrow}

:::: warning
::: title
Warning
:::

This feature is experimental, and the API can change in a future release
without warning.
::::

The `arrays.ArrowExtensionArray` is
backed by a `pyarrow.ChunkedArray` with a
`pyarrow.DataType`
instead of a NumPy array and data type. The `.dtype` of a
`arrays.ArrowExtensionArray` is an
`ArrowDtype`.

[Pyarrow](https://arrow.apache.org/docs/python/index.html) provides
similar array and [data
type](https://arrow.apache.org/docs/python/api/datatypes.html) support
as NumPy including first-class nullability support for all data types,
immutability and more.

The table below shows the equivalent pyarrow-backed (`pa`), pandas
extension, and numpy (`np`) types that are recognized by pandas.
Pyarrow-backed types below need to be passed into
`ArrowDtype` to be recognized by pandas
e.g. `pd.ArrowDtype(pa.bool_())`.

  PyArrow type                                                              pandas extension type                                NumPy type
  ------------------------------------------------------------------------- ---------------------------------------------------- ------------------
  `pyarrow.bool_`        `BooleanDtype`       `np.bool_`
  `pyarrow.int8`         `Int8Dtype`          `np.int8`
  `pyarrow.int16`        `Int16Dtype`         `np.int16`
  `pyarrow.int32`        `Int32Dtype`         `np.int32`
  `pyarrow.int64`        `Int64Dtype`         `np.int64`
  `pyarrow.uint8`        `UInt8Dtype`         `np.uint8`
  `pyarrow.uint16`       `UInt16Dtype`        `np.uint16`
  `pyarrow.uint32`       `UInt32Dtype`        `np.uint32`
  `pyarrow.uint64`       `UInt64Dtype`        `np.uint64`
  `pyarrow.float32`      `Float32Dtype`       `np.float32`
  `pyarrow.float64`      `Float64Dtype`       `np.float64`
  `pyarrow.time32`       (none)                                               (none)
  `pyarrow.time64`       (none)                                               (none)
  `pyarrow.timestamp`    `DatetimeTZDtype`    `np.datetime64`
  `pyarrow.date32`       (none)                                               (none)
  `pyarrow.date64`       (none)                                               (none)
  `pyarrow.duration`     (none)                                               `np.timedelta64`
  `pyarrow.binary`       (none)                                               (none)
  `pyarrow.string`       `StringDtype`        `np.str_`
  `pyarrow.decimal128`   (none)                                               (none)
  `pyarrow.list_`        (none)                                               (none)
  `pyarrow.map_`         (none)                                               (none)
  `pyarrow.dictionary`   `CategoricalDtype`   (none)

:::: note
::: title
Note
:::

Pyarrow-backed string support is provided by both
`pd.StringDtype("pyarrow")` and `pd.ArrowDtype(pa.string())`.
`pd.StringDtype("pyarrow")` is described below in the
`string section <api.arrays.string>` and
will be returned if the string alias `"string[pyarrow]"` is specified.
`pd.ArrowDtype(pa.string())` generally has better interoperability with
`ArrowDtype` of different types.
::::

While individual values in an
`arrays.ArrowExtensionArray` are stored
as a PyArrow objects, scalars are **returned** as Python scalars
corresponding to the data type, e.g. a PyArrow int64 will be returned as
Python int, or `NA` for missing values.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.ArrowExtensionArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
ArrowDtype
:::

For more information, please see the
`PyArrow user guide <pyarrow>`.

### Datetimes {#api.arrays.datetime}

NumPy cannot natively represent timezone-aware datetimes. pandas
supports this with the `arrays.DatetimeArray` extension array, which can hold timezone-naive or
timezone-aware values.

`Timestamp`, a subclass of
`datetime.datetime`, is pandas\' scalar
type for timezone-naive or timezone-aware datetime data.
`NaT` is the missing value for datetime
data.

::: {.autosummary toctree="api/"}
Timestamp
:::

#### Properties

::: {.autosummary toctree="api/"}
Timestamp.asm8 Timestamp.day Timestamp.dayofweek Timestamp.day_of_week
Timestamp.dayofyear Timestamp.day_of_year Timestamp.days_in_month
Timestamp.daysinmonth Timestamp.fold Timestamp.hour
Timestamp.is_leap_year Timestamp.is_month_end Timestamp.is_month_start
Timestamp.is_quarter_end Timestamp.is_quarter_start
Timestamp.is_year_end Timestamp.is_year_start Timestamp.max
Timestamp.microsecond Timestamp.min Timestamp.minute Timestamp.month
Timestamp.nanosecond Timestamp.quarter Timestamp.resolution
Timestamp.second Timestamp.tz Timestamp.tzinfo Timestamp.unit
Timestamp.value Timestamp.week Timestamp.weekofyear Timestamp.year
:::

#### Methods

::: {.autosummary toctree="api/"}
Timestamp.as_unit Timestamp.astimezone Timestamp.ceil Timestamp.combine
Timestamp.ctime Timestamp.date Timestamp.day_name Timestamp.dst
Timestamp.floor Timestamp.fromisocalendar Timestamp.fromisoformat
Timestamp.fromordinal Timestamp.fromtimestamp Timestamp.isocalendar
Timestamp.isoformat Timestamp.isoweekday Timestamp.month_name
Timestamp.normalize Timestamp.now Timestamp.replace Timestamp.round
Timestamp.strftime Timestamp.strptime Timestamp.time Timestamp.timestamp
Timestamp.timetuple Timestamp.timetz Timestamp.to_datetime64
Timestamp.to_numpy Timestamp.to_julian_date Timestamp.to_period
Timestamp.to_pydatetime Timestamp.today Timestamp.toordinal
Timestamp.tz_convert Timestamp.tz_localize Timestamp.tzname
Timestamp.utcfromtimestamp Timestamp.utcnow Timestamp.utcoffset
Timestamp.utctimetuple Timestamp.weekday
:::

A collection of timestamps may be stored in a
`arrays.DatetimeArray`. For
timezone-aware data, the `.dtype` of a
`arrays.DatetimeArray` is a
`DatetimeTZDtype`. For timezone-naive
data, `np.dtype("datetime64[ns]")` is used.

If the data are timezone-aware, then every value in the array must have
the same timezone.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.DatetimeArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
DatetimeTZDtype
:::

### Timedeltas {#api.arrays.timedelta}

NumPy can natively represent timedeltas. pandas provides
`Timedelta` for symmetry with
`Timestamp`. `NaT` is the missing value for timedelta data.

::: {.autosummary toctree="api/"}
Timedelta
:::

#### Properties

::: {.autosummary toctree="api/"}
Timedelta.asm8 Timedelta.components Timedelta.days Timedelta.max
Timedelta.microseconds Timedelta.min Timedelta.nanoseconds
Timedelta.resolution Timedelta.resolution_string Timedelta.seconds
Timedelta.unit Timedelta.value Timedelta.view
:::

#### Methods

::: {.autosummary toctree="api/"}
Timedelta.as_unit Timedelta.ceil Timedelta.floor Timedelta.isoformat
Timedelta.round Timedelta.to_pytimedelta Timedelta.to_timedelta64
Timedelta.to_numpy Timedelta.total_seconds
:::

A collection of `Timedelta` may be
stored in a `TimedeltaArray`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.TimedeltaArray
:::

### Periods {#api.arrays.period}

pandas represents spans of times as `Period` objects.

### Period

::: {.autosummary toctree="api/"}
Period
:::

#### Properties

::: {.autosummary toctree="api/"}
Period.day Period.dayofweek Period.day_of_week Period.dayofyear
Period.day_of_year Period.days_in_month Period.daysinmonth
Period.end_time Period.freq Period.freqstr Period.hour
Period.is_leap_year Period.minute Period.month Period.ordinal
Period.quarter Period.qyear Period.second Period.start_time Period.week
Period.weekday Period.weekofyear Period.year
:::

#### Methods

::: {.autosummary toctree="api/"}
Period.asfreq Period.now Period.strftime Period.to_timestamp
:::

A collection of `Period` may be stored
in a `arrays.PeriodArray`. Every period
in a `arrays.PeriodArray` must have the
same `freq`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.PeriodArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
PeriodDtype
:::

### Intervals {#api.arrays.interval}

Arbitrary intervals can be represented as `Interval` objects.

::: {.autosummary toctree="api/"}
Interval
:::

#### Properties

::: {.autosummary toctree="api/"}
Interval.closed Interval.closed_left Interval.closed_right
Interval.is_empty Interval.left Interval.length Interval.mid
Interval.open_left Interval.open_right Interval.overlaps Interval.right
:::

A collection of intervals may be stored in an
`arrays.IntervalArray`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.IntervalArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
IntervalDtype
:::

### Nullable integer {#api.arrays.integer_na}

`numpy.ndarray` cannot natively
represent integer-data with missing values. pandas provides this through
`arrays.IntegerArray`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.IntegerArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
Int8Dtype Int16Dtype Int32Dtype Int64Dtype UInt8Dtype UInt16Dtype
UInt32Dtype UInt64Dtype
:::

### Nullable float {#api.arrays.float_na}

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.FloatingArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
Float32Dtype Float64Dtype
:::

### Categoricals {#api.arrays.categorical}

pandas defines a custom data type for representing data that can take
only a limited, fixed set of values. The dtype of a
`Categorical` can be described by a
`CategoricalDtype`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
CategoricalDtype
:::

::: {.autosummary toctree="api/"}
CategoricalDtype.categories CategoricalDtype.ordered
:::

Categorical data can be stored in a
`pandas.Categorical`:

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
Categorical
:::

The alternative `Categorical.from_codes`
constructor can be used when you have the categories and integer codes
already:

::: {.autosummary toctree="api/"}
Categorical.from_codes
:::

The dtype information is available on the
`Categorical`

::: {.autosummary toctree="api/"}
Categorical.dtype Categorical.categories Categorical.ordered
Categorical.codes
:::

`np.asarray(categorical)` works by implementing the array interface. Be
aware, that this converts the `Categorical` back to a NumPy array, so categories and order information
is not preserved!

::: {.autosummary toctree="api/"}
Categorical.\_\_array\_\_
:::

A `Categorical` can be stored in a
`Series` or
`DataFrame`. To create a Series of dtype
`category`, use `cat = s.astype(dtype)` or `Series(..., dtype=dtype)`
where `dtype` is either

- the string `'category'`
- an instance of `CategoricalDtype`.

If the `Series` is of dtype
`CategoricalDtype`, `Series.cat` can be
used to change the categorical data. See
`api.series.cat` for more.

More methods are available on `Categorical`:

::: {.autosummary toctree="api/"}
Categorical.as_ordered Categorical.as_unordered
Categorical.set_categories Categorical.rename_categories
Categorical.reorder_categories Categorical.add_categories
Categorical.remove_categories Categorical.remove_unused_categories
Categorical.map
:::

### Sparse {#api.arrays.sparse}

Data where a single value is repeated many times (e.g. `0` or `NaN`) may
be stored efficiently as a `arrays.SparseArray`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.SparseArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
SparseDtype
:::

The `Series.sparse` accessor may be used to access sparse-specific
attributes and methods if the `Series`
contains sparse values. See `api.series.sparse` and `the user guide <sparse>`
for more.

### Strings {#api.arrays.string}

When working with text data, where each valid element is a string or
missing, we recommend using `StringDtype` (with the alias `"string"`).

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.StringArray arrays.ArrowStringArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
StringDtype
:::

The `Series.str` accessor is available for `Series` backed by a `arrays.StringArray`. See `api.series.str` for
more.

### Nullable Boolean {#api.arrays.bool}

The boolean dtype (with the alias `"boolean"`) provides support for
storing boolean data (`True`, `False`) with missing values, which is not
possible with a bool `numpy.ndarray`.

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
arrays.BooleanArray
:::

::: {.autosummary toctree="api/" template="autosummary/class_without_autosummary.rst"}
BooleanDtype
:::

## Utilities

### Constructors

::: {.autosummary toctree="api/"}
api.types.union_categoricals api.types.infer_dtype
api.types.pandas_dtype
:::

#### Data type introspection

::: {.autosummary toctree="api/"}
api.types.is_any_real_numeric_dtype api.types.is_bool_dtype
api.types.is_categorical_dtype api.types.is_complex_dtype
api.types.is_datetime64_any_dtype api.types.is_datetime64_dtype
api.types.is_datetime64_ns_dtype api.types.is_datetime64tz_dtype
api.types.is_dtype_equal api.types.is_extension_array_dtype
api.types.is_float_dtype api.types.is_int64_dtype
api.types.is_integer_dtype api.types.is_interval_dtype
api.types.is_numeric_dtype api.types.is_object_dtype
api.types.is_period_dtype api.types.is_signed_integer_dtype
api.types.is_string_dtype api.types.is_timedelta64_dtype
api.types.is_timedelta64_ns_dtype api.types.is_unsigned_integer_dtype
api.types.is_sparse
:::

#### Iterable introspection

::: {.autosummary toctree="api/"}
api.types.is_dict_like api.types.is_file_like api.types.is_list_like
api.types.is_named_tuple api.types.is_iterator
:::

#### Scalar introspection

::: {.autosummary toctree="api/"}
api.types.is_bool api.types.is_complex api.types.is_float
api.types.is_hashable api.types.is_integer api.types.is_number
api.types.is_re api.types.is_re_compilable api.types.is_scalar
:::