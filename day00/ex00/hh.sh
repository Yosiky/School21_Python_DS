#!/bin/shell

vacancy=$(echo $1 | sed 's/ /%20/g')
echo $vacancy
curl -k -H 'User-Agent: api-test-agent' "https://api.hh.ru/vacancies?text=$vacancy" 1> hh_copy.json
cat hh_copy.json | jq '.' 1> hh.json
rm hh_copy.json
