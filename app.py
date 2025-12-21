import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is an agent based model coureswork implemented in marimo
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Opinion Dynamics Model

    There are agents with an opinion - affiliation to a political party - who are interacting with their friends. The agent's opinion may change on each interaction under certain rules

    We are studying if the society of agents will converge on their opinion
    """)
    return


@app.cell
def _():
    from typing import List
    return


@app.class_definition
class Agents:
    id: int
    friends: list
    friend_intensity: list[dict[str: int, str: float]]
    resistance: float
    influence: float
    opinion: bool
    information_access: bool
    confidence: float


@app.class_definition
# Experimenting with classes

class Person:
    """Name and friends of a person"""
    name: str = ""
    friends: list = []

    def add_friend(self, friend: str):
        self.friends.append(friend)


@app.cell
def _():
    a = Person()
    b = Person()
    a.name = "Arun"
    a.add_friend("X")
    a.add_friend("Y")
    a.add_friend("Z")

    return a, b


@app.cell
def _(a):
    a.name
    return


@app.cell
def _(a):
    a.friends
    return


@app.cell
def _(a):
    print(type(a))
    print(type(a.name))
    print(type(a.friends))
    return


@app.cell
def _(b):
    b.friends
    return


@app.cell
def _(b):
    b.add_friend("W")
    return


@app.cell
def _(b):
    b.friends
    return


@app.cell
def _(a):
    a.friends
    return


@app.cell
def _():
    Person.name
    return


@app.cell
def _(a):
    a.name
    return


@app.cell
def _():
    Person.__doc__
    return


if __name__ == "__main__":
    app.run()
