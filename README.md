### 6.19 Coin change with at most k coins
dynamic programming table will be a 1-dimensional table.
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
  