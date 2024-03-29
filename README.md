# Outliner Tool

To aid in the creation and transition from idea, to draft, to outline, to file structure, and back again if needed.


## Purpose

Ever make an outline like this?

```
Section 1
    Chapter 1
        Intro to characters
    Chapter 2
        Starting the journey
    Chapter 3
        On their way
Section 2
    Chapter 4
        Running into trouble
    Chapter 5
        Running into more trouble
    Chapter 6
        Breakdown
Section 3
    Chapter 7
        Meeting friend
    Chapter 8
        Overcoming troubles
    Chapter 9
        Arriving back home
```

Now you want to move this to individual files like this:

```
Section 1
    Chapter 1.md
        Intro to characters
    Chapter 2.md
        Starting the journey
    Chapter 3.md
        On their way
Section 2
    Chapter 4.md
        Running into trouble
    Chapter 5.md
        Running into more trouble
    Chapter 6.md
        Breakdown
Section 3
    Chapter 7.md
        Meeting friend
    Chapter 8.md
        Overcoming troubles
    Chapter 9.md
        Arriving back home
```


Or this:


```
Section 1
    Chapter 1.md
        Intro to characters
        Bill, Bob
        Jill, Jane
    Chapter 2.md
        Starting the journey
    Chapter 3.md
        On their way
```

This last example would be one folder called "Chapter 1" containging three markdown files each with some content. The file `Chapter 1.md` would contain 3 lines of content.

You can create any plain text file type you want:

```
Project 1
    main.py
        def hello():
            print("hello world")
```

Will create a folder with a python file with the following content:

```python
def hello():
    print("hello world")
```

## Important Points

1. Any line with a `.` will be considered a file and not a folder (this does not apply to contents of a file)

2. Beware when calling files or folders the same name, they will be overwritten.

```
myfolder
    myfile.txt
        mycontents
        morecontents
    myfile.txt
        helloworld
```

This will end up with:

```
myfolder
    myfile.txt
        helloworld
```

3. Bear in mind that file systems implement their own ordering. So if you have a source file like this:

```
instructions
    first step.md
    second step.md
    third step.md
    fourth step.md
```

Once they are created, you will probably end up with a folder with the files ordered like this:

```
instructions
    first step.md
    fourth step.md
    second step.md
    third step.md
```

For this reason you can use the `number` argument as `True` in `create_main` to automatically number the folders and files so that they keep their order.

```
001 instructions
    001 first step.md
    002 second step.md
    003 third step.md
    004 fourth step.md
```

4. This tool does _not_ yet recognize spaces as equivalent to tabs. The input document _must_ use tabs for indentation.

5. If you leave a blank line without any content, be sure that it has the correct tab indentation level. For instance:

```
folder
    folder
        file.txt
            Title

            Content

```

If the line between `Title` and `Content` has zero tabs, this will cause unexpected results since the parser will take that to mean that its the end of the file, and then you have a new folder that has as a parent `file.txt` which will probably result in an error.

## Usage

1. Clone this repository.
1. Open `main.py`.
1. Modify the relevant paths and run it.

For example:

```python
from o_creator import create_main

# Insert full Linux (no ~) or Windows path here
source_file = "/home/i/Dropbox/Desktop/outliner_linux_test/outline.txt"
output = "/home/i/Dropbox/Desktop/outliner_linux_test/output"

# the argument number here is used to number the output folders and files
create_main(source_file, output, number = True)
```

This tool uses `pathlib` so Windows or Linux paths will work here.