{{ header }}

# Resampling {#api.resampling}

::: currentmodule
pandas.api.typing
:::

:::: note
::: title
Note
:::

For an overview, see `timeseries`.
::::

`pandas.api.typing.Resampler` instances
are returned by resample calls:
`pandas.DataFrame.resample`,
`pandas.Series.resample`.

## Indexing, iteration

::: {.autosummary toctree="api/"}
Resampler.\_\_iter\_\_ Resampler.groups Resampler.indices
Resampler.get_group
:::

## Function application

::: {.autosummary toctree="api/"}
Resampler.apply Resampler.aggregate Resampler.transform Resampler.pipe
:::

## Upsampling

::: {.autosummary toctree="api/"}
Resampler.ffill Resampler.bfill Resampler.nearest Resampler.asfreq
Resampler.interpolate
:::

## Computations / descriptive stats

::: {.autosummary toctree="api/"}
Resampler.count Resampler.nunique Resampler.first Resampler.last
Resampler.max Resampler.mean Resampler.median Resampler.min
Resampler.ohlc Resampler.prod Resampler.size Resampler.sem Resampler.std
Resampler.sum Resampler.var Resampler.quantile
:::