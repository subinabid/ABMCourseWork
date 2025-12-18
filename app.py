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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
