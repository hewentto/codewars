/*An isogram is a word that has no 
repeating letters, consecutive or 
non-consecutive. Implement a 
function that determines whether 
a string that contains only letters 
is an isogram. Assume the empty string 
is an isogram. Ignore letter case.*/

def is_isogram(string):
  lowercase = string.lower()
  counter = 0
  checker = ""
  for letter in lowercase:
    if letter not in checker:
      checker += letter
  if len(checker) < len(lowercase):
    return False
  else:
    return True
