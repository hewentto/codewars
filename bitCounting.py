/*Write a function that takes an (unsigned) 
integer as input, and returns the number 
of bits that are equal to one in the 
binary representation of that number.*/


def countBits(n):
  counter = 0
  for bit in bin(n):
    if bit == "1":
      counter +=1
  return counter