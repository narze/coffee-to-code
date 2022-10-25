def Conversion_4_Hacktober(wordy):
    coffee = wordy.lower()
    results = coffee.replace('ff', 'd', 1)
    final=results[:-1]
    return final.upper()
    

    
ans = Conversion_4_Hacktober("COFFEE")
print(ans)