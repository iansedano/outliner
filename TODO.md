# TODO

Long term goal is to make this a GUI app with Qt.

### Done

- clean up names, Scanner, Lexer, Tokenizer, Parser
- Line Number Handling


### Need
- CLI
- be able to get folder structure into text document without also getting content. (for high level reordering)
- Run tests with empty lines to check behavior
- Test with bad tab structure:
    ```
    folder
        file.txt
    folder
            file.txt
    ```
- Handle spaces as tabs
    ```
    folder
      file.txt
    folder
      file.txt
    ```
- Handle blank lines with no tabs/spaces
    ```
    folder
        file.txt
    folder
        folder
            file.txt
            Title

            Content
    ```

### Want
- warn about binary files and exit...

### Nice

- deal with binary files (keep content but don't display) - related to high level content as above.






