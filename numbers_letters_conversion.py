letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def letters_to_numbers(input_string):
  input_list = list(input_string)
  second_list = []
  for letter in input_list:
    second_list.append(letters.index(letter))
  return second_list
print(letters_to_numbers("a taco cat"))
print("testing that letters_to_numbers works on 'a taco cat' ")
assert letters_to_numbers("a taco cat") == [1, 0, 20, 1, 3, 15, 0, 3, 1, 20], "Idk lol"
print("PASSED")