ToDo_list = []
Done_list = []
flag=True
while flag:
	print("|***********************************************|")
	print("| To Add New Item Press 1                       |")
	print("| To Print the To Do list Press 2               |")
	print("| To Mark an item as Done Press 3               |")
	print("| To Print the done list press 4                |")
	print("| exist press 5                                 |")
	print("|***********************************************|")
	
	choice = input("Please enter your choice: ")
	if int(choice) == 1:
		Item = input("Please write the item to Add: ")
		ToDo_list.append(Item)
	
	elif int(choice) == 2:
		if len(ToDo_list) > 0:
			i = 0
			while i < len(ToDo_list):
				print(str(i+1) + '-' + str(ToDo_list[i]))
				i+=1
		else:
			print("To Do list is empty")
	
	
	elif int(choice) == 3:
		Item = input("Please Enter the number of item: ")
		Item = int(Item) - 1
		if Item < len(ToDo_list):
			Done_list.append(ToDo_list.pop(Item))
			print("Item moved to done list correctly")
		else:
			print("Selected Item not exist")
	
	elif int(choice) == 4:
		if len(Done_list) > 0:
			i = 0
			while i < len(Done_list):
				print(str(i+1) + '-' + str(Done_list[i]))
				i+=1
			
	elif int(choice) == 5:  
		print("Thank you for using the To-Do List Application. Goodbye!")
		flag=False  
	else:
		print("Wrong Choice, Please try again later")
