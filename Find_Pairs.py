a = [3, 4, 1, 7, 9, 17]
x = 8

def Find_Pairs(a, x):
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] + a[j] == x:
            return (i, j)
        if a[i] + a[j] < x:
            i += 1
        else:
            j -= 1
    return None


print(Find_Pairs(x, 8))

#I'm sorry this is not complete. I promise I did my best and I smiled at the computer. 
