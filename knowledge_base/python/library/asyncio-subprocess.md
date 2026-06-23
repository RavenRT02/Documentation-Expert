::: currentmodule
asyncio
:::

# Subprocesses {#asyncio-subprocess}

**Source code:** `Lib/asyncio/subprocess.py`, `Lib/asyncio/base_subprocess.py`

This section describes high-level async/await asyncio APIs to create and
manage subprocesses.

::: {#asyncio_example_subprocess_shell}
Here\'s an example of how asyncio can run a shell command and obtain its
result:

    import asyncio

    async def run(cmd):
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        print(f'[{cmd!r} exited with {proc.returncode}]')
        if stdout:
            print(f'[stdout]\n{stdout.decode()}')
        if stderr:
            print(f'[stderr]\n{stderr.decode()}')

    asyncio.run(run('ls /zzz'))
:::

will print:

    ['ls /zzz' exited with 1]
    [stderr]
    ls: /zzz: No such file or directory

Because all asyncio subprocess functions are asynchronous and asyncio
provides many tools to work with such functions, it is easy to execute
and monitor multiple subprocesses in parallel. It is indeed trivial to
modify the above example to run several commands simultaneously:

    async def main():
        await asyncio.gather(
            run('ls /zzz'),
            run('sleep 1; echo "hello"'))

    asyncio.run(main())

See also the Examples subsection.

## Creating Subprocesses

:::: {.function async=""}
create_subprocess_exec(program, *args, stdin=None, stdout=None,
stderr=None, limit=None,*\*kwds)

Create a subprocess.

The *limit* argument sets the buffer limit for
`StreamReader` wrappers for
`~asyncio.subprocess.Process.stdout` and
`~asyncio.subprocess.Process.stderr` (if
`subprocess.PIPE` is passed to *stdout*
and *stderr* arguments).

Return a `~asyncio.subprocess.Process`
instance.

See the documentation of `loop.subprocess_exec` for other parameters.

If the process object is garbage collected while the process is still
running, the child process will be killed.

::: versionchanged
3.10 Removed the *loop* parameter.
:::
::::

:::::: {.function async=""}
create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None,
limit=None, \*\*kwds)

Run the *cmd* shell command.

The *limit* argument sets the buffer limit for
`StreamReader` wrappers for
`~asyncio.subprocess.Process.stdout` and
`~asyncio.subprocess.Process.stderr` (if
`subprocess.PIPE` is passed to *stdout*
and *stderr* arguments).

Return a `~asyncio.subprocess.Process`
instance.

See the documentation of `loop.subprocess_shell` for other parameters.

If the process object is garbage collected while the process is still
running, the child process will be killed.

:::: important
::: title
Important
:::

It is the application\'s responsibility to ensure that all whitespace
and special characters are quoted appropriately to avoid [shell
injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection)
vulnerabilities. The `shlex.quote`
function can be used to properly escape whitespace and special shell
characters in strings that are going to be used to construct shell
commands.
::::

::: versionchanged
3.10 Removed the *loop* parameter.
:::
::::::

:::: note
::: title
Note
:::

Subprocesses are available for Windows if a
`ProactorEventLoop` is used. See
`Subprocess Support on Windows <asyncio-windows-subprocess>` for details.
::::

::: seealso
asyncio also has the following *low-level* APIs to work with
subprocesses: `loop.subprocess_exec`,
`loop.subprocess_shell`,
`loop.connect_read_pipe`,
`loop.connect_write_pipe`, as well as the
`Subprocess Transports <asyncio-subprocess-transports>` and
`Subprocess Protocols <asyncio-subprocess-protocols>`.
:::

## Constants

::: {.data module=""}
asyncio.subprocess.PIPE

Can be passed to the *stdin*, *stdout* or *stderr* parameters.

If *PIPE* is passed to *stdin* argument, the
`Process.stdin <asyncio.subprocess.Process.stdin>` attribute will point to a
`~asyncio.StreamWriter` instance.

If *PIPE* is passed to *stdout* or *stderr* arguments, the
`Process.stdout <asyncio.subprocess.Process.stdout>` and
`Process.stderr <asyncio.subprocess.Process.stderr>` attributes will point to
`~asyncio.StreamReader` instances.
:::

::: {.data module=""}
asyncio.subprocess.STDOUT

Special value that can be used as the *stderr* argument and indicates
that standard error should be redirected into standard output.
:::

::: {.data module=""}
asyncio.subprocess.DEVNULL

Special value that can be used as the *stdin*, *stdout* or *stderr*
argument to process creation functions. It indicates that the special
file `os.devnull` will be used for the
corresponding subprocess stream.
:::

## Interacting with Subprocesses

Both `create_subprocess_exec` and
`create_subprocess_shell` functions
return instances of the *Process* class. *Process* is a high-level
wrapper that allows communicating with subprocesses and watching for
their completion.

:::::::::::::::::::: {.asyncio.subprocess.Process module=""}
An object that wraps OS processes created by the
`~asyncio.create_subprocess_exec` and
`~asyncio.create_subprocess_shell`
functions.

This class is designed to have a similar API to the
`subprocess.Popen` class, but there are
some notable differences:

- unlike Popen, Process instances do not have an equivalent to the
  `~subprocess.Popen.poll` method;
- the `~asyncio.subprocess.Process.communicate` and `~asyncio.subprocess.Process.wait` methods don\'t have a *timeout* parameter: use the
  `~asyncio.wait_for` function;
- the
  `Process.wait() <asyncio.subprocess.Process.wait>` method is asynchronous, whereas
  `subprocess.Popen.wait` method is
  implemented as a blocking busy loop;
- the *universal_newlines* parameter is not supported.

This class is
`not thread safe <asyncio-multithreading>`.

See also the
`Subprocess and Threads <asyncio-subprocess-threads>` section.

::::: {.method async=""}
wait()

Wait for the child process to terminate.

Set and return the `returncode`
attribute.

:::: note
::: title
Note
:::

This method can deadlock when using `stdout=PIPE` or `stderr=PIPE` and
the child process generates so much output that it blocks waiting for
the OS pipe buffer to accept more data. Use the
`communicate` method when using pipes to
avoid this condition.
::::
:::::

:::: {.method async=""}
communicate(input=None)

Interact with process:

1.  send data to *stdin* (if *input* is not `None`);
2.  closes *stdin*;
3.  read data from *stdout* and *stderr*, until EOF is reached;
4.  wait for process to terminate.

The optional *input* argument is the data (`bytes` object) that will be sent to the child process.

Return a tuple `(stdout_data, stderr_data)`.

If either `BrokenPipeError` or
`ConnectionResetError` exception is raised
when writing *input* into *stdin*, the exception is ignored. This
condition occurs when the process exits before all data are written into
*stdin*.

If it is desired to send data to the process\' *stdin*, the process
needs to be created with `stdin=PIPE`. Similarly, to get anything other
than `None` in the result tuple, the process has to be created with
`stdout=PIPE` and/or `stderr=PIPE` arguments.

Note, that the data read is buffered in memory, so do not use this
method if the data size is large or unlimited.

::: versionchanged
3.12

*stdin* gets closed when `input=None` too.
:::
::::

::::: method
send_signal(signal)

Sends the signal *signal* to the child process.

:::: note
::: title
Note
:::

On Windows, `~signal.SIGTERM` is an
alias for `terminate`. `CTRL_C_EVENT` and
`CTRL_BREAK_EVENT` can be sent to processes started with a
*creationflags* parameter which includes `CREATE_NEW_PROCESS_GROUP`.
::::
:::::

::: method
terminate()

Stop the child process.

On POSIX systems this method sends `~signal.SIGTERM` to the child process.

On Windows the Win32 API function `!TerminateProcess` is called to stop the child process.
:::

::: method
kill()

Kill the child process.

On POSIX systems this method sends `~signal.SIGKILL` to the child process.

On Windows this method is an alias for `terminate`.
:::

::: attribute
stdin

Standard input stream (`~asyncio.StreamWriter`) or `None` if the process was created with `stdin=None`.
:::

::: attribute
stdout

Standard output stream (`~asyncio.StreamReader`) or `None` if the process was created with `stdout=None`.
:::

::: attribute
stderr

Standard error stream (`~asyncio.StreamReader`) or `None` if the process was created with `stderr=None`.
:::

:::: warning
::: title
Warning
:::

Use the `communicate` method rather than
`process.stdin.write() <stdin>`,
`await process.stdout.read() <stdout>` or
`await process.stderr.read() <stderr>`.
This avoids deadlocks due to streams pausing reading or writing and
blocking the child process.
::::

::: attribute
pid

Process identification number (PID).

Note that for processes created by the
`~asyncio.create_subprocess_shell`
function, this attribute is the PID of the spawned shell.
:::

::: attribute
returncode

Return code of the process when it exits.

A `None` value indicates that the process has not terminated yet.

For processes created with
`~asyncio.create_subprocess_exec`, a
negative value `-N` indicates that the child was terminated by signal
`N` (POSIX only).

For processes created with
`~asyncio.create_subprocess_shell`, the
return code reflects the exit status of the shell itself (e.g.
`/bin/sh`), which may map signals to codes such as `128+N`. See the
documentation of the shell (for example, the Bash manual\'s Exit Status)
for details.
:::
::::::::::::::::::::

### Subprocess and Threads {#asyncio-subprocess-threads}

Standard asyncio event loop supports running subprocesses from different
threads by default.

On Windows subprocesses are provided by
`ProactorEventLoop` only (default),
`SelectorEventLoop` has no subprocess
support.

Note that alternative event loop implementations might have own
limitations; please refer to their documentation.

::: seealso
The `Concurrency and multithreading in asyncio
<asyncio-multithreading>` section.
:::

### Examples

An example using the `~asyncio.subprocess.Process` class to control a subprocess and the
`StreamReader` class to read from its
standard output.

::: {#asyncio_example_create_subprocess_exec}
The subprocess is created by the
`create_subprocess_exec` function:

    import asyncio
    import sys

    async def get_date():
        code = 'import datetime as dt; print(dt.datetime.now())'

        # Create the subprocess; redirect the standard output
        # into a pipe.
        proc = await asyncio.create_subprocess_exec(
            sys.executable, '-c', code,
            stdout=asyncio.subprocess.PIPE)

        # Read one line of output.
        data = await proc.stdout.readline()
        line = data.decode('ascii').rstrip()

        # Wait for the subprocess exit.
        await proc.wait()
        return line

    date = asyncio.run(get_date())
    print(f"Current date: {date}")
:::

See also the
`same example <asyncio_example_subprocess_proto>` written using low-level APIs.