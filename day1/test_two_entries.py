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

import sys

from two_entries import file_to_integers, find_two_numbers_that_add_to, \
    main

EXAMPLE_FILE = "two_entries_example.txt"
EXAMPLE_NUMBERS= [1721, 979, 366, 299, 675, 1456]


def test_file_to_integers():
    assert list(file_to_integers(EXAMPLE_FILE)) == EXAMPLE_NUMBERS


def test_find_two_numbers_that_add_to():
    assert find_two_numbers_that_add_to(EXAMPLE_NUMBERS, 2020) == (1721, 299)


def test_main(capsys):
    sys.argv = ["", "2020", EXAMPLE_FILE]
    main()
    assert "The product of these numbers is: 514579" in capsys.readouterr().out
