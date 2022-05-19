# Markdown TOC Generator
A small Python script to generate a table of contents for a markdown file. 

## Usage
`./generate-toc.py --file PATH [--depth DEPTH] [--link PATH]`

- file
  - Path to the markdown file from which the TOC should be generated.
- depth
  - The depth to which headings should be included in the TOC (1-6).  
  ```
  ./generate-toc.py --file example.md --depth 3
  
  Output:
  - [heading1](#heading1)
    - [heading2](#heading2)
      - [heading3](#heading3)
  ```
- link
  - The specified path is appended before the links. This is useful when you want to refer to headings in another markdown file.  
  ```
  ./generate-toc.py --file example.md --depth 3 --link another-example.md
  
  Output:
  - [heading1](another-example.md#heading1)
    - [heading2](another-example.md#heading2)
      - [heading3](another-example.md#heading3)
  ```
