Add your answers to the Algorithms exercises here.

#Excercise I.

a.) Linear? The bigger n is, the bigger the loop grows. ```n*n*n``` is still n runtime.

b.) log n. i is being split in half, then looping back through to check a value that is plit in 
half; only to be split in half again.

c.) First for loop would be log n/ 2, but then second is n, and 3rd is n. Time is as big as the biggest runtime so it would probably be ```n**2/ n ^ 2```.

d.) Outside for loop is ```i < n``` but ```i*=2``` so I will double itself which means it gets to n, faster. Which would be log n. Nest for loop is n. So in total, ```n log n```?

e.) First loop is n, second loop is n, 3rd loop is n, 4th loop is n or constant to 10?
I guess it would be 3 ^ n if its constant, or 4 ^ n.

f.) Linear, mostly because of ```bunnies - 1``` 2 + before hand doesnt really add. It's a constant on a linear upscale.

g.) Looks linear, if arraysize is bigger go through ```array[arraysize -1]``` which means, counts down the array.

#Excercise II.

a.)
```
    def max_value(n):
    stored_value = []
        for i in n:
            j += i
            if a[j] and a[j] > a[i]
                return max(stored_value.append(a[j] - a[i]))
```

b.)
```
    def breaking_eggs(f):
        if egg_broken:
            from ground level to that f, and call recursively until it doesnt break

        elif egg_not_broken:
            find from point of where egg did not break, until it does break.
```

#Excercise III.

a.) If the array is already sorted, it would most likely only run a max of twice, but twice to check both sides of the pivot. Since you call it recursively, it would check/ sort things less than the pivtot, call recursively, then check/ sort things greater than the pivot. So O(n^2)

b.) That wouldn't matter, since you are calling it recursively, you still have an exisisting sort, to be sorted.
