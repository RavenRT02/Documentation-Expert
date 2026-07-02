# Question

How do I create directories recursively?

## Rank 1

- **Chunk ID:** python:glob:0004
- **Library:** python
- **Source:** library/glob.md

### Content

```text
Using the \"`**`\" pattern in large directory trees may consume an
inordinate amount of time.
::::  
:::: note
::: title
Note
:::  
This function may return duplicate path names if *pathname* contains
multiple \"`**`\" patterns and *recursive* is true.
::::  
:::: note
::: title
Note
:::  
Any `OSError` exceptions raised from
scanning the filesystem are suppressed. This includes
`PermissionError` when accessing
directories without read permission.
::::  
::: versionchanged
3.5 Support for recursive globs using \"`**`\".
:::  
::: versionchanged
3.10 Added the *root_dir* and *dir_fd* parameters.
:::  
::: versionchanged
3.11 Added the *include_hidden* parameter.
:::
:::::::::::::::  
:::::::::::: function
iglob(pathname, \*, root_dir=None, dir_fd=None, recursive=False,
include_hidden=False)  
Return an `iterator` which yields the
same values as `glob` without actually
storing them all simultaneously.  
::: audit-event
glob.glob pathname,recursive glob.iglob
:::  
:::
```

## Rank 2

- **Chunk ID:** python:pathlib:0047
- **Library:** python
- **Source:** library/pathlib.md

### Content

```text
::: method
Path.iterdir()  
When the path points to a directory, yield path objects of the directory
contents:  
>>> p = Path('docs')
>>> for child in p.iterdir(): child
...
PosixPath('docs/conf.py')
PosixPath('docs/_templates')
PosixPath('docs/make.bat')
PosixPath('docs/index.rst')
PosixPath('docs/_build')
PosixPath('docs/_static')
PosixPath('docs/Makefile')  
The children are yielded in arbitrary order, and the special entries
`'.'` and `'..'` are not included. If a file is removed from or added to
the directory after creating the iterator, it is unspecified whether a
path object for that file is included.  
If the path is not a directory or otherwise inaccessible,
`OSError` is raised.
:::  
::::::::::::: method
Path.glob(pattern, \*, case_sensitive=None, recurse_symlinks=False)  
Glob the given relative *pattern* in the directory represented by this
path, yielding all matching files (of any kind):  
>>> sorted(Path('.').glob('*.py'))
[PosixPath('pathlib.py'), PosixPath('setup.py'),
```

## Rank 3

- **Chunk ID:** python:venv:0006
- **Library:** python
- **Source:** library/venv.md

### Content

```text
Creates virtual Python environments in one or more target directories.
```

## Rank 4

- **Chunk ID:** langchain:code_splitter:0044
- **Library:** langchain
- **Source:** splitters/code_splitter.md

### Content

```text
$items = Get-ChildItem -Path $directoryPath

$files = $items | Where-Object { -not $_.PSIsContainer }

$sortedFiles = $files | Sort-Object LastWriteTime

foreach ($file in $sortedFiles) {
Write-Output ("Name: " + $file.Name + " | Last Write Time: " + $file.LastWriteTime)
}
`;
```

## Rank 5

- **Chunk ID:** python:os:0155
- **Library:** python
- **Source:** library/os.md

### Content

```text
and *ns* parameters.
:::  
::: versionchanged
3.6 Accepts a `path-like object`.
:::  
::: versionchanged
3.15 Accepts any real numbers as *times*, not only integers or floats.
:::
:::::::  
::::::::::: function
walk(top, topdown=True, onerror=None, followlinks=False)  
Generate the file names in a directory tree by walking the tree either
top-down or bottom-up. For each directory in the tree rooted at
directory *top* (including *top* itself), it yields a 3-tuple
`(dirpath, dirnames, filenames)`.  
*dirpath* is a string, the path to the directory. *dirnames* is a list
of the names of the subdirectories in *dirpath* (including symlinks to
directories, and excluding `'.'` and `'..'`). *filenames* is a list of
the names of the non-directory files in *dirpath*. Note that the names
in the lists contain no path components. To get a full path (which
begins with *top*) to a file or directory in *dirpath*, do
`os.path.join(dirpath, name)`. Whether or not the lists are sorted
depends on the file
```


---

# Question

How do I merge DataFrames?

## Rank 1

- **Chunk ID:** pandas:cookbook:0040
- **Library:** pandas
- **Source:** user_guide/cookbook.md

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

- **Chunk ID:** pandas:merging:0025
- **Library:** pandas
- **Source:** user_guide/merging.md

### Content

```text
`DataFrame.join` combines the columns of
multiple, potentially differently-indexed `DataFrame` into a single result `DataFrame`.  
::: ipython
python  
left = pd.DataFrame(  
: {\"A\": \[\"A0\", \"A1\", \"A2\"\], \"B\": \[\"B0\", \"B1\",
\"B2\"\]}, index=\[\"K0\", \"K1\", \"K2\"\]  
)  
right = pd.DataFrame(  
: {\"C\": \[\"C0\", \"C2\", \"C3\"\], \"D\": \[\"D0\", \"D2\",
\"D3\"\]}, index=\[\"K0\", \"K2\", \"K3\"\]  
)  
result = left.join(right) result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_join.png p.plot(\[left, right\], result,
labels=\[\"left\", \"right\"\], vertical=False); plt.close(\"all\");
:::  
::: ipython
python  
result = left.join(right, how=\"outer\") result
:::  
::: {.ipython suppress=""}
python  
\@savefig merging_join_outer.png p.plot(\[left, right\], result,
labels=\[\"left\", \"right\"\], vertical=False); plt.close(\"all\");
:::  
::: ipython
python  
result = left.join(right, how=\"inner\") result
:::  
::: {.ipython suppress=""}
python
```

## Rank 3

- **Chunk ID:** pandas:10min:0020
- **Library:** pandas
- **Source:** user_guide/10min.md

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

## Rank 4

- **Chunk ID:** pandas:merging:0021
- **Library:** pandas
- **Source:** user_guide/merging.md

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

## Rank 5

- **Chunk ID:** pandas:merging:0016
- **Library:** pandas
- **Source:** user_guide/merging.md

### Content

```text
`~pandas.merge` implements common SQL
style joining operations.  
- **one-to-one**: joining two `DataFrame` objects on their indexes which must contain unique
values.
- **many-to-one**: joining a unique index to one or more columns in a
different `DataFrame`.
- **many-to-many**: joining columns on columns.  
:::: note
::: title
Note
:::  
When joining columns on columns, potentially a many-to-many join, any
indexes on the passed `DataFrame`
objects **will be discarded**.
::::  
For a **many-to-many** join, if a key combination appears more than once
in both tables, the `DataFrame` will
have the **Cartesian product** of the associated data.  
::: ipython
python  
left = pd.DataFrame(  
:  
{  
: \"key\": \[\"K0\", \"K1\", \"K2\", \"K3\"\], \"A\": \[\"A0\",
\"A1\", \"A2\", \"A3\"\], \"B\": \[\"B0\", \"B1\", \"B2\", \"B3\"\],  
}  
)  
right = pd.DataFrame(  
:  
{  
: \"key\": \[\"K0\", \"K1\", \"K2\", \"K3\"\], \"C\": \[\"C0\",
\"C1\", \"C2\", \"C3\"\], \"D\": \[\"D0\", \"D1\", \"D2\",
```


---

# Question

What is PromptTemplate?

## Rank 1

- **Chunk ID:** langchain:INVALID_PROMPT_INPUT:0002
- **Library:** langchain
- **Source:** langchain/errors/INVALID_PROMPT_INPUT.md

### Content

```text
Here is an example of how you should respond:

{
"firstName": "John",
"lastName": "Doe",
"age": 21
}

Now, answer the following question:

{question}`);
```  
You might think that the above prompt template should require a single input key named question, but the JSON object will be interpreted as an additional variable because the curly braces (` from "@langchain/core/prompts";
import { ChatOpenAI } from "@langchain/openai";  
const prompt = PromptTemplate.fromTemplate(`You are a helpful assistant.  
Here is an example of how you should respond:  
{{
"firstName": "John",
"lastName": "Doe",
"age": 21
}}  
Now, answer the following question:  
{question}`);
```
:::
```

## Rank 2

- **Chunk ID:** langchain:INVALID_PROMPT_INPUT:0001
- **Library:** langchain
- **Source:** langchain/errors/INVALID_PROMPT_INPUT.md

### Content

```text
title: INVALID_PROMPT_INPUT  
{/* TODO: fix link when porting page */}
Occurs when a [prompt template](https://github.com/langchain-ai/langchain/blob/v0.3/docs/docs/concepts/prompt_templates.mdx) received missing or invalid input variables.  
:::js
One unexpected way this can occur is if you add a JSON object directly into a prompt template:  
```typescript
import { PromptTemplate } from "@langchain/core/prompts";
import { ChatOpenAI } from "@langchain/openai";

const prompt = PromptTemplate.fromTemplate(`You are a helpful assistant.

Here is an example of how you should respond:

{
"firstName": "John",
"lastName": "Doe",
"age": 21
}

Now, answer the following question:
```

## Rank 3

- **Chunk ID:** langchain:context-engineering:0010
- **Library:** langchain
- **Source:** langchain/context-engineering.md

### Content

```text
The system prompt sets the LLM's behavior and capabilities. Different users, contexts, or conversation stages need different instructions. Successful agents draw on memories, preferences, and configuration to provide the right instructions for the current state of the conversation.  
<Tabs>
<Tab title="State">
Access message count or conversation context from state:  
:::python  
```python
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest

@dynamic_prompt
def state_aware_prompt(request: ModelRequest) -> str:
# request.messages is a shortcut for request.state["messages"]
message_count = len(request.messages)

base = "You are a helpful assistant."

if message_count > 10:
base += "\nThis is a long conversation - be extra concise."

return base

agent = create_agent(
model="gpt-5.5",
tools=[...],
middleware=[state_aware_prompt]
)
```
:::  
:::js
```typescript
import { createAgent } from "langchain";
```

## Rank 4

- **Chunk ID:** langchain:mcp:0028
- **Library:** langchain
- **Source:** langchain/mcp.md

### Content

```text
[Prompts](https://modelcontextprotocol.io/docs/concepts/prompts) allow MCP servers to expose reusable prompt templates that can be retrieved and used by clients. LangChain converts MCP prompts into [messages](/oss/langchain/messages), making them easy to integrate into chat-based workflows.  
#### Loading prompts  
Use `client.get_prompt()` to load a prompt from an MCP server:  
```python
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({...})

# Load a prompt by name
messages = await client.get_prompt("server_name", "summarize")  # [!code highlight]

# Load a prompt with arguments
messages = await client.get_prompt(  # [!code highlight]
"server_name",  # [!code highlight]
"code_review",  # [!code highlight]
arguments={"language": "python", "focus": "security"}  # [!code highlight]
)  # [!code highlight]
```

## Rank 5

- **Chunk ID:** langchain:handoffs-customer-support:0022
- **Library:** langchain
- **Source:** langchain/multi-agent/handoffs-customer-support.md

### Content

```text
# Format prompt with state values (supports {warranty_status}, {issue_type}, etc.)
system_prompt = stage_config["prompt"].format(**request.state)

# Inject system prompt and step-specific tools
request = request.override(  # [!code highlight]
system_prompt=system_prompt,  # [!code highlight]
tools=stage_config["tools"],  # [!code highlight]
)

return handler(request)
```
:::  
:::js
```typescript
import { createMiddleware } from "langchain";

const applyStepMiddleware = createMiddleware({
name: "applyStep",
stateSchema: SupportState,
wrapModelCall: async (request, handler) => {
// Get current step (defaults to warranty_collector for first interaction)
const currentStep = request.state.currentStep ?? "warranty_collector"; // [!code highlight]

// Look up step configuration
const stepConfig = STEP_CONFIG[currentStep]; // [!code highlight]
```


---

# Question

How do i read a CSV?

## Rank 1

- **Chunk ID:** pandas:cookbook:0045
- **Library:** pandas
- **Source:** user_guide/cookbook.md

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

## Rank 2

- **Chunk ID:** pandas:cookbook:0049
- **Library:** pandas
- **Source:** user_guide/cookbook.md

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

## Rank 3

- **Chunk ID:** pandas:io:0085
- **Library:** pandas
- **Source:** user_guide/io.md

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

## Rank 4

- **Chunk ID:** pandas:io:0027
- **Library:** pandas
- **Source:** user_guide/io.md

### Content

```text
`read_csv` accepts the following common
arguments:  
#### Basic  
filepath_or_buffer : various  
: Either a path to a file (a `python:str`, `python:pathlib.Path`)
URL (including http, ftp, and S3 locations), or any object with a
`read()` method (such as an open file or
`~python:io.StringIO`).  
sep : str, defaults to `','` for `read_csv`, `\t` for `read_table`  
: Delimiter to use. If sep is `None`, the C engine cannot automatically
detect the separator, but the Python parsing engine can, meaning the
latter will be used and automatically detect the separator by
Python\'s builtin sniffer tool, `python:csv.Sniffer`. In addition, separators longer than 1 character and
different from `'\s+'` will be interpreted as regular expressions and
will also force the use of the Python parsing engine. Note that regex
delimiters are prone to ignoring quoted data. Regex example:
`'\\r\\t'`.  
delimiter : str, default `None`  
: Alternative argument name for sep.  
#### Column and index locations and
```

## Rank 5

- **Chunk ID:** python:csv:0025
- **Library:** python
- **Source:** library/csv.md

### Content

```text
The simplest example of reading a CSV file:  
import csv
with open('some.csv', newline='') as f:
reader = csv.reader(f)
for row in reader:
print(row)  
Reading a file with an alternate format:  
import csv
with open('passwd', newline='') as f:
reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
for row in reader:
print(row)  
The corresponding simplest possible writing example is:  
import csv
with open('some.csv', 'w', newline='') as f:
writer = csv.writer(f)
writer.writerows(someiterable)  
Since `open` is used to open a CSV file
for reading, the file will by default be decoded into unicode using the
system default encoding (see `locale.getencoding`). To decode a file using a different encoding, use the
`encoding` argument of open:  
import csv
with open('some.csv', newline='', encoding='utf-8') as f:
reader = csv.reader(f)
for row in reader:
print(row)  
The same applies to writing in something other than the system default
encoding: specify the encoding argument when
```


---

# Question

How do I iterate over a directory?

## Rank 1

- **Chunk ID:** python:modules:0019
- **Library:** python
- **Source:** tutorial/modules.md

### Content

```text
Without arguments, `dir` lists the names
you have defined currently:  
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']  
Note that it lists all types of names: variables, modules, functions,
etc.  
`dir` does not list the names of built-in
functions and variables. If you want a list of those, they are defined
in the standard module `builtins`:  
>>> import builtins
>>> dir(builtins)  # doctest: +NORMALIZE_WHITESPACE
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
'ImportWarning',
```

## Rank 2

- **Chunk ID:** python:xml.etree.elementtree:0021
- **Library:** python
- **Source:** library/xml.etree.elementtree.md

### Content

```text
root.findall(".")
```

## Rank 3

- **Chunk ID:** python:pathlib:0047
- **Library:** python
- **Source:** library/pathlib.md

### Content

```text
::: method
Path.iterdir()  
When the path points to a directory, yield path objects of the directory
contents:  
>>> p = Path('docs')
>>> for child in p.iterdir(): child
...
PosixPath('docs/conf.py')
PosixPath('docs/_templates')
PosixPath('docs/make.bat')
PosixPath('docs/index.rst')
PosixPath('docs/_build')
PosixPath('docs/_static')
PosixPath('docs/Makefile')  
The children are yielded in arbitrary order, and the special entries
`'.'` and `'..'` are not included. If a file is removed from or added to
the directory after creating the iterator, it is unspecified whether a
path object for that file is included.  
If the path is not a directory or otherwise inaccessible,
`OSError` is raised.
:::  
::::::::::::: method
Path.glob(pattern, \*, case_sensitive=None, recurse_symlinks=False)  
Glob the given relative *pattern* in the directory represented by this
path, yielding all matching files (of any kind):  
>>> sorted(Path('.').glob('*.py'))
[PosixPath('pathlib.py'), PosixPath('setup.py'),
```

## Rank 4

- **Chunk ID:** python:stdlib:0003
- **Library:** python
- **Source:** tutorial/stdlib.md

### Content

```text
The `glob` module provides a function for
making file lists from directory wildcard searches:  
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## Rank 5

- **Chunk ID:** python:functions:0004
- **Library:** python
- **Source:** library/functions.md

### Content

```text
| | `eval`                                                                                                   | | [`list()`](..%20class::%20list(iterable=(),%20/):noindex:)   | | `repr`                                                                                                                           |
| | `all`                                                                            | | `exec`                                                                                                   | | `locals`                      | | `reversed`                                                                                                                       |
| | `anext`                                                                          | |                                                                                                                                          | |
```


---

# Question

What is RecursiveCharacterTextSplitter?

## Rank 1

- **Chunk ID:** langchain:index:0024
- **Library:** langchain
- **Source:** splitters/index.md

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

- **Chunk ID:** langchain:code_splitter:0001
- **Library:** langchain
- **Source:** splitters/code_splitter.md

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

- **Chunk ID:** langchain:knowledge-base:0014
- **Library:** langchain
- **Source:** langchain/knowledge-base.md

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

- **Chunk ID:** langchain:code_splitter:0028
- **Library:** langchain
- **Source:** splitters/code_splitter.md

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

## Rank 5

- **Chunk ID:** langchain:index:0023
- **Library:** langchain
- **Source:** splitters/index.md

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


---

