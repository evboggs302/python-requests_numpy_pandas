# Using/Running Python in VS Code

1. `cd` into the directory that will house the project
2. Using the command `python3 -m venv venv/` will create the virtual environment that will house the required dependencies.
3. Next, "activate" the virtual environment using the command `source venv/bin/activate`
   - Now when you use `pip install <package>` it will install that package to the virtual environment for use.

- If you start getting a `unresolved import` error in your script, you will need to select a different Python interpretor.

---

_A lot of help was gained from this [article](https://towardsdatascience.com/virtual-environments-104c62d48c54)_