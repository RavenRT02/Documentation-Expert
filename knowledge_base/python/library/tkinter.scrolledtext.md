# `!tkinter.scrolledtext` \-\-- Scrolled text widget

::: {.module synopsis="Text widget with a vertical scroll bar."}
tkinter.scrolledtext
:::

**Source code:** `Lib/tkinter/scrolledtext.py`

The `!tkinter.scrolledtext` module
provides a class of the same name which implements a basic text widget
which has a vertical scroll bar configured to do the \"right thing.\"
Using the `ScrolledText` class is a lot
easier than setting up a text widget and scroll bar directly.

The text widget and scrollbar are packed together in a
`~tkinter.Frame`, and the methods of the
`~tkinter.Pack`,
`~tkinter.Grid` and
`~tkinter.Place` geometry managers are
acquired from the `~tkinter.Frame`
object. This allows the `ScrolledText`
widget to be used directly to achieve most normal geometry management
behavior.

Should more specific control be necessary, the following attributes are
available:

::::: {.ScrolledText(master=None, .**kw)}
::: attribute
frame

The frame which surrounds the text and scroll bar widgets.
:::

::: attribute
vbar

The scroll bar widget.
:::
:::::