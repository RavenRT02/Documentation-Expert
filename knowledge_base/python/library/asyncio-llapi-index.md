::: currentmodule
asyncio
:::

# Low-level API Index

This page lists all low-level asyncio APIs.

## Obtaining the Event Loop

  ---------------------------------------------- -----------------------------------
  `asyncio.get_running_loop`                                   the running event loop.

  `asyncio.get_event_loop`                                   or current via the current policy).

  `asyncio.set_event_loop`                                   the current policy.

  `asyncio.new_event_loop`
  ---------------------------------------------- -----------------------------------

**Examples**

- `Using asyncio.get_running_loop() <asyncio_example_future>`.

## Event Loop Methods

See also the main documentation section about the
`asyncio-event-loop-methods`.

**Lifecycle**

  --------------------------------------------- -----------------------------------
  `loop.run_until_complete`                                  complete.

  `loop.run_forever`

  `loop.stop`    Stop the event loop.

  `loop.close`   Close the event loop.

  `loop.is_running`                                  running.

  `loop.is_closed`                                  closed.

  `await`                                       Close asynchronous generators.
  `loop.shutdown_asyncgens`
  --------------------------------------------- -----------------------------------

**Debugging**

  ------------------------------------ -----------------------------------
  `loop.set_debug`

  `loop.get_debug`
  ------------------------------------ -----------------------------------

**Scheduling Callbacks**

  ----------------------------------------------- ------------------------------------
  `loop.call_soon` Invoke a callback soon.

  `loop.call_soon_threadsafe`                                    `loop.call_soon`.

  `loop.call_later`                                    time.

  `loop.call_at`   Invoke a callback *at* the given
                                                  time.
  ----------------------------------------------- ------------------------------------

**Thread/Interpreter/Process Pool**

  ----------------------------------------------- ------------------------------------------
  `await`                                         Run a CPU-bound or other blocking function
  `loop.run_in_executor`                                    `concurrent.futures` executor.

  `loop.set_default_executor`                                    `loop.run_in_executor`.
  ----------------------------------------------- ------------------------------------------

**Tasks and Futures**

  ------------------------------------------- --------------------------------------
  `loop.create_future`                                role="class"} object.

  `loop.create_task`                                `Task`.

  `loop.set_task_factory`                                `loop.create_task` to create
                                              `Tasks <Task>`.

  `loop.get_task_factory`                                `loop.create_task` uses to create
                                              `Tasks <Task>`.
  ------------------------------------------- --------------------------------------

**DNS**

  -------------------------------------- ----------------------------------------
  `await`                                Asynchronous version of
  `loop.getaddrinfo`                           role="meth"}.

  `await`                                Asynchronous version of
  `loop.getnameinfo`                           role="meth"}.
  -------------------------------------- ----------------------------------------

**Networking and IPC**

  --------------------------------------------------- ------------------------------------
  `await` `loop.create_connection`

  `await` `loop.create_server`

  `await`                                             Open a Unix socket connection.
  `loop.create_unix_connection`

  `await` `loop.create_unix_server`

  `await`                                             Wrap a
  `loop.connect_accepted_socket`                                        role="class"} into a
                                                      `(transport, protocol)` pair.

  `await`                                             Open a datagram (UDP) connection.
  `loop.create_datagram_endpoint`

  `await` `loop.sendfile`

  `await` `loop.start_tls`                                        TLS.

  `await` `loop.connect_read_pipe`                                        `(transport, protocol)` pair.

  `await` `loop.connect_write_pipe`                                        `(transport, protocol)` pair.
  --------------------------------------------------- ------------------------------------

**Sockets**

  --------------------------------------------- ------------------------------------
  `await` `loop.sock_recv`                                  `~socket.socket`.

  `await`                                       Receive data from the
  `loop.sock_recv_into`                                  role="class"} into a buffer.

  `await`                                       Receive a datagram from the
  `loop.sock_recvfrom`                                  role="class"}.

  `await`                                       Receive a datagram from the
  `loop.sock_recvfrom_into`                                  role="class"} into a buffer.

  `await` `loop.sock_sendall`                                  `~socket.socket`.

  `await` `loop.sock_sendto`                                  `~socket.socket` to the given address.

  `await` `loop.sock_connect`                                  `~socket.socket`.

  `await` `loop.sock_accept`                                  `~socket.socket` connection.

  `await`                                       Send a file over the
  `loop.sock_sendfile`                                  role="class"}.

  `loop.add_reader`                                  read availability.

  `loop.remove_reader`                                  read availability.

  `loop.add_writer`                                  write availability.

  `loop.remove_writer`                                  write availability.
  --------------------------------------------- ------------------------------------

**Unix Signals**

  ------------------------------------------------ -----------------------------------
  `loop.add_signal_handler`                                     `signal`.

  `loop.remove_signal_handler`                                     `signal`.
  ------------------------------------------------ -----------------------------------

**Subprocesses**

  ------------------------------------------- -----------------------------------
  `loop.subprocess_exec`

  `loop.subprocess_shell`                                command.
  ------------------------------------------- -----------------------------------

**Error Handling**

  ---------------------------------------------------- -----------------------------------
  `loop.call_exception_handler`

  `loop.set_exception_handler`

  `loop.get_exception_handler`

  `loop.default_exception_handler`                                         implementation.
  ---------------------------------------------------- -----------------------------------

**Examples**

- `Using asyncio.new_event_loop() and loop.run_forever()
  <asyncio_example_lowlevel_helloworld>`.
- `Using loop.call_later() <asyncio_example_call_later>`.
- Using `loop.create_connection()` to implement
  `an echo-client <asyncio_example_tcp_echo_client_protocol>`.
- Using `loop.create_connection()` to
  `connect a socket <asyncio_example_create_connection>`.
- `Using add_reader() to watch an FD for read events
  <asyncio_example_watch_fd>`.
- `Using loop.add_signal_handler() <asyncio_example_unix_signals>`.
- `Using loop.subprocess_exec() <asyncio_example_subprocess_proto>`.

## Transports

All transports implement the following methods:

  ------------------------------------------------------------------------------- -----------------------------------
  `transport.close() <BaseTransport.close>`        Close the transport.

  `transport.is_closing() <BaseTransport.is_closing>`                                                                    closing or is closed.

  `transport.get_extra_info() <BaseTransport.get_extra_info>`                                                                    transport.

  `transport.set_protocol() <BaseTransport.set_protocol>`

  `transport.get_protocol() <BaseTransport.get_protocol>`
  ------------------------------------------------------------------------------- -----------------------------------

Transports that can receive data (TCP and Unix connections, pipes, etc).
Returned from methods like `loop.create_connection`, `loop.create_unix_connection`, `loop.connect_read_pipe`,
etc:

**Read Transports**

  ------------------------------------------------------------------------------- -----------------------------------
  `transport.is_reading() <ReadTransport.is_reading>`                                                                    receiving.

  `transport.pause_reading() <ReadTransport.pause_reading>`

  `transport.resume_reading() <ReadTransport.resume_reading>`
  ------------------------------------------------------------------------------- -----------------------------------

Transports that can Send data (TCP and Unix connections, pipes, etc).
Returned from methods like `loop.create_connection`, `loop.create_unix_connection`, `loop.connect_write_pipe`,
etc:

**Write Transports**

  ------------------------------------------------------------------------------ -----------------------------------
  `transport.write() <WriteTransport.write>`      Write data to the transport.

  `transport.writelines() <WriteTransport.writelines>`

  `transport.can_write_eof() <WriteTransport.can_write_eof>`                                                                   role="const"} if the transport
                                                                                 supports sending EOF.

  `transport.write_eof() <WriteTransport.write_eof>`                                                                   buffered data.

  `transport.abort() <WriteTransport.abort>`      Close the transport immediately.

  `transport.get_write_buffer_size()                                             Return the current size of the
  <WriteTransport.get_write_buffer_size>`         output buffer.

  `transport.get_write_buffer_limits()                                           Return high and low water marks for
  <WriteTransport.get_write_buffer_limits>`       write flow control.

  `transport.set_write_buffer_limits()                                           Set new high and low water marks
  <WriteTransport.set_write_buffer_limits>`       for write flow control.
  ------------------------------------------------------------------------------ -----------------------------------

Transports returned by `loop.create_datagram_endpoint`:

**Datagram Transports**

  ------------------------------------------------------------------- -----------------------------------
  `transport.sendto() <DatagramTransport.sendto>`

  `transport.abort() <DatagramTransport.abort>`
  ------------------------------------------------------------------- -----------------------------------

Low-level transport abstraction over subprocesses. Returned by
`loop.subprocess_exec` and
`loop.subprocess_shell`:

**Subprocess Transports**

  ------------------------------------------------------------------------------------- -----------------------------------
  `transport.get_pid() <SubprocessTransport.get_pid>`    Return the subprocess process id.

  `transport.get_pipe_transport()                                                       Return the transport for the
  <SubprocessTransport.get_pipe_transport>`              requested communication pipe
                                                                                        (*stdin*, *stdout*, or *stderr*).

  `transport.get_returncode() <SubprocessTransport.get_returncode>`

  `transport.kill() <SubprocessTransport.kill>`          Kill the subprocess.

  `transport.send_signal() <SubprocessTransport.send_signal>`

  `transport.terminate() <SubprocessTransport.terminate>`

  `transport.close() <SubprocessTransport.close>`        Kill the subprocess and close all
                                                                                        pipes.
  ------------------------------------------------------------------------------------- -----------------------------------

## Protocols

Protocol classes can implement the following **callback methods**:

  ---------------------------------------------------------------------- -----------------------------------
  `callback`                                                             Called when a connection is made.
  `connection_made() <BaseProtocol.connection_made>`

  `callback`                                                             Called when the connection is lost
  `connection_lost() <BaseProtocol.connection_lost>`

  `callback`                                                             Called when the transport\'s buffer
  `pause_writing() <BaseProtocol.pause_writing>`

  `callback`                                                             Called when the transport\'s buffer
  `resume_writing() <BaseProtocol.resume_writing>`
  ---------------------------------------------------------------------- -----------------------------------

**Streaming Protocols (TCP, Unix Sockets, Pipes)**

  -------------------------------------------------------------- -----------------------------------
  `callback`                                                     Called when some data is received.
  `data_received() <Protocol.data_received>`

  `callback`                                                     Called when an EOF is received.
  `eof_received() <Protocol.eof_received>`
  -------------------------------------------------------------- -----------------------------------

**Buffered Streaming Protocols**

  ------------------------------------------------------------------------ -----------------------------------
  `callback`                                                               Called to allocate a new receive
  `get_buffer() <BufferedProtocol.get_buffer>`

  `callback`                                                               Called when the buffer was updated
  `buffer_updated() <BufferedProtocol.buffer_updated>`

  `callback`                                                               Called when an EOF is received.
  `eof_received() <BufferedProtocol.eof_received>`
  ------------------------------------------------------------------------ -----------------------------------

**Datagram Protocols**

  ------------------------------------------------------------------------ -----------------------------------
  `callback` `datagram_received()                                          Called when a datagram is received.
  <DatagramProtocol.datagram_received>`

  `callback`                                                               Called when a previous send or
  `error_received() <DatagramProtocol.error_received>`                                                             `OSError`.
  ------------------------------------------------------------------------ -----------------------------------

**Subprocess Protocols**

  -------------------------------------------------------------- --------------------------------------------------------------
  `callback`                                                     Called when the child process writes data into its *stdout* or
  `~SubprocessProtocol.pipe_data_received`

  `callback`                                                     Called when one of the pipes communicating with the child
  `~SubprocessProtocol.pipe_connection_lost`

  `callback` `process_exited()                                   Called when the child process has exited. It can be called
  <SubprocessProtocol.process_exited>`                                                   `~SubprocessProtocol.pipe_data_received` and
                                                                 `~SubprocessProtocol.pipe_connection_lost` methods.
  -------------------------------------------------------------- --------------------------------------------------------------

## Event Loop Policies

Policies is a low-level mechanism to alter the behavior of functions
like `asyncio.get_event_loop`. See also
the main `policies section <asyncio-policies>` for more details.

**Accessing Policies**

  --------------------------------------------------- -----------------------------------
  `asyncio.get_event_loop_policy`                                        policy.

  `asyncio.set_event_loop_policy`

  `AbstractEventLoopPolicy`
  --------------------------------------------------- -----------------------------------