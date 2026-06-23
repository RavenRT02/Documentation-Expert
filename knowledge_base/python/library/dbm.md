# `!dbm` \-\-- Interfaces to Unix \"databases\"

::: {.module synopsis="Interfaces to various Unix \"database\" formats."}
dbm
:::

**Source code:** `Lib/dbm/__init__.py`

`!dbm` is a generic interface to variants
of the DBM database:

- `dbm.sqlite3`
- `dbm.gnu`
- `dbm.ndbm`

If none of these modules are installed, the slow-but-simple
implementation in module `dbm.dumb` will
be used. There is a [third party
interface](https://www.jcea.es/programacion/pybsddb.htm) to the Oracle
Berkeley DB.

:::: note
::: title
Note
:::

None of the underlying modules will automatically shrink the disk space
used by the database file. However, `dbm.sqlite3`, `dbm.gnu` and
`dbm.dumb` provide a
`!reorganize` method that can be used for
this purpose.
::::

::: exception
error

A tuple containing the exceptions that can be raised by each of the
supported modules, with a unique exception also named
`dbm.error` as the first item \-\-- the
latter is used when `dbm.error` is raised.
:::

:::: function
whichdb(filename)

This function attempts to guess which of the several simple database
modules available \-\-- `dbm.sqlite3`,
`dbm.gnu`, `dbm.ndbm`, or `dbm.dumb` \-\-- should be
used to open a given file.

Return one of the following values:

- `None` if the file can\'t be opened because it\'s unreadable or
  doesn\'t exist
- the empty string (`''`) if the file\'s format can\'t be guessed
- a string containing the required module name, such as `'dbm.ndbm'` or
  `'dbm.gnu'`

::: versionchanged
3.11 *filename* accepts a `path-like object`.
:::
::::

:::: function
open(file, flag=\'r\', mode=0o666)

Open a database and return the corresponding database object.

param file

: The database file to open.

  If the database file already exists, the `whichdb` function is used to determine its type and the
  appropriate module is used; if it does not exist, the first submodule
  listed above that can be imported is used.

type file
: `path-like object`

param str flag

: - `'r'` (default): Open existing database for reading only.
  - `'w'`: Open existing database for reading and writing.
  - `'c'`: Open database for reading and writing, creating it if it
    doesn\'t exist.
  - `'n'`: Always create a new, empty database, open for reading and
    writing.

param int mode
: The Unix file access mode of the file (default: octal `0o666`), used
  only when the database has to be created.

::: versionchanged
3.11 *file* accepts a `path-like object`.
:::
::::

The object returned by `~dbm.open`
supports the basic functionality of mutable
`mappings <mapping>`; keys and their
corresponding values can be stored, retrieved, and deleted, and
iteration, the `in` operator and
methods `!keys`, `!get`, `!setdefault` and
`!clear` are available. The
`!keys` method returns a list instead of
a view object. The `!setdefault` method
requires two arguments.

Key and values are always stored as `bytes`. This means that when strings are used they are implicitly
converted to the default encoding before being stored.

These objects also support being used in a `with` statement, which will automatically close them when
done.

::: versionchanged
3.2 `!get` and
`!setdefault` methods are now available
for all `!dbm` backends.
:::

::: versionchanged
3.4 Added native support for the context management protocol to the
objects returned by `~dbm.open`.
:::

::: versionchanged
3.8 Deleting a key from a read-only database raises a database module
specific exception instead of `KeyError`.
:::

::: versionchanged
3.13 `!clear` methods are now available
for all `!dbm` backends.
:::

The following example records some hostnames and a corresponding title,
and then prints out the contents of the database:

    import dbm

    # Open database, creating it if necessary.
    with dbm.open('cache', 'c') as db:

        # Record some values
        db[b'hello'] = b'there'
        db['www.python.org'] = 'Python Website'
        db['www.cnn.com'] = 'Cable News Network'

        # Note that the keys are considered bytes now.
        assert db[b'www.python.org'] == b'Python Website'
        # Notice how the value is now in bytes.
        assert db['www.cnn.com'] == b'Cable News Network'

        # Often-used methods of the dict interface work too.
        print(db.get('python.org', b'not present'))

        # Storing a non-string key or value will raise an exception (most
        # likely a TypeError).
        db['www.yahoo.com'] = 4

    # db is automatically closed when leaving the with statement.

::: seealso

Module `shelve`

: Persistence module which stores non-string data.
:::

The individual submodules are described in the following sections.

## `!dbm.sqlite3` \-\-- SQLite backend for dbm

::: {.module synopsis="SQLite backend for dbm"}
dbm.sqlite3
:::

::: versionadded
3.13
:::

**Source code:** `Lib/dbm/sqlite3.py`

This module uses the standard library `sqlite3` module to provide an SQLite backend for the
`!dbm` module. The files created by
`!dbm.sqlite3` can thus be opened by
`sqlite3`, or any other SQLite browser,
including the SQLite CLI.

::: availability
not WASI.

This module does not work or is not available on WebAssembly. See
`wasm-availability` for more information.
:::

:::::::: function
open(filename, /, flag=\"r\", mode=0o666)

Open an SQLite database.

param filename
: The path to the database to be opened.

type filename
: `path-like object`

param str flag

:

> - `'r'` (default): Open existing database for reading only.
> - `'w'`: Open existing database for reading and writing.
> - `'c'`: Open database for reading and writing, creating it if it
>   doesn\'t exist.
> - `'n'`: Always create a new, empty database, open for reading and
>   writing.

param mode
: The Unix file access mode of the file (default: octal `0o666`), used
  only when the database has to be created.

The returned database object behaves similar to a mutable
`mapping`, but the
`!keys` method returns a list, and the
`!setdefault` method requires two
arguments. It also supports a \"closing\" context manager via the
`with` keyword.

The following methods are also provided:

::: method
sqlite3.close()

Close the SQLite database.
:::

:::::: method
sqlite3.reorganize()

If you have carried out a lot of deletions and would like to shrink the
space used on disk, this method will reorganize the database; otherwise,
deleted file space will be kept and reused as new (key, value) pairs are
added.

:::: note
::: title
Note
:::

While reorganizing, as much as two times the size of the original
database is required in free disk space. However, be aware that this
factor changes for each `!dbm` submodule.
::::

::: versionadded
3.15
:::
::::::
::::::::

## `!dbm.gnu` \-\-- GNU database manager

::: {.module synopsis="GNU database manager"}
dbm.gnu
:::

**Source code:** `Lib/dbm/gnu.py`

The `!dbm.gnu` module provides an
interface to the `GDBM (GNU dbm)`
library, similar to the `dbm.ndbm` module,
but with additional functionality like crash tolerance.

:::: note
::: title
Note
:::

The file formats created by `!dbm.gnu` and
`dbm.ndbm` are incompatible and can not be
used interchangeably.
::::

::: availability
not Android, not iOS, not WASI.

This module is not supported on
`mobile platforms <mobile-availability>`
or `WebAssembly platforms <wasm-availability>`.
:::

::: availability
Unix.
:::

::: exception
error

Raised on `!dbm.gnu`-specific errors, such
as I/O errors. `KeyError` is raised for
general mapping errors like specifying an incorrect key.
:::

::: data
open_flags

A string of characters the *flag* parameter of
`~dbm.gnu.open` supports.
:::

::::::::::::: function
open(filename, flag=\"r\", mode=0o666, /)

Open a GDBM database and return a `!gdbm` object.

param filename
: The database file to open.

type filename
: `path-like object`

param str flag

: - `'r'` (default): Open existing database for reading only.
  - `'w'`: Open existing database for reading and writing.
  - `'c'`: Open database for reading and writing, creating it if it
    doesn\'t exist.
  - `'n'`: Always create a new, empty database, open for reading and
    writing.

  The following additional characters may be appended to control how the
  database is opened:

  - `'f'`: Open the database in fast mode. Writes to the database will
    not be synchronized.
  - `'s'`: Synchronized mode. Changes to the database will be written
    immediately to the file.
  - `'u'`: Do not lock database.

  Not all flags are valid for all versions of GDBM. See the
  `open_flags` member for a list of
  supported flag characters.

param int mode
: The Unix file access mode of the file (default: octal `0o666`), used
  only when the database has to be created.

raises error
: If an invalid *flag* argument is passed.

::: versionchanged
3.11 *filename* accepts a `path-like object`.
:::

`!gdbm` objects behave similar to
mutable `mappings <mapping>`, but methods
`!items`, `!values`, `!pop`,
`!popitem`, and
`!update` are not supported, the
`!keys` method returns a list, and the
`!setdefault` method requires two
arguments. It also supports a \"closing\" context manager via the
`with` keyword.

::: versionchanged
3.2 Added the `!get` and
`!setdefault` methods.
:::

::: versionchanged
3.13 Added the `!clear` method.
:::

The following methods are also provided:

::: method
gdbm.close()

Close the GDBM database.
:::

::: method
gdbm.firstkey()

It\'s possible to loop over every key in the database using this method
and the `nextkey` method. The traversal
is ordered by GDBM\'s internal hash values, and won\'t be sorted by the
key values. This method returns the starting key.
:::

::: method
gdbm.nextkey(key)

Returns the key that follows *key* in the traversal. The following code
prints every key in the database `db`, without having to create a list
in memory that contains them all:

    k = db.firstkey()
    while k is not None:
        print(k)
        k = db.nextkey(k)
:::

::::: method
gdbm.reorganize()

If you have carried out a lot of deletions and would like to shrink the
space used by the GDBM file, this routine will reorganize the database.
`!gdbm` objects will not shorten the
length of a database file except by using this reorganization;
otherwise, deleted file space will be kept and reused as new (key,
value) pairs are added.

:::: note
::: title
Note
:::

While reorganizing, as much as one time the size of the original
database is required in free disk space. However, be aware that this
factor changes for each `!dbm` submodule.
::::
:::::

::: method
gdbm.sync()

When the database has been opened in fast mode, this method forces any
unwritten data to be written to the disk.
:::
:::::::::::::

## `!dbm.ndbm` \-\-- New Database Manager

::: {.module synopsis="The New Database Manager"}
dbm.ndbm
:::

**Source code:** `Lib/dbm/ndbm.py`

The `!dbm.ndbm` module provides an
interface to the `NDBM (New Database Manager)` library. This module can be used with the \"classic\" NDBM
interface or the `GDBM (GNU dbm)`
compatibility interface.

:::: note
::: title
Note
:::

The file formats created by `dbm.gnu` and
`!dbm.ndbm` are incompatible and can not
be used interchangeably.
::::

:::: warning
::: title
Warning
:::

The NDBM library shipped as part of macOS has an undocumented limitation
on the size of values, which can result in corrupted database files when
storing values larger than this limit. Reading such corrupted files can
result in a hard crash (segmentation fault).
::::

::: availability
not Android, not iOS, not WASI.

This module is not supported on
`mobile platforms <mobile-availability>`
or `WebAssembly platforms <wasm-availability>`.
:::

::: availability
Unix.
:::

::: exception
error

Raised on `!dbm.ndbm`-specific errors,
such as I/O errors. `KeyError` is raised
for general mapping errors like specifying an incorrect key.
:::

::: data
library

Name of the NDBM implementation library used.
:::

::::::: function
open(filename, flag=\"r\", mode=0o666, /)

Open an NDBM database and return an `!ndbm` object.

param filename
: The basename of the database file (without the
  `.dir` or `.pag` extensions).

type filename
: `path-like object`

param str flag

: - `'r'` (default): Open existing database for reading only.
  - `'w'`: Open existing database for reading and writing.
  - `'c'`: Open database for reading and writing, creating it if it
    doesn\'t exist.
  - `'n'`: Always create a new, empty database, open for reading and
    writing.

param int mode
: The Unix file access mode of the file (default: octal `0o666`), used
  only when the database has to be created.

::: versionchanged
3.11 Accepts `path-like object` for
filename.
:::

`!ndbm` objects behave similar to
mutable `mappings <mapping>`, but methods
`!items`, `!values`, `!pop`,
`!popitem`, and
`!update` are not supported, the
`!keys` method returns a list, and the
`!setdefault` method requires two
arguments. It also supports a \"closing\" context manager via the
`with` keyword.

::: versionchanged
3.2 Added the `!get` and
`!setdefault` methods.
:::

::: versionchanged
3.13 Added the `!clear` method.
:::

The following method is also provided:

::: method
ndbm.close()

Close the NDBM database.
:::
:::::::

## `!dbm.dumb` \-\-- Portable DBM implementation

::: {.module synopsis="Portable implementation of the simple DBM interface."}
dbm.dumb
:::

**Source code:** `Lib/dbm/dumb.py`

:::: note
::: title
Note
:::

The `!dbm.dumb` module is intended as a
last resort fallback for the `!dbm` module
when a more robust module is not available. The
`!dbm.dumb` module is not written for
speed and is not nearly as heavily used as the other database modules.
::::

The `!dbm.dumb` module provides a
persistent `dict`-like interface which
is written entirely in Python. Unlike other `!dbm` backends, such as `dbm.gnu`,
no external library is required.

The `!dbm.dumb` module defines the
following:

::: exception
error

Raised on `!dbm.dumb`-specific errors,
such as I/O errors. `KeyError` is raised
for general mapping errors like specifying an incorrect key.
:::

:::::::::::::::: function
open(filename, flag=\"c\", mode=0o666)

Open a `!dbm.dumb` database.

param filename

: The basename of the database file (without extensions). A new database
  creates the following files:

  - `{filename}.dat`
  - `{filename}.dir`

type database
: `path-like object`

param str flag

: - `'r'`: Open existing database for reading only.
  - `'w'`: Open existing database for reading and writing.
  - `'c'` (default): Open database for reading and writing, creating it
    if it doesn\'t exist.
  - `'n'`: Always create a new, empty database, open for reading and
    writing.

param int mode
: The Unix file access mode of the file (default: octal `0o666`), used
  only when the database has to be created.

:::: warning
::: title
Warning
:::

It is possible to crash the Python interpreter when loading a database
with a sufficiently large/complex entry due to stack depth limitations
in Python\'s AST compiler.
::::

:::: warning
::: title
Warning
:::

`!dbm.dumb` does not support concurrent
read/write access. (Multiple simultaneous read accesses are safe.) When
a program has the database open for writing, no other program should
have it open for reading or writing.
::::

::: versionchanged
3.5 `~dbm.dumb.open` always creates a new
database when *flag* is `'n'`.
:::

::: versionchanged
3.8 A database opened read-only if *flag* is `'r'`. A database is not
created if it does not exist if *flag* is `'r'` or `'w'`.
:::

::: versionchanged
3.11 *filename* accepts a `path-like object`.
:::

The returned database object behaves similar to a mutable
`mapping`, but the
`!keys` and `!items` methods return lists, and the
`!setdefault` method requires two
arguments. It also supports a \"closing\" context manager via the
`with` keyword.

The following methods are also provided:

::: method
dumbdbm.close()

Close the database.
:::

:::::: method
dumbdbm.reorganize()

If you have carried out a lot of deletions and would like to shrink the
space used on disk, this method will reorganize the database; otherwise,
deleted file space will not be reused.

:::: note
::: title
Note
:::

While reorganizing, no additional free disk space is required. However,
be aware that this factor changes for each `!dbm` submodule.
::::

::: versionadded
3.15
:::
::::::

::: method
dumbdbm.sync()

Synchronize the on-disk directory and data files. This method is called
by the `shelve.Shelf.sync` method.
:::
::::::::::::::::