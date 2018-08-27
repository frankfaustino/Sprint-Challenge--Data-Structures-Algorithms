Add your answers to the Algorithms exercises here.
Exercise 1
a - I think this is an example of linear time complexity (O(n)). While you're doing a lot of math, you're not doing anything n-times.
b -  This is an example of logarithmic, O(log n). I think this is the case because with each iteration, the data set becomes smaller by half.
c - I think this algorithm is quadradic, O(n^2). This time complexity is common with nested loops.
d - quasilinear, O(n log n) since i grows with each round of the loop
e - quadradic O(n ^ 3)
f - bunnyEars is linear time complexity, O(n).  
g - search is linear, O(n)

Exercise 2

Exercise 3
a - 
b - I feel like this could be figuered out using a binary search technique.  
n = floors
f-1 = safe_floor
start at n/2:
    floor = n/2
    egg breaks:
        floor / 2
        repeat until it doesn't break and fine tune
    egg doesn't break:
        n - floor / 2
        repeat until it breaks and fine tune

        

