# Retrieval Evaluation Report

- Retrieval K: 15
- Rerank Top K: 7

# Question 1

**Question:** What is RecursiveCharacterTextSplitter and how does it work?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | index |
| Section | splitters |
| Source | splitters/index.md |
| Chunk ID | langchain:index:0024 |
| Rerank Score | 0.9735 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | code_splitter |
| Section | splitters |
| Source | splitters/code_splitter.md |
| Chunk ID | langchain:code_splitter:0001 |
| Rerank Score | 0.8225 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | knowledge-base |
| Section | langchain |
| Source | langchain/knowledge-base.md |
| Chunk ID | langchain:knowledge-base:0014 |
| Rerank Score | 0.9724 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | index |
| Section | splitters |
| Source | splitters/index.md |
| Chunk ID | langchain:index:0023 |
| Rerank Score | 0.9946 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | code_splitter |
| Section | splitters |
| Source | splitters/code_splitter.md |
| Chunk ID | langchain:code_splitter:0028 |
| Rerank Score | 0.7642 |

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

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | recursive_text_splitter |
| Section | splitters |
| Source | splitters/recursive_text_splitter.md |
| Chunk ID | langchain:recursive_text_splitter:0006 |
| Rerank Score | 0.9588 |

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

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | code_splitter |
| Section | splitters |
| Source | splitters/code_splitter.md |
| Chunk ID | langchain:code_splitter:0038 |
| Rerank Score | 0.8034 |

### Content

```text
const haskellSplitter = RecursiveCharacterTextSplitter.fromLanguage(
"haskell",
{ chunkSize: 50, chunkOverlap: 0 }
);
const haskellDocs = haskellSplitter.createDocuments([{ pageContent: HASKELL_CODE }]);
console.log(haskellDocs);
```
```javascript
[
Document { metadata: {}, pageContent: 'main :: IO ()' },
Document { metadata: {}, pageContent: 'main = do\n    putStrLn "Hello, World!"\n-- Some' },
Document { metadata: {}, pageContent: 'sample functions\nadd :: Int -> Int -> Int\nadd x y' },
Document { metadata: {}, pageContent: '= x + y' }
]
```
:::
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | index |
| Section | splitters |
| Source | splitters/index.md |
| Chunk ID | langchain:index:0023 |
| Rerank Score | 0.9946 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | index |
| Section | splitters |
| Source | splitters/index.md |
| Chunk ID | langchain:index:0024 |
| Rerank Score | 0.9735 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | knowledge-base |
| Section | langchain |
| Source | langchain/knowledge-base.md |
| Chunk ID | langchain:knowledge-base:0014 |
| Rerank Score | 0.9724 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | recursive_text_splitter |
| Section | splitters |
| Source | splitters/recursive_text_splitter.md |
| Chunk ID | langchain:recursive_text_splitter:0006 |
| Rerank Score | 0.9588 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | code_splitter |
| Section | splitters |
| Source | splitters/code_splitter.md |
| Chunk ID | langchain:code_splitter:0002 |
| Rerank Score | 0.8999 |

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

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | code_splitter |
| Section | splitters |
| Source | splitters/code_splitter.md |
| Chunk ID | langchain:code_splitter:0039 |
| Rerank Score | 0.8868 |

### Content

```text
:::python
Here's an example using the PHP text splitter:  
```python
PHP_CODE = """<?php
namespace foo;
class Hello {
public function __construct() { }
}
function hello() {
echo "Hello World!";
}
interface Human {
public function breath();
}
trait Foo { }
enum Color
{
case Red;
case Blue;
}"""
php_splitter = RecursiveCharacterTextSplitter.from_language(
language=Language.PHP, chunk_size=50, chunk_overlap=0
)
php_docs = php_splitter.create_documents([PHP_CODE])
php_docs
```  
```text
[Document(metadata={}, page_content='<?php\nnamespace foo;'),
Document(metadata={}, page_content='class Hello {'),
Document(metadata={}, page_content='public function __construct() { }\n}'),
Document(metadata={}, page_content='function hello() {\n    echo "Hello World!";\n}'),
Document(metadata={}, page_content='interface Human {\n    public function breath();\n}'),
Document(metadata={}, page_content='trait Foo { }\nenum Color\n{\n    case Red;'),
Document(metadata={}, page_content='case
```

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | code_splitter |
| Section | splitters |
| Source | splitters/code_splitter.md |
| Chunk ID | langchain:code_splitter:0006 |
| Rerank Score | 0.8393 |

### Content

```text
:::python
Here's an example using the JS text splitter:  
```python
JS_CODE = """
function helloWorld() {
console.log("Hello, World!");
}

// Call the function
helloWorld();
"""

js_splitter = RecursiveCharacterTextSplitter.from_language(
language=Language.JS, chunk_size=60, chunk_overlap=0
)
js_docs = js_splitter.create_documents([JS_CODE])
js_docs
```  
```javascript
[Document(metadata={}, page_content='function helloWorld() {\n  console.log("Hello, World!");\n}'),
Document(metadata={}, page_content='// Call the function\nhelloWorld();')]
```
:::
:::js
Here's an example using the JS text splitter:  
```ts
const JS_CODE = `
function helloWorld() {
console.log("Hello, World!");
}

// Call the function
helloWorld();
`;
```


---

## Observation

_Write your observations here._

============================================================

# Question 2

**Question:** How do I read a CSV file into a Pandas DataFrame?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0046 |
| Rerank Score | 0.9929 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0189 |
| Rerank Score | 0.1173 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0045 |
| Rerank Score | 0.9956 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0049 |
| Rerank Score | 0.0163 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | 10min |
| Section | user_guide |
| Source | user_guide/10min.md |
| Chunk ID | pandas:10min:0033 |
| Rerank Score | 0.9895 |

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

## Rank 6

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0085 |
| Rerank Score | 0.9994 |

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

## Rank 7

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0094 |
| Rerank Score | 0.0543 |

### Content

```text
#### Writing to CSV format {#io.store_in_csv}  
The `Series` and `DataFrame` objects have an instance method `to_csv`
which allows storing the contents of the object as a
comma-separated-values file. The function takes a number of arguments.
Only the first is required.  
- `path_or_buf`: A string path to the file to write or a file object. If
a file object it must be opened with `newline=''`
- `sep` : Field delimiter for the output file (default \",\")
- `na_rep`: A string representation of a missing value (default \'\')
- `float_format`: Format string for floating point numbers
- `columns`: Columns to write (default None)
- `header`: Whether to write out the column names (default True)
- `index`: whether to write row (index) names (default True)
- `index_label`: Column label(s) for index column(s) if desired. If None
(default), and `header` and `index` are True, then the index names are
used. (A sequence should be given if the `DataFrame` uses MultiIndex).
- `mode` : Python write
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0085 |
| Rerank Score | 0.9994 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0045 |
| Rerank Score | 0.9956 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0046 |
| Rerank Score | 0.9929 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | 10min |
| Section | user_guide |
| Source | user_guide/10min.md |
| Chunk ID | pandas:10min:0033 |
| Rerank Score | 0.9895 |

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

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0044 |
| Rerank Score | 0.8995 |

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

## Rank 6

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0083 |
| Rerank Score | 0.6502 |

### Content

```text
= \'year,indiv,zit,xitn1977,\"A\",1.2,.6n1977,\"B\",1.5,.5\'
print(data) with open(\"mindex_ex.csv\", mode=\"w\") as f: f.write(data)
:::  
The `index_col` argument to `read_csv` can take a list of column numbers
to turn multiple columns into a `MultiIndex` for the index of the
returned object:  
::: ipython
python  
df = pd.read_csv(\"mindex_ex.csv\", index_col=\[0, 1\]) df
df.loc\[1977\]
:::  
::: {.ipython suppress=""}
python  
os.remove(\"mindex_ex.csv\")
:::  
#### Reading columns with a `MultiIndex` {#io.multi_index_columns}  
By specifying list of row locations for the `header` argument, you can
read in a `MultiIndex` for the columns. Specifying non-consecutive rows
will skip the intervening rows.  
::: ipython
python  
mi_idx = pd.MultiIndex.from_arrays(\[\[1, 2, 3, 4\], list(\"abcd\")\],
names=list(\"ab\")) mi_col = pd.MultiIndex.from_arrays(\[\[1, 2\],
list(\"ab\")\], names=list(\"cd\")) df = pd.DataFrame(np.ones((4, 2)),
index=mi_idx, columns=mi_col)
```

## Rank 7

| Field | Value |
|------|-------|
| Library | pandas |
| Module | basics |
| Section | user_guide |
| Source | user_guide/basics.md |
| Chunk ID | pandas:basics:0033 |
| Rerank Score | 0.6086 |

### Content

```text
In [148]: bb = pd.read_csv("data/baseball.csv", index_col="id")
```


---

## Observation

_Write your observations here._

============================================================

# Question 3

**Question:** What is the purpose of RunnableSequence in LangChain?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | skills-sql-assistant |
| Section | langchain |
| Source | langchain/multi-agent/skills-sql-assistant.md |
| Chunk ID | langchain:skills-sql-assistant:0056 |
| Rerank Score | 0.0044 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | knowledge-base |
| Section | langchain |
| Source | langchain/knowledge-base.md |
| Chunk ID | langchain:knowledge-base:0029 |
| Rerank Score | 0.1056 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | handoffs-customer-support |
| Section | langchain |
| Source | langchain/multi-agent/handoffs-customer-support.md |
| Chunk ID | langchain:handoffs-customer-support:0043 |
| Rerank Score | 0.2143 |

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

| Field | Value |
|------|-------|
| Library | python |
| Module | logging.handlers |
| Section | library |
| Source | library/logging.handlers.md |
| Chunk ID | python:logging.handlers:0052 |
| Rerank Score | 0.0001 |

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

| Field | Value |
|------|-------|
| Library | python |
| Module | queue |
| Section | library |
| Source | library/queue.md |
| Chunk ID | python:queue:0018 |
| Rerank Score | 0.0001 |

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

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | mcp |
| Section | langchain |
| Source | langchain/mcp.md |
| Chunk ID | langchain:mcp:0030 |
| Rerank Score | 0.0221 |

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

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | multiprocessing |
| Section | library |
| Source | library/multiprocessing.md |
| Chunk ID | python:multiprocessing:0099 |
| Rerank Score | 0.0002 |

### Content

```text
a shared `threading.Lock` object
and return a proxy for it.
:::  
::: method
Namespace()  
Create a shared `Namespace` object and
return a proxy for it.
:::  
::: method
Queue(\[maxsize\])  
Create a shared `queue.Queue` object and
return a proxy for it.
:::  
::: method
RLock()  
Create a shared `threading.RLock` object
and return a proxy for it.
:::  
::: method
Semaphore(\[value\])  
Create a shared `threading.Semaphore`
object and return a proxy for it.
:::  
::: method
Array(typecode, sequence)  
Create an array and return a proxy for it.
:::  
::: method
Value(typecode, value)  
Create an object with a writable `value` attribute and return a proxy
for it.
:::  
::: method
dict() dict(mapping) dict(sequence)  
Create a shared `dict` object and return
a proxy for it.
:::  
::: method
list() list(sequence)  
Create a shared `list` object and return
a proxy for it.
:::  
:::: method
set() set(sequence) set(mapping)  
Create a shared `set` object and return
a proxy for it.  
:::
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | philosophy |
| Section | langchain |
| Source | langchain/philosophy.md |
| Chunk ID | langchain:philosophy:0003 |
| Rerank Score | 0.9379 |

### Content

```text
more than just *text generation* - they should also be used to orchestrate more complex flows that interact with other data. LangChain makes it easy to define [tools](/oss/langchain/tools) that LLMs can use dynamically, as well as help with parsing of and access to unstructured data.
</Step>
</Steps>
```

## Rank 2

| Field | Value |
|------|-------|
| Library | langchain |
| Module | handoffs-customer-support |
| Section | langchain |
| Source | langchain/multi-agent/handoffs-customer-support.md |
| Chunk ID | langchain:handoffs-customer-support:0043 |
| Rerank Score | 0.2143 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | knowledge-base |
| Section | langchain |
| Source | langchain/knowledge-base.md |
| Chunk ID | langchain:knowledge-base:0029 |
| Rerank Score | 0.1056 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | mcp |
| Section | langchain |
| Source | langchain/mcp.md |
| Chunk ID | langchain:mcp:0030 |
| Rerank Score | 0.0221 |

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

| Field | Value |
|------|-------|
| Library | langchain |
| Module | short-term-memory |
| Section | langchain |
| Source | langchain/short-term-memory.md |
| Chunk ID | langchain:short-term-memory:0028 |
| Rerank Score | 0.0064 |

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

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | skills-sql-assistant |
| Section | langchain |
| Source | langchain/multi-agent/skills-sql-assistant.md |
| Chunk ID | langchain:skills-sql-assistant:0056 |
| Rerank Score | 0.0044 |

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

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | context |
| Section | concepts |
| Source | concepts/context.md |
| Chunk ID | langchain:context:0010 |
| Rerank Score | 0.0021 |

### Content

```text
**Dynamic runtime context** represents mutable data that can evolve during a single run and is managed through the LangGraph state object. This includes conversation history, intermediate results, and values derived from tools or LLM outputs. In LangGraph, the state object acts as [short-term memory](/oss/concepts/memory) during a run.  
<Tabs>
<Tab title="In an agent">
Example shows how to incorporate state into an agent **prompt**.  
:::python
State can also be accessed by the agent's **tools**, which can read or update the state as needed. See [tool calling guide](/oss/langchain/tools#short-term-memory-state) for details.
:::
:::js
State can also be accessed by the agent's **tools**, which can read or update the state as needed. See [tool calling guide](/oss/langchain/tools#access-context) for details.
:::  
:::python  
```python
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain.agents import AgentState
```


---

## Observation

_Write your observations here._

============================================================

# Question 4

**Question:** Hi

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | wsgiref |
| Section | library |
| Source | library/wsgiref.md |
| Chunk ID | python:wsgiref:0026 |
| Rerank Score | 0.6565 |

### Content

```text
return b"Hello World"
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0055 |
| Rerank Score | 0.1456 |

### Content

```text
def greet_bad(cond: bool) -> AnyStr:
return "hi there!" if cond else b"greetings!"
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | tempfile |
| Section | library |
| Source | library/tempfile.md |
| Chunk ID | python:tempfile:0022 |
| Rerank Score | 0.0113 |

### Content

```text
>>> fp.seek(0)
>>> fp.read()
b'Hello world!'
```

## Rank 4

| Field | Value |
|------|-------|
| Library | langchain |
| Module | academy |
| Section | langchain |
| Source | langchain/academy.md |
| Chunk ID | langchain:academy:0001 |
| Rerank Score | 0.0007 |

### Content

```text
title: LangChain Academy
url: https://academy.langchain.com/
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0056 |
| Rerank Score | 0.0206 |

### Content

```text
def greet_proper(cond: bool) -> str | bytes:
return "hi there!" if cond else b"greetings!"  
::: deprecated-removed
3.13 3.18 Deprecated in favor of the new
`type parameter syntax <type-params>`. Use
`class A[T: (str, bytes)]: ...` instead of importing `AnyStr`. See
`695` for more details.  
In Python 3.16, `AnyStr` will be removed from `typing.__all__`, and
deprecation warnings will be emitted at runtime when it is accessed or
imported from `typing`. `AnyStr` will be removed from `typing` in Python
3.18.
:::
::::  
::::: data
LiteralString  
Special type that includes only literal strings.  
Any string literal is compatible with `LiteralString`, as is another
`LiteralString`. However, an object typed as just `str` is not. A string
created by composing `LiteralString`-typed objects is also acceptable as
a `LiteralString`.  
Example:  
::: testcode  
def run_query(sql: LiteralString) -\> None:  
: \...  
def caller(arbitrary_string: str, literal_string: LiteralString) -\> None:  
:
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | mmap |
| Section | library |
| Source | library/mmap.md |
| Chunk ID | python:mmap:0012 |
| Rerank Score | 0.0051 |

### Content

```text
print(mm[:5])  # prints b"Hello"
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | inspect |
| Section | library |
| Source | library/inspect.md |
| Chunk ID | python:inspect:0063 |
| Rerank Score | 0.0541 |

### Content

```text
pass
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | wsgiref |
| Section | library |
| Source | library/wsgiref.md |
| Chunk ID | python:wsgiref:0026 |
| Rerank Score | 0.6565 |

### Content

```text
return b"Hello World"
```

## Rank 2

| Field | Value |
|------|-------|
| Library | pandas |
| Module | extensions |
| Section | reference |
| Source | reference/extensions.md |
| Chunk ID | pandas:extensions:0001 |
| Rerank Score | 0.4090 |

### Content

```text
{{ header }}
```

## Rank 3

| Field | Value |
|------|-------|
| Library | pandas |
| Module | index |
| Section | reference |
| Source | reference/index.md |
| Chunk ID | pandas:index:0001 |
| Rerank Score | 0.4090 |

### Content

```text
{{ header }}
```

## Rank 4

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | reference |
| Source | reference/io.md |
| Chunk ID | pandas:io:0001 |
| Rerank Score | 0.4090 |

### Content

```text
{{ header }}
```

## Rank 5

| Field | Value |
|------|-------|
| Library | pandas |
| Module | offset_frequency |
| Section | reference |
| Source | reference/offset_frequency.md |
| Chunk ID | pandas:offset_frequency:0001 |
| Rerank Score | 0.4090 |

### Content

```text
{{ header }}
```

## Rank 6

| Field | Value |
|------|-------|
| Library | pandas |
| Module | options |
| Section | reference |
| Source | reference/options.md |
| Chunk ID | pandas:options:0001 |
| Rerank Score | 0.4090 |

### Content

```text
{{ header }}
```

## Rank 7

| Field | Value |
|------|-------|
| Library | pandas |
| Module | series |
| Section | reference |
| Source | reference/series.md |
| Chunk ID | pandas:series:0001 |
| Rerank Score | 0.4090 |

### Content

```text
{{ header }}
```


---

## Observation

_Write your observations here._

============================================================

# Question 5

**Question:** Hello

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | wsgiref |
| Section | library |
| Source | library/wsgiref.md |
| Chunk ID | python:wsgiref:0026 |
| Rerank Score | 0.8915 |

### Content

```text
return b"Hello World"
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | tempfile |
| Section | library |
| Source | library/tempfile.md |
| Chunk ID | python:tempfile:0022 |
| Rerank Score | 0.1248 |

### Content

```text
>>> fp.seek(0)
>>> fp.read()
b'Hello world!'
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | mmap |
| Section | library |
| Source | library/mmap.md |
| Chunk ID | python:mmap:0012 |
| Rerank Score | 0.8290 |

### Content

```text
print(mm[:5])  # prints b"Hello"
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0055 |
| Rerank Score | 0.0012 |

### Content

```text
def greet_bad(cond: bool) -> AnyStr:
return "hi there!" if cond else b"greetings!"
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | tokenize |
| Section | library |
| Source | library/tokenize.md |
| Chunk ID | python:tokenize:0011 |
| Rerank Score | 0.0092 |

### Content

```text
NAME           'say_hello'
1,13-1,14:          OP             '('
1,14-1,15:          OP             ')'
1,15-1,16:          OP             ':'
1,16-1,17:          NEWLINE        '\n'
2,0-2,4:            INDENT         '    '
2,4-2,9:            NAME           'print'
2,9-2,10:           OP             '('
2,10-2,25:          STRING         '"Hello, World!"'
2,25-2,26:          OP             ')'
2,26-2,27:          NEWLINE        '\n'
3,0-3,1:            NL             '\n'
4,0-4,0:            DEDENT         ''
4,0-4,9:            NAME           'say_hello'
4,9-4,10:           OP             '('
4,10-4,11:          OP             ')'
4,11-4,12:          NEWLINE        '\n'
5,0-5,0:            ENDMARKER      ''
```  
The exact token type names can be displayed using the
`-e` option:  
``` shell-session
$ python -m tokenize -e hello.py
0,0-0,0:            ENCODING       'utf-8'
1,0-1,3:            NAME           'def'
1,4-1,13:           NAME           'say_hello'
1,13-1,14:
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0056 |
| Rerank Score | 0.0001 |

### Content

```text
def greet_proper(cond: bool) -> str | bytes:
return "hi there!" if cond else b"greetings!"  
::: deprecated-removed
3.13 3.18 Deprecated in favor of the new
`type parameter syntax <type-params>`. Use
`class A[T: (str, bytes)]: ...` instead of importing `AnyStr`. See
`695` for more details.  
In Python 3.16, `AnyStr` will be removed from `typing.__all__`, and
deprecation warnings will be emitted at runtime when it is accessed or
imported from `typing`. `AnyStr` will be removed from `typing` in Python
3.18.
:::
::::  
::::: data
LiteralString  
Special type that includes only literal strings.  
Any string literal is compatible with `LiteralString`, as is another
`LiteralString`. However, an object typed as just `str` is not. A string
created by composing `LiteralString`-typed objects is also acceptable as
a `LiteralString`.  
Example:  
::: testcode  
def run_query(sql: LiteralString) -\> None:  
: \...  
def caller(arbitrary_string: str, literal_string: LiteralString) -\> None:  
:
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | mmap |
| Section | library |
| Source | library/mmap.md |
| Chunk ID | python:mmap:0014 |
| Rerank Score | 0.0731 |

### Content

```text
mm.seek(0)
print(mm.readline())  # prints b"Hello  world!\n"
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | wsgiref |
| Section | library |
| Source | library/wsgiref.md |
| Chunk ID | python:wsgiref:0026 |
| Rerank Score | 0.8915 |

### Content

```text
return b"Hello World"
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | mmap |
| Section | library |
| Source | library/mmap.md |
| Chunk ID | python:mmap:0012 |
| Rerank Score | 0.8290 |

### Content

```text
print(mm[:5])  # prints b"Hello"
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | tempfile |
| Section | library |
| Source | library/tempfile.md |
| Chunk ID | python:tempfile:0022 |
| Rerank Score | 0.1248 |

### Content

```text
>>> fp.seek(0)
>>> fp.read()
b'Hello world!'
```

## Rank 4

| Field | Value |
|------|-------|
| Library | pandas |
| Module | frame |
| Section | reference |
| Source | reference/frame.md |
| Chunk ID | pandas:frame:0001 |
| Rerank Score | 0.0960 |

### Content

```text
{{ header }}
```

## Rank 5

| Field | Value |
|------|-------|
| Library | pandas |
| Module | general_functions |
| Section | reference |
| Source | reference/general_functions.md |
| Chunk ID | pandas:general_functions:0001 |
| Rerank Score | 0.0960 |

### Content

```text
{{ header }}
```

## Rank 6

| Field | Value |
|------|-------|
| Library | pandas |
| Module | indexing |
| Section | reference |
| Source | reference/indexing.md |
| Chunk ID | pandas:indexing:0001 |
| Rerank Score | 0.0960 |

### Content

```text
{{ header }}
```

## Rank 7

| Field | Value |
|------|-------|
| Library | pandas |
| Module | offset_frequency |
| Section | reference |
| Source | reference/offset_frequency.md |
| Chunk ID | pandas:offset_frequency:0001 |
| Rerank Score | 0.0960 |

### Content

```text
{{ header }}
```


---

## Observation

_Write your observations here._

============================================================

# Question 6

**Question:** How are you?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0055 |
| Rerank Score | 0.0000 |

### Content

```text
def greet_bad(cond: bool) -> AnyStr:
return "hi there!" if cond else b"greetings!"
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | wsgiref |
| Section | library |
| Source | library/wsgiref.md |
| Chunk ID | python:wsgiref:0026 |
| Rerank Score | 0.0002 |

### Content

```text
return b"Hello World"
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | inspect |
| Section | library |
| Source | library/inspect.md |
| Chunk ID | python:inspect:0063 |
| Rerank Score | 0.0002 |

### Content

```text
pass
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | tempfile |
| Section | library |
| Source | library/tempfile.md |
| Chunk ID | python:tempfile:0022 |
| Rerank Score | 0.0001 |

### Content

```text
>>> fp.seek(0)
>>> fp.read()
b'Hello world!'
```

## Rank 5

| Field | Value |
|------|-------|
| Library | pandas |
| Module | gotchas |
| Section | user_guide |
| Source | user_guide/gotchas.md |
| Chunk ID | pandas:gotchas:0001 |
| Rerank Score | 0.0001 |

### Content

```text
::: {#gotchas}
{{ header }}
:::
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0056 |
| Rerank Score | 0.0000 |

### Content

```text
def greet_proper(cond: bool) -> str | bytes:
return "hi there!" if cond else b"greetings!"  
::: deprecated-removed
3.13 3.18 Deprecated in favor of the new
`type parameter syntax <type-params>`. Use
`class A[T: (str, bytes)]: ...` instead of importing `AnyStr`. See
`695` for more details.  
In Python 3.16, `AnyStr` will be removed from `typing.__all__`, and
deprecation warnings will be emitted at runtime when it is accessed or
imported from `typing`. `AnyStr` will be removed from `typing` in Python
3.18.
:::
::::  
::::: data
LiteralString  
Special type that includes only literal strings.  
Any string literal is compatible with `LiteralString`, as is another
`LiteralString`. However, an object typed as just `str` is not. A string
created by composing `LiteralString`-typed objects is also acceptable as
a `LiteralString`.  
Example:  
::: testcode  
def run_query(sql: LiteralString) -\> None:  
: \...  
def caller(arbitrary_string: str, literal_string: LiteralString) -\> None:  
:
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | removed |
| Section | library |
| Source | library/removed.md |
| Chunk ID | python:removed:0001 |
| Rerank Score | 0.0001 |

### Content

```text
tocdepth
: 1
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | signal |
| Section | library |
| Source | library/signal.md |
| Chunk ID | python:signal:0038 |
| Rerank Score | 0.0924 |

### Content

```text
...
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | test |
| Section | library |
| Source | library/test.md |
| Chunk ID | python:test:0036 |
| Rerank Score | 0.0924 |

### Content

```text
...
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | test |
| Section | library |
| Source | library/test.md |
| Chunk ID | python:test:0037 |
| Rerank Score | 0.0924 |

### Content

```text
...
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | test |
| Section | library |
| Source | library/test.md |
| Chunk ID | python:test:0057 |
| Rerank Score | 0.0924 |

### Content

```text
...
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | test |
| Section | library |
| Source | library/test.md |
| Chunk ID | python:test:0058 |
| Rerank Score | 0.0924 |

### Content

```text
...
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | typing |
| Section | library |
| Source | library/typing.md |
| Chunk ID | python:typing:0148 |
| Rerank Score | 0.0924 |

### Content

```text
...
```

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | messages |
| Section | langchain |
| Source | langchain/messages.md |
| Chunk ID | langchain:messages:0027 |
| Rerank Score | 0.0006 |

### Content

```text
# String content
human_message = HumanMessage("Hello, how are you?")

# Provider-native format (e.g., OpenAI)
human_message = HumanMessage(content=[
{"type": "text", "text": "Hello, how are you?"},
{"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
])

# List of standard content blocks
human_message = HumanMessage(content_blocks=[
{"type": "text", "text": "Hello, how are you?"},
{"type": "image", "url": "https://example.com/image.jpg"},
])
```  
<Tip>
Specifying `content_blocks` when initializing a message will still populate message
`content`, but provides a type-safe interface for doing so.
</Tip>
:::  
:::js
```typescript
import { HumanMessage } from "langchain";

// String content
const humanMessage = new HumanMessage("Hello, how are you?");
```


---

## Observation

_Write your observations here._

============================================================

# Question 7

**Question:** Who won the FIFA World Cup?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | split_by_token |
| Section | splitters |
| Source | splitters/split_by_token.md |
| Chunk ID | langchain:split_by_token:0011 |
| Rerank Score | 0.0004 |

### Content

```text
Members of Congress and the Cabinet.

Justices of the Supreme Court.

My fellow Americans.

Last year COVID-19 kept us apart.

This year we are finally together again.

Tonight, we meet as Democrats Republicans and Independents.

But most importantly as Americans.

With a duty to one another to the American people to the Constitution.

And with an unwavering resolve that freedom will always triumph over tyranny.

Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.

But he badly miscalculated.

He thought he could roll into Ukraine and the world would roll over.

Instead he met a wall of strength he never imagined.

He met the Ukrainian people.

From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.
```
```

## Rank 2

| Field | Value |
|------|-------|
| Library | langchain |
| Module | split_by_token |
| Section | splitters |
| Source | splitters/split_by_token.md |
| Chunk ID | langchain:split_by_token:0009 |
| Rerank Score | 0.0000 |

### Content

```text
Last year COVID-19 kept us apart. This year we are finally together again.

Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans.

With a duty to one another to the American people to the Constitution.
```
:::  
:::python
```

## Rank 3

| Field | Value |
|------|-------|
| Library | langchain |
| Module | knowledge-base |
| Section | langchain |
| Source | langchain/knowledge-base.md |
| Chunk ID | langchain:knowledge-base:0020 |
| Rerank Score | 0.0000 |

### Content

```text
print(results[0])
```
```python
page_content='Table of Contents
PART I
ITEM 1. BUSINESS
GENERAL
NIKE, Inc. was incorporated in 1967 under the laws of the State of Oregon. As used in this Annual Report on Form 10-K (this "Annual Report"), the terms "we," "us," "our,"
"NIKE" and the "Company" refer to NIKE, Inc. and its predecessors, subsidiaries and affiliates, collectively, unless the context indicates otherwise.
Our principal business activity is the design, development and worldwide marketing and selling of athletic footwear, apparel, equipment, accessories and services. NIKE is
the largest seller of athletic footwear and apparel in the world. We sell our products through NIKE Direct operations, which are comprised of both NIKE-owned retail stores
and sales through our digital platforms (also referred to as "NIKE Brand Digital"), to retail accounts and to a mix of independent distributors, licensees and sales' metadata={'page': 3, 'source': '../example_data/nke-10k-2023.pdf',
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | mmap |
| Section | library |
| Source | library/mmap.md |
| Chunk ID | python:mmap:0013 |
| Rerank Score | 0.0011 |

### Content

```text
mm[6:] = b" world!\n"
```

## Rank 5

| Field | Value |
|------|-------|
| Library | langchain |
| Module | character_text_splitter |
| Section | splitters |
| Source | splitters/character_text_splitter.md |
| Chunk ID | langchain:character_text_splitter:0009 |
| Rerank Score | 0.0010 |

### Content

```text
Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.' metadata={'document': 1}
```
:::
:::js
Use `.createDocuments` to propagate metadata associated with each document to the output chunks:  
```ts
const metadatas = [{"document": 1}, {"document":
```

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | character_text_splitter |
| Section | splitters |
| Source | splitters/character_text_splitter.md |
| Chunk ID | langchain:character_text_splitter:0011 |
| Rerank Score | 0.1024 |

### Content

```text
always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.',
metadata: {'document': 1}
}
```
:::  
:::python
Use `.split_text` to obtain the string content directly:  
```python
text_splitter.split_text(state_of_the_union)[0]
```
```text
'Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as
```

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | split_by_token |
| Section | splitters |
| Source | splitters/split_by_token.md |
| Chunk ID | langchain:split_by_token:0015 |
| Rerank Score | 0.0006 |

### Content

```text
text_splitter = NLTKTextSplitter(chunk_size=1000)
```  
```python
texts = text_splitter.split_text(state_of_the_union)
print(texts[0])
```
```text
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.

Members of Congress and the Cabinet.

Justices of the Supreme Court.

My fellow Americans.

Last year COVID-19 kept us apart.

This year we are finally together again.

Tonight, we meet as Democrats Republicans and Independents.

But most importantly as Americans.

With a duty to one another to the American people to the Constitution.

And with an unwavering resolve that freedom will always triumph over tyranny.

Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.

But he badly miscalculated.

He thought he could roll into Ukraine and the world would roll over.

Instead he met a wall of strength he never imagined.

He met the Ukrainian people.
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | character_text_splitter |
| Section | splitters |
| Source | splitters/character_text_splitter.md |
| Chunk ID | langchain:character_text_splitter:0011 |
| Rerank Score | 0.1024 |

### Content

```text
always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.',
metadata: {'document': 1}
}
```
:::  
:::python
Use `.split_text` to obtain the string content directly:  
```python
text_splitter.split_text(state_of_the_union)[0]
```
```text
'Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as
```

## Rank 2

| Field | Value |
|------|-------|
| Library | langchain |
| Module | character_text_splitter |
| Section | splitters |
| Source | splitters/character_text_splitter.md |
| Chunk ID | langchain:character_text_splitter:0012 |
| Rerank Score | 0.0119 |

### Content

```text
year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.'
```  
:::
:::js
Use `.splitText` to obtain the string content directly:  
```ts
splitter.splitText(stateOfTheUnion)[0]
```
```text
'Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members
```

## Rank 3

| Field | Value |
|------|-------|
| Library | langchain |
| Module | custom-workflow |
| Section | langchain |
| Source | langchain/multi-agent/custom-workflow.md |
| Chunk ID | langchain:custom-workflow:0009 |
| Rerank Score | 0.0013 |

### Content

```text
Won MVP award.",
"Caitlin Clark 2024 rookie stats: 19.2 PPG, 8.4 APG, 5.7 RPG. Won Rookie of the Year.",
"Breanna Stewart 2024 stats: 20.4 PPG, 8.5 RPG, 3.5 APG.",
])
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | mmap |
| Section | library |
| Source | library/mmap.md |
| Chunk ID | python:mmap:0013 |
| Rerank Score | 0.0011 |

### Content

```text
mm[6:] = b" world!\n"
```

## Rank 5

| Field | Value |
|------|-------|
| Library | langchain |
| Module | character_text_splitter |
| Section | splitters |
| Source | splitters/character_text_splitter.md |
| Chunk ID | langchain:character_text_splitter:0009 |
| Rerank Score | 0.0010 |

### Content

```text
Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. \n\nHe thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. \n\nHe met the Ukrainian people. \n\nFrom President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world.' metadata={'document': 1}
```
:::
:::js
Use `.createDocuments` to propagate metadata associated with each document to the output chunks:  
```ts
const metadatas = [{"document": 1}, {"document":
```

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | split_by_token |
| Section | splitters |
| Source | splitters/split_by_token.md |
| Chunk ID | langchain:split_by_token:0015 |
| Rerank Score | 0.0006 |

### Content

```text
text_splitter = NLTKTextSplitter(chunk_size=1000)
```  
```python
texts = text_splitter.split_text(state_of_the_union)
print(texts[0])
```
```text
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.

Members of Congress and the Cabinet.

Justices of the Supreme Court.

My fellow Americans.

Last year COVID-19 kept us apart.

This year we are finally together again.

Tonight, we meet as Democrats Republicans and Independents.

But most importantly as Americans.

With a duty to one another to the American people to the Constitution.

And with an unwavering resolve that freedom will always triumph over tyranny.

Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways.

But he badly miscalculated.

He thought he could roll into Ukraine and the world would roll over.

Instead he met a wall of strength he never imagined.

He met the Ukrainian people.
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | asyncio-future |
| Section | library |
| Source | library/asyncio-future.md |
| Chunk ID | python:asyncio-future:0015 |
| Rerank Score | 0.0006 |

### Content

```text
loop.create_task(
set_after(fut, 1, '... world'))  
print('hello ...')
```


---

## Observation

_Write your observations here._

============================================================

# Question 8

**Question:** How do I crack coding interviews?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | appetite |
| Section | tutorial |
| Source | tutorial/appetite.md |
| Chunk ID | python:appetite:0001 |
| Rerank Score | 0.0000 |

### Content

```text
If you do much work on computers, eventually you find that there\'s some
task you\'d like to automate. For example, you may wish to perform a
search-and-replace over a large number of text files, or rename and
rearrange a bunch of photo files in a complicated way. Perhaps you\'d
like to write a small custom database, or a specialized GUI application,
or a simple game.  
If you\'re a professional software developer, you may have to work with
several C/C++/Java libraries but find the usual
write/compile/test/re-compile cycle is too slow. Perhaps you\'re writing
a test suite for such a library and find writing the testing code a
tedious task. Or maybe you\'ve written a program that could use an
extension language, and you don\'t want to design and implement a whole
new language for your application.  
Python is just the language for you.  
You could write a Unix shell script or Windows batch files for some of
these tasks, but shell scripts are best at moving around files and
changing text
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | test |
| Section | library |
| Source | library/test.md |
| Chunk ID | python:test:0007 |
| Rerank Score | 0.0024 |

### Content

```text
enough to make sure all
boundary and edge cases are tested.  
- Make sure all possible values are tested including invalid ones. This
makes sure that not only all valid values are acceptable but also that
improper values are handled correctly.  
- Exhaust as many code paths as possible. Test where branching occurs
and thus tailor input to make sure as many different paths through the
code are taken.  
- Add an explicit test for any bugs discovered for the tested code. This
will make sure that the error does not crop up again if the code is
changed in the future.  
- Make sure to clean up after your tests (such as close and remove all
temporary files).  
- If a test is dependent on a specific condition of the operating system
then verify the condition already exists before attempting the test.  
- Import as few modules as possible and do it as soon as possible. This
minimizes external dependencies of tests and also minimizes possible
anomalous behavior from side-effects of importing a
```

## Rank 3

| Field | Value |
|------|-------|
| Library | langchain |
| Module | handoffs-customer-support |
| Section | langchain |
| Source | langchain/multi-agent/handoffs-customer-support.md |
| Chunk ID | langchain:handoffs-customer-support:0049 |
| Rerank Score | 0.0000 |

### Content

```text
# Collect all tools from all step configurations
all_tools = [
record_warranty_status,
record_issue_type,
provide_solution,
escalate_to_human,
]

# Create the agent with step-based configuration and summarization
agent = create_agent(
model,
tools=all_tools,
state_schema=SupportState,
middleware=[
apply_step_config,
SummarizationMiddleware(
model="gpt-5.4-mini",
trigger=("tokens", 4000),
keep=("messages", 10)
)
],
checkpointer=InMemorySaver(),
)

# ============================================================================
# Test the workflow
# ============================================================================

if __name__ == "__main__":
thread_id = str(uuid7())
config = {"configurable": {"thread_id": thread_id}}

result = agent.invoke(
{"messages": [HumanMessage("Hi, my phone screen is cracked")]},
config
)

result = agent.invoke(
{"messages": [HumanMessage("Yes, it's still under warranty")]},
config
)
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | doctest |
| Section | library |
| Source | library/doctest.md |
| Chunk ID | python:doctest:0073 |
| Rerank Score | 0.0000 |

### Content

```text
to
`DocTestRunner.run`.
:::  
::: method
run(test, compileflags=None, out=None, clear_globs=True)  
Run the examples in *test* (a `DocTest`
object), and display the results using the writer function *out*. Return
a `TestResults` instance.  
The examples are run in the namespace `test.globs`. If *clear_globs* is
true (the default), then this namespace will be cleared after the test
runs, to help with garbage collection. If you would like to examine the
namespace after the test completes, then use *clear_globs=False*.  
*compileflags* gives the set of flags that should be used by the Python
compiler when running the examples. If not specified, then it will
default to the set of future-import flags that apply to *globs*.  
The output of each example is checked using the
`DocTestRunner`\'s output checker, and
the results are formatted by the
`!DocTestRunner.report_\*` methods.
:::  
::: method
summarize(verbose=None)  
Print a summary of all the test cases that have been run by
```

## Rank 5

| Field | Value |
|------|-------|
| Library | langchain |
| Module | router-knowledge-base |
| Section | langchain |
| Source | langchain/multi-agent/router-knowledge-base.md |
| Chunk ID | langchain:router-knowledge-base:0045 |
| Rerank Score | 0.0000 |

### Content

```text
return {"final_answer": synthesis_response.content}

# Build workflow
workflow = (
StateGraph(RouterState)
.add_node("classify", classify_query)
.add_node("github", query_github)
.add_node("notion", query_notion)
.add_node("slack", query_slack)
.add_node("synthesize", synthesize_results)
.add_edge(START, "classify")
.add_conditional_edges("classify", route_to_agents, ["github", "notion", "slack"])
.add_edge("github", "synthesize")
.add_edge("notion", "synthesize")
.add_edge("slack", "synthesize")
.add_edge("synthesize", END)
.compile()
)

if __name__ == "__main__":
result = workflow.invoke({
"query": "How do I authenticate API requests?"
})
```

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | human-in-the-loop |
| Section | langchain |
| Source | langchain/human-in-the-loop.md |
| Chunk ID | langchain:human-in-the-loop:0015 |
| Rerank Score | 0.0001 |

### Content

```text
# Resume with approval decision
agent.invoke(
Command( # [!code highlight]
resume={"decisions": [{"type": "approve"}]}  # or "reject" [!code highlight]
), # [!code highlight]
config=config, # Same thread ID to resume the paused conversation
version="v2",
)
```
:::  
:::js
```typescript
import { HumanMessage } from "@langchain/core/messages";
import { Command } from "@langchain/langgraph";

// You must provide a thread ID to associate the execution with a conversation thread,
// so the conversation can be paused and resumed (as is needed for human review).
const config = { configurable: { thread_id: "some_id" } }; // [!code highlight]

// Run the graph until the interrupt is hit.
const result = await agent.invoke(
{
messages: [new HumanMessage("Delete old records from the database")],
},
config // [!code highlight]
);
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | doctest |
| Section | library |
| Source | library/doctest.md |
| Chunk ID | python:doctest:0089 |
| Rerank Score | 0.0000 |

### Content

```text
examples stops working after a \"harmless\" change.  
Doctest also makes an excellent tool for regression testing, especially
if you don\'t skimp on explanatory text. By interleaving prose and
examples, it becomes much easier to keep track of what\'s actually being
tested, and why. When a test fails, good prose can make it much easier
to figure out what the problem is, and how it should be fixed. It\'s
true that you could write extensive comments in code-based testing, but
few programmers do. Many have found that using doctest approaches
instead leads to much clearer tests. Perhaps this is simply because
doctest makes writing prose a little easier than writing code, while
writing comments in code is a little harder. I think it goes deeper than
just that: the natural attitude when writing a doctest-based test is
that you want to explain the fine points of your software, and
illustrate them with examples. This in turn naturally leads to test
files that start with the simplest features,
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | test |
| Section | library |
| Source | library/test.md |
| Chunk ID | python:test:0007 |
| Rerank Score | 0.0024 |

### Content

```text
enough to make sure all
boundary and edge cases are tested.  
- Make sure all possible values are tested including invalid ones. This
makes sure that not only all valid values are acceptable but also that
improper values are handled correctly.  
- Exhaust as many code paths as possible. Test where branching occurs
and thus tailor input to make sure as many different paths through the
code are taken.  
- Add an explicit test for any bugs discovered for the tested code. This
will make sure that the error does not crop up again if the code is
changed in the future.  
- Make sure to clean up after your tests (such as close and remove all
temporary files).  
- If a test is dependent on a specific condition of the operating system
then verify the condition already exists before attempting the test.  
- Import as few modules as possible and do it as soon as possible. This
minimizes external dependencies of tests and also minimizes possible
anomalous behavior from side-effects of importing a
```

## Rank 2

| Field | Value |
|------|-------|
| Library | langchain |
| Module | human-in-the-loop |
| Section | langchain |
| Source | langchain/human-in-the-loop.md |
| Chunk ID | langchain:human-in-the-loop:0015 |
| Rerank Score | 0.0001 |

### Content

```text
# Resume with approval decision
agent.invoke(
Command( # [!code highlight]
resume={"decisions": [{"type": "approve"}]}  # or "reject" [!code highlight]
), # [!code highlight]
config=config, # Same thread ID to resume the paused conversation
version="v2",
)
```
:::  
:::js
```typescript
import { HumanMessage } from "@langchain/core/messages";
import { Command } from "@langchain/langgraph";

// You must provide a thread ID to associate the execution with a conversation thread,
// so the conversation can be paused and resumed (as is needed for human review).
const config = { configurable: { thread_id: "some_id" } }; // [!code highlight]

// Run the graph until the interrupt is hit.
const result = await agent.invoke(
{
messages: [new HumanMessage("Delete old records from the database")],
},
config // [!code highlight]
);
```

## Rank 3

| Field | Value |
|------|-------|
| Library | langchain |
| Module | streaming |
| Section | langchain |
| Source | langchain/streaming.md |
| Chunk ID | langchain:streaming:0018 |
| Rerank Score | 0.0000 |

### Content

```text
for chunk in agent.stream(  # [!code highlight]
{"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
stream_mode=["updates", "custom"],
version="v2",  # [!code highlight]
):
print(f"stream_mode: {chunk['type']}")  # [!code highlight]
print(f"content: {chunk['data']}")  # [!code highlight]
print("\n")
```  
```shell title="Output"
stream_mode: updates
content: {'model': {'messages': [AIMessage(content='', response_metadata={'token_usage': {'completion_tokens': 280, 'prompt_tokens': 132, 'total_tokens': 412, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 256, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-5-nano-2025-08-07', 'system_fingerprint': None, 'id': 'chatcmpl-C9tlgBzGEbedGYxZ0rTCz5F7OXpL7', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None},
```

## Rank 4

| Field | Value |
|------|-------|
| Library | langchain |
| Module | sql-agent |
| Section | langchain |
| Source | langchain/sql-agent.md |
| Chunk ID | langchain:sql-agent:0020 |
| Rerank Score | 0.0000 |

### Content

```text
≈ 48.5 minutes (about 2,911,783 ms).
```  
The agent correctly wrote a query, checked the query, and ran it to inform its final response.  
<Note>
You can inspect all aspects of the above run, including steps taken, tools invoked, what prompts were seen by the LLM, and more in the [LangSmith trace](https://smith.langchain.com/public/653d218b-af67-4854-95ca-6abecb9b2520/r).
</Note>  
:::  
</Step>
<Step title="(Optional) Use Studio">  
:::python
[Studio](/langsmith/studio) provides a "client side" loop as well as memory so you can run this as a chat interface and query the database. You can ask questions like "Tell me the scheme of the database" or "Show me the invoices for the 5 top customers". You will see the SQL command that is generated and the resulting output. The details of how to get that started are below.
<Accordion title="Run your agent in Studio">  
In addition to the previously mentioned packages, you will need to:  
```shell
pip install -U langgraph-cli[inmem]>=0.4.0
```
```

## Rank 5

| Field | Value |
|------|-------|
| Library | langchain |
| Module | handoffs-customer-support |
| Section | langchain |
| Source | langchain/multi-agent/handoffs-customer-support.md |
| Chunk ID | langchain:handoffs-customer-support:0049 |
| Rerank Score | 0.0000 |

### Content

```text
# Collect all tools from all step configurations
all_tools = [
record_warranty_status,
record_issue_type,
provide_solution,
escalate_to_human,
]

# Create the agent with step-based configuration and summarization
agent = create_agent(
model,
tools=all_tools,
state_schema=SupportState,
middleware=[
apply_step_config,
SummarizationMiddleware(
model="gpt-5.4-mini",
trigger=("tokens", 4000),
keep=("messages", 10)
)
],
checkpointer=InMemorySaver(),
)

# ============================================================================
# Test the workflow
# ============================================================================

if __name__ == "__main__":
thread_id = str(uuid7())
config = {"configurable": {"thread_id": thread_id}}

result = agent.invoke(
{"messages": [HumanMessage("Hi, my phone screen is cracked")]},
config
)

result = agent.invoke(
{"messages": [HumanMessage("Yes, it's still under warranty")]},
config
)
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | appetite |
| Section | tutorial |
| Source | tutorial/appetite.md |
| Chunk ID | python:appetite:0001 |
| Rerank Score | 0.0000 |

### Content

```text
If you do much work on computers, eventually you find that there\'s some
task you\'d like to automate. For example, you may wish to perform a
search-and-replace over a large number of text files, or rename and
rearrange a bunch of photo files in a complicated way. Perhaps you\'d
like to write a small custom database, or a specialized GUI application,
or a simple game.  
If you\'re a professional software developer, you may have to work with
several C/C++/Java libraries but find the usual
write/compile/test/re-compile cycle is too slow. Perhaps you\'re writing
a test suite for such a library and find writing the testing code a
tedious task. Or maybe you\'ve written a program that could use an
extension language, and you don\'t want to design and implement a whole
new language for your application.  
Python is just the language for you.  
You could write a Unix shell script or Windows batch files for some of
these tasks, but shell scripts are best at moving around files and
changing text
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | doctest |
| Section | library |
| Source | library/doctest.md |
| Chunk ID | python:doctest:0073 |
| Rerank Score | 0.0000 |

### Content

```text
to
`DocTestRunner.run`.
:::  
::: method
run(test, compileflags=None, out=None, clear_globs=True)  
Run the examples in *test* (a `DocTest`
object), and display the results using the writer function *out*. Return
a `TestResults` instance.  
The examples are run in the namespace `test.globs`. If *clear_globs* is
true (the default), then this namespace will be cleared after the test
runs, to help with garbage collection. If you would like to examine the
namespace after the test completes, then use *clear_globs=False*.  
*compileflags* gives the set of flags that should be used by the Python
compiler when running the examples. If not specified, then it will
default to the set of future-import flags that apply to *globs*.  
The output of each example is checked using the
`DocTestRunner`\'s output checker, and
the results are formatted by the
`!DocTestRunner.report_\*` methods.
:::  
::: method
summarize(verbose=None)  
Print a summary of all the test cases that have been run by
```


---

## Observation

_Write your observations here._

============================================================

# Question 9

**Question:** What is the capital of France?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | datetime |
| Section | library |
| Source | library/datetime.md |
| Chunk ID | python:datetime:0109 |
| Rerank Score | 0.0009 |

### Content

```text
|
|           |                               | | So, Mo, \..., Sa  |        |
|           |                               |   (de_DE)           |        |
+-----------+-------------------------------+---------------------+--------+
| > `%A`    | Weekday as locale\'s full     | | Sunday, Monday,   | \(1\)  |
|           | name.                         |   \..., Saturday    |        |
|           |                               |   (en_US);          |        |
|           |                               | | Sonntag, Montag,  |        |
|           |                               |   \..., Samstag     |        |
|           |                               |   (de_DE)           |        |
+-----------+-------------------------------+---------------------+--------+
| > `%b`    | Month as locale\'s            | | Jan, Feb, \...,   | \(1\)  |
|           | abbreviated name.             |   Dec (en_US);      |        |
|           |                               | | Jan, Feb, \...,   |
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | datetime |
| Section | library |
| Source | library/datetime.md |
| Chunk ID | python:datetime:0110 |
| Rerank Score | 0.0002 |

### Content

```text
| \(1\)  |
|           | abbreviated name.             |   Dec (en_US);      |        |
|           |                               | | Jan, Feb, \...,   |        |
|           |                               |   Dez (de_DE)       |        |
+-----------+-------------------------------+---------------------+--------+
| > `%B`    | Month as locale\'s full name. | | January,          | \(1\)  |
|           |                               |   February, \...,   |        |
|           |                               |   December (en_US); |        |
|           |                               | | Januar, Februar,  |        |
|           |                               |   \..., Dezember    |        |
|           |                               |   (de_DE)           |        |
+-----------+-------------------------------+---------------------+--------+
| > `%c`    | Locale\'s appropriate date    | | Tue Aug 16        | \(1\)  |
|           | and time representation.      |   21:30:00 1988
```

## Rank 3

| Field | Value |
|------|-------|
| Library | langchain |
| Module | built-in |
| Section | langchain |
| Source | langchain/middleware/built-in.md |
| Chunk ID | langchain:built-in:0114 |
| Rerank Score | 0.0000 |

### Content

```text
@tool
def get_weather(city: str) -> str:
"""Get the weather in a city."""
return f"The weather in {city} is sunny."

agent = create_agent(
model="claude-sonnet-4-6",
middleware=[
SubAgentMiddleware(
default_model="claude-sonnet-4-6",
default_tools=[],
subagents=[
{
"name": "weather",
"description": "This subagent can get weather in cities.",
"system_prompt": "Use the get_weather tool to get the weather in a city.",
"tools": [get_weather],
"model": "gpt-5.5",
"middleware": [],
}
],
)
],
)
```
:::  
:::js
```typescript
import { tool } from "langchain";
import { createAgent } from "langchain";
import { createSubAgentMiddleware } from "deepagents";
import { z } from "zod";

const getWeather = tool(
async ({ city }: { city: string }) => {
return `The weather in ${city} is sunny.`;
},
{
name: "get_weather",
description: "Get the weather in a city.",
schema: z.object({
city: z.string(),
}),
},
);
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | time |
| Section | library |
| Source | library/time.md |
| Chunk ID | python:time:0019 |
| Rerank Score | 0.0001 |

### Content

```text
| Notes |
+===========+================================================+=======+
| `%a`      | Locale\'s abbreviated weekday name.            |       |
+-----------+------------------------------------------------+-------+
| `%A`      | Locale\'s full weekday name.                   |       |
+-----------+------------------------------------------------+-------+
| `%b`      | Locale\'s abbreviated month name.              |       |
+-----------+------------------------------------------------+-------+
| `%B`      | Locale\'s full month name.                     |       |
+-----------+------------------------------------------------+-------+
| `%c`      | Locale\'s appropriate date and time            |       |
|           | representation.                                |       |
+-----------+------------------------------------------------+-------+
| `%d`      | Day of the month as a decimal number           |       |
|           | \[01,31\].
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | functions |
| Section | library |
| Source | library/functions.md |
| Chunk ID | python:functions:0005 |
| Rerank Score | 0.0010 |

### Content

```text
| |                                                               | | `round`                                                                                                                          |
| | `any`                                                                            | | \*\*F\*\*                                                                                                                               | | \*\*M\*\*                                                    | |                                                                                                                                                                  |
| | `ascii`                                                                          | | `filter`                                                                                                 | | `map`
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | calendar |
| Section | library |
| Source | library/calendar.md |
| Chunk ID | python:calendar:0025 |
| Rerank Score | 0.0023 |

### Content

```text
October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
1             1  2  3  4  5                   1  2  3
2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
```  
The following options are accepted:  
::: program
calendar
:::  
::: option  
`--help, -h`  
:  
Show the help message and exit.
:::  
::: option  
`--locale LOCALE, -L LOCALE`  
:  
The locale to use for month and weekday names. Defaults to English.
:::  
::: option  
`--encoding ENCODING, -e ENCODING`  
:  
The encoding to use for output. `--encoding` is required if `--locale` is set.
:::  
::: option
\--type {text,html}, -t {text,html}  
Print the calendar to the terminal as text, or as an HTML
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | datetime |
| Section | library |
| Source | library/datetime.md |
| Chunk ID | python:datetime:0111 |
| Rerank Score | 0.0003 |

### Content

```text
> `%c`    | Locale\'s appropriate date    | | Tue Aug 16        | \(1\)  |
|           | and time representation.      |   21:30:00 1988     |        |
|           |                               |   (en_US);          |        |
|           |                               | | Di 16 Aug         |        |
|           |                               |   21:30:00 1988     |        |
|           |                               |   (de_DE)           |        |
+-----------+-------------------------------+---------------------+--------+
| > `%C`    | The year divided by 100 and   | 01, 02, \..., 99    | \(0\)  |
|           | truncated to an integer as a  |                     |        |
|           | zero-padded decimal number.   |                     |        |
+-----------+-------------------------------+---------------------+--------+
| > `%d`    | Day of the month as a         | 01, 02, \..., 31    | (9),   |
|           | zero-padded decimal number.   |                     | (10)
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | langchain |
| Module | models |
| Section | langchain |
| Source | langchain/models.md |
| Chunk ID | langchain:models:0099 |
| Rerank Score | 0.0195 |

### Content

```text
class GetPopulation(BaseModel):
"""Get the current population in a given location"""

location: str = Field(description="The city and state, e.g. San Francisco, CA")

model = init_chat_model(temperature=0)
model_with_tools = model.bind_tools([GetWeather, GetPopulation])
```

## Rank 2

| Field | Value |
|------|-------|
| Library | pandas |
| Module | 10min |
| Section | user_guide |
| Source | user_guide/10min.md |
| Chunk ID | pandas:10min:0001 |
| Rerank Score | 0.0075 |

### Content

```text
::: {#10min}
{{ header }}
:::
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | calendar |
| Section | library |
| Source | library/calendar.md |
| Chunk ID | python:calendar:0025 |
| Rerank Score | 0.0023 |

### Content

```text
October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
1             1  2  3  4  5                   1  2  3
2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
```  
The following options are accepted:  
::: program
calendar
:::  
::: option  
`--help, -h`  
:  
Show the help message and exit.
:::  
::: option  
`--locale LOCALE, -L LOCALE`  
:  
The locale to use for month and weekday names. Defaults to English.
:::  
::: option  
`--encoding ENCODING, -e ENCODING`  
:  
The encoding to use for output. `--encoding` is required if `--locale` is set.
:::  
::: option
\--type {text,html}, -t {text,html}  
Print the calendar to the terminal as text, or as an HTML
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | codecs |
| Section | library |
| Source | library/codecs.md |
| Chunk ID | python:codecs:0064 |
| Rerank Score | 0.0012 |

### Content

```text
|
|                 | 8859, cp819, latin,      |                          |
|                 | latin1, L1               |                          |
+-----------------+--------------------------+--------------------------+
| iso8859_2       | iso-8859-2, latin2, L2   | Central and Eastern      |
|                 |                          | Europe                   |
+-----------------+--------------------------+--------------------------+
| iso8859_3       | iso-8859-3, latin3, L3   | Esperanto, Maltese       |
+-----------------+--------------------------+--------------------------+
| iso8859_4       | iso-8859-4, latin4, L4   | Northern Europe          |
+-----------------+--------------------------+--------------------------+
| iso8859_5       | iso-8859-5, cyrillic     | Belarusian, Bulgarian,   |
|                 |                          | Macedonian, Russian,     |
|                 |                          | Serbian
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | functions |
| Section | library |
| Source | library/functions.md |
| Chunk ID | python:functions:0005 |
| Rerank Score | 0.0010 |

### Content

```text
| |                                                               | | `round`                                                                                                                          |
| | `any`                                                                            | | \*\*F\*\*                                                                                                                               | | \*\*M\*\*                                                    | |                                                                                                                                                                  |
| | `ascii`                                                                          | | `filter`                                                                                                 | | `map`
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | datetime |
| Section | library |
| Source | library/datetime.md |
| Chunk ID | python:datetime:0109 |
| Rerank Score | 0.0009 |

### Content

```text
|
|           |                               | | So, Mo, \..., Sa  |        |
|           |                               |   (de_DE)           |        |
+-----------+-------------------------------+---------------------+--------+
| > `%A`    | Weekday as locale\'s full     | | Sunday, Monday,   | \(1\)  |
|           | name.                         |   \..., Saturday    |        |
|           |                               |   (en_US);          |        |
|           |                               | | Sonntag, Montag,  |        |
|           |                               |   \..., Samstag     |        |
|           |                               |   (de_DE)           |        |
+-----------+-------------------------------+---------------------+--------+
| > `%b`    | Month as locale\'s            | | Jan, Feb, \...,   | \(1\)  |
|           | abbreviated name.             |   Dec (en_US);      |        |
|           |                               | | Jan, Feb, \...,   |
```

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | quickstart |
| Section | langchain |
| Source | langchain/quickstart.md |
| Chunk ID | langchain:quickstart:0007 |
| Rerank Score | 0.0007 |

### Content

```text
def get_weather(city: str) -> str:
"""Get weather for a given city."""
return f"It's always sunny in {city}!"

agent = create_agent(
model="openrouter:anthropic/claude-sonnet-4-6",
tools=[get_weather],
system_prompt="You are a helpful assistant",
)

result = agent.invoke(
{"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```
```python Fireworks
from langchain.agents import create_agent

def get_weather(city: str) -> str:
"""Get weather for a given city."""
return f"It's always sunny in {city}!"

agent = create_agent(
model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
tools=[get_weather],
system_prompt="You are a helpful assistant",
)

result = agent.invoke(
{"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```
```python Baseten
from langchain.agents import create_agent
```


---

## Observation

_Write your observations here._

============================================================

# Question 10

**Question:** How do I create a path?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | stat |
| Section | library |
| Source | library/stat.md |
| Chunk ID | python:stat:0006 |
| Rerank Score | 0.0002 |

### Content

```text
callback(pathname)
else:
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0031 |
| Rerank Score | 0.7293 |

### Content

```text
Concrete path objects can be created from, and represented as, \'file\'
URIs conforming to `8089`.  
:::: note
::: title
Note
:::  
File URIs are not portable across machines with different
`filesystem encodings <filesystem-encoding>`.
::::  
::::: classmethod
Path.from_uri(uri)  
Return a new path object from parsing a \'file\' URI. For example:  
>>> p = Path.from_uri('file:///etc/hosts')
PosixPath('/etc/hosts')  
On Windows, DOS device and UNC paths may be parsed from URIs:  
>>> p = Path.from_uri('file:///c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file://server/share')
WindowsPath('//server/share')  
Several variant forms are supported:  
>>> p = Path.from_uri('file:////server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file://///server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file:c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file:/c|/windows')
WindowsPath('c:/windows')  
`ValueError` is raised if the URI does
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0016 |
| Rerank Score | 0.0861 |

### Content

```text
path:  
>>> p = PurePosixPath('/')
>>> p.parent
PurePosixPath('/')
>>> p = PurePosixPath('.')
>>> p.parent
PurePosixPath('.')  
:::: note
::: title
Note
:::  
This is a purely lexical operation, hence the following behaviour:  
>>> p = PurePosixPath('foo/..')
>>> p.parent  
PurePosixPath(\'foo\')  
If you want to walk an arbitrary filesystem path upwards, it is
recommended to first call `Path.resolve`
so as to resolve symlinks and eliminate `".."` components.
::::
:::::  
::: attribute
PurePath.name  
A string representing the final path component, excluding the drive and
root, if any:  
>>> PurePosixPath('my/library/setup.py').name
'setup.py'  
UNC drive names are not considered:  
>>> PureWindowsPath('//some/share/setup.py').name
'setup.py'
>>> PureWindowsPath('//some/share').name
''
:::  
:::: attribute
PurePath.suffix  
The last dot-separated portion of the final component, if any:  
>>> PurePosixPath('my/library/setup.py').suffix
'.py'
>>>
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0010 |
| Rerank Score | 0.3268 |

### Content

```text
The slash operator helps create child paths, like
`os.path.join`. If the argument is an
absolute path, the previous path is ignored. On Windows, the drive is
not reset when the argument is a rooted relative path (e.g., `r'\foo'`):  
>>> p = PurePath('/etc')
>>> p
PurePosixPath('/etc')
>>> p / 'init.d' / 'apache2'
PurePosixPath('/etc/init.d/apache2')
>>> q = PurePath('bin')
>>> '/usr' / q
PurePosixPath('/usr/bin')
>>> p / '/an_absolute_path'
PurePosixPath('/an_absolute_path')
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')  
A path object can be used anywhere an object implementing
`os.PathLike` is accepted:  
>>> import os
>>> p = PurePath('/etc')
>>> os.fspath(p)
'/etc'  
The string representation of a path is the raw filesystem path itself
(in native form, e.g. with backslashes under Windows), which you can
pass to any function taking a file path as a string:  
>>> p = PurePath('/etc')
>>> str(p)
'/etc'
>>> p = PureWindowsPath('c:/Program
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | asyncio-task |
| Section | library |
| Source | library/asyncio-task.md |
| Chunk ID | python:asyncio-task:0054 |
| Rerank Score | 0.0013 |

### Content

```text
pathlib.Path("example.txt").write_text("hello world", encoding="utf8")
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0002 |
| Rerank Score | 0.0257 |

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

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | site |
| Section | library |
| Source | library/site.md |
| Chunk ID | python:site:0018 |
| Rerank Score | 0.0531 |

### Content

```text
with the
`-S` flag.  
::: versionchanged
3.3 This function used to be called unconditionally.
:::
::::  
::: function
makepath(\*paths)  
Join *paths* with `os.path.join`, attempt
to make the result absolute with `os.path.abspath`, and return a 2-tuple containing the absolute path and its
case-normalized form as produced by `os.path.normcase`. If `os.path.abspath` raises
`OSError`, the joined path is used
unchanged for the case-normalization step.  
The second element of the returned tuple is the form used throughout the
`!site` module to compare paths on
case-insensitive file systems, and is what populates the `known_paths`
sets that prevent duplicate `sys.path`
entries in various APIs within this module.
:::  
:::::::: StartupState(known_paths=None)
Instances of this class accumulate interpreter startup configuration
data from one or more site directories. They are the preferred interface
for batching the processing of `.pth` and
`.start` files across multiple site
directories, so
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0031 |
| Rerank Score | 0.7293 |

### Content

```text
Concrete path objects can be created from, and represented as, \'file\'
URIs conforming to `8089`.  
:::: note
::: title
Note
:::  
File URIs are not portable across machines with different
`filesystem encodings <filesystem-encoding>`.
::::  
::::: classmethod
Path.from_uri(uri)  
Return a new path object from parsing a \'file\' URI. For example:  
>>> p = Path.from_uri('file:///etc/hosts')
PosixPath('/etc/hosts')  
On Windows, DOS device and UNC paths may be parsed from URIs:  
>>> p = Path.from_uri('file:///c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file://server/share')
WindowsPath('//server/share')  
Several variant forms are supported:  
>>> p = Path.from_uri('file:////server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file://///server/share')
WindowsPath('//server/share')
>>> p = Path.from_uri('file:c:/windows')
WindowsPath('c:/windows')
>>> p = Path.from_uri('file:/c|/windows')
WindowsPath('c:/windows')  
`ValueError` is raised if the URI does
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0057 |
| Rerank Score | 0.4751 |

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

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0010 |
| Rerank Score | 0.3268 |

### Content

```text
The slash operator helps create child paths, like
`os.path.join`. If the argument is an
absolute path, the previous path is ignored. On Windows, the drive is
not reset when the argument is a rooted relative path (e.g., `r'\foo'`):  
>>> p = PurePath('/etc')
>>> p
PurePosixPath('/etc')
>>> p / 'init.d' / 'apache2'
PurePosixPath('/etc/init.d/apache2')
>>> q = PurePath('bin')
>>> '/usr' / q
PurePosixPath('/usr/bin')
>>> p / '/an_absolute_path'
PurePosixPath('/an_absolute_path')
>>> PureWindowsPath('c:/Windows', '/Program Files')
PureWindowsPath('c:/Program Files')  
A path object can be used anywhere an object implementing
`os.PathLike` is accepted:  
>>> import os
>>> p = PurePath('/etc')
>>> os.fspath(p)
'/etc'  
The string representation of a path is the raw filesystem path itself
(in native form, e.g. with backslashes under Windows), which you can
pass to any function taking a file path as a string:  
>>> p = PurePath('/etc')
>>> str(p)
'/etc'
>>> p = PureWindowsPath('c:/Program
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | contextlib |
| Section | library |
| Source | library/contextlib.md |
| Chunk ID | python:contextlib:0015 |
| Rerank Score | 0.2033 |

### Content

```text
cm = open(file_or_path)
else:
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0033 |
| Rerank Score | 0.1975 |

### Content

```text
:::: classmethod
Path.home()  
Return a new path object representing the user\'s home directory (as
returned by `os.path.expanduser` with `~`
construct). If the home directory can\'t be resolved,
`RuntimeError` is raised.  
>>> Path.home()
PosixPath('/home/antoine')  
::: versionadded
3.5
:::
::::  
:::: method
Path.expanduser()  
Return a new path with expanded `~` and `~user` constructs, as returned
by `os.path.expanduser`. If a home
directory can\'t be resolved, `RuntimeError` is raised.  
>>> p = PosixPath('~/films/Monty Python')
>>> p.expanduser()
PosixPath('/home/eric/films/Monty Python')  
::: versionadded
3.5
:::
::::  
::: classmethod
Path.cwd()  
Return a new path object representing the current directory (as returned
by `os.getcwd`):  
>>> Path.cwd()
PosixPath('/home/antoine/pathlib')
:::  
::: method
Path.absolute()  
Make the path absolute, without normalization or resolving symlinks.
Returns a new path object:  
>>> p = Path('tests')
>>> p
PosixPath('tests')
>>>
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | pathlib |
| Section | library |
| Source | library/pathlib.md |
| Chunk ID | python:pathlib:0016 |
| Rerank Score | 0.0861 |

### Content

```text
path:  
>>> p = PurePosixPath('/')
>>> p.parent
PurePosixPath('/')
>>> p = PurePosixPath('.')
>>> p.parent
PurePosixPath('.')  
:::: note
::: title
Note
:::  
This is a purely lexical operation, hence the following behaviour:  
>>> p = PurePosixPath('foo/..')
>>> p.parent  
PurePosixPath(\'foo\')  
If you want to walk an arbitrary filesystem path upwards, it is
recommended to first call `Path.resolve`
so as to resolve symlinks and eliminate `".."` components.
::::
:::::  
::: attribute
PurePath.name  
A string representing the final path component, excluding the drive and
root, if any:  
>>> PurePosixPath('my/library/setup.py').name
'setup.py'  
UNC drive names are not considered:  
>>> PureWindowsPath('//some/share/setup.py').name
'setup.py'
>>> PureWindowsPath('//some/share').name
''
:::  
:::: attribute
PurePath.suffix  
The last dot-separated portion of the final component, if any:  
>>> PurePosixPath('my/library/setup.py').suffix
'.py'
>>>
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | site |
| Section | library |
| Source | library/site.md |
| Chunk ID | python:site:0018 |
| Rerank Score | 0.0531 |

### Content

```text
with the
`-S` flag.  
::: versionchanged
3.3 This function used to be called unconditionally.
:::
::::  
::: function
makepath(\*paths)  
Join *paths* with `os.path.join`, attempt
to make the result absolute with `os.path.abspath`, and return a 2-tuple containing the absolute path and its
case-normalized form as produced by `os.path.normcase`. If `os.path.abspath` raises
`OSError`, the joined path is used
unchanged for the case-normalization step.  
The second element of the returned tuple is the form used throughout the
`!site` module to compare paths on
case-insensitive file systems, and is what populates the `known_paths`
sets that prevent duplicate `sys.path`
entries in various APIs within this module.
:::  
:::::::: StartupState(known_paths=None)
Instances of this class accumulate interpreter startup configuration
data from one or more site directories. They are the preferred interface
for batching the processing of `.pth` and
`.start` files across multiple site
directories, so
```


---

## Observation

_Write your observations here._

============================================================

# Question 11

**Question:** How do I merge data?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0040 |
| Rerank Score | 0.1180 |

### Content

```text
The `Join <merging.join>` docs.  
[Concatenate two dataframes with overlapping index (emulate R
rbind)](https://stackoverflow.com/questions/14988480/pandas-version-of-rbind)  
::: ipython
python  
rng = pd.date_range(\"2000-01-01\", periods=6) df1 =
pd.DataFrame(np.random.randn(6, 3), index=rng, columns=\[\"A\", \"B\",
\"C\"\]) df2 = df1.copy()
:::  
Depending on df construction, `ignore_index` may be needed  
::: ipython
python  
df = pd.concat(\[df1, df2\], ignore_index=True) df
:::  
Self Join of a DataFrame `2996`  
::: ipython
python  
df = pd.DataFrame(  
:  
data={  
: \"Area\": \[\"A\"\] \* 5 + \[\"C\"\] \* 2, \"Bins\": \[110\] \* 2 +
\[160\] \* 3 + \[40\] \* 2, \"Test_0\": \[0, 1, 0, 1, 2, 0, 1\],
\"Data\": np.random.randn(7),  
}  
) df  
df\[\"Test_1\"\] = df\[\"Test_0\"\] - 1  
pd.merge(  
: df, df, left_on=\[\"Bins\", \"Area\", \"Test_0\"\],
right_on=\[\"Bins\", \"Area\", \"Test_1\"\], suffixes=(\"\_L\",
\"\_R\"),  
)
:::  
[How to set the index
```

## Rank 2

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0021 |
| Rerank Score | 0.0008 |

### Content

```text
df  
ser = pd.Series(  
: \[\"a\", \"b\", \"c\", \"d\", \"e\", \"f\"\],
index=pd.MultiIndex.from_arrays( \[\[\"A\", \"B\", \"C\"\] \* 2, \[1,
2, 3, 4, 5, 6\]\], names=\[\"Let\", \"Num\"\] ),  
) ser  
pd.merge(df, ser.reset_index(), on=\[\"Let\", \"Num\"\])
:::  
Performing an outer join with duplicate join keys in
`DataFrame`:  
::: ipython
python  
left = pd.DataFrame({\"A\": \[1, 2\], \"B\": \[2, 2\]})  
right = pd.DataFrame({\"A\": \[4, 5, 6\], \"B\": \[2, 2, 2\]})  
result = pd.merge(left, right, on=\"B\", how=\"outer\") result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_merge_on_key_dup.png p.plot(\[left, right\], result,
labels=\[\"left\", \"right\"\], vertical=False); plt.close(\"all\");
:::  
:::: warning
::: title
Warning
:::  
Merging on duplicate keys significantly increase the dimensions of the
result and can cause a memory overflow.
::::
```

## Rank 3

| Field | Value |
|------|-------|
| Library | pandas |
| Module | aliases |
| Section | reference |
| Source | reference/aliases.md |
| Chunk ID | pandas:aliases:0013 |
| Rerank Score | 0.0048 |

### Content

```text
::: type                  | Argument type for `merge_cells` in                                                    |
| ExcelWriterMergeCells     | `DataFrame's <pandas.DataFrame.to_excel>` and          |
| :::                       | `Series' <pandas.Series.to_excel>` `to_excel()`        |
|                           | methods                                                                               |
+---------------------------+---------------------------------------------------------------------------------------+
| ::: type                  | Type of paths for files for I/O methods                                               |
| FilePath                  |                                                                                       |
| :::                       |                                                                                       |
+---------------------------+---------------------------------------------------------------------------------------+
|
```

## Rank 4

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0086 |
| Rerank Score | 0.0325 |

### Content

```text
It\'s best to use `~pandas.concat` to
combine multiple files. See the
`cookbook<cookbook.csv.multiple_files>`
for an example.
```

## Rank 5

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0036 |
| Rerank Score | 0.1104 |

### Content

```text
`merge_ordered` combines ordered data
such as numeric or time series data with optional filling of missing
data with `fill_method`.  
::: ipython
python  
left = pd.DataFrame(  
: {\"k\": \[\"K0\", \"K1\", \"K1\", \"K2\"\], \"lv\": \[1, 2, 3, 4\],
\"s\": \[\"a\", \"b\", \"c\", \"d\"\]}  
)  
right = pd.DataFrame({\"k\": \[\"K1\", \"K2\", \"K4\"\], \"rv\": \[1, 2,
3\]})  
pd.merge_ordered(left, right, fill_method=\"ffill\", left_by=\"s\")
:::
```

## Rank 6

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0015 |
| Rerank Score | 0.0424 |

### Content

```text
`~pandas.merge` performs join operations
similar to relational databases like SQL. Users who are familiar with
SQL but new to pandas can reference a
`comparison with SQL<compare_with_sql.join>`.
```

## Rank 7

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0017 |
| Rerank Score | 0.0318 |

### Content

```text
right = pd.DataFrame(  
:  
{  
: \"key\": \[\"K0\", \"K1\", \"K2\", \"K3\"\], \"C\": \[\"C0\",
\"C1\", \"C2\", \"C3\"\], \"D\": \[\"D0\", \"D1\", \"D2\", \"D3\"\],  
}  
) result = pd.merge(left, right, on=\"key\") result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_merge_on_key.png p.plot(\[left, right\], result,
labels=\[\"left\", \"right\"\], vertical=False); plt.close(\"all\");
:::  
The `how` argument to `~pandas.merge`
specifies which keys are included in the resulting table. If a key
combination **does not appear** in either the left or right tables, the
values in the joined table will be `NA`. Here is a summary of the `how`
options and their SQL equivalent names:  
Merge method   SQL Join Name        Description
-------------- -------------------- ------------------------------------------
`left`         `LEFT OUTER JOIN`    Use keys from left frame only  
`right`        `RIGHT OUTER JOIN`   Use keys from right frame only  
`outer`        `FULL OUTER JOIN`
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | pandas |
| Module | 10min |
| Section | user_guide |
| Source | user_guide/10min.md |
| Chunk ID | pandas:10min:0021 |
| Rerank Score | 0.2962 |

### Content

```text
`merge` enables SQL style join types
along specific columns. See the
`Database style joining <merging.join>`
section.  
::: ipython
python  
left = pd.DataFrame({\"key\": \[\"foo\", \"foo\"\], \"lval\": \[1, 2\]})
right = pd.DataFrame({\"key\": \[\"foo\", \"foo\"\], \"rval\": \[4,
5\]}) left right pd.merge(left, right, on=\"key\")
:::  
`merge` on unique keys:  
::: ipython
python  
left = pd.DataFrame({\"key\": \[\"foo\", \"bar\"\], \"lval\": \[1, 2\]})
right = pd.DataFrame({\"key\": \[\"foo\", \"bar\"\], \"rval\": \[4,
5\]}) left right pd.merge(left, right, on=\"key\")
:::
```

## Rank 2

| Field | Value |
|------|-------|
| Library | pandas |
| Module | cookbook |
| Section | user_guide |
| Source | user_guide/cookbook.md |
| Chunk ID | pandas:cookbook:0040 |
| Rerank Score | 0.1180 |

### Content

```text
The `Join <merging.join>` docs.  
[Concatenate two dataframes with overlapping index (emulate R
rbind)](https://stackoverflow.com/questions/14988480/pandas-version-of-rbind)  
::: ipython
python  
rng = pd.date_range(\"2000-01-01\", periods=6) df1 =
pd.DataFrame(np.random.randn(6, 3), index=rng, columns=\[\"A\", \"B\",
\"C\"\]) df2 = df1.copy()
:::  
Depending on df construction, `ignore_index` may be needed  
::: ipython
python  
df = pd.concat(\[df1, df2\], ignore_index=True) df
:::  
Self Join of a DataFrame `2996`  
::: ipython
python  
df = pd.DataFrame(  
:  
data={  
: \"Area\": \[\"A\"\] \* 5 + \[\"C\"\] \* 2, \"Bins\": \[110\] \* 2 +
\[160\] \* 3 + \[40\] \* 2, \"Test_0\": \[0, 1, 0, 1, 2, 0, 1\],
\"Data\": np.random.randn(7),  
}  
) df  
df\[\"Test_1\"\] = df\[\"Test_0\"\] - 1  
pd.merge(  
: df, df, left_on=\[\"Bins\", \"Area\", \"Test_0\"\],
right_on=\[\"Bins\", \"Area\", \"Test_1\"\], suffixes=(\"\_L\",
\"\_R\"),  
)
:::  
[How to set the index
```

## Rank 3

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0036 |
| Rerank Score | 0.1104 |

### Content

```text
`merge_ordered` combines ordered data
such as numeric or time series data with optional filling of missing
data with `fill_method`.  
::: ipython
python  
left = pd.DataFrame(  
: {\"k\": \[\"K0\", \"K1\", \"K1\", \"K2\"\], \"lv\": \[1, 2, 3, 4\],
\"s\": \[\"a\", \"b\", \"c\", \"d\"\]}  
)  
right = pd.DataFrame({\"k\": \[\"K1\", \"K2\", \"K4\"\], \"rv\": \[1, 2,
3\]})  
pd.merge_ordered(left, right, fill_method=\"ffill\", left_by=\"s\")
:::
```

## Rank 4

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0009 |
| Rerank Score | 0.0469 |

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

## Rank 5

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0015 |
| Rerank Score | 0.0424 |

### Content

```text
`~pandas.merge` performs join operations
similar to relational databases like SQL. Users who are familiar with
SQL but new to pandas can reference a
`comparison with SQL<compare_with_sql.join>`.
```

## Rank 6

| Field | Value |
|------|-------|
| Library | pandas |
| Module | io |
| Section | user_guide |
| Source | user_guide/io.md |
| Chunk ID | pandas:io:0086 |
| Rerank Score | 0.0325 |

### Content

```text
It\'s best to use `~pandas.concat` to
combine multiple files. See the
`cookbook<cookbook.csv.multiple_files>`
for an example.
```

## Rank 7

| Field | Value |
|------|-------|
| Library | pandas |
| Module | merging |
| Section | user_guide |
| Source | user_guide/merging.md |
| Chunk ID | pandas:merging:0017 |
| Rerank Score | 0.0318 |

### Content

```text
right = pd.DataFrame(  
:  
{  
: \"key\": \[\"K0\", \"K1\", \"K2\", \"K3\"\], \"C\": \[\"C0\",
\"C1\", \"C2\", \"C3\"\], \"D\": \[\"D0\", \"D1\", \"D2\", \"D3\"\],  
}  
) result = pd.merge(left, right, on=\"key\") result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_merge_on_key.png p.plot(\[left, right\], result,
labels=\[\"left\", \"right\"\], vertical=False); plt.close(\"all\");
:::  
The `how` argument to `~pandas.merge`
specifies which keys are included in the resulting table. If a key
combination **does not appear** in either the left or right tables, the
values in the joined table will be `NA`. Here is a summary of the `how`
options and their SQL equivalent names:  
Merge method   SQL Join Name        Description
-------------- -------------------- ------------------------------------------
`left`         `LEFT OUTER JOIN`    Use keys from left frame only  
`right`        `RIGHT OUTER JOIN`   Use keys from right frame only  
`outer`        `FULL OUTER JOIN`
```


---

## Observation

_Write your observations here._

============================================================

# Question 12

**Question:** What is metadata?

# Dense Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0014 |
| Rerank Score | 0.0003 |

### Content

```text
you can extract using the
`!metadata` function:  
>>> wheel_metadata = metadata('wheel')  # doctest: +SKIP  
The keys of the returned data structure name the metadata keywords, and
the values are returned unparsed from the distribution metadata:  
>>> wheel_metadata['Requires-Python']  # doctest: +SKIP
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'  
`PackageMetadata` also presents a
`!json` attribute that returns all the
metadata in a JSON-compatible form per
[PEP 566](http://www.python.org/dev/peps/pep-0566/ "PEP 566"):  
>>> wheel_metadata.json['requires_python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'  
The full set of available metadata is not described here. See the PyPA
[Core metadata
specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
for additional details.  
::: versionchanged
3.15 Previously and incidentally, if a METADATA file was missing from a
distribution, an empty `PackageMetadata` would be returned,
indistinguishable
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0025 |
| Rerank Score | 0.0104 |

### Content

```text
*context* is a
`DistributionFinder.Context` instance,
used to modify the search for distributions. Alternatively, *kwargs* may
contain keyword arguments for constructing a new
`!DistributionFinder.Context`.
:::  
::: {.attribute type="PackageMetadata"}
metadata  
Raises `MetadataNotFound` if the METADATA
file is not present in the distribution.  
There are all kinds of additional metadata available on
`!Distribution` instances as a
`PackageMetadata` instance:  
>>> dist.metadata['Requires-Python']  # doctest: +SKIP
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
>>> dist.metadata['License']  # doctest: +SKIP
'MIT'  
The full set of available metadata is not described here. See the PyPA
[Core metadata
specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
for additional details.
:::  
::: {.attribute type="str"}
name
:::  
::: {.attribute type="list[str]"}
requires
:::  
:::: {.attribute type="str"}
version  
A few metadata fields are also
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0015 |
| Rerank Score | 0.0147 |

### Content

```text
Previously and incidentally, if a METADATA file was missing from a
distribution, an empty `PackageMetadata` would be returned,
indistinguishable from an empty METADATA file. Now, a missing METADATA
file triggers a `MetadataNotFound` exception.
:::  
::: versionchanged
3.10 The `Description` is now included in the metadata when presented
through the payload. Line continuation characters have been removed.  
The `json` attribute was added.
:::
```

## Rank 4

| Field | Value |
|------|-------|
| Library | langchain |
| Module | knowledge-base |
| Section | langchain |
| Source | langchain/knowledge-base.md |
| Chunk ID | langchain:knowledge-base:0006 |
| Rerank Score | 0.0022 |

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

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0001 |
| Rerank Score | 0.0029 |

### Content

```text
::: {.module synopsis="Accessing package metadata"}
importlib.metadata
:::  
::: versionadded
3.8
:::  
::: versionchanged
3.10 `importlib.metadata` is no longer provisional.
:::  
**Source code:** `Lib/importlib/metadata/__init__.py`  
`importlib.metadata` is a library that provides access to the metadata
of an installed [Distribution
Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package),
such as its entry points or its top-level names ([Import
Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)s,
modules, if any). Built in part on Python\'s import system, this library
provides the entry point and metadata APIs that were previously exposed
by the now-removed `pkg_resources` package. Along with
`importlib.resources`, it supersedes
`pkg_resources`.  
`importlib.metadata` operates on third-party *distribution packages*
installed into Python\'s `site-packages` directory via tools such as
`pip`. Specifically, it works
```

## Rank 6

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0013 |
| Rerank Score | 0.0155 |

### Content

```text
::: function
metadata(distribution_name)  
Return the distribution metadata corresponding to the named distribution
package as a `PackageMetadata` instance.  
Raises `PackageNotFoundError` if the named
distribution package is not installed in the current Python environment.  
Raises `MetadataNotFound` if a
distribution package is present but no METADATA file is present.
:::  
::: PackageMetadata
A concrete implementation of the [PackageMetadata
protocol](https://importlib-metadata.readthedocs.io/en/latest/api.html#importlib_metadata.PackageMetadata).  
In addition to providing the defined protocol methods and attributes,
subscripting the instance is equivalent to calling the
`!get` method.
:::  
Every [Distribution
Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
includes some metadata, which you can extract using the
`!metadata` function:  
>>> wheel_metadata = metadata('wheel')  # doctest: +SKIP  
The keys of the returned data structure name the
```

## Rank 7

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0032 |
| Rerank Score | 0.0020 |

### Content

```text
`PathFinder`, serving
metadata for distribution packages found on the file system.  
The abstract class `importlib.abc.MetaPathFinder` defines the interface expected of finders by Python\'s
import system. `importlib.metadata` extends this protocol by looking for
an optional `find_distributions` callable on the finders from
`sys.meta_path` and presents this
extended interface as the `DistributionFinder` abstract base class, which defines this abstract method:  
@abc.abstractmethod
def find_distributions(context=DistributionFinder.Context()) -> Iterable[Distribution]:
"""Return an iterable of all Distribution instances capable of
loading the metadata for packages for the indicated ``context``.
"""  
The `DistributionFinder.Context` object
provides `~DistributionFinder.Context.path` and `~DistributionFinder.Context.name` properties indicating the path to search and name to match
and may supply other relevant context sought by the consumer.  
In practice, to support finding distribution
```


---

# Reranked Retrieval

## Rank 1

| Field | Value |
|------|-------|
| Library | python |
| Module | tkinter |
| Section | library |
| Source | library/tkinter.md |
| Chunk ID | python:tkinter:0276 |
| Rerank Score | 0.9202 |

### Content

```text
Read image data from the file named *filename* into the image.  
*format* specifies the format of the image data in the file.  
*metadata* is a dictionary passed to the image format driver. It
requires Tcl/Tk 9.0 or newer.  
*from_coords* specifies a rectangular sub-region of the image file data
to be copied to the destination image. It must be a tuple or a list of 1
to 4 integers `(x1, y1, x2, y2)`. If only *x1* and *y1* are specified,
the region extends from `(x1, y1)` to the bottom-right corner of the
image in the file. If all four coordinates are given, they specify
diagonally opposite corners of the region. If *from_coords* is not
given, the whole of the image in the file is read.  
*to* specifies the coordinates of the top-left corner of the region of
the image into which the data are read. The default is `(0, 0)`.  
If *shrink* is true, the size of the image is reduced, if necessary, so
that the region into which the file data are read is at the bottom-right
corner of the
```

## Rank 2

| Field | Value |
|------|-------|
| Library | python |
| Module | tkinter |
| Section | library |
| Source | library/tkinter.md |
| Chunk ID | python:tkinter:0275 |
| Rerank Score | 0.2150 |

### Content

```text
to the colors given in *data*, which must be a
string or a nested sequence of horizontal rows of pixel colors (for
example `"{red green} {blue yellow}"`).  
*to* specifies the coordinates of the region of the image into which the
data are copied. It must be a tuple or a list of 2 or 4 integers
`(x1, y1)` or `(x1, y1, x2, y2)` giving the top-left corner, and
optionally the bottom-right corner, of the region. The default position
is `(0, 0)`.  
*format* specifies the format of the image *data*, so that only image
file format handlers whose names begin with it are tried.  
*metadata* is a dictionary passed to the image format driver. It
requires Tcl/Tk 9.0 or newer.  
::: versionchanged
next Added the *format* and *metadata* parameters.
:::
::::  
::::: method
read(filename, format=None, \*, from_coords=None, to=None, shrink=False,
metadata=None)  
Read image data from the file named *filename* into the image.  
*format* specifies the format of the image data in the file.  
*metadata* is
```

## Rank 3

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0013 |
| Rerank Score | 0.0155 |

### Content

```text
::: function
metadata(distribution_name)  
Return the distribution metadata corresponding to the named distribution
package as a `PackageMetadata` instance.  
Raises `PackageNotFoundError` if the named
distribution package is not installed in the current Python environment.  
Raises `MetadataNotFound` if a
distribution package is present but no METADATA file is present.
:::  
::: PackageMetadata
A concrete implementation of the [PackageMetadata
protocol](https://importlib-metadata.readthedocs.io/en/latest/api.html#importlib_metadata.PackageMetadata).  
In addition to providing the defined protocol methods and attributes,
subscripting the instance is equivalent to calling the
`!get` method.
:::  
Every [Distribution
Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
includes some metadata, which you can extract using the
`!metadata` function:  
>>> wheel_metadata = metadata('wheel')  # doctest: +SKIP  
The keys of the returned data structure name the
```

## Rank 4

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0015 |
| Rerank Score | 0.0147 |

### Content

```text
Previously and incidentally, if a METADATA file was missing from a
distribution, an empty `PackageMetadata` would be returned,
indistinguishable from an empty METADATA file. Now, a missing METADATA
file triggers a `MetadataNotFound` exception.
:::  
::: versionchanged
3.10 The `Description` is now included in the metadata when presented
through the payload. Line continuation characters have been removed.  
The `json` attribute was added.
:::
```

## Rank 5

| Field | Value |
|------|-------|
| Library | python |
| Module | importlib.metadata |
| Section | library |
| Source | library/importlib.metadata.md |
| Chunk ID | python:importlib.metadata:0025 |
| Rerank Score | 0.0104 |

### Content

```text
*context* is a
`DistributionFinder.Context` instance,
used to modify the search for distributions. Alternatively, *kwargs* may
contain keyword arguments for constructing a new
`!DistributionFinder.Context`.
:::  
::: {.attribute type="PackageMetadata"}
metadata  
Raises `MetadataNotFound` if the METADATA
file is not present in the distribution.  
There are all kinds of additional metadata available on
`!Distribution` instances as a
`PackageMetadata` instance:  
>>> dist.metadata['Requires-Python']  # doctest: +SKIP
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
>>> dist.metadata['License']  # doctest: +SKIP
'MIT'  
The full set of available metadata is not described here. See the PyPA
[Core metadata
specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata)
for additional details.
:::  
::: {.attribute type="str"}
name
:::  
::: {.attribute type="list[str]"}
requires
:::  
:::: {.attribute type="str"}
version  
A few metadata fields are also
```

## Rank 6

| Field | Value |
|------|-------|
| Library | langchain |
| Module | character_text_splitter |
| Section | splitters |
| Source | splitters/character_text_splitter.md |
| Chunk ID | langchain:character_text_splitter:0010 |
| Rerank Score | 0.0100 |

### Content

```text
`.createDocuments` to propagate metadata associated with each document to the output chunks:  
```ts
const metadatas = [{"document": 1}, {"document": 2}]
const documents = splitter.createDocuments(
[{ pageContent: stateOfTheUnion }, { pageContent: stateOfTheUnion }],
{ metadatas: metadatas }
);
console.log(documents[0]);
```
```javascript
Document {
pageContent: 'Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  \n\nLast year COVID-19 kept us apart. This year we are finally together again. \n\nTonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. \n\nWith a duty to one another to the American people to the Constitution. \n\nAnd with an unwavering resolve that freedom will always triumph over tyranny. \n\nSix days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his
```

## Rank 7

| Field | Value |
|------|-------|
| Library | langchain |
| Module | messages |
| Section | langchain |
| Source | langchain/messages.md |
| Chunk ID | langchain:messages:0024 |
| Rerank Score | 0.0032 |

### Content

```text
or data for downstream processing without cluttering the model's context.  
<Accordion title="Example: Using artifact for retrieval metadata">
For example, a [retrieval](/oss/langchain/retrieval) tool could retrieve a passage from a document for reference by a model. Where message `content` contains text that the model will reference, an `artifact` can contain document identifiers or other metadata that an application can use (e.g., to render a page). See example below:  
:::python  
```python
from langchain.messages import ToolMessage
```


---

## Observation

_Write your observations here._

============================================================

