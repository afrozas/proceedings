#!/bin/bash
IFS='
'
for d in ` ls -d "$PWD"/*/` ; do
    echo "$d"
    source /media/enigmaeth/My\ Passport/eniext/code/experimental/proceedings/.env/bin/activate
    python3 /media/enigmaeth/My\ Passport/eniext/code/experimental/proceedings/src/run.py $d 
done