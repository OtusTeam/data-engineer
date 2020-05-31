#!/bin/bash

HEADER="Content-Type: application/json"
DATA=$( cat << EOF
{
    "settings": {
        "number_of_shards": 1
    },
    "mappings": {
        "wikichange_short": {
            "properties": {
                "CREATEDAT": {
                    "type": "date"
                },
                "WIKIPAGE": {
                    "type": "keyword",
                    "index": "no"
                },
                "USERNAME": {
                    "type": "keyword"
                },
                "DIFFURL": {
                    "type": "text",
                    "index": "no"
                }
            }
        }
    }
}

EOF);

curl -XPUT -H "${HEADER}" --data "${DATA}" 'http://localhost:9200/wikilang?pretty'
echo