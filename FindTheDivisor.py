/*Create a function named divisors/Divisors 
that takes an integer and returns an array 
with all of the integer's divisors(except 
for 1 and the number itself). If the number 
is prime return the string '(integer) is 
prime' (null in C#) (use Either String a in 
Haskell and Result<Vec<u32>, String> in Rust).*/


def divisors(integer):

  answer = []
  for i in range(2, integer):
    if integer % i == 0:
      answer.append(i)
  if len(answer) < 1:
    answer = str(integer) + " is prime"
  return answer