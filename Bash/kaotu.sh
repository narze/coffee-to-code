#!/bin/bash

COFFEE_WORD=$1
CODE_WORD='Code'

if [ -z "$COFFEE_WORD" ]; then
    echo "Coffee word require"
    exit 1;
fi

result=$(echo "$COFFEE_WORD" | tr '[:upper:]' '[:lower:]' | sed "s/coffee/$CODE_WORD/")
echo $result