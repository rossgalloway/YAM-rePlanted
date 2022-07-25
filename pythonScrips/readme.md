# How to Run Python Scripts Using the Command-Line

A Python interactive session will allow you to write a lot of lines of code, but once you close the session, you lose everything you’ve written. That’s why the usual way of writing Python programs is by using plain text files. By convention, those files will use the .py extension. (On Windows systems the extension can also be .pyw.)

Python code files can be created with any plain text editor. If you are new to Python programming, you can try Sublime Text, which is a powerful and easy-to-use editor, but you can use any editor you like.

To keep moving forward in this tutorial, you’ll need to create a test script. Open your favorite text editor and write the following code:

```
!/usr/bin/env python3
```

print('Hello World!')

Save the file in your working directory with the name hello.py. With the test script ready, you can continue reading.
Using the python Command

To run Python scripts with the python command, you need to open a command-line and type in the word python, or python3 if you have both versions, followed by the path to your script, just like this:

```
$ python3 hello.py
Hello World!
```

If everything works okay, after you press Enter, you’ll see the phrase Hello World! on your screen. That’s it! You’ve just run your first Python script!

If this doesn’t work right, maybe you’ll need to check your system PATH, your Python installation, the way you created the hello.py script, the place where you saved it, and so on.

This is the most basic and practical way to run Python scripts.
