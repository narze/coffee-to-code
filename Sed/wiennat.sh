#!/bin/sh
export O="I <3 coffee"

# case sensitive
echo "case sensitive"
echo "before: $O"
echo ">> $O" | sed "s/coffee/code/"
echo ">> $O" | sed "s/Coffee/code/"
echo

# case insensitive
echo "case insensitive"
echo "before: $O"
echo ">> $O" | sed "s/coffee/code/"
echo ">> $O" | sed "s/Coffee/code/i"
echo

# replace global 
echo "replace global"
echo "before: $O $O"
echo ">> $O $O" | sed "s/coffee/code/"
echo ">> $O $O" | sed "s/coffee/code/g"
echo

