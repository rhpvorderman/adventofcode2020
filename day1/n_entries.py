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
This program tries to solve the problem to find N entries in a list of
numbers that add up to a desired outcome
"""
import argparse
import itertools
import math
from typing import Generator, Iterable


def file_to_integers(path) -> Generator[int, None, None]:
    """
    Converts a file that contains a list of integers to a generator that
    yields these integers.
    """
    with open(path, "rt") as file_handler:
        for line in file_handler:
            yield int(line.strip())


def find_n_numbers_that_add_to(numbers: Iterable[int],
                               n: int,
                               desired_outcome: int) -> Iterable[int]:
    """Finds a combination of n nunbers in a list (or other iterable) of
    numbers that add up to the desired outcome. Returns the numbers."""
    # Coming up with an algorithm that returns all possible combinations of n
    # in a list of numbers is fun, but not necessary as this is already
    # provided in the itertools module of the standard library.
    for number_combination in itertools.combinations(numbers, n):
        if sum(number_combination) == desired_outcome:
            return number_combination
    raise ValueError(f"No {n} numbers add up to {desired_outcome} in this "
                     f"list.")


def main():
    parser = argparse.ArgumentParser(
        description="Search a list for two numbers that add up to the "
                    "desired outcome. Returns the numbers and their product.")
    parser.add_argument("N", type=int,
                        help="The amount of numbers that should add to "
                             "the desired outcome.")
    parser.add_argument("desired_outcome", type=int,
                        help="The number that two numbers should add up to.")
    parser.add_argument("number_list", type=str,
                        help="The file with a list of numbers to use. Each "
                             "number should be on its own line.")
    args = parser.parse_args()
    correct_numbers = find_n_numbers_that_add_to(
        file_to_integers(args.number_list),
        args.N,
        args.desired_outcome)
    print(f"The numbers are {', '.join(str(n) for n in correct_numbers)}")
    # The product can be calculated with the math library since python 3.8.
    print(f"The product of these numbers is: "
          f"{math.prod(correct_numbers)}")


if __name__ == "__main__":
    main()