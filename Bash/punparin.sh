#!/bin/bash

if echo $1 | grep -Eqi "^coffee$"; then
    echo "Code"
fi;
