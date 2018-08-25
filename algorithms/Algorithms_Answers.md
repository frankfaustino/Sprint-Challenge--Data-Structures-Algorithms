Add your answers to the Algorithms exercises here.

## Excercise 1
    a.  O(n) runtime as loop grows only as n grows
    b.  O(log n) runtime as loop is being reduced by half every iteration
    c.  O(n^2) runtime even though it's a triple nested loop the outer loop is reducing itself
    d.  O(n log n) runtime as outside loop is reducing the amount of times it runs by doubling i
    e.  O(n^3) the first 3 loops are O(n) and 4th loop is O(1)
    f.  O(n)
    g.  O(n)

## Excercise 2
    a.
        def find_max(a):
            vals = []
            for i, _ in enumerate(a):
                j = i + 1
                if a[j] and a[j] > a[i]:
                    vals.append(a[j] - a[i])
            return max(vals)

    b. Find the median (m) floor between 0 and n and drop egg from there
        If egg breaks:
            Find median between 0 and m
            repeat process until egg does not break

        Else if egg doesnt break:
            Find median between m and n
            repeat until egg does break and f = m -1


## Exercise 3
    a. O(n^2) One recurse call will be repeated more than the other
    b. O(n log n) ? As its recursive calls are being evenly split
