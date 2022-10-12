#!/bin/bash
echo 'Hi, This bash for convert string [coffee] to [code]'
read -p "Plese, type only coffee !: " VAR1
mug='coffee'

if [[ "$VAR1" == "$mug" ]]; then
    echo "code"
else
    echo "hmm!,Only typing coffee"
fi
