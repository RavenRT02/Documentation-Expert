# `!tty` \-\-- Terminal control functions

::: {.module synopsis="Utility functions that perform common terminal control operations."}
tty
:::

**Source code:** `Lib/tty.py`

The `!tty` module defines functions for
putting the tty into cbreak and raw modes.

::: availability
Unix.
:::

Because it requires the `termios` module,
it will work only on Unix.

The `!tty` module defines the following
functions:

:::: function
cfmakeraw(mode)

Convert the tty attribute list *mode*, which is a list like the one
returned by `termios.tcgetattr`, to that
of a tty in raw mode.

::: versionadded
3.12
:::
::::

::::: function
cfmakecbreak(mode)

Convert the tty attribute list *mode*, which is a list like the one
returned by `termios.tcgetattr`, to that
of a tty in cbreak mode.

This clears the `ECHO` and `ICANON` local mode flags in *mode* as well
as setting the minimum input to 1 byte with no delay.

::: versionadded
3.12
:::

::: versionchanged
3.12.2 The `ICRNL` flag is no longer cleared. This matches Linux and
macOS `stty cbreak` behavior and what `setcbreak` historically did.
:::
:::::

:::: function
setraw(fd, when=termios.TCSAFLUSH)

Change the mode of the file descriptor *fd* to raw. If *when* is
omitted, it defaults to `termios.TCSAFLUSH`, and is passed to `termios.tcsetattr`. The return value of `termios.tcgetattr` is saved before setting *fd* to raw mode; this value is
returned.

::: versionchanged
3.12 The return value is now the original tty attributes, instead of
`None`.
:::
::::

::::: function
setcbreak(fd, when=termios.TCSAFLUSH)

Change the mode of file descriptor *fd* to cbreak. If *when* is omitted,
it defaults to `termios.TCSAFLUSH`, and
is passed to `termios.tcsetattr`. The
return value of `termios.tcgetattr` is
saved before setting *fd* to cbreak mode; this value is returned.

This clears the `ECHO` and `ICANON` local mode flags as well as setting
the minimum input to 1 byte with no delay.

::: versionchanged
3.12 The return value is now the original tty attributes, instead of
`None`.
:::

::: versionchanged
3.12.2 The `ICRNL` flag is no longer cleared. This restores the behavior
of Python 3.11 and earlier as well as matching what Linux, macOS, & BSDs
describe in their `stty(1)` man pages regarding cbreak mode.
:::
:::::

::: seealso

Module `termios`

: Low-level terminal control interface.
:::