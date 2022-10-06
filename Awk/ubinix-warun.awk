#!/usr/bin/awk -f
{ sub(/Coffee/,"Code"); sub(/coffee/,"code"); sub(/COFFEE/,"CODE"); print }

# echo "I 🧡 Coffee"  | awk -E ./ubinix-warun.awk 
# echo "I 🧡 coffee"  | awk -E ./ubinix-warun.awk
# echo "I 🧡 COFFEE"  | awk -E ./ubinix-warun.awk
