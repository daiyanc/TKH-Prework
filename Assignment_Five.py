names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
even_list = []
odd_list = []
for name in names_list:
  if len(name) % 2 == 0:
    even_list.append(name)
  else:
    odd_list.append(name)
print_even_list = []
print_odd_list = []
for name in even_list:
  name = 'c' + name[1:len(name)]
  print_even_list.append(name)
for name in odd_list:
  name = name[0:len(name) - 1] + 'b'
  print_odd_list.append(name)
print (print_even_list)
print (print_odd_list)