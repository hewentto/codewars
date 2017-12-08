/*If we list all the natural numbers below 
10 that are multiples of 3 or 5, we get 3, 
5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the 
sum of all the multiples of 3 or 5 below the 
number passed in.*/

#include <stdio.h>
int solution(int number) {
  int sum = 0;
  int remainder3;
  int remainder5;
  for(int i = 1; i < number;)
  {
    remainder3 = i % 3;
    remainder5 = i % 5;
    //make sure if both is true it only counts it once
    if ( remainder3 ==0 && remainder5 == 0)
    {
      sum += i;
      i++;
     } 
    else if ( remainder3 == 0 || remainder5 ==0)
    {
      sum+= i;
      i++;
    }
    else
    {  
      i++;
    }
  }
  return sum;
}