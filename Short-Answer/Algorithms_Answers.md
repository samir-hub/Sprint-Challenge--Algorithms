#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The time complexity is O(n) because the number of times that the loop will run is proportional to n. 


b) The time complexity is O(n^2). For n=1, it runs 0 times. For n=5, it runs 15 times. For n=10, it runs 40 times and for n=20, it runs 100 times. This is clearly exponential. 


c) The time complexity is O(n) because the function will get called approximately n times. 

## Exercise II

One solution is to drop eggs starting in the first floor and keep going upstairs until the egg breaks. This would be very inefficient. The best solution would be to start at n/2 and see if the egg breaks. If it breaks, try n/4 and so on. This is like a binary search. The time complexity is O(log(n))
