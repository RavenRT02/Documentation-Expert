# Question

What is RecursiveCharacterTextSplitter and how does it work?

# Base retrieval

## Rank 1

### Content

```text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(document)
```
:::
:::js
```ts
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const splitter = new RecursiveCharacterTextSplitter({ chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.splitText(document)
```
:::  
**Available text splitters**:
- [Recursively split text](/oss/integrations/splitters/recursive_text_splitter)
```

## Rank 2

### Content

```text
title: "Splitting code text splitter integration guide"  
@[RecursiveCharacterTextSplitter] includes prebuilt lists of separators that are useful for [splitting text](/oss/integrations/splitters/) in a specific programming language.  
:::python
Supported languages are stored in the `langchain_text_splitters.Language` enum. They include:  
```
"cpp",
"go",
"java",
"kotlin",
"js",
"ts",
"php",
"proto",
"python",
"rst",
"ruby",
"rust",
"scala",
"swift",
"markdown",
"latex",
"html",
"sol",
"csharp",
"cobol",
"c",
"lua",
"perl",
"haskell"
```  
To view the list of separators for a given language, pass a value from this enum into
```python
RecursiveCharacterTextSplitter.get_separators_for_language
```  
To instantiate a splitter that is tailored for a specific language, pass a value from the enum into
```python
RecursiveCharacterTextSplitter.from_language
```
:::  
:::js
Supported languages are kept in the `SupportedTextSplitterLanguages` type. They include:
```

## Rank 3

### Content

```text
text_splitter = RecursiveCharacterTextSplitter(
chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

print(len(all_splits))
```
:::
:::js
```typescript
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const textSplitter = new RecursiveCharacterTextSplitter({
chunkSize: 1000,
chunkOverlap: 200,
});

const allSplits = await textSplitter.splitDocuments(docs);
```

## Rank 4

### Content

```text
Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain's `RecursiveCharacterTextSplitter` implements this concept:  
- The [`RecursiveCharacterTextSplitter`](/oss/integrations/splitters/recursive_text_splitter) attempts to keep larger units (e.g., paragraphs) intact.
- If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
- This process continues down to the word level if necessary.  
Example usage:  
:::python
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

## Rank 5

### Content

```text
const htmlSplitter = RecursiveCharacterTextSplitter.fromLanguage(
"html",
{ chunkSize: 60, chunkOverlap: 0 }
);
const htmlDocs = htmlSplitter.createDocuments([{ pageContent: htmlText }]);
console.log(htmlDocs);
```
```javascript
[
Document { metadata: {}, pageContent: '<!DOCTYPE html>\n<html>' },
Document { metadata: {}, pageContent: '<head>\n        <title>🦜️🔗 LangChain</title>' },
Document { metadata: {}, pageContent: '<style>\n            body {\n                font-family: Aria' },
Document { metadata: {}, pageContent: 'l, sans-serif;\n            }\n            h1 {' },
Document { metadata: {}, pageContent: 'color: darkblue;\n            }\n        </style>\n    </head' },
Document { metadata: {}, pageContent: '>' },
Document { metadata: {}, pageContent: '<body>' },
Document { metadata: {}, pageContent: '<div>\n            <h1>🦜️🔗 LangChain</h1>' },
Document { metadata: {}, pageContent: '<p>⚡ Building applications with LLMs through composability ⚡' },
Document { metadata: {},
```


---

# Reranked retrieval

## Rank 1

### Content

```text
Text is naturally organized into hierarchical units such as paragraphs, sentences, and words. We can leverage this inherent structure to inform our splitting strategy, creating split that maintain natural language flow, maintain semantic coherence within split, and adapts to varying levels of text granularity. LangChain's `RecursiveCharacterTextSplitter` implements this concept:  
- The [`RecursiveCharacterTextSplitter`](/oss/integrations/splitters/recursive_text_splitter) attempts to keep larger units (e.g., paragraphs) intact.
- If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
- This process continues down to the word level if necessary.  
Example usage:  
:::python
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

## Rank 2

### Content

```text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_text(document)
```
:::
:::js
```ts
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const splitter = new RecursiveCharacterTextSplitter({ chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.splitText(document)
```
:::  
**Available text splitters**:
- [Recursively split text](/oss/integrations/splitters/recursive_text_splitter)
```

## Rank 3

### Content

```text
text_splitter = RecursiveCharacterTextSplitter(
chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

print(len(all_splits))
```
:::
:::js
```typescript
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";

const textSplitter = new RecursiveCharacterTextSplitter({
chunkSize: 1000,
chunkOverlap: 200,
});

const allSplits = await textSplitter.splitDocuments(docs);
```

## Rank 4

### Content

```text
const splitter = new RecursiveCharacterTextSplitter({ chunkSize: 100, chunkOverlap: 0 })
const texts = splitter.createDocuments([{ pageContent: "..." }])
```
```javascript
[
{ pageContent: "...", metadata: {} },
]
```
:::  
Let's go through the parameters set above for `RecursiveCharacterTextSplitter`:  
:::python
- `chunk_size`: The maximum size of a chunk, where size is determined by the `length_function`.
- `chunk_overlap`: Target overlap between chunks. Overlapping chunks helps to mitigate loss of information when context is divided between chunks.
- `length_function`: Function determining the chunk size.
- `is_separator_regex`: Whether the separator list (defaulting to `["\n\n", "\n", " ", ""]`) should be interpreted as regex.
:::  
:::js
- `chunkSize`: The maximum size of a chunk, where size is determined by the `lengthFunction`.
- `chunkOverlap`: Target overlap between chunks. Overlapping chunks helps to mitigate loss of information when context is divided between chunks.
:::
```

## Rank 5

### Content

```text
:::js
Supported languages are kept in the `SupportedTextSplitterLanguages` type. They include:  
```
"cpp",
"go",
"java",
"js",
"php",
"proto",
"python",
"rst",
"ruby",
"rust",
"scala",
"swift",
"markdown",
"latex",
"html",
"sol",
```  
To view the list of separators for a given language, pass a value from this enum into
```ts
RecursiveCharacterTextSplitter.getSeparatorsForLanguage()
```  
To instantiate a splitter that is tailored for a specific language, pass a value from the enum into
```ts
RecursiveCharacterTextSplitter.fromLanguage()
```
:::  
Below we demonstrate examples for the various languages.  
:::python
```python
pip install -qU langchain-text-splitters
```
:::
:::js
<CodeGroup>
```bash npm
npm install @langchain/textsplitters
```  
```bash pnpm
pnpm install @langchain/textsplitters
```  
```bash yarn
yarn add @langchain/textsplitters
```  
```bash bun
bun add @langchain/textsplitters
```
</CodeGroup>
:::  
:::python
```python
from langchain_text_splitters import
```


---

# Question

Explain the difference between pandas.merge() and pandas.concat().

# Base retrieval

## Rank 1

### Content

```text
The `~pandas.concat` function
concatenates an arbitrary amount of `Series` or `DataFrame` objects
along an axis while performing optional set logic (union or
intersection) of the indexes on the other axes. Like
`numpy.concatenate`, `~pandas.concat`
takes a list or dict of homogeneously-typed objects and concatenates
them.  
::: ipython
python  
df1 = pd.DataFrame(  
:  
{  
: \"A\": \[\"A0\", \"A1\", \"A2\", \"A3\"\], \"B\": \[\"B0\", \"B1\",
\"B2\", \"B3\"\], \"C\": \[\"C0\", \"C1\", \"C2\", \"C3\"\], \"D\":
\[\"D0\", \"D1\", \"D2\", \"D3\"\],  
}, index=\[0, 1, 2, 3\],  
)  
df2 = pd.DataFrame(  
:  
{  
: \"A\": \[\"A4\", \"A5\", \"A6\", \"A7\"\], \"B\": \[\"B4\", \"B5\",
\"B6\", \"B7\"\], \"C\": \[\"C4\", \"C5\", \"C6\", \"C7\"\], \"D\":
\[\"D4\", \"D5\", \"D6\", \"D7\"\],  
}, index=\[4, 5, 6, 7\],  
)  
df3 = pd.DataFrame(  
:  
{  
: \"A\": \[\"A8\", \"A9\", \"A10\", \"A11\"\], \"B\": \[\"B8\",
\"B9\", \"B10\", \"B11\"\], \"C\": \[\"C8\", \"C9\", \"C10\",
\"C11\"\], \"D\":
```

## Rank 2

### Content

```text
:  
{  
: \"A\": \[\"A8\", \"A9\", \"A10\", \"A11\"\], \"B\": \[\"B8\",
\"B9\", \"B10\", \"B11\"\], \"C\": \[\"C8\", \"C9\", \"C10\",
\"C11\"\], \"D\": \[\"D8\", \"D9\", \"D10\", \"D11\"\],  
}, index=\[8, 9, 10, 11\],  
)  
frames = \[df1, df2, df3\] result = pd.concat(frames) result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_concat_basic.png p.plot(frames, result,
labels=\[\"df1\", \"df2\", \"df3\"\], vertical=True);
plt.close(\"all\");
:::  
:::: note
::: title
Note
:::  
`~pandas.concat` makes a full copy of the
data, and iteratively reusing `~pandas.concat` can create unnecessary copies. Collect all
`DataFrame` or
`Series` objects in a list before using
`~pandas.concat`.  
``` python
frames = [process_your_file(f) for f in files]
result = pd.concat(frames)
```
::::  
:::: note
::: title
Note
:::  
When concatenating `DataFrame` with
named axes, pandas will attempt to preserve these index/column names
whenever possible. In the case where all inputs share a
```

## Rank 3

### Content

```text
pandas provides various methods for combining and comparing
`Series` or
`DataFrame`.  
- `~pandas.concat`: Merge multiple
`Series` or
`DataFrame` objects along a shared
index or column
- `DataFrame.join`: Merge multiple
`DataFrame` objects along the columns
- `DataFrame.combine_first`: Update
missing values with non-missing values in the same location
- `~pandas.merge`: Combine two
`Series` or
`DataFrame` objects with SQL-style
joining
- `~pandas.merge_ordered`: Combine two
`Series` or
`DataFrame` objects along an ordered
axis
- `~pandas.merge_asof`: Combine two
`Series` or
`DataFrame` objects by near instead of
exact matching keys
- `Series.compare` and
`DataFrame.compare`: Show differences
in values between two `Series` or
`DataFrame` objects
```

## Rank 4

### Content

```text
`~pandas.merge` performs join operations
similar to relational databases like SQL. Users who are familiar with
SQL but new to pandas can reference a
`comparison with SQL<compare_with_sql.join>`.
```

## Rank 5

### Content

```text
You can concatenate a mix of `Series`
and `DataFrame` objects. The
`Series` will be transformed to
`DataFrame` with the column name as the
name of the `Series`.  
::: ipython
python  
s1 = pd.Series(\[\"X0\", \"X1\", \"X2\", \"X3\"\], name=\"X\") result =
pd.concat(\[df1, s1\], axis=1) result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_concat_mixed_ndim.png p.plot(\[df1, s1\], result,
labels=\[\"df1\", \"s1\"\], vertical=False); plt.close(\"all\");
:::  
Unnamed `Series` will be numbered
consecutively.  
::: ipython
python  
s2 = pd.Series(\[\"\_0\", \"\_1\", \"\_2\", \"\_3\"\]) result =
pd.concat(\[df1, s2, s2, s2\], axis=1) result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_concat_unnamed_series.png p.plot(\[df1, s2\], result,
labels=\[\"df1\", \"s2\"\], vertical=False); plt.close(\"all\");
:::  
`ignore_index=True` will drop all name references.  
::: ipython
python  
result = pd.concat(\[df1, s1\], axis=1, ignore_index=True) result
:::  
:::
```


---

# Reranked retrieval

## Rank 1

### Content

```text
pandas provides various methods for combining and comparing
`Series` or
`DataFrame`.  
- `~pandas.concat`: Merge multiple
`Series` or
`DataFrame` objects along a shared
index or column
- `DataFrame.join`: Merge multiple
`DataFrame` objects along the columns
- `DataFrame.combine_first`: Update
missing values with non-missing values in the same location
- `~pandas.merge`: Combine two
`Series` or
`DataFrame` objects with SQL-style
joining
- `~pandas.merge_ordered`: Combine two
`Series` or
`DataFrame` objects along an ordered
axis
- `~pandas.merge_asof`: Combine two
`Series` or
`DataFrame` objects by near instead of
exact matching keys
- `Series.compare` and
`DataFrame.compare`: Show differences
in values between two `Series` or
`DataFrame` objects
```

## Rank 2

### Content

```text
The `~pandas.concat` function
concatenates an arbitrary amount of `Series` or `DataFrame` objects
along an axis while performing optional set logic (union or
intersection) of the indexes on the other axes. Like
`numpy.concatenate`, `~pandas.concat`
takes a list or dict of homogeneously-typed objects and concatenates
them.  
::: ipython
python  
df1 = pd.DataFrame(  
:  
{  
: \"A\": \[\"A0\", \"A1\", \"A2\", \"A3\"\], \"B\": \[\"B0\", \"B1\",
\"B2\", \"B3\"\], \"C\": \[\"C0\", \"C1\", \"C2\", \"C3\"\], \"D\":
\[\"D0\", \"D1\", \"D2\", \"D3\"\],  
}, index=\[0, 1, 2, 3\],  
)  
df2 = pd.DataFrame(  
:  
{  
: \"A\": \[\"A4\", \"A5\", \"A6\", \"A7\"\], \"B\": \[\"B4\", \"B5\",
\"B6\", \"B7\"\], \"C\": \[\"C4\", \"C5\", \"C6\", \"C7\"\], \"D\":
\[\"D4\", \"D5\", \"D6\", \"D7\"\],  
}, index=\[4, 5, 6, 7\],  
)  
df3 = pd.DataFrame(  
:  
{  
: \"A\": \[\"A8\", \"A9\", \"A10\", \"A11\"\], \"B\": \[\"B8\",
\"B9\", \"B10\", \"B11\"\], \"C\": \[\"C8\", \"C9\", \"C10\",
\"C11\"\], \"D\":
```

## Rank 3

### Content

```text
`~pandas.merge` performs join operations
similar to relational databases like SQL. Users who are familiar with
SQL but new to pandas can reference a
`comparison with SQL<compare_with_sql.join>`.
```

## Rank 4

### Content

```text
pandas provides various facilities for easily combining together
`Series` and
`DataFrame` objects with various kinds
of set logic for the indexes and relational algebra functionality in the
case of join / merge-type operations.  
See the `Merging section <merging>`.  
Concatenating pandas objects together row-wise with
`concat`:  
::: ipython
python  
df = pd.DataFrame(np.random.randn(10, 4)) df  
\# break it into pieces pieces = \[df\[:3\], df\[3:7\], df\[7:\]\]  
pd.concat(pieces)
:::  
:::: note
::: title
Note
:::  
Adding a column to a `DataFrame` is
relatively fast. However, adding a row requires a copy, and may be
expensive. We recommend passing a pre-built list of records to the
`DataFrame` constructor instead of
building a `DataFrame` by iteratively
appending records to it.
::::
```

## Rank 5

### Content

```text
:  
{  
: \"A\": \[\"A8\", \"A9\", \"A10\", \"A11\"\], \"B\": \[\"B8\",
\"B9\", \"B10\", \"B11\"\], \"C\": \[\"C8\", \"C9\", \"C10\",
\"C11\"\], \"D\": \[\"D8\", \"D9\", \"D10\", \"D11\"\],  
}, index=\[8, 9, 10, 11\],  
)  
frames = \[df1, df2, df3\] result = pd.concat(frames) result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_concat_basic.png p.plot(frames, result,
labels=\[\"df1\", \"df2\", \"df3\"\], vertical=True);
plt.close(\"all\");
:::  
:::: note
::: title
Note
:::  
`~pandas.concat` makes a full copy of the
data, and iteratively reusing `~pandas.concat` can create unnecessary copies. Collect all
`DataFrame` or
`Series` objects in a list before using
`~pandas.concat`.  
``` python
frames = [process_your_file(f) for f in files]
result = pd.concat(frames)
```
::::  
:::: note
::: title
Note
:::  
When concatenating `DataFrame` with
named axes, pandas will attempt to preserve these index/column names
whenever possible. In the case where all inputs share a
```


---

# Question

How do I create a pathlib.Path object and check whether a file exists?

# Base retrieval

## Rank 1

### Content

```text
that allows to check if
it `exists()`, to traverse using `joinpath()` and `parent`, and to
retrieve data using `read_text()` and `read_bytes()`.
:::  
The `!files` function takes a
[Distribution
Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
name and returns all of the files installed by this distribution. For
example:  
>>> util = [p for p in files('wheel') if 'util.py' in str(p)][0]  # doctest: +SKIP
>>> util  # doctest: +SKIP
PackagePath('wheel/util.py')
>>> util.size  # doctest: +SKIP
859
>>> util.dist  # doctest: +SKIP
<importlib.metadata._hooks.PathDistribution object at 0x101e0cef0>
>>> util.hash  # doctest: +SKIP
<FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>  
Once you have the file, you can also read its contents:  
>>> print(util.read_text())  # doctest: +SKIP
import base64
import sys
...
def as_bytes(s):
if isinstance(s, text_type):
return s.encode('utf-8')
return s  
You can also use the `!locate` method
```

## Rank 2

### Content

```text
if os.path.exists(fn):
respond("200 OK", [("Content-Type", mime_type)])
return util.FileWrapper(open(fn, "rb"))
else:
respond("404 Not Found", [("Content-Type", "text/plain")])
return [b"not found"]  
if __name__ == "__main__":
```

## Rank 3

### Content

```text
An example using *enter_result*:  
def process_file(file_or_path):
if isinstance(file_or_path, str):
```

## Rank 4

### Content

```text
`Path.expanduser`[^2]
`os.path.realpath`                                         `Path.resolve`
`os.path.abspath`                                          `Path.absolute`[^3]
`os.path.exists`                                           `Path.exists`
`os.path.isfile`                                           `Path.is_file`
`os.path.isdir`                                            `Path.is_dir`
`os.path.islink`                                           `Path.is_symlink`
`os.path.isjunction`                                       `Path.is_junction`
`os.path.ismount`                                          `Path.is_mount`
`os.path.samefile`                                         `Path.samefile`
`os.getcwd`                                                `Path.cwd`
`os.stat`                                                  `Path.stat`
`os.lstat`                                                 `Path.lstat`
`os.listdir`
```

## Rank 5

### Content

```text
that are found. If a path is a valid file system path but no
finder is found on `sys.path_hooks` then
`None` is stored.  
Originally specified in `302`.
:::  
:::::::: data
platform  
A string containing a platform identifier. Known values are:  
System           `platform` value
---------------- ------------------
AIX              `'aix'`
Android          `'android'`
Emscripten       `'emscripten'`
FreeBSD          `'freebsd'`
iOS              `'ios'`
Linux            `'linux'`
macOS            `'darwin'`
Windows          `'win32'`
Windows/Cygwin   `'cygwin'`
WASI             `'wasi'`  
On Unix systems not listed in the table, the value is the lowercased OS
name as returned by `uname -s`, with the first part of the version as
returned by `uname -r` appended, e.g. `'sunos5'`, *at the time when
Python was built*. Unless you want to test for a specific system
version, it is therefore recommended to use the following idiom:  
if sys.platform.startswith('sunos'):
```


---

# Reranked retrieval

## Rank 1

### Content

```text
:::: method
Path.touch(mode=0o666, exist_ok=True)  
Create a file at this given path. If *mode* is given, it is combined
with the process\'s `umask` value to determine the file mode and access
flags. If the file already exists, the function succeeds when *exist_ok*
is true (and its modification time is updated to the current time),
otherwise `FileExistsError` is raised.  
::: seealso
The `~Path.open`,
`~Path.write_text` and
`~Path.write_bytes` methods are often
used to create files.
:::
::::  
::::: method
Path.mkdir(mode=0o777, parents=False, exist_ok=False, \*,
parent_mode=None)  
Create a new directory at this given path. If *mode* is given, it is
combined with the process\'s `umask` value to determine the file mode
and access flags. If the path already exists,
`FileExistsError` is raised.  
If *parents* is true, any missing parents of this path are created as
needed; they are created with the default permissions without taking
*mode* into account (mimicking the POSIX `mkdir -p`
```

## Rank 2

### Content

```text
print('symlink')
... elif p.info.is_dir():
...     print('directory')
... elif p.info.exists():
...     print('something else')
... else:
...     print('not found')
...
directory  
If the path was generated from `Path.iterdir` then this attribute is initialized with some information
about the file type gleaned from scanning the parent directory. Merely
accessing `Path.info` does not perform
any filesystem queries.  
To fetch up-to-date information, it\'s best to call
`Path.is_dir`,
`~Path.is_file` and
`~Path.is_symlink` rather than methods of
this attribute. There is no way to reset the cache; instead you can
create a new path object with an empty info cache via `p = Path(p)`.  
::: versionadded
3.14
:::
::::
```

## Rank 3

### Content

```text
that allows to check if
it `exists()`, to traverse using `joinpath()` and `parent`, and to
retrieve data using `read_text()` and `read_bytes()`.
:::  
The `!files` function takes a
[Distribution
Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
name and returns all of the files installed by this distribution. For
example:  
>>> util = [p for p in files('wheel') if 'util.py' in str(p)][0]  # doctest: +SKIP
>>> util  # doctest: +SKIP
PackagePath('wheel/util.py')
>>> util.size  # doctest: +SKIP
859
>>> util.dist  # doctest: +SKIP
<importlib.metadata._hooks.PathDistribution object at 0x101e0cef0>
>>> util.hash  # doctest: +SKIP
<FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>  
Once you have the file, you can also read its contents:  
>>> print(util.read_text())  # doctest: +SKIP
import base64
import sys
...
def as_bytes(s):
if isinstance(s, text_type):
return s.encode('utf-8')
return s  
You can also use the `!locate` method
```

## Rank 4

### Content

```text
Importing the main class:  
>>> from pathlib import Path  
Listing subdirectories:  
>>> p = Path('.')
>>> [x for x in p.iterdir() if x.is_dir()]
[PosixPath('.hg'), PosixPath('docs'), PosixPath('dist'),
PosixPath('__pycache__'), PosixPath('build')]  
Listing Python source files in this directory tree:  
>>> list(p.glob('**/*.py'))
[PosixPath('test_pathlib.py'), PosixPath('setup.py'),
PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
PosixPath('build/lib/pathlib.py')]  
Navigating inside a directory tree:  
>>> p = Path('/etc')
>>> q = p / 'init.d' / 'reboot'
>>> q
PosixPath('/etc/init.d/reboot')
>>> q.resolve()
PosixPath('/etc/rc.d/init.d/halt')  
Querying path properties:  
>>> q.exists()
True
>>> q.is_dir()
False  
Opening a file:  
>>> with q.open() as f: f.readline()
...
'#!/bin/bash\n'
```

## Rank 5

### Content

```text
if os.path.exists(fn):
respond("200 OK", [("Content-Type", mime_type)])
return util.FileWrapper(open(fn, "rb"))
else:
respond("404 Not Found", [("Content-Type", "text/plain")])
return [b"not found"]  
if __name__ == "__main__":
```


---

# Question

What is the difference between a Python list and a tuple?

# Base retrieval

## Rank 1

### Content

```text
We saw that lists and strings have many common properties, such as
indexing and slicing operations. They are two examples of *sequence*
data types (see `typesseq`). Since Python
is an evolving language, other sequence data types may be added. There
is also another standard sequence data type: the *tuple*.  
A tuple consists of a number of values separated by commas, for
instance:  
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> # they support unpacking just like lists:
>>> x = [1, 2, 3]
>>> 0, *x, 4
(0, 1, 2, 3, 4)  
As you see, on output tuples are always enclosed in
```

## Rank 2

### Content

```text
[3, 2, 1])
>>> # they support unpacking just like lists:
>>> x = [1, 2, 3]
>>> 0, *x, 4
(0, 1, 2, 3, 4)  
As you see, on output tuples are always enclosed in parentheses, so that
nested tuples are interpreted correctly; they may be input with or
without surrounding parentheses, although often parentheses are
necessary anyway (if the tuple is part of a larger expression). It is
not possible to assign to the individual items of a tuple, however it is
possible to create tuples which contain mutable objects, such as lists.  
Though tuples may seem similar to lists, they are often used in
different situations and for different purposes. Tuples are
`immutable`, and usually contain a
heterogeneous sequence of elements that are accessed via unpacking (see
later in this section) or indexing (or even by attribute in the case of
`namedtuples <collections.namedtuple>`).
Lists are `mutable`, and their elements
are usually homogeneous and are accessed by iterating over the list.  
A special problem
```

## Rank 3

### Content

```text
Tuples are immutable sequences, typically used to store collections of
heterogeneous data (such as the 2-tuples produced by the
`enumerate` built-in). Tuples are also
used for cases where an immutable sequence of homogeneous data is needed
(such as allowing storage in a `set` or
`dict` instance).  
::: {.tuple(iterable=(), ./)}
Tuples may be constructed in a number of ways:  
- Using a pair of parentheses to denote the empty tuple: `()`
- Using a trailing comma for a singleton tuple: `a,` or `(a,)`
- Separating items with commas: `a, b, c` or `(a, b, c)`
- Using the `tuple` built-in: `tuple()`
or `tuple(iterable)`  
The constructor builds a tuple whose items are the same and in the same
order as *iterable*\'s items. *iterable* may be either a sequence, a
container that supports iteration, or an iterator object. If *iterable*
is already a tuple, it is returned unchanged. For example,
`tuple('abc')` returns `('a', 'b', 'c')` and `tuple( [1, 2, 3] )`
returns `(1, 2, 3)`. If no argument is
```

## Rank 4

### Content

```text
(traversing levels),
lists go vertically (scanning levels).
::::  
Importantly, a list of tuples indexes several complete `MultiIndex`
keys, whereas a tuple of lists refer to several values within a level:  
::: ipython
python  
s = pd.Series(  
: \[1, 2, 3, 4, 5, 6\], index=pd.MultiIndex.from_product(\[\[\"A\",
\"B\"\], \[\"c\", \"d\", \"e\"\]\]),  
) s.loc\[\[(\"A\", \"c\"), (\"B\", \"d\")\]\] \# list of tuples
s.loc\[(\[\"A\", \"B\"\], \[\"c\", \"d\"\])\] \# tuple of lists
:::
```

## Rank 5

### Content

```text
<collections.namedtuple>`).
Lists are `mutable`, and their elements
are usually homogeneous and are accessed by iterating over the list.  
A special problem is the construction of tuples containing 0 or 1 items:
the syntax has some extra quirks to accommodate these. Empty tuples are
constructed by an empty pair of parentheses; a tuple with one item is
constructed by following a value with a comma (it is not sufficient to
enclose a single value in parentheses). Ugly, but effective. For
example:  
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)  
The statement `t = 12345, 54321, 'hello!'` is an example of *tuple
packing*: the values `12345`, `54321` and `'hello!'` are packed together
in a tuple. The reverse operation is also possible:  
>>> x, y, z = t  
This is called, appropriately enough, *sequence unpacking* and works for
any sequence on the right-hand side. Sequence unpacking requires that
there are
```


---

# Reranked retrieval

## Rank 1

### Content

```text
(traversing levels),
lists go vertically (scanning levels).
::::  
Importantly, a list of tuples indexes several complete `MultiIndex`
keys, whereas a tuple of lists refer to several values within a level:  
::: ipython
python  
s = pd.Series(  
: \[1, 2, 3, 4, 5, 6\], index=pd.MultiIndex.from_product(\[\[\"A\",
\"B\"\], \[\"c\", \"d\", \"e\"\]\]),  
) s.loc\[\[(\"A\", \"c\"), (\"B\", \"d\")\]\] \# list of tuples
s.loc\[(\[\"A\", \"B\"\], \[\"c\", \"d\"\])\] \# tuple of lists
:::
```

## Rank 2

### Content

```text
We saw that lists and strings have many common properties, such as
indexing and slicing operations. They are two examples of *sequence*
data types (see `typesseq`). Since Python
is an evolving language, other sequence data types may be added. There
is also another standard sequence data type: the *tuple*.  
A tuple consists of a number of values separated by commas, for
instance:  
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> # they support unpacking just like lists:
>>> x = [1, 2, 3]
>>> 0, *x, 4
(0, 1, 2, 3, 4)  
As you see, on output tuples are always enclosed in
```

## Rank 3

### Content

```text
Python knows a number of *compound* data types, used to group together
other values. The most versatile is the *list*, which can be written as
a list of comma-separated values (items) between square brackets. Lists
might contain items of different types, but usually the items all have
the same type. :  
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]  
Like strings (and all other built-in `sequence` types), lists can be indexed and sliced:  
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]  
Lists also support operations like concatenation:  
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  
Unlike strings, which are `immutable`,
lists are a `mutable` type, i.e. it is
possible to change their content:  
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27,
```

## Rank 4

### Content

```text
<collections.namedtuple>`).
Lists are `mutable`, and their elements
are usually homogeneous and are accessed by iterating over the list.  
A special problem is the construction of tuples containing 0 or 1 items:
the syntax has some extra quirks to accommodate these. Empty tuples are
constructed by an empty pair of parentheses; a tuple with one item is
constructed by following a value with a comma (it is not sufficient to
enclose a single value in parentheses). Ugly, but effective. For
example:  
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)  
The statement `t = 12345, 54321, 'hello!'` is an example of *tuple
packing*: the values `12345`, `54321` and `'hello!'` are packed together
in a tuple. The reverse operation is also possible:  
>>> x, y, z = t  
This is called, appropriately enough, *sequence unpacking* and works for
any sequence on the right-hand side. Sequence unpacking requires that
there are
```

## Rank 5

### Content

```text
z: Mapping[str, str | int] = {}  
`list` only accepts one type argument,
so a type checker would emit an error on the `y` assignment above.
Similarly, `~collections.abc.Mapping`
only accepts two type arguments: the first indicates the type of the
keys, and the second indicates the type of the values.  
Unlike most other Python containers, however, it is common in idiomatic
Python code for tuples to have elements which are not all of the same
type. For this reason, tuples are special-cased in Python\'s typing
system. `tuple` accepts *any number* of
type arguments:
```


---

# Question

How do I read a CSV file into a Pandas DataFrame?

# Base retrieval

## Rank 1

### Content

```text
a context manager and using that handle to read. [See
here](https://stackoverflow.com/questions/17789907/pandas-convert-winzipped-csv-file-to-data-frame)  
[Inferring dtypes from a
file](https://stackoverflow.com/questions/15555005/get-inferred-dataframe-types-iteratively-using-chunksize)  
Dealing with bad lines `2886`  
[Write a multi-row index CSV without writing
duplicates](https://stackoverflow.com/questions/17349574/pandas-write-multiindex-rows-with-to-csv)  
#### Reading multiple files to create a single DataFrame {#cookbook.csv.multiple_files}  
The best way to combine multiple files into a single DataFrame is to
read the individual frames one by one, put all of the individual frames
into a list, and then combine the frames in the list using
`pd.concat`:  
::: ipython
python  
for i in range(3):  
: data = pd.DataFrame(np.random.randn(10, 4))
data.to_csv(\"file\_{}.csv\".format(i))  
files = \[\"file_0.csv\", \"file_1.csv\", \"file_2.csv\"\] result =
pd.concat(\[pd.read_csv(f)
```

## Rank 2

### Content

```text
A handy way to grab data is to use the
`~DataFrame.read_clipboard` method, which
takes the contents of the clipboard buffer and passes them to the
`read_csv` method. For instance, you can copy the following text to the
clipboard (CTRL-C on many operating systems):  
``` console
A B C
x 1 4 p
y 2 5 q
z 3 6 r
```  
And then import the data directly to a `DataFrame` by calling:  
``` python
>>> clipdf = pd.read_clipboard()
>>> clipdf
A B C
x 1 4 p
y 2 5 q
z 3 6 r
```  
The `to_clipboard` method can be used to write the contents of a
`DataFrame` to the clipboard. Following which you can paste the
clipboard contents into other applications (CTRL-V on many operating
systems). Here we illustrate writing a `DataFrame` into clipboard and
reading it back.  
``` python
>>> df = pd.DataFrame(
...     {"A": [1, 2, 3], "B": [4, 5, 6], "C": ["p", "q", "r"]}, index=["x", "y", "z"]
... )
```

## Rank 3

### Content

```text
The `CSV <io.read_csv_table>` docs  
[read_csv in action](https://www.datacamp.com/tutorial/pandas-read-csv)  
[appending to a
csv](https://stackoverflow.com/questions/17134942/pandas-dataframe-output-end-of-csv)  
[Reading a csv
chunk-by-chunk](https://stackoverflow.com/questions/11622652/large-persistent-dataframe-in-pandas/12193309#12193309)  
[Reading only certain rows of a csv
chunk-by-chunk](https://stackoverflow.com/questions/19674212/pandas-data-frame-select-rows-and-clear-memory)  
[Reading the first few lines of a
frame](https://stackoverflow.com/questions/15008970/way-to-read-first-few-lines-for-pandas-dataframe)  
Reading a file that is compressed but not by `gzip/bz2` (the native
compressed formats which `read_csv` understands). This example shows a
`WinZipped` file, but is a general application of opening the file
within a context manager and using that handle to read. [See
here](https://stackoverflow.com/questions/17789907/pandas-convert-winzipped-csv-file-to-data-frame)
```

## Rank 4

### Content

```text
12\], index_col=0,
parse_dates=True, header=10,  
)
:::  
####### Option 2: read column names and then data  
::: ipython
python  
pd.read_csv(StringIO(data), sep=\";\", header=10, nrows=10).columns
columns = pd.read_csv(StringIO(data), sep=\";\", header=10,
nrows=10).columns pd.read_csv( StringIO(data), sep=\";\", index_col=0,
header=12, parse_dates=True, names=columns )
:::
```

## Rank 5

### Content

```text
`Writing to a csv file: <io.store_in_csv>`
using `DataFrame.to_csv`  
::: ipython
python  
df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
df.to_csv(\"foo.csv\")
:::  
`Reading from a csv file: <io.read_csv_table>` using `read_csv`  
::: ipython
python  
pd.read_csv(\"foo.csv\")
:::  
::: {.ipython suppress=""}
python  
import os  
os.remove(\"foo.csv\")
:::
```


---

# Reranked retrieval

## Rank 1

### Content

```text
`read_csv` is capable of inferring delimited (not necessarily
comma-separated) files, as pandas uses the
`python:csv.Sniffer` class of the csv
module. For this, you have to specify `sep=None`.  
::: ipython
python  
df = pd.DataFrame(np.random.randn(10, 4)) df.to_csv(\"tmp2.csv\",
sep=\":\", index=False) pd.read_csv(\"tmp2.csv\", sep=None,
engine=\"python\")
:::  
::: {.ipython suppress=""}
python  
os.remove(\"tmp2.csv\")
:::
```

## Rank 2

### Content

```text
The `CSV <io.read_csv_table>` docs  
[read_csv in action](https://www.datacamp.com/tutorial/pandas-read-csv)  
[appending to a
csv](https://stackoverflow.com/questions/17134942/pandas-dataframe-output-end-of-csv)  
[Reading a csv
chunk-by-chunk](https://stackoverflow.com/questions/11622652/large-persistent-dataframe-in-pandas/12193309#12193309)  
[Reading only certain rows of a csv
chunk-by-chunk](https://stackoverflow.com/questions/19674212/pandas-data-frame-select-rows-and-clear-memory)  
[Reading the first few lines of a
frame](https://stackoverflow.com/questions/15008970/way-to-read-first-few-lines-for-pandas-dataframe)  
Reading a file that is compressed but not by `gzip/bz2` (the native
compressed formats which `read_csv` understands). This example shows a
`WinZipped` file, but is a general application of opening the file
within a context manager and using that handle to read. [See
here](https://stackoverflow.com/questions/17789907/pandas-convert-winzipped-csv-file-to-data-frame)
```

## Rank 3

### Content

```text
a context manager and using that handle to read. [See
here](https://stackoverflow.com/questions/17789907/pandas-convert-winzipped-csv-file-to-data-frame)  
[Inferring dtypes from a
file](https://stackoverflow.com/questions/15555005/get-inferred-dataframe-types-iteratively-using-chunksize)  
Dealing with bad lines `2886`  
[Write a multi-row index CSV without writing
duplicates](https://stackoverflow.com/questions/17349574/pandas-write-multiindex-rows-with-to-csv)  
#### Reading multiple files to create a single DataFrame {#cookbook.csv.multiple_files}  
The best way to combine multiple files into a single DataFrame is to
read the individual frames one by one, put all of the individual frames
into a list, and then combine the frames in the list using
`pd.concat`:  
::: ipython
python  
for i in range(3):  
: data = pd.DataFrame(np.random.randn(10, 4))
data.to_csv(\"file\_{}.csv\".format(i))  
files = \[\"file_0.csv\", \"file_1.csv\", \"file_2.csv\"\] result =
pd.concat(\[pd.read_csv(f)
```

## Rank 4

### Content

```text
`Writing to a csv file: <io.store_in_csv>`
using `DataFrame.to_csv`  
::: ipython
python  
df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
df.to_csv(\"foo.csv\")
:::  
`Reading from a csv file: <io.read_csv_table>` using `read_csv`  
::: ipython
python  
pd.read_csv(\"foo.csv\")
:::  
::: {.ipython suppress=""}
python  
import os  
os.remove(\"foo.csv\")
:::
```

## Rank 5

### Content

```text
You can indicate the data type for the whole `DataFrame` or individual
columns:  
::: ipython
python  
import numpy as np  
data = \"a,b,c,dn1,2,3,4n5,6,7,8n9,10,11\" print(data)  
df = pd.read_csv(StringIO(data), dtype=object) df df\[\"a\"\]\[0\] df =
pd.read_csv(StringIO(data), dtype={\"b\": object, \"c\": np.float64,
\"d\": \"Int64\"}) df.dtypes
:::  
Fortunately, pandas offers more than one way to ensure that your
column(s) contain only one `dtype`. If you\'re unfamiliar with these
concepts, you can see `here<basics.dtypes>` to learn more about dtypes, and
`here<basics.object_conversion>` to learn
more about `object` conversion in pandas.  
For instance, you can use the `converters` argument of
`~pandas.read_csv`:  
::: ipython
python  
data = \"col_1n1n2n\'A\'n4.22\" df = pd.read_csv(StringIO(data),
converters={\"col_1\": str}) df
df\[\"col_1\"\].apply(type).value_counts()
:::  
Or you can use the `~pandas.to_numeric`
function to coerce the dtypes after reading in the data,  
:::
```


---

# Question

What is the purpose of RunnableSequence in LangChain?

# Base retrieval

## Rank 1

### Content

```text
<Accordion title="View complete runnable script">  
Here's a complete, runnable implementation combining all the pieces from this tutorial:  
:::python
```python
from langchain_core.utils.uuid import uuid7
from typing import TypedDict, NotRequired
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, ModelResponse, AgentMiddleware
from langchain.messages import SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from typing import Callable

# Define skill structure
class Skill(TypedDict):
"""A skill that can be progressively disclosed to the agent."""
name: str
description: str
content: str

# Define skills with schemas and business logic
SKILLS: list[Skill] = [
{
"name": "sales_analytics",
"description": "Database schema and business logic for sales data analysis including customers, orders, and revenue.",
"content": """# Sales Analytics Schema

## Tables
```

## Rank 2

### Content

```text
LangChain @[`VectorStore`] objects do not subclass @[Runnable]. LangChain @[Retrievers] are Runnables, so they implement a standard set of methods (e.g., synchronous and asynchronous `invoke` and `batch` operations). Although we can construct retrievers from vector stores, retrievers can interface with non-vector store sources of data, as well (such as external APIs).  
:::python
We can create a simple version of this ourselves, without subclassing `Retriever`. If we choose what method we wish to use to retrieve documents, we can create a runnable easily. Below we will build one around the `similarity_search` method:  
```python
from typing import List

from langchain_core.documents import Document
from langchain_core.runnables import chain

@chain
def retriever(query: str) -> List[Document]:
return vector_store.similarity_search(query, k=1)
```

## Rank 3

### Content

```text
Here's everything together in a runnable script:  
<Expandable title="Complete code" defaultOpen={false}>
:::python
```python
"""
Customer Support State Machine Example

This example demonstrates the state machine pattern.
A single agent dynamically changes its behavior based on the current_step state,
creating a state machine for sequential information collection.
"""

from langchain_core.utils.uuid import uuid7

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from typing import Callable, Literal
from typing_extensions import NotRequired

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, SummarizationMiddleware
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool, ToolRuntime

model = init_chat_model("google_genai:gemini-3.5-flash")
```

## Rank 4

### Content

```text
whether your `args` are
pickleable. (Note that you may have to consider not only your own code
but also code in any libraries that you use.)
::::
:::::  
::: method
enqueue(record)  
Enqueues the record on the queue using `put_nowait()`; you may want to
override this if you want to use blocking behaviour, or a timeout, or a
customized queue implementation.
:::  
:::: attribute
listener  
When created via configuration using
`~logging.config.dictConfig`, this
attribute will contain a `QueueListener`
instance for use with this handler. Otherwise, it will be `None`.  
::: versionadded
3.12
:::
::::
::::::::::::::
```

## Rank 5

### Content

```text
`Empty` exception (*timeout* is
ignored in that case).
:::  
::: method
SimpleQueue.get_nowait()  
Equivalent to `get(False)`.
:::  
::: seealso  
Class `multiprocessing.Queue`  
: A queue class for use in a multi-processing (rather than
multi-threading) context.  
`collections.deque` is an alternative
implementation of unbounded queues with fast atomic
`~collections.deque.append` and
`~collections.deque.popleft` operations
that do not require locking and also support indexing.
:::
```


---

# Reranked retrieval

## Rank 1

### Content

```text
more than just *text generation* - they should also be used to orchestrate more complex flows that interact with other data. LangChain makes it easy to define [tools](/oss/langchain/tools) that LLMs can use dynamically, as well as help with parsing of and access to unstructured data.
</Step>
</Steps>
```

## Rank 2

### Content

```text
Here's everything together in a runnable script:  
<Expandable title="Complete code" defaultOpen={false}>
:::python
```python
"""
Customer Support State Machine Example

This example demonstrates the state machine pattern.
A single agent dynamically changes its behavior based on the current_step state,
creating a state machine for sequential information collection.
"""

from langchain_core.utils.uuid import uuid7

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from typing import Callable, Literal
from typing_extensions import NotRequired

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, SummarizationMiddleware
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool, ToolRuntime

model = init_chat_model("google_genai:gemini-3.5-flash")
```

## Rank 3

### Content

```text
LangChain @[`VectorStore`] objects do not subclass @[Runnable]. LangChain @[Retrievers] are Runnables, so they implement a standard set of methods (e.g., synchronous and asynchronous `invoke` and `batch` operations). Although we can construct retrievers from vector stores, retrievers can interface with non-vector store sources of data, as well (such as external APIs).  
:::python
We can create a simple version of this ourselves, without subclassing `Retriever`. If we choose what method we wish to use to retrieve documents, we can create a runnable easily. Below we will build one around the `similarity_search` method:  
```python
from typing import List

from langchain_core.documents import Document
from langchain_core.runnables import chain

@chain
def retriever(query: str) -> List[Document]:
return vector_store.similarity_search(query, k=1)
```

## Rank 4

### Content

```text
MCP servers run as separate processes—they can't access LangGraph runtime information like the [store](/oss/langgraph/stores), [context](/oss/langchain/context-engineering), or agent state. **Interceptors bridge this gap** by giving you access to this runtime context during MCP tool execution.  
Interceptors also provide middleware-like control over tool calls: you can modify requests, implement retries, add headers dynamically, or short-circuit execution entirely.  
| Section | Description |
|---------|-------------|
| Accessing runtime context | Read user IDs, API keys, store data, and agent state |
| State updates and commands | Update agent state or control graph flow with `Command` |
| Writing interceptors | Patterns for modifying requests, composing interceptors, and error handling |  
#### Accessing runtime context  
When MCP tools are used within a LangChain agent (via `create_agent`), interceptors receive access to the `ToolRuntime` context. This provides access to the tool
```

## Rank 5

### Content

```text
config: RunnableConfig = {"configurable": {"thread_id": "1"}}
agent.invoke({"messages": "hi, my name is bob"}, config)
agent.invoke({"messages": "write a short poem about cats"}, config)
agent.invoke({"messages": "now do the same but for dogs"}, config)
final_response = agent.invoke({"messages": "what's my name?"}, config)

final_response["messages"][-1].pretty_print()
"""
================================== Ai Message ==================================

Your name is Bob!
"""
```  
See [`SummarizationMiddleware`](/oss/langchain/middleware#summarization) for more configuration options.
:::
:::js
To summarize message history in an agent, use the built-in [`summarizationMiddleware`](/oss/langchain/middleware#summarization):  
```typescript
import { createAgent, summarizationMiddleware } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const checkpointer = new MemorySaver();
```


---

# Question

How can I filter rows in a Pandas DataFrame using multiple conditions?

# Base retrieval

## Rank 1

### Content

```text
Select rows where `df.A` is greater than `0`.  
::: ipython
python  
df\[df\[\"A\"\] \> 0\]
:::  
Selecting values from a `DataFrame`
where a boolean condition is met:  
::: ipython
python  
df\[df \> 0\]
:::  
Using `~Series.isin` method for
filtering:  
::: ipython
python  
df2 = df.copy() df2\[\"E\"\] = \[\"one\", \"one\", \"two\", \"three\",
\"four\", \"three\"\] df2 df2\[df2\[\"E\"\].isin(\[\"two\",
\"four\"\])\]
:::
```

## Rank 2

### Content

```text
= pd.DataFrame({\"A\": np.arange(8), \"B\": list(\"aabbbbcc\")})
dff.groupby(\"B\").filter(lambda x: len(x) \> 2)
:::  
Alternatively, instead of dropping the offending groups, we can return a
like-indexed objects where the groups that do not pass the filter are
filled with NaNs.  
::: ipython
python  
dff.groupby(\"B\").filter(lambda x: len(x) \> 2, dropna=False)
:::  
For DataFrames with multiple columns, filters should explicitly specify
a column as the filter criterion.  
::: ipython
python  
dff\[\"C\"\] = np.arange(8) dff.groupby(\"B\").filter(lambda x:
len(x\[\"C\"\]) \> 2)
:::
```

## Rank 3

### Content

```text
you want to check for.  
::: ipython
python  
values = {\'ids\': \[\'a\', \'b\'\], \'vals\': \[1, 3\]}  
df.isin(values)
:::  
To return the DataFrame of booleans where the values are *not* in the
original DataFrame, use the `~` operator:  
::: ipython
python  
values = {\'ids\': \[\'a\', \'b\'\], \'vals\': \[1, 3\]}  
\~df.isin(values)
:::  
Combine DataFrame\'s `isin` with the `any()` and `all()` methods to
quickly select subsets of your data that meet a given criteria. To
select a row where each column meets its own criterion:  
::: ipython
python  
values = {\'ids\': \[\'a\', \'b\'\], \'ids2\': \[\'a\', \'c\'\],
\'vals\': \[1, 3\]}  
row_mask = df.isin(values).all(axis=1)  
df\[row_mask\]
:::
```

## Rank 4

### Content

```text
[Select with multi-column
criteria](https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe)  
::: ipython
python  
df = pd.DataFrame(  
: {\"AAA\": \[4, 5, 6, 7\], \"BBB\": \[10, 20, 30, 40\], \"CCC\": \[100,
50, -30, -50\]}  
) df
:::  
\...and (without assignment returns a Series)  
::: ipython
python  
df.loc\[(df\[\"BBB\"\] \< 25) & (df\[\"CCC\"\] \>= -40), \"AAA\"\]
:::  
\...or (without assignment returns a Series)  
::: ipython
python  
df.loc\[(df\[\"BBB\"\] \> 25) \| (df\[\"CCC\"\] \>= -40), \"AAA\"\]
:::  
\...or (with assignment modifies the DataFrame.)  
::: ipython
python  
df.loc\[(df\[\"BBB\"\] \> 25) \| (df\[\"CCC\"\] \>= 75), \"AAA\"\] = 999
df
:::  
[Select rows with data closest to certain value using
argsort](https://stackoverflow.com/questions/17758023/return-rows-in-a-dataframe-closest-to-a-user-defined-number)  
::: ipython
python  
df = pd.DataFrame(  
: {\"AAA\": \[4, 5, 6, 7\], \"BBB\": \[10, 20, 30, 40\], \"CCC\":
```

## Rank 5

### Content

```text
Consider the `~Series.isin` method of
`Series`, which returns a boolean vector that is true wherever the
`Series` elements exist in the passed list. This allows you to select
rows where one or more columns have values you want:  
::: ipython
python  
s = pd.Series(np.arange(5), index=np.arange(5)\[::-1\], dtype=\'int64\')
s s.isin(\[2, 4, 6\]) s\[s.isin(\[2, 4, 6\])\]
:::  
The same method is available for `Index` objects and is useful for the
cases when you don\'t know which of the sought labels are in fact
present:  
::: ipython
python  
s\[s.index.isin(\[2, 4, 6\])\]  
\# compare it to the following s.reindex(\[2, 4, 6\])
:::  
In addition to that, `MultiIndex` allows selecting a separate level to
use in the membership check:  
::: ipython
python  
s_mi = pd.Series(np.arange(6),  
: index=pd.MultiIndex.from_product(\[\[0, 1\], \[\'a\', \'b\',
\'c\'\]\]))  
s_mi s_mi.iloc\[s_mi.index.isin(\[(1, \'a\'), (2, \'b\'), (0,
\'c\')\])\] s_mi.iloc\[s_mi.index.isin(\[\'a\', \'c\',
```


---

# Reranked retrieval

## Rank 1

### Content

```text
= pd.DataFrame({\"A\": np.arange(8), \"B\": list(\"aabbbbcc\")})
dff.groupby(\"B\").filter(lambda x: len(x) \> 2)
:::  
Alternatively, instead of dropping the offending groups, we can return a
like-indexed objects where the groups that do not pass the filter are
filled with NaNs.  
::: ipython
python  
dff.groupby(\"B\").filter(lambda x: len(x) \> 2, dropna=False)
:::  
For DataFrames with multiple columns, filters should explicitly specify
a column as the filter criterion.  
::: ipython
python  
dff\[\"C\"\] = np.arange(8) dff.groupby(\"B\").filter(lambda x:
len(x\[\"C\"\]) \> 2)
:::
```

## Rank 2

### Content

```text
Select rows where `df.A` is greater than `0`.  
::: ipython
python  
df\[df\[\"A\"\] \> 0\]
:::  
Selecting values from a `DataFrame`
where a boolean condition is met:  
::: ipython
python  
df\[df \> 0\]
:::  
Using `~Series.isin` method for
filtering:  
::: ipython
python  
df2 = df.copy() df2\[\"E\"\] = \[\"one\", \"one\", \"two\", \"three\",
\"four\", \"three\"\] df2 df2\[df2\[\"E\"\].isin(\[\"two\",
\"four\"\])\]
:::
```

## Rank 3

### Content

```text
[Select with multi-column
criteria](https://stackoverflow.com/questions/15315452/selecting-with-complex-criteria-from-pandas-dataframe)  
::: ipython
python  
df = pd.DataFrame(  
: {\"AAA\": \[4, 5, 6, 7\], \"BBB\": \[10, 20, 30, 40\], \"CCC\": \[100,
50, -30, -50\]}  
) df
:::  
\...and (without assignment returns a Series)  
::: ipython
python  
df.loc\[(df\[\"BBB\"\] \< 25) & (df\[\"CCC\"\] \>= -40), \"AAA\"\]
:::  
\...or (without assignment returns a Series)  
::: ipython
python  
df.loc\[(df\[\"BBB\"\] \> 25) \| (df\[\"CCC\"\] \>= -40), \"AAA\"\]
:::  
\...or (with assignment modifies the DataFrame.)  
::: ipython
python  
df.loc\[(df\[\"BBB\"\] \> 25) \| (df\[\"CCC\"\] \>= 75), \"AAA\"\] = 999
df
:::  
[Select rows with data closest to certain value using
argsort](https://stackoverflow.com/questions/17758023/return-rows-in-a-dataframe-closest-to-a-user-defined-number)  
::: ipython
python  
df = pd.DataFrame(  
: {\"AAA\": \[4, 5, 6, 7\], \"BBB\": \[10, 20, 30, 40\], \"CCC\":
```

## Rank 4

### Content

```text
| `DataFrame's <pandas.DataFrame.compare>` and           |
|                           | `Series' <pandas.Series.compare>` `compare()` methods  |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `indexer` and `indices` in                                          |
| TakeIndexer               | `DataFrame's <pandas.DataFrame.take>` and              |
| :::                       | `Series' <pandas.Series.take>` `take()` methods        |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Argument type for `ambiguous` in time operations                                      |
| TimeAmbiguous             |                                                                                       |
| :::                       |
```

## Rank 5

### Content

```text
The `indexing <indexing>` docs.  
[Using both row labels and value
conditionals](https://stackoverflow.com/questions/14725068/pandas-using-row-labels-in-boolean-indexing)  
::: ipython
python  
df = pd.DataFrame(  
: {\"AAA\": \[4, 5, 6, 7\], \"BBB\": \[10, 20, 30, 40\], \"CCC\": \[100,
50, -30, -50\]}  
) df  
df\[(df.AAA \<= 6) & (df.index.isin(\[0, 2, 4\]))\]
:::  
Use loc for label-oriented slicing and iloc positional slicing
`2904`  
::: ipython
python  
df = pd.DataFrame(  
: {\"AAA\": \[4, 5, 6, 7\], \"BBB\": \[10, 20, 30, 40\], \"CCC\": \[100,
50, -30, -50\]}, index=\[\"foo\", \"bar\", \"boo\", \"kar\"\],  
)
:::  
There are 2 explicit slicing methods, with a third general case  
1.  Positional-oriented (Python slicing style : exclusive of end)
2.  Label-oriented (Non-Python slicing style : inclusive of end)
3.  General (Either slicing style : depends on if the slice contains
labels or positions)  
::: ipython
python df.iloc\[0:3\] \# Positional  
df.loc\[\"bar\":\"kar\"\] \#
```


---

# Question

Explain the difference between os.path and pathlib.

# Base retrieval

## Rank 1

### Content

```text
pathlib implements path operations using `PurePath` and `Path` objects, and so
it\'s said to be *object-oriented*. On the other hand, the
`os` and `os.path` modules supply functions that work with low-level `str` and
`bytes` objects, which is a more *procedural* approach. Some users
consider the object-oriented style to be more readable.  
Many functions in `os` and
`os.path` support `bytes` paths and
`paths relative to directory descriptors <dir_fd>`. These features aren\'t available in pathlib.  
Python\'s `str` and `bytes` types, and portions of the
`os` and `os.path` modules, are written in C and are very speedy. pathlib is
written in pure Python and is often slower, but rarely slow enough to
matter.  
pathlib\'s path normalization is slightly more opinionated and
consistent than `os.path`. For example,
whereas `os.path.abspath` eliminates
\"`..`\" segments from a path, which may change its meaning if symlinks
are involved, `Path.absolute` preserves
these segments for greater
```

## Rank 2

### Content

```text
eliminates
\"`..`\" segments from a path, which may change its meaning if symlinks
are involved, `Path.absolute` preserves
these segments for greater safety.  
pathlib\'s path normalization may render it unsuitable for some
applications:  
1.  pathlib normalizes `Path("my_folder/")` to `Path("my_folder")`,
which changes a path\'s meaning when supplied to various operating
system APIs and command-line utilities. Specifically, the absence of
a trailing separator may allow the path to be resolved as either a
file or directory, rather than a directory only.
2.  pathlib normalizes `Path("./my_program")` to `Path("my_program")`,
which changes a path\'s meaning when used as an executable search
path, such as in a shell or when spawning a child process.
Specifically, the absence of a separator in the path may force it to
be looked up in `PATH` rather than
the current directory.  
As a consequence of these differences, pathlib is not a drop-in
replacement for `os.path`.
```

## Rank 3

### Content

```text
::: {.module synopsis="Object-oriented filesystem paths"}
pathlib
:::  
::: versionadded
3.4
:::  
**Source code:** `Lib/pathlib/`  
This module offers classes representing filesystem paths with semantics
appropriate for different operating systems. Path classes are divided
between `pure paths <pure-paths>`, which
provide purely computational operations without I/O, and
`concrete paths <concrete-paths>`, which
inherit from pure paths but also provide I/O operations.  
![Inheritance diagram showing the classes available in pathlib. The
most basic class is PurePath, which has three direct subclasses:
PurePosixPath, PureWindowsPath, and Path. Further to these four
classes, there are two classes that use multiple inheritance:
PosixPath subclasses PurePosixPath and Path, and WindowsPath
subclasses PureWindowsPath and Path.](pathlib-inheritance.png){.invert-in-dark-mode
.invert-in-dark-modealign-center}  
If you\'ve never used this module before or just aren\'t sure which
class is right for
```

## Rank 4

### Content

```text
::: {.module synopsis="Operations on pathnames."}
os.path
:::  
**Source code:** `Lib/genericpath.py`,
`Lib/posixpath.py` (for POSIX) and
`Lib/ntpath.py` (for Windows).  
This module implements some useful functions on pathnames. To read or
write files see `open`, and for accessing
the filesystem see the `os` module. The
path parameters can be passed as strings, or bytes, or any object
implementing the `os.PathLike` protocol.  
Unlike a Unix shell, Python does not do any *automatic* path expansions.
Functions such as `expanduser` and
`expandvars` can be invoked explicitly
when an application desires shell-like path expansion. (See also the
`glob` module.)  
::: seealso
The `pathlib` module offers high-level
path objects.
:::  
:::: note
::: title
Note
:::  
All of these functions accept either only bytes or only string objects
as their parameters. The result is an object of the same type, if a path
or file name is returned.
::::  
:::: note
::: title
Note
:::  
Since different
```

## Rank 5

### Content

```text
If you\'ve never used this module before or just aren\'t sure which
class is right for your task, `Path` is
most likely what you need. It instantiates a
`concrete path <concrete-paths>` for the
platform the code is running on.  
Pure paths are useful in some special cases; for example:  
1.  If you want to manipulate Windows paths on a Unix machine (or vice
versa). You cannot instantiate a `WindowsPath` when running on Unix, but you can instantiate
`PureWindowsPath`.
2.  You want to make sure that your code only manipulates paths without
actually accessing the OS. In this case, instantiating one of the
pure classes may be useful since those simply don\'t have any
OS-accessing operations.  
::: seealso
`428`: The pathlib module \--
object-oriented filesystem paths.
:::  
::: seealso
For low-level path manipulation on strings, you can also use the
`os.path` module.
:::
```


---

# Reranked retrieval

## Rank 1

### Content

```text
pathlib implements path operations using `PurePath` and `Path` objects, and so
it\'s said to be *object-oriented*. On the other hand, the
`os` and `os.path` modules supply functions that work with low-level `str` and
`bytes` objects, which is a more *procedural* approach. Some users
consider the object-oriented style to be more readable.  
Many functions in `os` and
`os.path` support `bytes` paths and
`paths relative to directory descriptors <dir_fd>`. These features aren\'t available in pathlib.  
Python\'s `str` and `bytes` types, and portions of the
`os` and `os.path` modules, are written in C and are very speedy. pathlib is
written in pure Python and is often slower, but rarely slow enough to
matter.  
pathlib\'s path normalization is slightly more opinionated and
consistent than `os.path`. For example,
whereas `os.path.abspath` eliminates
\"`..`\" segments from a path, which may change its meaning if symlinks
are involved, `Path.absolute` preserves
these segments for greater
```

## Rank 2

### Content

```text
::: {.module synopsis="Operations on pathnames."}
os.path
:::  
**Source code:** `Lib/genericpath.py`,
`Lib/posixpath.py` (for POSIX) and
`Lib/ntpath.py` (for Windows).  
This module implements some useful functions on pathnames. To read or
write files see `open`, and for accessing
the filesystem see the `os` module. The
path parameters can be passed as strings, or bytes, or any object
implementing the `os.PathLike` protocol.  
Unlike a Unix shell, Python does not do any *automatic* path expansions.
Functions such as `expanduser` and
`expandvars` can be invoked explicitly
when an application desires shell-like path expansion. (See also the
`glob` module.)  
::: seealso
The `pathlib` module offers high-level
path objects.
:::  
:::: note
::: title
Note
:::  
All of these functions accept either only bytes or only string objects
as their parameters. The result is an object of the same type, if a path
or file name is returned.
::::  
:::: note
::: title
Note
:::  
Since different
```

## Rank 3

### Content

```text
eliminates
\"`..`\" segments from a path, which may change its meaning if symlinks
are involved, `Path.absolute` preserves
these segments for greater safety.  
pathlib\'s path normalization may render it unsuitable for some
applications:  
1.  pathlib normalizes `Path("my_folder/")` to `Path("my_folder")`,
which changes a path\'s meaning when supplied to various operating
system APIs and command-line utilities. Specifically, the absence of
a trailing separator may allow the path to be resolved as either a
file or directory, rather than a directory only.
2.  pathlib normalizes `Path("./my_program")` to `Path("my_program")`,
which changes a path\'s meaning when used as an executable search
path, such as in a shell or when spawning a child process.
Specifically, the absence of a separator in the path may force it to
be looked up in `PATH` rather than
the current directory.  
As a consequence of these differences, pathlib is not a drop-in
replacement for `os.path`.
```

## Rank 4

### Content

```text
If you\'ve never used this module before or just aren\'t sure which
class is right for your task, `Path` is
most likely what you need. It instantiates a
`concrete path <concrete-paths>` for the
platform the code is running on.  
Pure paths are useful in some special cases; for example:  
1.  If you want to manipulate Windows paths on a Unix machine (or vice
versa). You cannot instantiate a `WindowsPath` when running on Unix, but you can instantiate
`PureWindowsPath`.
2.  You want to make sure that your code only manipulates paths without
actually accessing the OS. In this case, instantiating one of the
pure classes may be useful since those simply don\'t have any
OS-accessing operations.  
::: seealso
`428`: The pathlib module \--
object-oriented filesystem paths.
:::  
::: seealso
For low-level path manipulation on strings, you can also use the
`os.path` module.
:::
```

## Rank 5

### Content

```text
::: {.module synopsis="Object-oriented filesystem paths"}
pathlib
:::  
::: versionadded
3.4
:::  
**Source code:** `Lib/pathlib/`  
This module offers classes representing filesystem paths with semantics
appropriate for different operating systems. Path classes are divided
between `pure paths <pure-paths>`, which
provide purely computational operations without I/O, and
`concrete paths <concrete-paths>`, which
inherit from pure paths but also provide I/O operations.  
![Inheritance diagram showing the classes available in pathlib. The
most basic class is PurePath, which has three direct subclasses:
PurePosixPath, PureWindowsPath, and Path. Further to these four
classes, there are two classes that use multiple inheritance:
PosixPath subclasses PurePosixPath and Path, and WindowsPath
subclasses PureWindowsPath and Path.](pathlib-inheritance.png){.invert-in-dark-mode
.invert-in-dark-modealign-center}  
If you\'ve never used this module before or just aren\'t sure which
class is right for
```


---

# Question

What are Python dictionary comprehensions? Provide an example.

# Base retrieval

## Rank 1

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

## Rank 3

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

## Rank 4

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


---

# Reranked retrieval

## Rank 1

### Content

```text
Another useful data type built into Python is the *dictionary* (see
`typesmapping`). Dictionaries are
sometimes found in other languages as \"associative memories\" or
\"associative arrays\". Unlike sequences, which are indexed by a range
of numbers, dictionaries are indexed by *keys*, which can be any
immutable type; strings and numbers can always be keys. Tuples can be
used as keys if they contain only strings, numbers, or tuples; if a
tuple contains any mutable object either directly or indirectly, it
cannot be used as a key. You can\'t use lists as keys, since lists can
be modified in place using index assignments, slice assignments, or
methods like `~list.append` and
`~list.extend`.  
It is best to think of a dictionary as a set of *key: value* pairs, with
the requirement that the keys are unique (within one dictionary). A pair
of braces creates an empty dictionary: `{}`. Placing a comma-separated
list of key:value pairs within the braces adds initial key:value pairs
to the
```

## Rank 2

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

## Rank 3

### Content

```text
Consistent with the dict-like interface,
`~DataFrame.items` iterates through
key-value pairs:  
- **Series**: (index, scalar value) pairs
- **DataFrame**: (column, Series) pairs  
For example:  
::: ipython
python  
for label, ser in df.items():  
: print(label) print(ser)
:::
```

## Rank 4

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

## Rank 5

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


---

# Question

What is the purpose of metadata in LangChain Document objects?

# Base retrieval

## Rank 1

### Content

```text
LangChain implements a @[Document] abstraction, which is intended to represent a unit of text and associated metadata. It has three attributes:  
:::python
- `page_content`: a string representing the content;
- `metadata`: a dict containing arbitrary metadata;
- `id`: (optional) a string identifier for the document.
:::
:::js
- `pageContent`: a string representing the content;
- `metadata`: a dict containing arbitrary metadata;
- `id`: (optional) a string identifier for the document.
:::  
The `metadata` attribute can capture information about the source of the document, its relationship to other documents, and other information. Note that an individual @[`Document`] object often represents a chunk of a larger document.  
We can generate sample documents when desired:  
:::python
```python
from langchain_core.documents import Document
```

## Rank 2

### Content

```text
To create LangChain @[Document] objects (e.g., for use in downstream tasks), use `.createDocuments`.  
```ts
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";
```

## Rank 3

### Content

```text
more than just *text generation* - they should also be used to orchestrate more complex flows that interact with other data. LangChain makes it easy to define [tools](/oss/langchain/tools) that LLMs can use dynamically, as well as help with parsing of and access to unstructured data.
</Step>
</Steps>
```

## Rank 4

### Content

```text
LangChain organizes components into these main categories:  
| Category | Purpose | Key Components | Use Cases |
|----------|---------|---------------|-----------|
| **[Models](/oss/langchain/models)** | AI reasoning and generation | Chat models, LLMs, Embedding models | Text generation, reasoning, semantic understanding |
| **[Tools](/oss/langchain/tools)** | External capabilities | APIs, databases, etc. | Web search, data access, computations |
| **[Agents](/oss/langchain/agents)** | Orchestration and reasoning | ReAct agents, tool calling agents | Nondeterministic workflows, decision making |
| **[Memory](/oss/langchain/short-term-memory)** | Context preservation | Message history, custom state | Conversations, stateful interactions |
| **[Retrievers](/oss/integrations/retrievers)** | Information access | Vector retrievers, web retrievers | RAG, knowledge base search |
| **[Document processing](/oss/integrations/document_loaders)** | Data ingestion | Loaders, splitters, transformers
```

## Rank 5

### Content

```text
<h1>🦜️🔗 LangChain</h1>' },
Document { metadata: {}, pageContent: '<p>⚡ Building applications with LLMs through composability ⚡' },
Document { metadata: {}, pageContent: '</p>\n        </div>' },
Document { metadata: {}, pageContent: '<div>\n            As an open-source project in a rapidly dev' },
Document { metadata: {}, pageContent: 'eloping field, we are extremely open to contributions.' },
Document { metadata: {}, pageContent: '</div>\n    </body>\n</html>' }
]
```
:::
```


---

# Reranked retrieval

## Rank 1

### Content

```text
LangChain implements a @[Document] abstraction, which is intended to represent a unit of text and associated metadata. It has three attributes:  
:::python
- `page_content`: a string representing the content;
- `metadata`: a dict containing arbitrary metadata;
- `id`: (optional) a string identifier for the document.
:::
:::js
- `pageContent`: a string representing the content;
- `metadata`: a dict containing arbitrary metadata;
- `id`: (optional) a string identifier for the document.
:::  
The `metadata` attribute can capture information about the source of the document, its relationship to other documents, and other information. Note that an individual @[`Document`] object often represents a chunk of a larger document.  
We can generate sample documents when desired:  
:::python
```python
from langchain_core.documents import Document
```

## Rank 2

### Content

```text
<h1>🦜️🔗 LangChain</h1>' },
Document { metadata: {}, pageContent: '<p>⚡ Building applications with LLMs through composability ⚡' },
Document { metadata: {}, pageContent: '</p>\n        </div>' },
Document { metadata: {}, pageContent: '<div>\n            As an open-source project in a rapidly dev' },
Document { metadata: {}, pageContent: 'eloping field, we are extremely open to contributions.' },
Document { metadata: {}, pageContent: '</div>\n    </body>\n</html>' }
]
```
:::
```

## Rank 3

### Content

```text
## What is LangChain?

# Hopefully this code block isn't split
LangChain is a framework for...

As an open-source project in a rapidly developing field, we are extremely open to contributions.
`;

const mdSplitter = RecursiveCharacterTextSplitter.fromLanguage(
"markdown",
{ chunkSize: 60, chunkOverlap: 0 }
);
const mdDocs = mdSplitter.createDocuments([ markdownText ]);
console.log(mdDocs);
```
```javascript
[
Document { metadata: {}, pageContent: '# 🦜️🔗 LangChain' },
Document { metadata: {}, pageContent: '⚡ Building applications with LLMs through composability ⚡' },
Document { metadata: {}, pageContent: '## What is LangChain?' },
Document { metadata: {}, pageContent: "# Hopefully this code block isn't split" },
Document { metadata: {}, pageContent: 'LangChain is a framework for...' },
Document { metadata: {}, pageContent: 'As an open-source project in a rapidly developing field, we' },
Document { metadata: {}, pageContent: 'are extremely open to contributions.' }
]
```
:::
```

## Rank 4

### Content

```text
more than just *text generation* - they should also be used to orchestrate more complex flows that interact with other data. LangChain makes it easy to define [tools](/oss/langchain/tools) that LLMs can use dynamically, as well as help with parsing of and access to unstructured data.
</Step>
</Steps>
```

## Rank 5

### Content

```text
documents = [
Document(
page_content="Dogs are great companions, known for their loyalty and friendliness.",
metadata={"source": "mammal-pets-doc"},
),
Document(
page_content="Cats are independent pets that often enjoy their own space.",
metadata={"source": "mammal-pets-doc"},
),
]
```
:::
:::js
```typescript
import { Document } from "@langchain/core/documents";

const documents = [
new Document({
pageContent:
"Dogs are great companions, known for their loyalty and friendliness.",
metadata: { source: "mammal-pets-doc" },
}),
new Document({
pageContent: "Cats are independent pets that often enjoy their own space.",
metadata: { source: "mammal-pets-doc" },
}),
];
```
:::
```


---

