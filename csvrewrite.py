#!/usr/bin/python3

#
# PyCSVRewrite (c) 2023 Benjamin Hottell
#
# Rewrites CSV files under different dialects and/or with different delimiters.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import csv
import argparse

VERSION='1.0.1'

def csv_args_dict(
        delim=None,
        dialect=None):

    ret = {}

    if delim is not None:
        ret['delimiter'] = delim

    if dialect is not None:
        ret['dialect'] = dialect

    return ret


def read_file_or_stdin(path):
    if path is None:
        return sys.stdin
    return open(path, 'r')


def write_file_or_stdout(path):
    if path is None:
        return sys.stdout
    return open(path, 'w')


# an exception to represent that the user gave us bad arguments
class UserException(Exception):
    pass

# delimiter must be a 1-character string, but the user may have provided
# something like \t which is a two-character string. so, let's intercept
# two-character strings and 'unescape' them.

SPECIAL_DELIMITERS = {
    '\\t': '\t',
    '\\0': '\0',
}

def get_delimiter(delim):
    if delim is None:
        return None

    if delim in SPECIAL_DELIMITERS:
        delim = SPECIAL_DELIMITERS[delim]

    if len(delim) != 1:
        specials = ', '.join(SPECIAL_DELIMITERS.keys())
        raise UserException(
            f"Delimiter must be a 1-character string, or one of: {specials}")

    return delim

def get_dialect(dialect):
    if dialect is None:
        return None

    if not dialect in csv.list_dialects():
        raise UserException('No such dialect: ' + dialect)

    return dialect


# see #main() below
def main_no_catch():
    argp = argparse.ArgumentParser(
        prog='csvrewrite',
        description='Rewrites CSV (or similar) files under different dialects and delimiters.')

    argp.add_argument(
        '--version',
        action='store_true', default=False,
        help='print the version and exit')

    argp.add_argument(
        '--input', '-i',
        help='file to read from (if not specified, read from stdin)')

    argp.add_argument(
        '--output', '-o',
        help='file to write to (if not specified, read from stdout)')

    argp.add_argument(
        '--input-delimiter', '--id',
        help='specify the delimiter of the input file (optional)')

    argp.add_argument(
        '--output-delimiter', '--od',
        help='specify the delimiter of the output file (optional)')

    argp.add_argument(
        '--dialects',
        action='store_true', default=False,
        help='list available dialects and exit (see --input-dialect and --output-dialect)')

    argp.add_argument(
        '--input-dialect', '--il',
        help='specify the CSV dialect of the input file (optional)')

    argp.add_argument(
        '--output-dialect', '--ol',
        help='specify the CSV dialect of the output file (optional)')

    args = argp.parse_args()

    if args.version:
        print(VERSION)
        return 0

    if args.dialects:
        for d in csv.list_dialects():
            print(d)
        return 0

    input_delim = get_delimiter(args.input_delimiter)
    output_delim = get_delimiter(args.output_delimiter)

    input_dialect = get_dialect(args.input_dialect)
    output_dialect = get_dialect(args.output_dialect)

    with read_file_or_stdin(args.input) as in_file:
        with write_file_or_stdout(args.output) as out_file:

            csvreader = csv.reader(
                in_file,
                **csv_args_dict(
                    delim=input_delim,
                    dialect=args.input_dialect))

            csvwriter = csv.writer(
                out_file,
                **csv_args_dict(
                    delim=output_delim,
                    dialect=args.output_dialect))

            for row in csvreader:
                csvwriter.writerow(row)

    return 0


# wrappers may be interested in intercepting exceptions emitted by main and
# calling sys.exit on their own terms. these wrappers should call
# #main_no_catch()
def main():
    try:
        sys.exit(main_no_catch())
    except KeyboardInterrupt as e:
        sys.exit(1)
    except UserException as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

