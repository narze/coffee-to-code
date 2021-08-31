caffine=data.split(sep="coffee")
c2c=str()
for code in caffine:
    if code!=caffine[-1]:
        c2c+=code+"Code"
    else:
        c2c+=code
