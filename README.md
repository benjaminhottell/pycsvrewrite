# PyCSVRewrite

PyCSVRewrite is a Python 3 script that will rewrite a CSV (or similar) file under a new dialect and delimiter.

This script can be used to convert a CSV file to a TSV file, among other conversions.


## Installation

All you need to do is run `pip install .` inside of this directory.

Alternatively, you can invoke `csvrewrite.py` directly as it is a self-contained script.


## Usage

These usage examples assume that the `csvrewrite` script is available on your PATH. (See the installation section above)

Check the script's version:

```
$ csvrewrite --version
```

Convert a CSV file to a TSV file:

```
$ csvrewrite --input-delimiter ',' --output-delimiter '\t' -i "input.csv" -o "output.tsv"
```

List available dialects:

```
$ csvrewrite --dialects
```

Convert a CSV file from one dialect to another (reading from stdin and writing to stdout):

```
$ csvrewrite --input-dialect 'excel' --output-dialect 'excel-tab'
```

For all potential options, use `--help`.



## Testing

See the `test` directory and the `test.sh` script within.

More robust testing is welcome.

