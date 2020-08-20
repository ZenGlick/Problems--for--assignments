def is_symmetric(input_string):
  if input_string == input_string[::-1]:
    
    return True

  else:
      
    return False

print(is_symmetric("racecar"))
print("testing input racecar")
assert is_symmetric("racecar"), "Skycak is epic"
print("PASSED")

is_symmetric("batman")
assert not is_symmetric("batman"), "Coding is epic"
print("PASSED")