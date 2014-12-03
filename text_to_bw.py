# Copyright (C) 2014  Ken Reese
#
#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License along
#     with this program; if not, write to the Free Software Foundation, Inc.,
#     51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import sys
from subprocess import call

def read_input_suffix_array(filename):
    with open(filename) as f:
        return map(int, f.readline().strip().split(' '))


def read_input_text(filename):
    with open(filename) as f:
        return f.readline().strip()


def construct_bw_transform(suffix_array, text):
    for i in suffix_array:
        sys.stdout.write(text[(i + len(text) - 1) % len(text)])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "USAGE: python text_to_bw.py [Text] [Suffix Array] > [output]"
        print "\t\tOR\t\t"
        print "USAGE: python text_to_bw.py [Text] > [output]"
        sys.exit(0)

    if len(sys.argv) == 2:
        call(["./radixSA", sys.argv[1], "suffix_array.txt"])

    print

    sys.argv.append("suffix_array.txt")

    text = read_input_text(sys.argv[1])
    suffix_array = read_input_suffix_array(sys.argv[2])
    construct_bw_transform(suffix_array, text)

    print

