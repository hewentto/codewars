//Calculate the average of given list of numbers


#include <stdio.h>
#include <string.h>
double find_average(double* array, int length) {
  double sum = 0;
  for(int i = 0; i < length; i++)
  {
    sum += array[i];
  }
  return sum / length;
  printf("%f", sum);
}