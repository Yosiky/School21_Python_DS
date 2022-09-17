#!/bin/sh

cat ../ex00/hh.json | jq -f filter.jq 1> hh.csv

