::: currentmodule
asyncio
:::

# Exceptions {#asyncio-exceptions}

**Source code:** `Lib/asyncio/exceptions.py`

:::: exception
TimeoutError

A deprecated alias of `TimeoutError`,
raised when the operation has exceeded the given deadline.

::: versionchanged
3.11

This class was made an alias of `TimeoutError`.
:::
::::

:::: exception
CancelledError

The operation has been cancelled.

This exception can be caught to perform custom operations when asyncio
Tasks are cancelled. In almost all situations the exception must be
re-raised.

::: versionchanged
3.8

`CancelledError` is now a subclass of
`BaseException` rather than
`Exception`.
:::
::::

::: exception
InvalidStateError

Invalid internal state of `Task` or
`Future`.

Can be raised in situations like setting a result value for a *Future*
object that already has a result value set.
:::

::: exception
SendfileNotAvailableError

The \"sendfile\" syscall is not available for the given socket or file
type.

A subclass of `RuntimeError`.
:::

::::: exception
IncompleteReadError

The requested read operation did not complete fully.

Raised by the `asyncio stream APIs<asyncio-streams>`.

This exception is a subclass of `EOFError`.

::: attribute
expected

The total number (`int`) of expected
bytes.
:::

::: attribute
partial

A string of `bytes` read before the end
of stream was reached.
:::
:::::

:::: exception
LimitOverrunError

Reached the buffer size limit while looking for a separator.

Raised by the `asyncio stream APIs <asyncio-streams>`.

::: attribute
consumed

The total number of to be consumed bytes.
:::
::::