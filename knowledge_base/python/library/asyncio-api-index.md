::: currentmodule
asyncio
:::

# High-level API Index

This page lists all high-level async/await enabled asyncio APIs.

## Tasks

Utilities to run asyncio programs, create Tasks, and await on multiple
things with timeouts.

  ---------------------------------------------- -----------------------------------
  `run`           Create event loop, run a coroutine,
                                                 close the loop.

  `Runner`       A context manager that simplifies
                                                 multiple async function calls.

  `Task`         Task object.

  `TaskGroup`    A context manager that holds a
                                                 group of tasks. Provides a
                                                 convenient and reliable way to wait
                                                 for all tasks in the group to
                                                 finish.

  `create_task`   Start an asyncio Task, then returns
                                                 it.

  `current_task`  Return the current Task.

  `all_tasks`     Return all tasks that are not yet
                                                 finished for an event loop.

  `await` `sleep` Sleep for a number of seconds.

  `await` `gather`                                   concurrently.

  `await` `wait_for`

  `await` `shield`

  `await` `wait`  Monitor for completion.

  `timeout`       Run with a timeout. Useful in cases
                                                 when `wait_for` is not suitable.

  `to_thread`     Asynchronously run a function in a
                                                 separate OS thread.

  `run_coroutine_threadsafe`                                   OS thread.

  `for in` `as_completed`                                   loop.
  ---------------------------------------------- -----------------------------------

**Examples**

- `Using asyncio.gather() to run things in parallel
  <asyncio_example_gather>`.
- `Using asyncio.wait_for() to enforce a timeout
  <asyncio_example_waitfor>`.
- `Cancellation <asyncio_example_task_cancel>`.
- `Using asyncio.sleep() <asyncio_example_sleep>`.
- See also the main
  `Tasks documentation page <coroutine>`.

## Queues

Queues should be used to distribute work amongst multiple asyncio Tasks,
implement connection pools, and pub/sub patterns.

  ----------------------------------- -----------------------------------
  `Queue`

  `PriorityQueue`

  `LifoQueue`
  ----------------------------------- -----------------------------------

**Examples**

- `Using asyncio.Queue to distribute workload between several
  Tasks <asyncio_example_queue_dist>`.
- See also the
  `Queues documentation page <asyncio-queues>`.

## Subprocesses

Utilities to spawn subprocesses and run shell commands.

  --------------------------------------------- -----------------------------------
  `await`                                       Create a subprocess.
  `create_subprocess_exec`

  `await`                                       Run a shell command.
  `create_subprocess_shell`
  --------------------------------------------- -----------------------------------

**Examples**

- `Executing a shell command <asyncio_example_subprocess_shell>`.
- See also the `subprocess APIs <asyncio-subprocess>` documentation.

## Streams

High-level APIs to work with network IO.

  ------------------------------------------ -----------------------------------
  `await`                                    Establish a TCP connection.
  `open_connection`

  `await`                                    Establish a Unix socket connection.
  `open_unix_connection`

  `await` `start_server`

  `await`                                    Start a Unix socket server.
  `start_unix_server`

  `StreamReader`                              receive network data.

  `StreamWriter`                              send network data.
  ------------------------------------------ -----------------------------------

**Examples**

- `Example TCP client <asyncio_example_stream>`.
- See also the `streams APIs <asyncio-streams>` documentation.

## Synchronization

Threading-like synchronization primitives that can be used in Tasks.

  -------------------------------------- -----------------------------------
  `Lock` A mutex lock.

  `Event`

  `Condition`

  `Semaphore`

  `BoundedSemaphore`

  `Barrier`
  -------------------------------------- -----------------------------------

**Examples**

- `Using asyncio.Event <asyncio_example_sync_event>`.
- `Using asyncio.Barrier <asyncio_example_barrier>`.
- See also the documentation of asyncio
  `synchronization primitives <asyncio-sync>`.

## Exceptions

  ------------------------------------------------ -----------------------------------
  `asyncio.CancelledError`                                      See also
                                                   `Task.cancel`.

  `asyncio.BrokenBarrierError`                                      See also
                                                   `Barrier.wait`.
  ------------------------------------------------ -----------------------------------

**Examples**

- `Handling CancelledError to run code on cancellation request
  <asyncio_example_task_cancel>`.
- See also the full list of
  `asyncio-specific exceptions <asyncio-exceptions>`.