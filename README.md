# PyCSVRewrite

PyCSVRewrite is a Python 3 script that will rewrite a CSV (or similar) file under a new dialect and delimiter.

This script can be used to convert a CSV file to a TSV file, among other conversions.

## Usage

Check the script's version:

```
$ python3 csvrewrite.py --version
```

Convert a CSV file to a TSV file:

```
$ python3 csvrewrite.py --input-delimiter ',' --output-delimiter '\t' -i "input.csv" -o "output.tsv"
```

List available dialects:

```
$ python3 csvrewrite.py --dialects
```

Convert a CSV file from one dialect to another (reading from stdin and writing to stdout):

```
$ python3 csvrewrite.py --input-dialect 'excel' --output-dialect 'excel-tab'
```

For all potential options, use `--help`.

## Testing

See the `test` directory and the `test.sh` script within.

More robust testing is welcome.

