Add your answers to the Algorithms exercises here.

a - O(n) - runs n times

b - O(logn) because you are finding the last item in the array, halfing its index value everytime. You reach a logarithmic time complexity

c - O(logn)^1/2)??

d - O(nlog*n) - it has a Logarithmic complexity at the first loop because the index is multiplied by 2, reaching it's limit n faster. The Inner loop is O(n)

**NOTE - whats the difference between  O(nlog*n) and  O(nlogn)???**

e - O(n^3 - 3 loops and 1 linear loop
f - O(n) - because it's linear recursive function
g - O(n)

II

a -
```python
def findeth(a):
    #find the smallest & bigget elements
    j = a.index(max(a))
    i = a.index(min(a))
    return a[j] - a[i]

print("should expect 2: ",findeth([1, 2, 3]))
print("should expect 99: ", findeth([1, 2, 3, 4, 100]))
print("should expect 50: ", findeth([1, 2, 3, 40, 0, 50]))
print("should expect 2: ", findeth([1, 2, 3]))   
```

b - I would make an O(logn) time complexity by going to the middle floor and dropping an egg. I would then adjust the height to the new midway point based on my findings.

III

a - O(n^2) - we are traversing the array with quicksort using the first element. We would have to compare that first element to it's neighbor (O(n)) and sort it. THen we would need to go back to the new first Index and compare that to it's neighbors and sort it as well. Don't do this.

b - O(logn - Similar to II.a above,c we are cutting the items we are sorting throgh in half making a log(n) curve 



