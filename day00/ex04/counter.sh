#!/bin/sh

echo '"name","count"' > hh_uniq_positions.csv
cat ../ex03/hh_positions.csv | cut -d ',' -f 3 | sort | uniq -c | awk '{print $2","$1}' >> hh_uniq_positions.csv

