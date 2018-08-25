def findeth(a):
    #find the smallest & bigget elements
    j = a.index(max(a))
    i = a.index(min(a))
    return a[j] - a[i]


print("  should expect 2:",findeth([1, 2, 3]))
print("  should expect 99:", findeth([1, 2, 3, 4, 100]))
print("  should expect 50:", findeth([1, 2, 3, 40, 0, 50]))
print("  should expect 2:", findeth([1, 2, 3]))