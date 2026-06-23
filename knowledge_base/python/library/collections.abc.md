# `!collections.abc` \-\-- Abstract Base Classes for Containers

::: {.module synopsis="Abstract base classes for containers"}
collections.abc
:::

::: versionadded
3.3 Formerly, this module was part of the
`collections` module.
:::

**Source code:** `Lib/_collections_abc.py`

::: testsetup
-

from collections.abc import \* import itertools \_\_name\_\_ =
\'\<doctest\>\'
:::

This module provides
`abstract base classes <abstract base class>` that can be used to test whether a class provides a
particular interface; for example, whether it is
`hashable` or whether it is a
`mapping`.

An `issubclass` or
`isinstance` test for an interface works
in one of three ways.

1)  A newly written class can inherit directly from one of the abstract
    base classes. The class must supply the required abstract methods.
    The remaining mixin methods come from inheritance and can be
    overridden if desired. Other methods may be added as needed:

    ::: testcode

    class C(Sequence): \# Direct inheritance

    : def \_\_init\_\_(self): \... \# Extra method not required by the
      ABC def \_\_getitem\_\_(self, index): \... \# Required abstract
      method def \_\_len\_\_(self): \... \# Required abstract method def
      count(self, value): \... \# Optionally override a mixin method
    :::

    ::: doctest
    \>\>\> issubclass(C, Sequence) True \>\>\> isinstance(C(), Sequence)
    True
    :::

2)  Existing classes and built-in classes can be registered as \"virtual
    subclasses\" of the ABCs. Those classes should define the full API
    including all of the abstract methods and all of the mixin methods.
    This lets users rely on `issubclass`
    or `isinstance` tests to determine
    whether the full interface is supported. The exception to this rule
    is for methods that are automatically inferred from the rest of the
    API:

    ::: testcode

    class D: \# No inheritance

    : def \_\_init\_\_(self): \... \# Extra method not required by the
      ABC def \_\_getitem\_\_(self, index): \... \# Abstract method def
      \_\_len\_\_(self): \... \# Abstract method def count(self, value):
      \... \# Mixin method def index(self, value): \... \# Mixin method

    Sequence.register(D) \# Register instead of inherit
    :::

    ::: doctest
    \>\>\> issubclass(D, Sequence) True \>\>\> isinstance(D(), Sequence)
    True
    :::

    In this example, class `!D` does not
    need to define `__contains__`, `__iter__`, and `__reversed__`
    because the `in-operator <comparisons>`, the `iteration <iterable>` logic, and the `reversed` function automatically fall back to using `__getitem__`
    and `__len__`.

3)  Some simple interfaces are directly recognizable by the presence of
    the required methods (unless those methods have been set to
    `None`):

    ::: testcode

    class E:

    : def \_\_iter\_\_(self): \... def \_\_next\_\_(self): \...
    :::

    ::: doctest
    \>\>\> issubclass(E, Iterable) True \>\>\> isinstance(E(), Iterable)
    True
    :::

    Complex interfaces do not support this last technique because an
    interface is more than just the presence of method names. Interfaces
    specify semantics and relationships between methods that cannot be
    inferred solely from the presence of specific method names. For
    example, knowing that a class supplies `__getitem__`, `__len__`, and
    `__iter__` is insufficient for distinguishing a
    `Sequence` from a
    `Mapping`.

::: versionadded
3.9 These abstract classes now support `[]`. See
`types-genericalias` and
`585`.
:::

## Collections Abstract Base Classes

The collections module offers the following
`ABCs <abstract base class>`:

::: tabularcolumns
\|l\|L\|L\|L\|
:::

  ABC                                                     Inherits from                                                                                                                      Abstract Methods                                                     Mixin Methods
  ------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  `Container`[^1]                                                                                                                                            `__contains__`
  `Hashable`[^2]                                                                                                                                             `__hash__`
  `Iterable`[^3][^4]                                                                                                                                         `__iter__`
  `Iterator`[^5]          `Iterable`                                                                                         `__next__`                                                           `__iter__`
  `Reversible`[^6]        `Iterable`                                                                                         `__reversed__`
  `Generator`[^7]         `Iterator`                                                                                         `send`, `throw`                                                      `close`, `__iter__`, `__next__`
  `Sized`[^8]                                                                                                                                                `__len__`
  `Callable`[^9]                                                                                                                                             `__call__`
  `Collection`[^10]       `Sized`, `Iterable`, `Container`   `__contains__`, `__iter__`, `__len__`
  `Sequence`              `Reversible`, `Collection`                                         `__getitem__`, `__len__`                                             `__contains__`, `__iter__`, `__reversed__`, `index`, and `count`
  `MutableSequence`       `Sequence`                                                                                         `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert`     Inherited `Sequence` methods and `append`, `clear`, `reverse`, `extend`, `pop`, `remove`, and `__iadd__`
  `ByteString`            `Sequence`                                                                                         `__getitem__`, `__len__`                                             Inherited `Sequence` methods
  `Set`                   `Collection`                                                                                       `__contains__`, `__iter__`, `__len__`                                `__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__and__`, `__or__`, `__sub__`, `__rsub__`, `__xor__`, `__rxor__` and `isdisjoint`
  `MutableSet`            `Set`                                                                                              `__contains__`, `__iter__`, `__len__`, `add`, `discard`              Inherited `Set` methods and `clear`, `pop`, `remove`, `__ior__`, `__iand__`, `__ixor__`, and `__isub__`
  `Mapping`               `Collection`                                                                                       `__getitem__`, `__iter__`, `__len__`                                 `__contains__`, `keys`, `items`, `values`, `get`, `__eq__`, and `__ne__`
  `MutableMapping`        `Mapping`                                                                                          `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__`   Inherited `Mapping` methods and `pop`, `popitem`, `clear`, `update`, and `setdefault`
  `MappingView`           `Sized`                                                                                                                                                                 `__init__`, `__len__` and `__repr__`
  `ItemsView`             `MappingView`, `Set`                                                                                                                    `__contains__`, `__iter__`
  `KeysView`              `MappingView`, `Set`                                                                                                                    `__contains__`, `__iter__`
  `ValuesView`            `MappingView`, `Collection`                                                                                                             `__contains__`, `__iter__`
  `Awaitable`[^11]                                                                                                                                           `__await__`
  `Coroutine`[^12]        `Awaitable`                                                                                        `send`, `throw`                                                      `close`
  `AsyncIterable`[^13]                                                                                                                                       `__aiter__`
  `AsyncIterator`[^14]    `AsyncIterable`                                                                                    `__anext__`                                                          `__aiter__`
  `AsyncGenerator`[^15]   `AsyncIterator`                                                                                    `asend`, `athrow`                                                    `aclose`, `__aiter__`, `__anext__`
  `Buffer`[^16]                                                                                                                                              `__buffer__`

**Footnotes**

## Collections Abstract Base Classes \-- Detailed Descriptions

::: Container
ABC for classes that provide the
`~object.__contains__` method.
:::

::: Hashable
ABC for classes that provide the `~object.__hash__` method.
:::

::: Sized
ABC for classes that provide the `~object.__len__` method.
:::

::: Callable
ABC for classes that provide the `~object.__call__` method.

See `annotating-callables` for details on
how to use `!Callable` in type
annotations.
:::

::: Iterable
ABC for classes that provide the `~container.__iter__` method.

Checking `isinstance(obj, Iterable)` detects classes that are registered
as `Iterable` or that have an
`~container.__iter__` method, but it does
not detect classes that iterate with the
`~object.__getitem__` method. The only
reliable way to determine whether an object is
`iterable` is to call `iter(obj)`.
:::

:::: Collection
ABC for sized iterable container classes.

::: versionadded
3.6
:::
::::

::: Iterator
ABC for classes that provide the `~iterator.__iter__` and `~iterator.__next__`
methods. See also the definition of `iterator`.
:::

:::: Reversible
ABC for iterable classes that also provide the
`~object.__reversed__` method.

::: versionadded
3.6
:::
::::

:::: Generator
ABC for `generator` classes that
implement the protocol defined in `342`
that extends `iterators <iterator>` with
the `~generator.send`,
`~generator.throw` and
`~generator.close` methods.

See `annotating-generators-and-coroutines`
for details on using `!Generator` in
type annotations.

::: versionadded
3.5
:::
::::

:::::: {.Sequence .MutableSequence .ByteString}
ABCs for read-only and mutable `sequences <sequence>`.

Implementation note: Some of the mixin methods, such as
`~container.__iter__`,
`~object.__reversed__`, and
`~sequence.index` make repeated calls to
the underlying `~object.__getitem__`
method. Consequently, if `~object.__getitem__` is implemented with constant access speed, the mixin
methods will have linear performance; however, if the underlying method
is linear (as it would be with a linked list), the mixins will have
quadratic performance and will likely need to be overridden.

:::: method
index(value, start=0, stop=None)

Return first index of *value*.

Raises `ValueError` if the value is not
present.

Supporting the *start* and *stop* arguments is optional, but
recommended.

::: versionchanged
3.5 The `~sequence.index` method gained
support for the *stop* and *start* arguments.
:::
::::

::: deprecated-removed
3.12 3.17 The `ByteString` ABC has been
deprecated.

Use `isinstance(obj, collections.abc.Buffer)` to test if `obj`
implements the `buffer protocol <bufferobjects>` at runtime. For use in type annotations, either use
`Buffer` or a union that explicitly
specifies the types your code supports (e.g.,
`bytes | bytearray | memoryview`).

`!ByteString` was originally intended to
be an abstract class that would serve as a supertype of both
`bytes` and
`bytearray`. However, since the ABC
never had any methods, knowing that an object was an instance of
`!ByteString` never actually told you
anything useful about the object. Other common buffer types such as
`memoryview` were also never understood
as subtypes of `!ByteString` (either at
runtime or by static type checkers).

See `PEP 688 <688#current-options>` for
more details.
:::
::::::

::: {.Set .MutableSet}
ABCs for read-only and mutable `sets <types-set>`.
:::

::: {.Mapping .MutableMapping}
ABCs for read-only and mutable `mappings <mapping>`.
:::

::: {.MappingView .ItemsView .KeysView .ValuesView}
ABCs for mapping, items, keys, and values
`views <dictionary view>`.
:::

:::::: Awaitable
ABC for `awaitable` objects, which can be
used in `await` expressions. Custom
implementations must provide the `~object.__await__` method.

`Coroutine <coroutine>` objects and
instances of the `~collections.abc.Coroutine` ABC are all instances of this ABC.

:::: note
::: title
Note
:::

In CPython, generator-based coroutines
(`generators <generator>` decorated with
`types.coroutine`) are *awaitables*, even
though they do not have an `~object.__await__` method. Using `isinstance(gencoro, Awaitable)` for them
will return `False`. Use `inspect.isawaitable` to detect them.
::::

::: versionadded
3.5
:::
::::::

:::::: Coroutine
ABC for `coroutine` compatible classes.
These implement the following methods, defined in
`coroutine-objects`:
`~coroutine.send`,
`~coroutine.throw`, and
`~coroutine.close`. Custom
implementations must also implement
`~object.__await__`. All
`Coroutine` instances are also instances
of `Awaitable`.

:::: note
::: title
Note
:::

In CPython, generator-based coroutines
(`generators <generator>` decorated with
`types.coroutine`) are *awaitables*, even
though they do not have an `~object.__await__` method. Using `isinstance(gencoro, Coroutine)` for them
will return `False`. Use `inspect.isawaitable` to detect them.
::::

See `annotating-generators-and-coroutines`
for details on using `!Coroutine` in
type annotations. The variance and order of type parameters correspond
to those of `Generator`.

::: versionadded
3.5
:::
::::::

:::: AsyncIterable
ABC for classes that provide an `__aiter__` method. See also the
definition of `asynchronous iterable`.

::: versionadded
3.5
:::
::::

:::: AsyncIterator
ABC for classes that provide `__aiter__` and `__anext__` methods. See
also the definition of `asynchronous iterator`.

::: versionadded
3.5
:::
::::

:::: AsyncGenerator
ABC for `asynchronous generator` classes
that implement the protocol defined in `525` and `492`.

See `annotating-generators-and-coroutines`
for details on using `!AsyncGenerator`
in type annotations.

::: versionadded
3.6
:::
::::

:::: Buffer
ABC for classes that provide the `~object.__buffer__` method, implementing the
`buffer protocol <bufferobjects>`. See
`688`.

::: versionadded
3.12
:::
::::

## Examples and Recipes

ABCs allow us to ask classes or instances if they provide particular
functionality, for example:

    size = None
    if isinstance(myvar, collections.abc.Sized):
        size = len(myvar)

Several of the ABCs are also useful as mixins that make it easier to
develop classes supporting container APIs. For example, to write a class
supporting the full `Set` API, it is
only necessary to supply the three underlying abstract methods:
`~object.__contains__`,
`~container.__iter__`, and
`~object.__len__`. The ABC supplies the
remaining methods such as `!__and__` and
`~frozenset.isdisjoint`:

    class ListBasedSet(collections.abc.Set):
        ''' Alternate set implementation favoring space over speed
            and not requiring the set elements to be hashable. '''
        def __init__(self, iterable):
            self.elements = lst = []
            for value in iterable:
                if value not in lst:
                    lst.append(value)

        def __iter__(self):
            return iter(self.elements)

        def __contains__(self, value):
            return value in self.elements

        def __len__(self):
            return len(self.elements)

    s1 = ListBasedSet('abcdef')
    s2 = ListBasedSet('defghi')
    overlap = s1 & s2            # The __and__() method is supported automatically

Notes on using `Set` and
`MutableSet` as a mixin:

\(1\)

: Since some set operations create new sets, the default mixin methods
  need a way to create new instances from an
  `iterable`. The class constructor is
  assumed to have a signature in the form `ClassName(iterable)`. That
  assumption is factored-out to an internal
  `classmethod` called
  `!_from_iterable` which calls
  `cls(iterable)` to produce a new set. If the `Set` mixin is being used in a class with a different
  constructor signature, you will need to override
  `!_from_iterable` with a classmethod or
  regular method that can construct new instances from an iterable
  argument.

\(2\)

: To override the comparisons (presumably for speed, as the semantics
  are fixed), redefine `~object.__le__`
  and `~object.__ge__`, then the other
  operations will automatically follow suit.

\(3\)

: The `Set` mixin provides a
  `!_hash` method to compute a hash value
  for the set; however, `~object.__hash__` is not defined because not all sets are
  `hashable` or immutable. To add set
  hashability using mixins, inherit from both `Set` and `Hashable`, then
  define `__hash__ = Set._hash`.

::: seealso
- [OrderedSet recipe](https://code.activestate.com/recipes/576694/) for
  an example built on `MutableSet`.
- For more about ABCs, see the `abc`
  module and `3119`.
:::

[^1]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^2]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^3]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^4]: Checking `isinstance(obj, Iterable)` detects classes that are
    registered as `Iterable` or that
    have an `~container.__iter__` method,
    but it does not detect classes that iterate with the
    `~object.__getitem__` method. The
    only reliable way to determine whether an object is
    `iterable` is to call `iter(obj)`.

[^5]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^6]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^7]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^8]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^9]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^10]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^11]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^12]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^13]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^14]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^15]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.

[^16]: These ABCs override
    `~abc.ABCMeta.__subclasshook__` to
    support testing an interface by verifying the required methods are
    present and have not been set to `None`. This only works for simple interfaces. More complex
    interfaces require registration or direct subclassing.