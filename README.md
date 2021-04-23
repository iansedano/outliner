# Outliner Tool

To aid in the creation and transition from idea, to draft, to outline, to file structure, and back again if needed.


# Issues

Have run into a large issue - using `*` to flag ITEMS, or any reserved identifier like `#` or `$` is that my simple implementation of a lexer will pick these up.

If freedom is to be given to use any file type: For example in this source file

```
* myfolder
    * myfile.txt
        mycontents
        morecontents
    * myfile.py
        def hi(x):
            x = x * 2
            return x
    * nextfolder
        * anotherfolder
            * myfile.txt
                helloworld
* last folder
    * finalfile.js
        console.log("hello world");

```

Then the `*` in the Python file will be interpreted as an ITEM.


# Restrictions

- any line with a `.` will be considered a file and not a folder (this does not apply to contents of a file)