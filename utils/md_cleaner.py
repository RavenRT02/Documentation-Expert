import re
from pathlib import Path

def remove_image(text):
    """Remove image links like 
    ![Inheritance diagram showing...](pathlib-inheritance.png) from markdown by
    taking text, replacing every matching char in pattern with empty string '' and return text"""
    
    pattern = r'!\[.*?\]\(.*?\)'        # ![any text](any text)
    return re.sub(pattern, '', text)         


def remove_horizontal_lines(text):
    """Remove horizontal lines like
    ----------------------- from markdown"""

    pattern = r'^\s*([-*_])\1{2,}\s*$'   
    # [start] [one or more whitespace] [group -or*or_ as 1] [if grp 1 repeat > 2] [one or more whitespace] [end]
    # A line containing only 3 or more - or * or _ characters.
    # we use \1 because we are goruping that and matching for following lines, if - is grouped then only that is matched not * or _
    # MULTILINE - applies ^----$ to everyline one at a time
    return re.sub(pattern, '', text, flags=re.MULTILINE)


def remove_index_blocks(text):
    """
    Remove blocks like:
    ::: index
    pair: module; pathlib
    pair: class; Path
    :::
    """
    pattern = r'^::: index\s*\n.*?^:::\s*$'
    return re.sub(pattern, '', text, flags=re.MULTILINE | re.DOTALL)


def clean_sphinx_rules(text):
    """clean spinx rules like `Path`{.interpreted-text role="class"}
    to `Path` in markdown"""

    pattern = r'(`[^`]+`)\{[^}]*\}'
    return re.sub(pattern, r'\1', text)      # group everything within '' and subsititute it with the pattern


def clean_sphinx_refs(text):
    """
    Convert: [](#id1) [PurePath](#purepath)
    or `PurePath` """

    pattern = r'\[([^\]]+)\]\(#.*?\)'      # [PurePath] is grouped , this is replaced for the whole pattern
    return re.sub(pattern, r'\1', text)


def clean_extra_newlines(text):
    """Replace 3 or more newlines with 2 newlines"""
    return re.sub(r'\n{3,}', '\n\n', text).strip()


def remove_trailing_spaces(text):

    return '\n'.join(line.rstrip() for line in text.splitlines())


def remove_empty_headings(text):

    pattern = r'^#+\s*$'
    return re.sub(pattern, '', text, flags=re.MULTILINE)
 


def clean_markdown(text):
    """use all helper functions to clean markdwon"""

    text = remove_image(text)
    text = remove_horizontal_lines(text)
    text = remove_index_blocks(text)

    text = clean_sphinx_rules(text)
    text = clean_sphinx_refs(text)

    text = remove_empty_headings(text)

    text = remove_trailing_spaces(text)

    text = clean_extra_newlines(text)

    return text


if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent.parent
    source = BASE_DIR / "pandoc_test_output" / "pathlib.md"
    destination = BASE_DIR / "cleaned_markdown" / "pathlib.md"

    """with open(source, encoding='utf-8') as file:
        text = file.read()

    cleaned_file = clean_markdown(text)

    with open(destination, 'w', encoding='utf-8') as file:
        file.write(cleaned_file)"""
    
    text = source.read_text(encoding='utf-8')
    cleaned_file = clean_markdown(text)
    destination.write_text(cleaned_file, encoding='utf-8')