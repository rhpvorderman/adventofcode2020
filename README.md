# Advent of Code 2020: Problems solved with Python

These are my answers for the [Advent of Code 2020](
https://adventofcode.com/2020/) challenge. I use Python as my main programming 
language for this exercise. 

# Overarching goal: show novice users some good Python code examples.
Having been programming in Python for a few years now, I have learned a lot
about how to write nice, readable and correctly working Python programs. I am
by no means a Python guru, just somebody who likes to share lessons learned. 
If you see some solutions that can be improved, feel free to make a PR!

## Goal: show off the stdlib
Python has many useful builtin features or functions that can be used to 
solve problems as stated in "Advent of Code". I hope to highlight these 
features by solving the problems and hope this encourages people to read the
Python documentation more when they are trying to tackle a problem.

## Goal: provide functional programming examples
The programs follow the functional programming paradigm as much as possible.
The functions should return the same output when given the same arguments. 
There is no internal "state" to take into account. This simplifies testing and
code maintenance.

## Goal: provide examples for testing
All programs are tested using [pytest](https://docs.pytest.org/en/latest/). 
This ensures that they work before the solution is submitted. It also shows
new users how to write a few simple tests.
