# TODO

Long term goal is to make this a GUI app with Qt.

### Clean up

- clean up names, Scanner, Lexer, Tokenizer, Parser


### Error Checking

- Add warning about file names
- Run tests with empty lines to check behavior
- Test with bad tab structure:

```
folder
    file.txt
folder
        file.txt
```

### Line Number Handling Feature

- Line Number Handling
Add a module that will take care of number handling
and as a byproduct, deal with using the same name


```
folder
    file.md
    file.md
    file.md
folder
    file.md
    file.md
```

With a argument like:

```python
create_folders(source_file, output, numbering = true, pad = 2)
```

```
01 folder
    01 file.md
    02 file.md
    03 file.md
02 folder
    01 file.md
    02 file.md
```

Possibly with more advanced config like

```python
numbering_config = {
    global_config : {
        numbering : true,
        pad : true,
        delete_existing_format: "^\d{3} " # Will remove existing numbering if match
    },
    custom_configs: [
        {
            tab_level: 0, # Will override numbering at that tab level
            pad: 3
        }
    ]
}
```

Maybe even there is some kind of analyzer that checks for padding and recommends...