import marimo

__generated_with = "0.18.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    # Class names start with Capital letter


    class Student:
        """Students in a group"""

        def __init__(self, name: str, batch: int, group: str):
            self.name = name
            self.batch = batch
            self.group = group

        def __str__(self):
            return f"{self.name} - {str(self.batch)}{self.group}"


    # Line 4 above is a docstring. All Classes ant non-obvious functions should have a docstrings which indicates the purpose

    # name:str indicates the variable name is a string. If you recollect the discussion form class
    return (Student,)


@app.cell
def _():
    # A list in python stores a collection of objects, seperated by comma
    # A dictionary in python stores data in key: value format 
    STUDENT_LIST = [
        {"name": "Apple", "batch": 17, "group":"A"},
        {"name": "Mango", "batch": 17, "group":"B"},
        {"name": "Orange", "batch": 17, "group":"C"}
    ]

    # Above student list is a list of dicts
    return (STUDENT_LIST,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `**` is an unpacking operator

    ```
    [Student(**student) for student in STUDENT_LIST ]
    ``` is a generator
    """)
    return


@app.cell
def _(STUDENT_LIST, Student):
    students = [Student(**student) for student in STUDENT_LIST ]
    return (students,)


@app.cell
def _(students):
    # The first item in Student is accessed with index [0]
    # elements of a class are accessed usinghte . operator
    students[0].name

    # The above line signifies the name of the first student object
    return


@app.cell
def _(students):
    students[2].__str__()
    return


@app.cell
def _(Student):
    # The class Course inherits Student
    class Course(Student):
        """Course offered"""

        def __init__(self, course: str, name:str, batch:int, group:str):
            super().__init__(name, batch, group)
            self.course = course

    return (Course,)


@app.cell
def _(Course, STUDENT_LIST):
    x = Course("ABM", **STUDENT_LIST[0])
    return (x,)


@app.cell
def _(x):
    x.name
    return


@app.cell
def _(x):
    x.course
    return


if __name__ == "__main__":
    app.run()
