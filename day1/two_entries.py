#!/usr/bin/python3

# Copyright (c) 2020 Ruben Vorderman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This program tries to solve the problem to find two entries in a list of
numbers that add up to 2020
"""
import argparse
import itertools
from typing import Generator, Iterable, Tuple


def file_to_integers(path) -> Generator[int, None, None]:
    """
    Converts a file that contains a list of integers to a generator that
    yields these integers.
    """
    with open(path, "rt") as file_handler:
        for line in file_handler:
            yield int(line.strip())


def find_two_numbers_that_add_to(numbers: Iterable[int],
                                 desired_outcome: int) -> Tuple[int, int]:
    """Finds two numbers in a list (or other iterable) of numbers that
    add up to the desired outcome. Returns the two numbers."""
    # Coming up with an algorithm that returns all possible combinations of 2
    # in a list of numbers is fun, but not necessary as this is already
    # provided in the itertools module of the standard library.
    for left, right in itertools.combinations(numbers, 2):
        if left + right == desired_outcome:
            return left, right
    raise ValueError(f"No numbers add up to {desired_outcome} in this list.")


def main():
    parser = argparse.ArgumentParser(
        description="Search a list for two numbers that add up to the "
                    "desired outcome. Returns the numbers and the result of"
                    "the multiplication.")
    parser.add_argument("desired_outcome", type=int,
                        help="The number that two numbers should add up to.")
    parser.add_argument("number_list", type=str,
                        help="The file with a list of numbers to use. Each"
                             "number should be on its own line.")
    args = parser.parse_args()
    left, right = find_two_numbers_that_add_to(
        file_to_integers(args.number_list),
        args.desired_outcome)
    print(f"The two numbers are {left} and {right}")
    print(f"The product of these numbers is: {left * right}")
