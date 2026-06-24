{{ header }}

::: {#api.typing.aliases}
{{ header }}
:::

# pandas typing aliases

## Typing aliases

::: module
pandas.api.typing.aliases
:::

<style>
td > dl.py.type { margin-bottom: 0; }
td > dl.py.type .descclassname { display: none; }
</style>

The typing declarations in `pandas/_typing.py` are considered private,
and used by pandas developers for type checking of the pandas code base.
For users, it is highly recommended to use the `pandas-stubs` package
that represents the officially supported type declarations for users of
pandas. They are documented here for users who wish to use these
declarations in their own python code that calls pandas or expects
certain results.

:::: warning
::: title
Warning
:::

Note that the definitions and use cases of these aliases are subject to
change without notice in any major, minor, or patch release of pandas.
::::

Each of these aliases listed in the table below can be found by
importing them from `pandas.api.typing.aliases`.

+---------------------------+---------------------------------------------------------------------------------------+
| Alias                     | Meaning                                                                               |
+===========================+=======================================================================================+
| ::: type                  | Type of functions that can be passed to                                               |
| AggFuncType               | `DataFrame's <pandas.DataFrame.agg>`,                  |
| :::                       | `Series' <pandas.Series.agg>`, and                     |
|                           | `DataFrameGroupBy's <pandas.api.typing.DataFrameGroupBy.aggregate>` `aggregate()` methods                                                    |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `join` in `DataFrame's <pandas.DataFrame.align>` and `Series' <pandas.Series.align>`       |
| :::                       | `align()` methods                                                                     |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `how` in `DataFrame's <pandas.DataFrame.dropna>` and `Series' <pandas.Series.dropna>`      |
| :::                       | `dropna()` methods                                                                    |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Used to represent `~pandas.api.extensions.ExtensionArray`, `numpy` arrays, `~pandas.Index` and    |
| :::                       | `~pandas.Series`                                      |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Used to represent `~pandas.api.extensions.ExtensionArray`, `numpy` arrays                                                         |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type in `DataFrame's <pandas.DataFrame.astype>` and `Series' <pandas.Series.astype>`      |
| :::                       | `astype()` methods                                                                    |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | `AnyArrayLike` plus sequences (not strings) and     |
| Axes                      | `range`                                                                               |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `axis` in many methods                                              |
| Axis                      |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `engine` in `pandas.read_csv`        |
| CSVEngine                 |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `colspace` in `pandas.DataFrame.to_html`                                                                          |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `compression` in all I/O output methods except                      |
| CompressionOptions        | `pandas.DataFrame.to_parquet`                          |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `correlation` in                                                    |
| CorrelationMethod         | `DataFrame's <pandas.DataFrame.corr>` and              |
| :::                       | `Series' <pandas.Series.corr>` `corr()` methods        |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `keep` in                                                           |
| DropKeep                  | `DataFrame's <pandas.DataFrame.drop_duplicates>` and   |
| :::                       | `Series' <pandas.Series.drop_duplicates>`              |
|                           | `drop_duplicates()` methods                                                           |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Types as objects that can be used to specify dtypes                                   |
| Dtype                     |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `dtype` in various methods                                          |
| DtypeArg                  |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `dtype_backend` in various methods                                  |
| DtypeBackend              |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Numpy dtypes and Extension dtypes                                                     |
| DtypeObj                  |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `if_sheet_exists` in `~pandas.ExcelWriter`                                                                         |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `merge_cells` in                                                    |
| ExcelWriterMergeCells     | `DataFrame's <pandas.DataFrame.to_excel>` and          |
| :::                       | `Series' <pandas.Series.to_excel>` `to_excel()`        |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Type of paths for files for I/O methods                                               |
| FilePath                  |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `method` in various methods where NA values are filled              |
| FillnaOptions             |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `float_format` in                                                   |
| FloatFormatType           | `DataFrame's <pandas.DataFrame.to_string>` and         |
| :::                       | `Series' <pandas.Series.to_string>` `to_string()`      |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `formatters` in                                                     |
| FormattersType            | `DataFrame's <pandas.DataFrame.to_string>` and         |
| :::                       | `Series' <pandas.Series.to_string>` `to_string()`      |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `orient` in                                                         |
| FromDictOrient            | `DataFrame.from_dict() <pandas.DataFrame.from_dict>`   |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `flavor` in `pandas.read_html`       |
| HTMLFlavors               |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `errors` in multiple methods                                        |
| IgnoreRaise               |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `level` in multiple methods                                         |
| IndexLabel                |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `interpolate` in                                                    |
| InterpolateOptions        | `DataFrame's <pandas.DataFrame.interpolate>` and       |
| :::                       | `Series' <pandas.Series.interpolate>` `interpolate()`  |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `closed` in `~pandas.Interval`,     |
| IntervalClosedType        | `~pandas.IntervalIndex`, and `inclusive` in various   |
| :::                       | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Restriction for `closed` to be `left` or `right` in                                   |
| IntervalLeftRight         | `~pandas.Interval`,                                   |
| :::                       | `~pandas.IntervalIndex`, and `inclusive` in various   |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `engine` in `pandas.read_json`       |
| JSONEngine                |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for the return type of a callable for argument `default_handler` in     |
| JSONSerializable          | `DataFrame's <pandas.DataFrame.to_json>` and           |
| :::                       | `Series' <pandas.Series.to_json>` `to_json()` methods  |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `how` in `pandas.merge_ordered` and  |
| JoinHow                   | for `join` in `Series.align() <pandas.Series.align>`   |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `validate` in                                                       |
| JoinValidate              | `DataFrame.join() <pandas.DataFrame.join>`             |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for arguments that can be either a single value or a list of values in  |
| ListLike                  | various methods                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `how` in `pandas.merge`              |
| MergeHow                  |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `validate` in `pandas.merge`         |
| MergeValidate             |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `na_position` in                                                    |
| NaPosition                | `DataFrame's <pandas.DataFrame.sort_values>` and       |
| :::                       | `Series' <pandas.Series.sort_values>` `sort_values()`  |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `keep` in                                                           |
| NsmallestNlargestKeep     | `DataFrame's <pandas.DataFrame.nlargest>` and          |
| :::                       | `Series' <pandas.Series.nlargest>` `nlargest()`,       |
|                           | `DataFrame's <pandas.DataFrame.nsmallest>` and         |
|                           | `Series' <pandas.Series.nsmallest>` `nsmallest()`, and |
|                           | `SeriesGroupBy's <pandas.api.typing.SeriesGroupBy.nlargest>` `nlargest()` methods                                                     |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `errors` in                                                         |
| OpenFileErrors            | `DataFrame's <pandas.DataFrame.to_hdf>`,               |
| :::                       | `Series' <pandas.Series.to_hdf>` `to_hdf()` methods,   |
|                           | and `DataFrame's <pandas.DataFrame.to_csv>` and        |
|                           | `Series' <pandas.Series.to_csv>` `to_csv()` methods    |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Return type for `ordered <pandas.CategoricalDtype.ordered>` in `pandas.CategoricalDtype` and         |
| :::                       | `pandas.Categorical`                                  |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `compression` in                                                    |
| ParquetCompressionOptions | `DataFrame.to_parquet() <pandas.DataFrame.to_parquet>` |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `interpolation` in                                                  |
| QuantileInterpolation     | `DataFrame's <pandas.DataFrame.quantile>` and          |
| :::                       | `Series' <pandas.Series.quantile>` `quantile()`        |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Additional argument type corresponding to buffers for various file reading methods    |
| ReadBuffer                |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Additional argument type corresponding to buffers for                                 |
| ReadCsvBuffer             | `pandas.read_csv`                                      |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Additional argument type corresponding to buffers for                                 |
| ReadPickleBuffer          | `pandas.read_pickle`                                   |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `reindex` in                                                        |
| ReindexMethod             | `DataFrame's <pandas.DataFrame.reindex>` and           |
| :::                       | `Series' <pandas.Series.reindex>` `reindex()` methods  |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Types that can be stored in `~pandas.Series` with     |
| Scalar                    | non-object dtype                                                                      |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type used for scalar indexing operations, such as the `key` argument in      |
| ScalarIndexer             | `__getitem__()` methods                                                               |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type used for sequence indexing operations, such as the `key` argument in    |
| SequenceIndexer           | `__getitem__()` methods                                                               |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Used for arguments that require sequences, but not plain strings                      |
| SequenceNotStr            |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument types for `start` and `end` in                                               |
| SliceType                 | `Index.slice_locs() <pandas.Index.slice_locs>`         |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `kind` in                                                           |
| SortKind                  | `DataFrame's <pandas.DataFrame.sort_values>` and       |
| :::                       | `Series' <pandas.Series.sort_values>` `sort_values()`  |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `storage_options` in various file output methods                    |
| StorageOptions            |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `suffixes` in `pandas.merge`,        |
| Suffixes                  | `pandas.merge_ordered`, and                            |
| :::                       | `DataFrame's <pandas.DataFrame.compare>` and           |
|                           | `Series' <pandas.Series.compare>` `compare()` methods  |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `indexer` and `indices` in                                          |
| TakeIndexer               | `DataFrame's <pandas.DataFrame.take>` and              |
| :::                       | `Series' <pandas.Series.take>` `take()` methods        |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `ambiguous` in time operations                                      |
| TimeAmbiguous             |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `origin` in                                                         |
| TimeGrouperOrigin         | `DataFrame's <pandas.DataFrame.resample>`,             |
| :::                       | `Series' <pandas.Series.resample>` `resample()`        |
|                           | methods and for `~pandas.Grouper`                     |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `nonexistent` in time operations                                    |
| TimeNonexistent           |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Time unit argument and return type for `pandas.Timedelta.unit`, arguments `unit` and `date_unit`                                        |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `offset` in various methods, such as                                |
| TimedeltaConvertibleTypes | `DataFrame's <pandas.DataFrame.resample>` and          |
| :::                       | `Series' <pandas.Series.resample>` `resample()`,       |
|                           | `halflife` in `DataFrame's <pandas.DataFrame.ewm>`,    |
|                           | `DataFrameGroupBy's <pandas.api.typing.DataFrameGroupBy.ewm>`, and `Series' <pandas.Series.ewm>`        |
|                           | `ewm()`, and `start` and `end` in `pandas.timedelta_range`                                                                          |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `origin` in                                                         |
| TimestampConvertibleTypes | `DataFrame's <pandas.DataFrame.resample>` and          |
| :::                       | `Series' <pandas.Series.resample>` `resample()`, and   |
|                           | in `pandas.to_datetime`                                |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `byteorder` in                                                      |
| ToStataByteorder          | `DataFrame.to_stata() <pandas.DataFrame.to_stata>`     |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `how` in                                                            |
| ToTimestampHow            | `DataFrame's <pandas.DataFrame.to_timestamp>` and      |
| :::                       | `Series' <pandas.Series.to_timestamp>`                 |
|                           | `to_timestamp()` methods, and `convention` in                                         |
|                           | `DataFrame's <pandas.DataFrame.resample>` and          |
|                           | `Series' <pandas.Series.resample>` `resample()`        |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `join` in                                                           |
| UpdateJoin                | `DataFrame.update() <pandas.DataFrame.update>`         |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `usecols` in `pandas.read_clipboard`, `pandas.read_csv` and                    |
| :::                       | `pandas.read_excel`                                    |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `method` in                                                         |
| WindowingRankType         | `Rolling's <pandas.api.typing.Rolling.rank>` and       |
| :::                       | `Expanding's <pandas.api.typing.Expanding.rank>`       |
|                           | `rank()` methods, applicable in rolling and expanding window operations               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Additional argument type corresponding to buffers for various file output methods     |
| WriteBuffer               |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Additional argument type corresponding to buffers for                                 |
| WriteExcelBuffer          | `DataFrame's <pandas.DataFrame.to_excel>`,             |
| :::                       | `Series' <pandas.Series.to_excel>` and                 |
|                           | `Styler's <pandas.io.formats.style.Styler.to_excel>`   |
|                           | `to_excel()` methods                                                                  |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `parser` in                                                         |
| XMLParsers                | `DataFrame.to_xml() <pandas.DataFrame.to_xml>` and     |
| :::                       | `pandas.read_xml`                                      |
+---------------------------+---------------------------------------------------------------------------------------+