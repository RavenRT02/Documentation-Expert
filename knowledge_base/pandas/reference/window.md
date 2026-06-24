{{ header }}

# Window {#api.window}

:::: note
::: title
Note
:::

For an overview, see `window`.
::::

`pandas.api.typing.Rolling` instances
are returned by `.rolling` calls:
`pandas.DataFrame.rolling` and
`pandas.Series.rolling`.
`pandas.api.typing.Expanding` instances
are returned by `.expanding` calls:
`pandas.DataFrame.expanding` and
`pandas.Series.expanding`.
`pandas.api.typing.ExponentialMovingWindow` instances are returned by `.ewm` calls:
`pandas.DataFrame.ewm` and
`pandas.Series.ewm`.

## Rolling window functions {#api.functions_rolling}

::: currentmodule
pandas.api.typing
:::

::: {.autosummary toctree="api/"}
Rolling.count Rolling.sum Rolling.mean Rolling.median Rolling.var
Rolling.std Rolling.min Rolling.max Rolling.first Rolling.last
Rolling.corr Rolling.cov Rolling.skew Rolling.kurt Rolling.apply
Rolling.pipe Rolling.aggregate Rolling.quantile Rolling.sem Rolling.rank
Rolling.nunique
:::

## Weighted window functions {#api.functions_window}

::: currentmodule
pandas.api.typing
:::

::: {.autosummary toctree="api/"}
Window.mean Window.sum Window.var Window.std
:::

## Expanding window functions {#api.functions_expanding}

::: currentmodule
pandas.api.typing
:::

::: {.autosummary toctree="api/"}
Expanding.count Expanding.sum Expanding.mean Expanding.median
Expanding.var Expanding.std Expanding.min Expanding.max Expanding.first
Expanding.last Expanding.corr Expanding.cov Expanding.skew
Expanding.kurt Expanding.apply Expanding.pipe Expanding.aggregate
Expanding.quantile Expanding.sem Expanding.rank Expanding.nunique
:::

## Exponentially-weighted window functions {#api.functions_ewm}

::: currentmodule
pandas.api.typing
:::

::: {.autosummary toctree="api/"}
ExponentialMovingWindow.mean ExponentialMovingWindow.sum
ExponentialMovingWindow.std ExponentialMovingWindow.var
ExponentialMovingWindow.corr ExponentialMovingWindow.cov
:::

## Window indexer {#api.indexers_window}

::: currentmodule
pandas
:::

Base class for defining custom window boundaries.

::: {.autosummary toctree="api/"}
api.indexers.BaseIndexer api.indexers.FixedForwardWindowIndexer
api.indexers.VariableOffsetWindowIndexer
:::