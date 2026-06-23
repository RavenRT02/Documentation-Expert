# `!types` \-\-- Dynamic type creation and names for built-in types

::: {.module synopsis="Names for built-in types."}
types
:::

**Source code:** `Lib/types.py`

This module defines utility functions to assist in dynamic creation of
new types.

It also defines names for some object types that are used by the
standard Python interpreter, but not exposed as builtins like
`int` or `str` are.

Finally, it provides some additional type-related utility classes and
functions that are not fundamental enough to be builtins.

## Dynamic Type Creation

:::: function
new_class(name, bases=(), kwds=None, exec_body=None)

Creates a class object dynamically using the appropriate metaclass.

The first three arguments are the components that make up a class
definition header: the class name, the base classes (in order), the
keyword arguments (such as `metaclass`).

The *exec_body* argument is a callback that is used to populate the
freshly created class namespace. It should accept the class namespace as
its sole argument and update the namespace directly with the class
contents. If no callback is provided, it has the same effect as passing
in `lambda ns: None`.

::: versionadded
3.3
:::
::::

::::: function
prepare_class(name, bases=(), kwds=None)

Calculates the appropriate metaclass and creates the class namespace.

The arguments are the components that make up a class definition header:
the class name, the base classes (in order) and the keyword arguments
(such as `metaclass`).

The return value is a 3-tuple: `metaclass, namespace, kwds`

*metaclass* is the appropriate metaclass, *namespace* is the prepared
class namespace and *kwds* is an updated copy of the passed in *kwds*
argument with any `'metaclass'` entry removed. If no *kwds* argument is
passed in, this will be an empty dict.

::: versionadded
3.3
:::

::: versionchanged
3.6

The default value for the `namespace` element of the returned tuple has
changed. Now an insertion-order-preserving mapping is used when the
metaclass does not have a `__prepare__` method.
:::
:::::

::: seealso

`metaclasses`

: Full details of the class creation process supported by these
  functions

`3115` - Metaclasses in Python 3000

: Introduced the `__prepare__` namespace hook
:::

:::: function
resolve_bases(bases)

Resolve MRO entries dynamically as specified by `560`.

This function looks for items in *bases* that are not instances of
`type`, and returns a tuple where each
such object that has an `~object.__mro_entries__` method is replaced with an unpacked result of calling this
method. If a *bases* item is an instance of `type`, or it doesn\'t have an
`!__mro_entries__` method, then it is
included in the return tuple unchanged.

::: versionadded
3.7
:::
::::

:::: function
get_original_bases(cls, /)

Return the tuple of objects originally given as the bases of *cls*
before the `~object.__mro_entries__`
method has been called on any bases (following the mechanisms laid out
in `560`). This is useful for
introspecting `Generics <user-defined-generics>`.

For classes that have an `__orig_bases__` attribute, this function
returns the value of `cls.__orig_bases__`. For classes without the
`__orig_bases__` attribute,
`cls.__bases__ <type.__bases__>` is
returned.

Examples:

    from typing import TypeVar, Generic, NamedTuple, TypedDict

    T = TypeVar("T")
    class Foo(Generic[T]): ...
    class Bar(Foo[int], float): ...
    class Baz(list[str]): ...
    Eggs = NamedTuple("Eggs", [("a", int), ("b", str)])
    Spam = TypedDict("Spam", {"a": int, "b": str})

    assert Bar.__bases__ == (Foo, float)
    assert get_original_bases(Bar) == (Foo[int], float)

    assert Baz.__bases__ == (list,)
    assert get_original_bases(Baz) == (list[str],)

    assert Eggs.__bases__ == (tuple,)
    assert get_original_bases(Eggs) == (NamedTuple,)

    assert Spam.__bases__ == (dict,)
    assert get_original_bases(Spam) == (TypedDict,)

    assert int.__bases__ == (object,)
    assert get_original_bases(int) == (object,)

::: versionadded
3.12
:::
::::

::: seealso
`560` - Core support for typing module and
generic types
:::

## Standard Interpreter Types

This module provides names for many of the types that are required to
implement a Python interpreter. It deliberately avoids including some of
the types that arise only incidentally during processing such as the
`listiterator` type.

Typical use of these names is for `isinstance` or `issubclass` checks.

If you instantiate any of these types, note that signatures may vary
between Python versions.

Standard names are defined for the following types:

:::: NoneType
The type of `None`.

::: versionadded
3.10
:::
::::

:::: {.FunctionType .LambdaType}
The type of user-defined functions and functions created by
`lambda` expressions.

::: audit-event
function.\_\_new\_\_ code types.FunctionType
:::

The audit event only occurs for direct instantiation of function
objects, and is not raised for normal compilation.
::::

::: GeneratorType
The type of `generator`-iterator objects,
created by generator functions.
:::

:::: CoroutineType
The type of `coroutine` objects, created
by `async def` functions.

::: versionadded
3.5
:::
::::

:::: AsyncGeneratorType
The type of `asynchronous generator`-iterator objects, created by asynchronous generator
functions.

::: versionadded
3.6
:::
::::

::::: CodeType(**kwargs)

The type of `code objects <code-objects>`
such as returned by `compile`.

::: audit-event
code.\_\_new\_\_
code,filename,name,argcount,posonlyargcount,kwonlyargcount,nlocals,stacksize,flags
types.CodeType
:::

Note that the audited arguments may not match the names or positions
required by the initializer. The audit event only occurs for direct
instantiation of code objects, and is not raised for normal compilation.
:::::

:::: CellType
The type for cell objects: such objects are used as containers for a
function\'s `closure variables <closure variable>`.

::: versionadded
3.8
:::
::::

::: MethodType
The type of methods of user-defined class instances.
:::

::: {.BuiltinFunctionType .BuiltinMethodType}
The type of built-in functions like `len`
or `sys.exit`, and methods of built-in
classes. (Here, the term \"built-in\" means \"written in C\".)
:::

:::: WrapperDescriptorType
The type of methods of some built-in data types and base classes such as
`object.__init__` or
`object.__lt__`.

::: versionadded
3.7
:::
::::

:::: MethodWrapperType
The type of *bound* methods of some built-in data types and base
classes. For example it is the type of `object().__str__`.

::: versionadded
3.7
:::
::::

:::: NotImplementedType
The type of `NotImplemented`.

::: versionadded
3.10
:::
::::

:::: MethodDescriptorType
The type of methods of some built-in data types such as
`str.join`.

::: versionadded
3.7
:::
::::

:::: ClassMethodDescriptorType
The type of *unbound* class methods of some built-in data types such as
`dict.__dict__['fromkeys']`.

::: versionadded
3.7
:::
::::

:::: {.ModuleType(name, .doc=None)}
The type of `modules <module>`. The
constructor takes the name of the module to be created and optionally
its `docstring`.

::: seealso

`Documentation on module objects <module-objects>`

: Provides details on the special attributes that can be found on
  instances of `!ModuleType`.

`importlib.util.module_from_spec`

: Modules created using the `!ModuleType` constructor are created with many of their special
  attributes unset or set to default values.
  `!module_from_spec` provides a more
  robust way of creating `!ModuleType`
  instances which ensures the various attributes are set appropriately.
:::
::::

:::: EllipsisType
The type of `Ellipsis`.

::: versionadded
3.10
:::
::::

:::::: {.GenericAlias(t_origin, .t_args)}
The type of
`parameterized generics <types-genericalias>` such as `list[int]`.

`t_origin` should be a non-parameterized generic class, such as `list`,
`tuple` or `dict`. `t_args` should be a `tuple` (possibly of length 1) of types which parameterize
`t_origin`:

    >>> from types import GenericAlias

    >>> list[int] == GenericAlias(list, (int,))
    True
    >>> dict[str, int] == GenericAlias(dict, (str, int))
    True

::: versionadded
3.9
:::

::: versionchanged
3.9.2 This type can now be subclassed.
:::

::: seealso

`Generic Alias Types<types-genericalias>`

: In-depth documentation on instances of
  `!types.GenericAlias`

`585` - Type Hinting Generics In Standard Collections

: Introducing the `!types.GenericAlias`
  class
:::
::::::

::::: UnionType
The type of `union type expressions<types-union>`.

::: versionadded
3.10
:::

::: versionchanged
3.14

This is now an alias for `typing.Union`.
:::
:::::

::: {.TracebackType(tb_next, .tb_frame, .tb_lasti, .tb_lineno)}
The type of traceback objects such as found in
`sys.exception().__traceback__`.

See `the language reference <traceback-objects>` for details of the available attributes and operations, and
guidance on creating tracebacks dynamically.
:::

::: FrameType
The type of `frame objects <frame-objects>` such as found in
`tb.tb_frame <traceback.tb_frame>` if
`tb` is a traceback object.
:::

::::: FrameLocalsProxyType
The type of frame locals proxy objects, as found on the
`frame.f_locals` attribute.

::: versionadded
3.15
:::

::: seealso
`667`
:::
:::::

::::: LazyImportType
The type of lazy import proxy objects. These objects are created when a
module is lazily imported and serve as placeholders until the module is
actually accessed. This type can be used to detect lazy imports
programmatically.

::: versionadded
3.15
:::

::: seealso
`810`
:::
:::::

::: GetSetDescriptorType
The type of objects defined in extension modules with `PyGetSetDef`,
such as `FrameType.f_locals <frame.f_locals>` or `array.array.typecode`. This type is used as descriptor
for object attributes; it has the same purpose as the
`property` type, but for classes defined
in extension modules.
:::

:::: MemberDescriptorType
The type of objects defined in extension modules with `PyMemberDef`,
such as `datetime.timedelta.days`. This type is used as descriptor for
simple C data members which use standard conversion functions; it has
the same purpose as the `property` type,
but for classes defined in extension modules.

In addition, when a class is defined with a
`~object.__slots__` attribute, then for
each slot, an instance of `!MemberDescriptorType` will be added as an attribute on the class. This allows
the slot to appear in the class\'s `~type.__dict__`.

::: impl-detail
In other implementations of Python, this type may be identical to
`GetSetDescriptorType`.
:::
::::

:::::::::::::::::: MappingProxyType(mapping)
Read-only proxy of a mapping. It provides a dynamic view on the
mapping\'s entries, which means that when the mapping changes, the view
reflects these changes.

`!MappingProxyType`s are
`generic <generics>` over two types,
signifying (respectively) the types of the underlying mapping\'s keys
and values.

::: versionadded
3.3
:::

::: versionchanged
3.9

Updated to support the new union (`|`) operator from
`584`, which simply delegates to the
underlying mapping.
:::

::: describe
key in proxy

Return `True` if the underlying mapping has a key *key*, else `False`.
:::

::: describe
proxy\[key\]

Return the item of the underlying mapping with key *key*. Raises a
`KeyError` if *key* is not in the
underlying mapping.
:::

::: describe
iter(proxy)

Return an iterator over the keys of the underlying mapping. This is a
shortcut for `iter(proxy.keys())`.
:::

::: describe
len(proxy)

Return the number of items in the underlying mapping.
:::

::: method
copy()

Return a shallow copy of the underlying mapping.
:::

::: method
get(key\[, default\])

Return the value for *key* if *key* is in the underlying mapping, else
*default*. If *default* is not given, it defaults to `None`, so that
this method never raises a `KeyError`.
:::

::: method
items()

Return a new view of the underlying mapping\'s items (`(key, value)`
pairs).
:::

::: method
keys()

Return a new view of the underlying mapping\'s keys.
:::

::: method
values()

Return a new view of the underlying mapping\'s values.
:::

:::: describe
reversed(proxy)

Return a reverse iterator over the keys of the underlying mapping.

::: versionadded
3.9
:::
::::

:::: describe
hash(proxy)

Return a hash of the underlying mapping.

::: versionadded
3.12
:::
::::
::::::::::::::::::

:::: CapsuleType
The type of `capsule objects <capsules>`.

::: versionadded
3.13
:::
::::

## Additional Utility Classes and Functions

:::::: SimpleNamespace
A simple `object` subclass that provides
attribute access to its namespace, as well as a meaningful repr.

Unlike `object`, with
`!SimpleNamespace` you can add and
remove attributes.

`SimpleNamespace` objects may be
initialized in the same way as `dict`:
either with keyword arguments, with a single positional argument, or
with both. When initialized with keyword arguments, those are directly
added to the underlying namespace. Alternatively, when initialized with
a positional argument, the underlying namespace will be updated with
key-value pairs from that argument (either a mapping object or an
`iterable` object producing key-value
pairs). All such keys must be strings.

The type is roughly equivalent to the following code:

    class SimpleNamespace:
        def __init__(self, mapping_or_iterable=(), /, **kwargs):
            self.__dict__.update(mapping_or_iterable)
            self.__dict__.update(kwargs)

        def __repr__(self):
            items = (f"{k}={v!r}" for k, v in self.__dict__.items())
            return "{}({})".format(type(self).__name__, ", ".join(items))

        def __eq__(self, other):
            if isinstance(self, SimpleNamespace) and isinstance(other, SimpleNamespace):
               return self.__dict__ == other.__dict__
            return NotImplemented

`SimpleNamespace` may be useful as a replacement for `class NS: pass`.
However, for a structured record type use
`~collections.namedtuple` instead.

`!SimpleNamespace` objects are supported
by `copy.replace`.

::: versionadded
3.3
:::

::: versionchanged
3.9 Attribute order in the repr changed from alphabetical to insertion
(like `dict`).
:::

::: versionchanged
3.13 Added support for an optional positional argument.
:::
::::::

:::: function
DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)

Route attribute access on a class to \_\_getattr\_\_.

This is a descriptor, used to define attributes that act differently
when accessed through an instance and through a class. Instance access
remains normal, but access to an attribute through a class will be
routed to the class\'s \_\_getattr\_\_ method; this is done by raising
AttributeError.

This allows one to have properties active on an instance, and have
virtual attributes on the class with the same name (see
`enum.Enum` for an example).

::: versionadded
3.4
:::
::::

## Coroutine Utility Functions

:::: function
coroutine(gen_func)

This function transforms a `generator`
function into a `coroutine function`
which returns a generator-based coroutine. The generator-based coroutine
is still a `generator iterator`, but is
also considered to be a `coroutine`
object and is `awaitable`. However, it
may not necessarily implement the `~object.__await__` method.

If *gen_func* is a generator function, it will be modified in-place.

If *gen_func* is not a generator function, it will be wrapped. If it
returns an instance of `collections.abc.Generator`, the instance will be wrapped in an *awaitable* proxy
object. All other types of objects will be returned as is.

::: versionadded
3.5
:::
::::