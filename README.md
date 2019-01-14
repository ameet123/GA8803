### 6.19 Coin change with at most k coins
+ dynamic programming table will be a 1-dimensional table.
+ define the problem in words:
<br>Let I(i) = # of coins needed to make the change. The index of this array shall match the change being made. 
i.e. at index 4, the change being made is 4.
+ define recursion:<br>
Let I(b) = min { 1 + I(b - xi) }, b: 1->W, W = coin value being changed.
+ Constraints: <br>
I is updated only if, b = C(b), the change being made
+ how the table is filled out:<br>
The table is initialized to 0 and is filled out from left to right, starting with index 1. 
Iterating over the coin value, W, starting with 1, the table is filled out matching the value with the table index.
+ pseudocode:<br>
    0. Let B=x1, x2, ..., x<sub>n</sub> ; x<sub>i</sub> = coin of value x<sub>i</sub>, W = value to change using coins
    1. initialize C(i)=0 and I(i) = 0 for i:0 -> W  
    2. for b: 1&rarr; W
        3. for i: 0&rarr;B
            4. if x<sub>i</sub> &le; b and C(b) &le; x<sub>i</sub> + C(b - xi):<br>
                5. C(b) = x<sub>i</sub> + C(b - xi)
            6. if b == C(b):
                7. I(b) = min { 1+I(b-x<sub>i</sub>); I(b)}
    8. return I(B)
    
### 6.20 Optimal Binary Search Tree
#### Approach:
We start from the first word/node in lexicographically ascending order. For each index/node, the corresponding optimal
tree is stored in an array at the corresponding index. At each index/word, the tree at previous index is used as a 
starting point.<br>
The algorithm iterates over all the words from the first up to but not including the current index being explored. It
injects each of these words into the base tree from previous index starting fresh and then computes the cost of the new
tree thus generated. Of all such (i-1) trees, the one with minimum cost is selected and installed as the tree at index i.
<br> The algorithm actually iterates from -1 instead of 0, in order to enable the new node to be injected at the root
as well.<br>
In the actual implementation, the tree is constructed as a linked list of nodes with two instance variables, left and 
right.

+ dynamic programming table is a 1-D array of trees.
+ *define the problem in words*:
<br>Let T(i) = Optimal tree at index i, including the word at i.
+ *define recursion*:
<br> T(i) = T(i-1) + min{T(i-1) + j; 0<=j<i} , tree with minimum cost out of all trees with different positions for 
node i.
+ *how the table is filled out*:<br>
The 1-D array is initialized with the tree for the first node. The array is filled out from left to right, as the 
algorithm computes the optimal tree at each index.
+ *pseudocode*:<br>
```text
 1. Let f = { f<sub>1</sub>, f<sub>2</sub>, ..., f<sub>n</sub> } ,
                            frequencies of words in alphabetically ascending order. 
 2. Initialize 1-D array T(0) = tree(0), tree(0) is the tree with just the first word.
 3. for i: 1-> n, n = # of words
 4.     prev_tree = T(i-1)
 5.     cost = cost(prev_tree)
 6.     cur_tree = prev_tree
 7.     for j: -1 -> i
 8.         new_tree = inject node i into prev_tree at index j
 9.         new_cost = cost (new_tree) 
 10.         if new_cost < cost:
 11.            cost = new_cost
 12.            cur_tree = new_tree
 13.    T(i) = cur_tree
 14. return T(n)            
 ```
+ *running time*:<br>
inserting the node is `O(lg n)` and BFS to find the cost is `O(n)`
The total running time is,<br>
n * [ lg n + n ]<br>Simplifying, the total running time of the algorithm => 
**O(n<sup>2</sup>)**