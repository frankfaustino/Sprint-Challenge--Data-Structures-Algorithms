Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

    * It would be O(n), just like BFS it will always search O(n-1) (subtracting each node as it goes since it is already searched) with a total of O(n) because it still has to go the length of the tree.

2. What is the space complexity of your `depth_first_for_each` function?
    
    * In my case since I used recursion, it would be worse case scanario of O(h), where h is the height of the tree. It will be the height of the tree because if a left child has many other trees that have children, my recursion call will have to traverse (and add up the system stack) untill it can traverse no more.

3. What is the runtime complexity of your `breadth_first_for_each` method?

    * I would guess it is linear O(n) because you will be searching every node once. And for the same explanation given in DFS above ^^^

4. What is the space complexity of your `breadth_first_for_each` method?

    * It would be linear O(n), since you will at worse, (in my case) have a "visited" array that stores all the elements of the tree that you hold. Otherwise it would probably be constant O(1) since you just pop the value, check if left, right, then append/ queue it back. Or just leave it popped/ dequeed.

5. What is the runtime complexity of your `heapsort` function?
    
    * If implemented and optimized to the best of it's abilities, it will be O(n log n), mostly because when you heapsort you sort of partition a segment, and it will have to iterate that segment, and sort it, which is N. But since it is sorted by segments, you will only sort each segment first so log n. Therefore it will be (n log n). n for linear search/ sort of partitioned data, and the partitioning itself of a larger data is log n.

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

    * Since I am creating a new heap and putting that sorted heap into a new array it will probably be O(1), it will take up the exact amount of data that was given to it. Large data? Large storage. Small data? Small storage. And since I return a new one, it is probably doubled. One for original heap, and another for sorted heap. But still constant though since double of 1 is still 1.