1. Interpolation search starts at a point where the key is more likely to occur making it possibly faster. More efficient than binary when the data is uniformly distributed.

2. The search performance will be negatively effected because if there are some numbers that are more likely than others, it makes the estimate of where to start the search inaccurate and will make it take more time.

3. The code to get the position. You would need to change it to fit the distribution you want so it starts at an accurate estimate.

4. When the data is unordered. 

5. Linear search performs better when working with small data sets. 

6. You could implement a function that checks the size of the data set before performing the search to use a linear search if it is smaller. Presorting the data would also help. 
