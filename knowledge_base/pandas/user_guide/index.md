{{ header }}

# User Guide {#user_guide}

The User Guide covers all of pandas by topic area. Each of the
subsections introduces a topic (such as \"working with missing data\"),
and discusses how pandas approaches the problem, with many examples
throughout.

Users brand-new to pandas should start with `10min`.

For a high level summary of the pandas fundamentals, see
`dsintro` and `basics`.

Further information on any specific method can be obtained in the
`api`.

## How to read these guides

In these guides you will see input code inside code blocks such as:

    import pandas as pd
    pd.DataFrame({'A': [1, 2, 3]})

or:

::: ipython
python

import pandas as pd pd.DataFrame({\'A\': \[1, 2, 3\]})
:::

The first block is a standard Python input, while in the second the
`In [1]:` indicates the input is inside a
[notebook](https://jupyter.org). In Jupyter Notebooks the last line is
printed and plots are shown inline.

For example:

::: ipython
python

a = 1 a
:::

is equivalent to:

    a = 1
    print(a)

## Guides

::: {.toctree maxdepth="2"}
10min dsintro basics io pyarrow indexing advanced merging reshaping text
missing_data duplicates categorical integer_na boolean visualization
style user_defined_functions groupby window timeseries timedeltas
options enhancingperf scale sparse gotchas migration cookbook
:::