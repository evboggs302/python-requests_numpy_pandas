# Using/Running Python in VS Code

1. `cd` into the directory that will house the project
2. Using the command `python3 -m venv venv/` will create the virtual environment that will house the required dependencies.
3. Next, "activate" the virtual environment using the command `source venv/bin/activate`
   - Now when you use `pip install <package>` it will install that package to the virtual environment for use.

- If you start getting a `unresolved import` error in your script, you will need to select a different Python interpretor.
    - There should be multiple options to select from, but the one I've found the most success with is the `"venv/bin/python3.9"` interpreter.
- If you need to update the version of python:
  1.  download from the official python website
  2.  deactivate the current virtual environmnet
  3.  remove the venv directory from your project
  4.  create a new venv pointing to `venv/bin/python3`
  5.  run the command `python3 -m venv --upgrade YOUR_VENV_DIRECTORY`

_Insight was gained from this [article](https://towardsdatascience.com/virtual-environments-104c62d48c54)._

---

# Requests Library

- Dyanmic URL parameters can be achieved using either an `F-String` or the `format()` method.
- Default encoding will be the default encoding of your virtual environment. If one isn't set, unicode will be used. (This is why I specified the encoding when writing to the file.)

---

# Context Managers

- Context managers spin up the needed resources for the operation at hand, and then **automatically closes** those resources after completion. This is why the `.close()` method isn't required.
- Using `with` effectively can help avoid resource leaks and make code easier to read.
- Using context managers with file operations is a common use case, but there are other uses that make sense.
  - Connecting to a DataBase
  - Lock objects in threading
  - Custom conext management classes using the `contextlib`
  ```py
  from contextlib import contextmanager
  ```

---

# NumPy

---

# Pandas

---

_This project is currently a work in progress._
