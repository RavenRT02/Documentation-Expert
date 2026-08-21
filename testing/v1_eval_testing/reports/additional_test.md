# Retrieval Evaluation Report

- Retrieval K: 15
- Rerank Top K: 7

# Question 1

**Question:** what is dict comprehension ?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0027 |
| Rerank Score | 0.9752 |

### Content

```text
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create dictionaries from
arbitrary key and value expressions:  
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}  
And dictionary unpacking (via `**`) can be used to merge multiple
dictionaries:  
>>> odds = {i: i**2 for i in (1, 3, 5)}
>>> evens = {i: i**2 for i in (2, 4, 6)}
>>> {**odds, **evens}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}  
>>> all_values = [odds, evens, {0: 0}]
>>> {**i for i in all_values}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36, 0: 0}  
When the keys are simple strings, it is sometimes easier to specify
pairs using keyword arguments:  
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | unittest.mock |
| Section | library |
| Source | library/unittest.mock.md |
| Chunk ID | python:unittest.mock:0068 |
| Rerank Score | 0.0225 |

### Content

```text
:::: function
patch.dict(in_dict, values=(), clear=False, \*\*kwargs)  
Patch a dictionary, or dictionary like object, and restore the
dictionary to its original state after the test, where the restored
dictionary is a copy of the dictionary as it was before the test.  
*in_dict* can be a dictionary or a mapping like container. If it is a
mapping then it must at least support getting, setting and deleting
items plus iterating over keys.  
*in_dict* can also be a string specifying the name of the dictionary,
which will then be fetched by importing it.  
*values* can be a dictionary of values to set in the dictionary.
*values* can also be an iterable of `(key, value)` pairs.  
If *clear* is true then the dictionary will be cleared before the new
values are set.  
`patch.dict` can also be called with
arbitrary keyword arguments to set values in the dictionary.  
::: versionchanged
3.8  
`patch.dict` now returns the patched
dictionary when used as a context manager.
:::
::::  
`patch.dict`
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | compression.zstd |
| Section | library |
| Source | library/compression.zstd.md |
| Chunk ID | python:compression.zstd:0023 |
| Rerank Score | 0.0083 |

### Content

```text
any format restrictions. `False` means
*dict_content* is an ordinary Zstandard dictionary, created from
Zstandard functions, for example, `train_dict` or the external `zstd`
CLI.  
When passing a `!ZstdDict` to a
function, the `!as_digested_dict` and
`!as_undigested_dict` attributes can
control how the dictionary is loaded by passing them as the `zstd_dict`
argument, for example, `compress(data, zstd_dict=zd.as_digested_dict)`.
Digesting a dictionary is a costly operation that occurs when loading a
Zstandard dictionary. When making multiple calls to compression or
decompression, passing a digested dictionary will reduce the overhead of
loading the dictionary.  
> ---------------------------------------------------------------------------------------
>                                   Digested dictionary                Undigested
>                                                                      dictionary
>   ------------------------------- ----------------------------------
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0227 |
| Rerank Score | 0.0021 |

### Content

```text
behavior
was an implementation detail of CPython from 3.6.
:::  
Dictionaries are `generic <generics>` over
two types, signifying (respectively) the types of the dictionary\'s keys
and values.  
These are the operations that dictionaries support (and therefore,
custom mapping types should support too):  
::: describe
list(d)  
Return a list of all the keys used in the dictionary *d*.
:::  
::: describe
len(d)  
Return the number of items in the dictionary *d*.
:::  
:::: describe
d\[key\]  
Return the item of *d* with key *key*. Raises a
`KeyError` if *key* is not in the map.  
If a subclass of dict defines a method
`~object.__missing__` and *key* is not
present, the `d[key]` operation calls that method with the key *key* as
argument. The `d[key]` operation then returns or raises whatever is
returned or raised by the `__missing__(key)` call. No other operations
or methods invoke `~object.__missing__`.
If `~object.__missing__` is not defined,
`KeyError` is raised.
`~object.__missing__`
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | itertools |
| Section | library |
| Source | library/itertools.md |
| Chunk ID | python:itertools:0076 |
| Rerank Score | 0.0027 |

### Content

```text
\[\'D\', \'c\', \'B\', \'A\'\]  
\>\>\> d = dict(a=1, b=2, c=3) \>\>\> it = iter_except(d.popitem,
KeyError) \>\>\> d\[\'d\'\] = 4 \>\>\> next(it) (\'d\', 4) \>\>\>
next(it) (\'c\', 3) \>\>\> next(it) (\'b\', 2) \>\>\> d\[\'e\'\] = 5
\>\>\> next(it) (\'e\', 5) \>\>\> next(it) (\'a\', 1) \>\>\> next(it,
\'empty\') \'empty\'  
\>\>\> first_true(\'ABC0DEF1\', \'9\', str.isdigit) \'0\' \>\>\> \#
Verify that inputs are consumed lazily \>\>\> it = iter(\'ABC0DEF1\')
\>\>\> first_true(it, predicate=str.isdigit) \'0\' \>\>\> \'\'.join(it)
\'DEF1\'  
\>\>\> multinomial(5, 2, 2, 1, 1) 83160 \>\>\> word = \'coffee\' \>\>\>
multinomial(\*Counter(word).values()) == len(set(permutations(word)))
True  
\>\>\> list(running_mean(\[8.5, 9.5, 7.5, 6.5\])) \[8.5, 9.0, 8.5, 8.0\]
\>\>\> list(running_mean(\[37, 33, 38, 28\])) \[37.0, 35.0, 36.0, 34.0\]  
\>\>\> list(running_min(\[37, 33, 38, 28\])) \[37, 33, 33, 28\]  
\>\>\> list(running_max(\[37, 33, 38, 28\])) \[37, 37, 38, 38\]  
\>\>\>
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0028 |
| Rerank Score | 0.0017 |

### Content

```text
When looping through dictionaries, the key and corresponding value can
be retrieved at the same time using the `~dict.items` method. :  
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave  
When looping through a sequence, the position index and corresponding
value can be retrieved at the same time using the
`enumerate` function. :  
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe  
To loop over two or more sequences at the same time, the entries can be
paired with the `zip` function. :  
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.  
To loop over a sequence in
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0026 |
| Rerank Score | 0.6983 |

### Content

```text
a list of all the keys used
in the dictionary, in insertion order (if you want it sorted, just use
`sorted(d)` instead). To check whether a single key is in the
dictionary, use the `in` keyword.  
Here is a small example using a dictionary:  
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> tel['irv']
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'irv'
>>> print(tel.get('irv'))
None
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False  
The `dict` constructor builds
dictionaries directly from sequences of key-value pairs:  
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0027 |
| Rerank Score | 0.9752 |

### Content

```text
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create dictionaries from
arbitrary key and value expressions:  
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}  
And dictionary unpacking (via `**`) can be used to merge multiple
dictionaries:  
>>> odds = {i: i**2 for i in (1, 3, 5)}
>>> evens = {i: i**2 for i in (2, 4, 6)}
>>> {**odds, **evens}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}  
>>> all_values = [odds, evens, {0: 0}]
>>> {**i for i in all_values}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36, 0: 0}  
When the keys are simple strings, it is sometimes easier to specify
pairs using keyword arguments:  
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0026 |
| Rerank Score | 0.6983 |

### Content

```text
a list of all the keys used
in the dictionary, in insertion order (if you want it sorted, just use
`sorted(d)` instead). To check whether a single key is in the
dictionary, use the `in` keyword.  
Here is a small example using a dictionary:  
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> tel['irv']
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'irv'
>>> print(tel.get('irv'))
None
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False  
The `dict` constructor builds
dictionaries directly from sequences of key-value pairs:  
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | compression.zstd |
| Section | library |
| Source | library/compression.zstd.md |
| Chunk ID | python:compression.zstd:0022 |
| Rerank Score | 0.0300 |

### Content

```text
suggestions on the maximum dictionary size.  
The *level* argument (an integer) is the compression level expected to
be passed to the compressors using this dictionary. The dictionary
information varies for each compression level, so tuning for the proper
compression level can make compression more efficient.
:::  
::: {.ZstdDict(dict_content, ./, .*, .is_raw=False)}
A wrapper around Zstandard dictionaries. Dictionaries can be used to
improve the compression of many small chunks of data. Use
`train_dict` if you need to train a new
dictionary from sample data.  
The *dict_content* argument (a `bytes-like object`), is the already trained dictionary information.  
The *is_raw* argument, a boolean, is an advanced parameter controlling
the meaning of *dict_content*. `True` means *dict_content* is a \"raw
content\" dictionary, without any format restrictions. `False` means
*dict_content* is an ordinary Zstandard dictionary, created from
Zstandard functions, for example, `train_dict` or the
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | unittest.mock |
| Section | library |
| Source | library/unittest.mock.md |
| Chunk ID | python:unittest.mock:0068 |
| Rerank Score | 0.0225 |

### Content

```text
:::: function
patch.dict(in_dict, values=(), clear=False, \*\*kwargs)  
Patch a dictionary, or dictionary like object, and restore the
dictionary to its original state after the test, where the restored
dictionary is a copy of the dictionary as it was before the test.  
*in_dict* can be a dictionary or a mapping like container. If it is a
mapping then it must at least support getting, setting and deleting
items plus iterating over keys.  
*in_dict* can also be a string specifying the name of the dictionary,
which will then be fetched by importing it.  
*values* can be a dictionary of values to set in the dictionary.
*values* can also be an iterable of `(key, value)` pairs.  
If *clear* is true then the dictionary will be cleared before the new
values are set.  
`patch.dict` can also be called with
arbitrary keyword arguments to set values in the dictionary.  
::: versionchanged
3.8  
`patch.dict` now returns the patched
dictionary when used as a context manager.
:::
::::  
`patch.dict`
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | compression.zstd |
| Section | library |
| Source | library/compression.zstd.md |
| Chunk ID | python:compression.zstd:0023 |
| Rerank Score | 0.0083 |

### Content

```text
any format restrictions. `False` means
*dict_content* is an ordinary Zstandard dictionary, created from
Zstandard functions, for example, `train_dict` or the external `zstd`
CLI.  
When passing a `!ZstdDict` to a
function, the `!as_digested_dict` and
`!as_undigested_dict` attributes can
control how the dictionary is loaded by passing them as the `zstd_dict`
argument, for example, `compress(data, zstd_dict=zd.as_digested_dict)`.
Digesting a dictionary is a costly operation that occurs when loading a
Zstandard dictionary. When making multiple calls to compression or
decompression, passing a digested dictionary will reduce the overhead of
loading the dictionary.  
> ---------------------------------------------------------------------------------------
>                                   Digested dictionary                Undigested
>                                                                      dictionary
>   ------------------------------- ----------------------------------
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0233 |
| Rerank Score | 0.0080 |

### Content

```text
:::: describe
d \|= other  
Update the dictionary *d* with keys and values from *other*, which may
be either a `mapping` or an
`iterable` of key/value pairs. The values
of *other* take priority when *d* and *other* share keys.  
::: versionadded
3.9
:::
::::  
Dictionaries and dictionary views are reversible. :  
>>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> d
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
>>> list(reversed(d))
['four', 'three', 'two', 'one']
>>> list(reversed(d.values()))
[4, 3, 2, 1]
>>> list(reversed(d.items()))
[('four', 4), ('three', 3), ('two', 2), ('one', 1)]  
::: versionchanged
3.8 Dictionaries are now reversible.
:::  
::: seealso
`frozendict` and
`types.MappingProxyType` can be used to
create a read-only view of a `dict`.
:::
:::::::::::::::::::::::::::::::::  
::: seealso
For detailed information on thread-safety guarantees for
`dict` objects, see
`thread-safety-dict`.
:::
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | itertools |
| Section | library |
| Source | library/itertools.md |
| Chunk ID | python:itertools:0076 |
| Rerank Score | 0.0027 |

### Content

```text
\[\'D\', \'c\', \'B\', \'A\'\]  
\>\>\> d = dict(a=1, b=2, c=3) \>\>\> it = iter_except(d.popitem,
KeyError) \>\>\> d\[\'d\'\] = 4 \>\>\> next(it) (\'d\', 4) \>\>\>
next(it) (\'c\', 3) \>\>\> next(it) (\'b\', 2) \>\>\> d\[\'e\'\] = 5
\>\>\> next(it) (\'e\', 5) \>\>\> next(it) (\'a\', 1) \>\>\> next(it,
\'empty\') \'empty\'  
\>\>\> first_true(\'ABC0DEF1\', \'9\', str.isdigit) \'0\' \>\>\> \#
Verify that inputs are consumed lazily \>\>\> it = iter(\'ABC0DEF1\')
\>\>\> first_true(it, predicate=str.isdigit) \'0\' \>\>\> \'\'.join(it)
\'DEF1\'  
\>\>\> multinomial(5, 2, 2, 1, 1) 83160 \>\>\> word = \'coffee\' \>\>\>
multinomial(\*Counter(word).values()) == len(set(permutations(word)))
True  
\>\>\> list(running_mean(\[8.5, 9.5, 7.5, 6.5\])) \[8.5, 9.0, 8.5, 8.0\]
\>\>\> list(running_mean(\[37, 33, 38, 28\])) \[37.0, 35.0, 36.0, 34.0\]  
\>\>\> list(running_min(\[37, 33, 38, 28\])) \[37, 33, 33, 28\]  
\>\>\> list(running_max(\[37, 33, 38, 28\])) \[37, 37, 38, 38\]  
\>\>\>
```


---

## Observation

_Write your observations here._

============================================================

# Question 2

**Question:** what is list comprehension ?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0011 |
| Rerank Score | 0.9796 |

### Content

```text
target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]  
List comprehensions can contain complex expressions and nested
functions:  
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0008 |
| Rerank Score | 0.9954 |

### Content

```text
List comprehensions provide a concise way to create lists. Common
applications are to make new lists where each element is the result of
some operations applied to each member of another sequence or iterable,
or to create a subsequence of those elements that satisfy a certain
condition.  
For example, assume we want to create a list of squares, like:  
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
Note that this creates (or overwrites) a variable named `x` that still
exists after the loop completes. We can calculate the list of squares
without any side effects using:  
squares = list(map(lambda x: x**2, range(10)))  
or, equivalently:  
squares = [x**2 for x in range(10)]  
which is more concise and readable.  
A list comprehension consists of brackets containing an expression
followed by a `!for` clause, then zero
or more `!for` or
`!if` clauses. The result will be a
new list resulting from evaluating the
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | ast |
| Section | library |
| Source | library/ast.md |
| Chunk ID | python:ast:0029 |
| Rerank Score | 0.4133 |

### Content

```text
:::: {.comprehension(target, .iter, .ifs, .is_async)}
One `for` clause in a comprehension. `target` is the reference to use
for each element - typically a `Name` or
`Tuple` node. `iter` is the object to
iterate over. `ifs` is a list of test expressions: each `for` clause can
have multiple `ifs`.  
`is_async` indicates a comprehension is asynchronous (using an
`async for` instead of `for`). The value is an integer (0 or 1).  
::: doctest
\>\>\> print(ast.dump(ast.parse(\'\[ord(c) for line in file for c in
line\]\', mode=\'eval\'), \... indent=4)) \# Multiple comprehensions in
one. Expression( body=ListComp( elt=Call( func=Name(id=\'ord\'), args=\[
Name(id=\'c\')\]), generators=\[ comprehension( target=Name(id=\'line\',
ctx=Store()), iter=Name(id=\'file\'), is_async=0), comprehension(
target=Name(id=\'c\', ctx=Store()), iter=Name(id=\'line\'),
is_async=0)\]))  
\>\>\> print(ast.dump(ast.parse(\'(n\*\*2 for n in it if n\>5 if
n\<10)\', mode=\'eval\'), \... indent=4)) \# generator
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0012 |
| Rerank Score | 0.9148 |

### Content

```text
The initial expression in a list comprehension can be any arbitrary
expression, including another list comprehension.  
Consider the following example of a 3x4 matrix implemented as a list of
3 lists of length 4:  
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]  
The following list comprehension will transpose rows and columns:  
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]  
As we saw in the previous section, the inner list comprehension is
evaluated in the context of the `for`
that follows it, so this example is equivalent to:  
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]  
which, in turn, is the same as:  
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0015 |
| Rerank Score | 0.5916 |

### Content

```text
be used in list comprehensions, as a way to build a
new list representing the concatenation of an arbitrary number of
iterables:  
>>> x = [[1, 2, 3], [4, 5, 6], [], [7], [8, 9]]
>>> [*element for element in x]
[1, 2, 3, 4, 5, 6, 7, 8, 9]  
Note that the effect is that each element from `x` is unpacked. This
works for arbitrary iterable objects, not just lists:  
>>> x = [[1, 2, 3], 'cat', {'spam': 'eggs'}]
>>> [*element for element in x]
[1, 2, 3, 'c', 'a', 't', 'spam']  
But if the objects in `x` are not iterable, this expression would again
raise an exception.
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0057 |
| Rerank Score | 0.8395 |

### Content

```text
Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).  
::::: {.list(iterable=(), ./)}
Lists may be constructed in several ways:  
- Using a pair of square brackets to denote the empty list: `[]`
- Using square brackets, separating items with commas: `[a]`,
`[a, b, c]`
- Using a list comprehension: `[x for x in iterable]`
- Using the type constructor: `list()` or `list(iterable)`  
The constructor builds a list whose items are the same and in the same
order as *iterable*\'s items. *iterable* may be either a sequence, a
container that supports iteration, or an iterator object. If *iterable*
is already a list, a copy is made and returned, similar to
`iterable[:]`. For example, `list('abc')` returns `['a', 'b', 'c']` and
`list( (1, 2, 3) )` returns `[1, 2, 3]`. If no argument is given, the
constructor creates a new empty list, `[]`.  
Many other operations also produce lists, including
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | itertools |
| Section | library |
| Source | library/itertools.md |
| Chunk ID | python:itertools:0056 |
| Rerank Score | 0.0005 |

### Content

```text
= iter(\'abcdef\')
\>\>\> take(3, it) \[\'a\', \'b\', \'c\'\] \>\>\> list(it) \[\'d\',
\'e\', \'f\'\]  
\>\>\> list(prepend(1, \[2, 3, 4\])) \[1, 2, 3, 4\]  
\>\>\> list(enumerate(\'abc\')) \[(0, \'a\'), (1, \'b\'), (2, \'c\')\]  
\>\>\> for \_ in loops(5): \... print(\'hi\') \... hi hi hi hi hi  
\>\>\> list(tail(3, \'ABCDEFG\')) \[\'E\', \'F\', \'G\'\] \>\>\> \#
Verify the input is consumed greedily \>\>\> input_iterator =
iter(\'ABCDEFG\') \>\>\> output_iterator = tail(3, input_iterator)
\>\>\> list(input_iterator) \[\]  
\>\>\> it = iter(range(10)) \>\>\> consume(it, 3) \>\>\> \# Verify the
input is consumed lazily \>\>\> next(it) 3 \>\>\> \# Verify the input is
consumed completely \>\>\> consume(it) \>\>\> next(it, \'Done\')
\'Done\'  
\>\>\> nth(\'abcde\', 3) \'d\' \>\>\> nth(\'abcde\', 9) is None True
\>\>\> \# Verify that the input is consumed lazily \>\>\> it =
iter(\'abcde\') \>\>\> nth(it, 2) \'c\' \>\>\> list(it) \[\'d\', \'e\'\]  
\>\>\> \[all_equal(s) for s in (\'\',
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0008 |
| Rerank Score | 0.9954 |

### Content

```text
List comprehensions provide a concise way to create lists. Common
applications are to make new lists where each element is the result of
some operations applied to each member of another sequence or iterable,
or to create a subsequence of those elements that satisfy a certain
condition.  
For example, assume we want to create a list of squares, like:  
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
Note that this creates (or overwrites) a variable named `x` that still
exists after the loop completes. We can calculate the list of squares
without any side effects using:  
squares = list(map(lambda x: x**2, range(10)))  
or, equivalently:  
squares = [x**2 for x in range(10)]  
which is more concise and readable.  
A list comprehension consists of brackets containing an expression
followed by a `!for` clause, then zero
or more `!for` or
`!if` clauses. The result will be a
new list resulting from evaluating the
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0011 |
| Rerank Score | 0.9796 |

### Content

```text
target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]  
List comprehensions can contain complex expressions and nested
functions:  
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0012 |
| Rerank Score | 0.9148 |

### Content

```text
The initial expression in a list comprehension can be any arbitrary
expression, including another list comprehension.  
Consider the following example of a 3x4 matrix implemented as a list of
3 lists of length 4:  
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]  
The following list comprehension will transpose rows and columns:  
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]  
As we saw in the previous section, the inner list comprehension is
evaluated in the context of the `for`
that follows it, so this example is equivalent to:  
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]  
which, in turn, is the same as:  
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0057 |
| Rerank Score | 0.8395 |

### Content

```text
Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).  
::::: {.list(iterable=(), ./)}
Lists may be constructed in several ways:  
- Using a pair of square brackets to denote the empty list: `[]`
- Using square brackets, separating items with commas: `[a]`,
`[a, b, c]`
- Using a list comprehension: `[x for x in iterable]`
- Using the type constructor: `list()` or `list(iterable)`  
The constructor builds a list whose items are the same and in the same
order as *iterable*\'s items. *iterable* may be either a sequence, a
container that supports iteration, or an iterator object. If *iterable*
is already a list, a copy is made and returned, similar to
`iterable[:]`. For example, `list('abc')` returns `['a', 'b', 'c']` and
`list( (1, 2, 3) )` returns `[1, 2, 3]`. If no argument is given, the
constructor creates a new empty list, `[]`.  
Many other operations also produce lists, including
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0015 |
| Rerank Score | 0.5916 |

### Content

```text
be used in list comprehensions, as a way to build a
new list representing the concatenation of an arbitrary number of
iterables:  
>>> x = [[1, 2, 3], [4, 5, 6], [], [7], [8, 9]]
>>> [*element for element in x]
[1, 2, 3, 4, 5, 6, 7, 8, 9]  
Note that the effect is that each element from `x` is unpacked. This
works for arbitrary iterable objects, not just lists:  
>>> x = [[1, 2, 3], 'cat', {'spam': 'eggs'}]
>>> [*element for element in x]
[1, 2, 3, 'c', 'a', 't', 'spam']  
But if the objects in `x` are not iterable, this expression would again
raise an exception.
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | ast |
| Section | library |
| Source | library/ast.md |
| Chunk ID | python:ast:0029 |
| Rerank Score | 0.4133 |

### Content

```text
:::: {.comprehension(target, .iter, .ifs, .is_async)}
One `for` clause in a comprehension. `target` is the reference to use
for each element - typically a `Name` or
`Tuple` node. `iter` is the object to
iterate over. `ifs` is a list of test expressions: each `for` clause can
have multiple `ifs`.  
`is_async` indicates a comprehension is asynchronous (using an
`async for` instead of `for`). The value is an integer (0 or 1).  
::: doctest
\>\>\> print(ast.dump(ast.parse(\'\[ord(c) for line in file for c in
line\]\', mode=\'eval\'), \... indent=4)) \# Multiple comprehensions in
one. Expression( body=ListComp( elt=Call( func=Name(id=\'ord\'), args=\[
Name(id=\'c\')\]), generators=\[ comprehension( target=Name(id=\'line\',
ctx=Store()), iter=Name(id=\'file\'), is_async=0), comprehension(
target=Name(id=\'c\', ctx=Store()), iter=Name(id=\'line\'),
is_async=0)\]))  
\>\>\> print(ast.dump(ast.parse(\'(n\*\*2 for n in it if n\>5 if
n\<10)\', mode=\'eval\'), \... indent=4)) \# generator
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0010 |
| Rerank Score | 0.0293 |

### Content

```text
:  
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
File "<stdin>", line 1
[x, x**2 for x in range(6)]
^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2,
```


---

## Observation

_Write your observations here._

============================================================

# Question 3

**Question:** what is dictionary comprehension ?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0027 |
| Rerank Score | 0.1023 |

### Content

```text
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create dictionaries from
arbitrary key and value expressions:  
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}  
And dictionary unpacking (via `**`) can be used to merge multiple
dictionaries:  
>>> odds = {i: i**2 for i in (1, 3, 5)}
>>> evens = {i: i**2 for i in (2, 4, 6)}
>>> {**odds, **evens}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}  
>>> all_values = [odds, evens, {0: 0}]
>>> {**i for i in all_values}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36, 0: 0}  
When the keys are simple strings, it is sometimes easier to specify
pairs using keyword arguments:  
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0225 |
| Rerank Score | 0.0002 |

### Content

```text
for that key becomes the corresponding value in the new
dictionary.  
If keyword arguments are given, the keyword arguments and their values
are added to the dictionary created from the positional argument. If a
key being added is already present, the value from the keyword argument
replaces the value from the positional argument.  
Dictionaries compare equal if and only if they have the same
`(key, value)` pairs (regardless of ordering). Order comparisons
(\'\<\', \'\<=\', \'\>=\', \'\>\') raise `TypeError`. To illustrate dictionary creation and equality, the
following examples all return a dictionary equal to
`{"one": 1, "two": 2, "three": 3}`:  
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> f = dict({'one': 1, 'three': 3}, two=2)
>>> a == b == c == d == e == f
True  
Providing keyword arguments
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | unittest.mock |
| Section | library |
| Source | library/unittest.mock.md |
| Chunk ID | python:unittest.mock:0068 |
| Rerank Score | 0.0010 |

### Content

```text
:::: function
patch.dict(in_dict, values=(), clear=False, \*\*kwargs)  
Patch a dictionary, or dictionary like object, and restore the
dictionary to its original state after the test, where the restored
dictionary is a copy of the dictionary as it was before the test.  
*in_dict* can be a dictionary or a mapping like container. If it is a
mapping then it must at least support getting, setting and deleting
items plus iterating over keys.  
*in_dict* can also be a string specifying the name of the dictionary,
which will then be fetched by importing it.  
*values* can be a dictionary of values to set in the dictionary.
*values* can also be an iterable of `(key, value)` pairs.  
If *clear* is true then the dictionary will be cleared before the new
values are set.  
`patch.dict` can also be called with
arbitrary keyword arguments to set values in the dictionary.  
::: versionchanged
3.8  
`patch.dict` now returns the patched
dictionary when used as a context manager.
:::
::::  
`patch.dict`
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0234 |
| Rerank Score | 0.0009 |

### Content

```text
The objects returned by `dict.keys`,
`dict.values` and
`dict.items` are *view objects*. They
provide a dynamic view on the dictionary\'s entries, which means that
when the dictionary changes, the view reflects these changes.  
Dictionary views can be iterated over to yield their respective data,
and support membership tests:  
::: describe
len(dictview)  
Return the number of entries in the dictionary.
:::  
:::: describe
iter(dictview)  
Return an iterator over the keys, values or items (represented as tuples
of `(key, value)`) in the dictionary.  
Keys and values are iterated over in insertion order. This allows the
creation of `(value, key)` pairs using `zip`: `pairs = zip(d.values(), d.keys())`. Another way to create
the same list is `pairs = [(v, k) for (k, v) in d.items()]`.  
Iterating views while adding or deleting entries in the dictionary may
raise a `RuntimeError` or fail to iterate
over all entries.  
::: versionchanged
3.7 Dictionary order is guaranteed to be insertion
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | stdtypes |
| Section | library |
| Source | library/stdtypes.md |
| Chunk ID | python:stdtypes:0227 |
| Rerank Score | 0.0006 |

### Content

```text
behavior
was an implementation detail of CPython from 3.6.
:::  
Dictionaries are `generic <generics>` over
two types, signifying (respectively) the types of the dictionary\'s keys
and values.  
These are the operations that dictionaries support (and therefore,
custom mapping types should support too):  
::: describe
list(d)  
Return a list of all the keys used in the dictionary *d*.
:::  
::: describe
len(d)  
Return the number of items in the dictionary *d*.
:::  
:::: describe
d\[key\]  
Return the item of *d* with key *key*. Raises a
`KeyError` if *key* is not in the map.  
If a subclass of dict defines a method
`~object.__missing__` and *key* is not
present, the `d[key]` operation calls that method with the key *key* as
argument. The `d[key]` operation then returns or raises whatever is
returned or raised by the `__missing__(key)` call. No other operations
or methods invoke `~object.__missing__`.
If `~object.__missing__` is not defined,
`KeyError` is raised.
`~object.__missing__`
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | ast |
| Section | library |
| Source | library/ast.md |
| Chunk ID | python:ast:0029 |
| Rerank Score | 0.1335 |

### Content

```text
:::: {.comprehension(target, .iter, .ifs, .is_async)}
One `for` clause in a comprehension. `target` is the reference to use
for each element - typically a `Name` or
`Tuple` node. `iter` is the object to
iterate over. `ifs` is a list of test expressions: each `for` clause can
have multiple `ifs`.  
`is_async` indicates a comprehension is asynchronous (using an
`async for` instead of `for`). The value is an integer (0 or 1).  
::: doctest
\>\>\> print(ast.dump(ast.parse(\'\[ord(c) for line in file for c in
line\]\', mode=\'eval\'), \... indent=4)) \# Multiple comprehensions in
one. Expression( body=ListComp( elt=Call( func=Name(id=\'ord\'), args=\[
Name(id=\'c\')\]), generators=\[ comprehension( target=Name(id=\'line\',
ctx=Store()), iter=Name(id=\'file\'), is_async=0), comprehension(
target=Name(id=\'c\', ctx=Store()), iter=Name(id=\'line\'),
is_async=0)\]))  
\>\>\> print(ast.dump(ast.parse(\'(n\*\*2 for n in it if n\>5 if
n\<10)\', mode=\'eval\'), \... indent=4)) \# generator
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | inputoutput |
| Section | tutorial |
| Source | tutorial/inputoutput.md |
| Chunk ID | python:inputoutput:0006 |
| Rerank Score | 0.0009 |

### Content

```text
strings, using placeholders like
`$x` and replacing them with values from a dictionary. This syntax is
easy to use, although it offers much less control for formatting.
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | ast |
| Section | library |
| Source | library/ast.md |
| Chunk ID | python:ast:0029 |
| Rerank Score | 0.1335 |

### Content

```text
:::: {.comprehension(target, .iter, .ifs, .is_async)}
One `for` clause in a comprehension. `target` is the reference to use
for each element - typically a `Name` or
`Tuple` node. `iter` is the object to
iterate over. `ifs` is a list of test expressions: each `for` clause can
have multiple `ifs`.  
`is_async` indicates a comprehension is asynchronous (using an
`async for` instead of `for`). The value is an integer (0 or 1).  
::: doctest
\>\>\> print(ast.dump(ast.parse(\'\[ord(c) for line in file for c in
line\]\', mode=\'eval\'), \... indent=4)) \# Multiple comprehensions in
one. Expression( body=ListComp( elt=Call( func=Name(id=\'ord\'), args=\[
Name(id=\'c\')\]), generators=\[ comprehension( target=Name(id=\'line\',
ctx=Store()), iter=Name(id=\'file\'), is_async=0), comprehension(
target=Name(id=\'c\', ctx=Store()), iter=Name(id=\'line\'),
is_async=0)\]))  
\>\>\> print(ast.dump(ast.parse(\'(n\*\*2 for n in it if n\>5 if
n\<10)\', mode=\'eval\'), \... indent=4)) \# generator
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0027 |
| Rerank Score | 0.1023 |

### Content

```text
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create dictionaries from
arbitrary key and value expressions:  
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}  
And dictionary unpacking (via `**`) can be used to merge multiple
dictionaries:  
>>> odds = {i: i**2 for i in (1, 3, 5)}
>>> evens = {i: i**2 for i in (2, 4, 6)}
>>> {**odds, **evens}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}  
>>> all_values = [odds, evens, {0: 0}]
>>> {**i for i in all_values}
{1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36, 0: 0}  
When the keys are simple strings, it is sometimes easier to specify
pairs using keyword arguments:  
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | datastructures |
| Section | tutorial |
| Source | tutorial/datastructures.md |
| Chunk ID | python:datastructures:0026 |
| Rerank Score | 0.0937 |

### Content

```text
a list of all the keys used
in the dictionary, in insertion order (if you want it sorted, just use
`sorted(d)` instead). To check whether a single key is in the
dictionary, use the `in` keyword.  
Here is a small example using a dictionary:  
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> tel['irv']
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'irv'
>>> print(tel.get('irv'))
None
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False  
The `dict` constructor builds
dictionaries directly from sequences of key-value pairs:  
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}  
In addition, dict comprehensions can be used to create
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | itertools |
| Section | library |
| Source | library/itertools.md |
| Chunk ID | python:itertools:0076 |
| Rerank Score | 0.0037 |

### Content

```text
\[\'D\', \'c\', \'B\', \'A\'\]  
\>\>\> d = dict(a=1, b=2, c=3) \>\>\> it = iter_except(d.popitem,
KeyError) \>\>\> d\[\'d\'\] = 4 \>\>\> next(it) (\'d\', 4) \>\>\>
next(it) (\'c\', 3) \>\>\> next(it) (\'b\', 2) \>\>\> d\[\'e\'\] = 5
\>\>\> next(it) (\'e\', 5) \>\>\> next(it) (\'a\', 1) \>\>\> next(it,
\'empty\') \'empty\'  
\>\>\> first_true(\'ABC0DEF1\', \'9\', str.isdigit) \'0\' \>\>\> \#
Verify that inputs are consumed lazily \>\>\> it = iter(\'ABC0DEF1\')
\>\>\> first_true(it, predicate=str.isdigit) \'0\' \>\>\> \'\'.join(it)
\'DEF1\'  
\>\>\> multinomial(5, 2, 2, 1, 1) 83160 \>\>\> word = \'coffee\' \>\>\>
multinomial(\*Counter(word).values()) == len(set(permutations(word)))
True  
\>\>\> list(running_mean(\[8.5, 9.5, 7.5, 6.5\])) \[8.5, 9.0, 8.5, 8.0\]
\>\>\> list(running_mean(\[37, 33, 38, 28\])) \[37.0, 35.0, 36.0, 34.0\]  
\>\>\> list(running_min(\[37, 33, 38, 28\])) \[37, 33, 33, 28\]  
\>\>\> list(running_max(\[37, 33, 38, 28\])) \[37, 37, 38, 38\]  
\>\>\>
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | compression.zstd |
| Section | library |
| Source | library/compression.zstd.md |
| Chunk ID | python:compression.zstd:0023 |
| Rerank Score | 0.0012 |

### Content

```text
any format restrictions. `False` means
*dict_content* is an ordinary Zstandard dictionary, created from
Zstandard functions, for example, `train_dict` or the external `zstd`
CLI.  
When passing a `!ZstdDict` to a
function, the `!as_digested_dict` and
`!as_undigested_dict` attributes can
control how the dictionary is loaded by passing them as the `zstd_dict`
argument, for example, `compress(data, zstd_dict=zd.as_digested_dict)`.
Digesting a dictionary is a costly operation that occurs when loading a
Zstandard dictionary. When making multiple calls to compression or
decompression, passing a digested dictionary will reduce the overhead of
loading the dictionary.  
> ---------------------------------------------------------------------------------------
>                                   Digested dictionary                Undigested
>                                                                      dictionary
>   ------------------------------- ----------------------------------
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | unittest.mock |
| Section | library |
| Source | library/unittest.mock.md |
| Chunk ID | python:unittest.mock:0068 |
| Rerank Score | 0.0010 |

### Content

```text
:::: function
patch.dict(in_dict, values=(), clear=False, \*\*kwargs)  
Patch a dictionary, or dictionary like object, and restore the
dictionary to its original state after the test, where the restored
dictionary is a copy of the dictionary as it was before the test.  
*in_dict* can be a dictionary or a mapping like container. If it is a
mapping then it must at least support getting, setting and deleting
items plus iterating over keys.  
*in_dict* can also be a string specifying the name of the dictionary,
which will then be fetched by importing it.  
*values* can be a dictionary of values to set in the dictionary.
*values* can also be an iterable of `(key, value)` pairs.  
If *clear* is true then the dictionary will be cleared before the new
values are set.  
`patch.dict` can also be called with
arbitrary keyword arguments to set values in the dictionary.  
::: versionchanged
3.8  
`patch.dict` now returns the patched
dictionary when used as a context manager.
:::
::::  
`patch.dict`
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | inputoutput |
| Section | tutorial |
| Source | tutorial/inputoutput.md |
| Chunk ID | python:inputoutput:0006 |
| Rerank Score | 0.0009 |

### Content

```text
strings, using placeholders like
`$x` and replacing them with values from a dictionary. This syntax is
easy to use, although it offers much less control for formatting.
```


---

## Observation

_Write your observations here._

============================================================

