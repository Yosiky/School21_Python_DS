#!/bin/sh

vacancy=$(echo $1 | sed 's/ /%20/g')
echo "You want to search : $vacancy"
echo
curl  "https://api.hh.ru/vacancies?text=$vacancy&page=0&per_page=20" 1> hh_copy.json
cat hh_copy.json | jq '.' 1> hh.json
rm hh_copy.json
