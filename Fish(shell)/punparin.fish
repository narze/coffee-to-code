#!/bin/fish

if string match -q -- $argv[1] coffee Coffee
    echo "Code"
end
