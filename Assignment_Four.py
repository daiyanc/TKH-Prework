names_list = []
username = input("Please enter a name. Enter 0 to exit. ")
while username != "0":
  names_list.append(username)
  username = input("Please enter another name. Enter 0 to exit. ")
print(names_list)
