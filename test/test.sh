#!/bin/sh

set -e

_app() {
	python3 ../csvrewrite.py "$@"
}

# diff configured such that its only looking for meaningful differences between
# CSV files
_diff() {
	diff --strip-trailing-cr "$@"
}

# test: empty input results in empty output
printf '' | _app > "output/empty_out.txt"
touch "output/empty_real.txt" # create an empty file
_diff "output/empty_out.txt" "output/empty_real.txt"

# test: rainbow.csv -> rainbow.csv (no meaningful changes to data or format)
_app -i "rainbow.csv" -o "output/rainbow.csv"
_diff "rainbow.csv" "output/rainbow.csv"

# repeat above test but using stdin and stdout
_app < "rainbow.csv" > "output/rainbow.csv"
_diff "rainbow.csv" "output/rainbow.csv"

# test: rainbow.csv -> rainbow.tsv
_app -i "rainbow.csv" -o "output/rainbow.tsv" --od '\t'
_diff "rainbow.tsv" "output/rainbow.tsv"

# test: rainbow.tsv -> rainbow.csv
_app -i "rainbow.tsv" -o "output/rainbow.csv" --id '\t' --od ','
_diff "rainbow.csv" "output/rainbow.csv"

# test: rainbow.tsv -> rainbow.csv
_app -i "rainbow.tsv" -o "output/rainbow.csv" --id '\t' --od ','
_diff "rainbow.csv" "output/rainbow.csv"

# test: rainbow.tsv -> rainbow.csv (via excel dialect)
_app -i "rainbow.tsv" -o "output/rainbow.csv" --il 'excel-tab' --ol 'excel'
_diff "rainbow.csv" "output/rainbow.csv"

# test: rainbow.csv -> rainbow.tsv (via excel dialect)
_app -i "rainbow.csv" -o "output/rainbow.tsv" --il 'excel' --ol 'excel-tab'
_diff "rainbow.tsv" "output/rainbow.tsv"

