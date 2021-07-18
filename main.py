def get_middle_items_from_list(mylist):
	#check if the length of mylist is even or odd
	if len(mylist) % 2 != 0:
		return mylist[len(mylist) // 2]
	else:
		return mylist[(len(mylist)//2)-1 : (len(mylist)//2)+1]

#definition of two variables, one is the loop control and the other is the actual list
control = None
mylist = []

#the loop
while control != "stop":
	control = input("Insert an item: ")
	if control != "stop":
		mylist.append(control)

print(f"Your list is: {mylist}")
print(f"Your list has the item(s) {get_middle_items_from_list(mylist)} in the middle")