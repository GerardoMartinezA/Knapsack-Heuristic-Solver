from io import open
import random
from operator import itemgetter,attrgetter
import time
import sys

items = []
item = []

def get_data(text):  
	try:
		cast = int(input(text + " > "))  
	except ValueError:
		print("\nOnly integer values allowed")  
		sys.exit()
	return cast

def writes_result(file_name,objective_f,heuristic):
	file = open(file_name,'a')
	file.write("\n--------------------------------\n"
		+"Heuristic #"+str(heuristic)+"\n"
		+"k = "+str(objective_f))
	file.close()

start_time = time.time() #Start the timer
def objective_f(w,items,n):  
        elements = set()  
        current_w = w  
        k = 0 # Initialize k to work
        for i in range(0,n):
            if(items[i][2]<=current_w): # If Wi fits on the backpack, puts item
                k += items[i][1]  
                current_w -= items[i][2] # Current capacity of the backpack updates
                elements.add(items[i][0])  
            if(current_w==0): 
                break;
        print("\nThe Objective Function = "+str(k)+"\n\n\n") # Prints the final gain
        print("\nRUNNING TIME: --- %s seconds ---" % (time.time() - start_time)) # Prints Running time
        return k


def calculate_b(items_sort,n):
	aux_items_sort = []  
	for i in range(0,n):
		bi = items_sort[i][1] / items_sort[i][2]  
		aux_items_sort.append([(i+1),bi,items_sort[i][1],items_sort[i][2]])
 
	aux_items_sort.sort(key=itemgetter(1),reverse=True)  
	for i in range(0,n):
		del aux_items_sort[i][1] 
 
	return aux_items_sort

def read_instance(data):
	with open(data,'r') as file: # Reading the instance and making validations
		i = 0
		for line in file:
			try:
				if((int(line.split()[0]))>0 and (int(line.split()[1]))>0): # Validates if values are positive and > 0
					item = [i,int(line.split()[0]),int(line.split()[1])]	
					items.append(item)

					i+=1
				else:
					print("\nYou can´t give me negative values, please correct the values of "
						+str(data)) # Stops the program if negative values
					sys.exit()

			except ValueError: # Validates if values are integer
				print("\nPlease, correct the values of "+str(data)+" , characters and not "
					"integer values are not allowed")
				sys.exit()

	itemsAmount = items[0][1] # Reads the number of items
	knapsackCapacity = items[0][2] # Reads the knapsack capacity
	del items[0]
	return items,itemsAmount,knapsackCapacity 

def copy(value):
	reseted = None
	reseted = value[:]
	return reseted


def menu(w,n,items):
	while True:
		items_sort = copy(items)
		option = input("\nSelect an heuristic: "
		"\n1. Heuristic A "
	 	"\n2. Heuristic B"
	 	"\n3. Heuristic C" 
		"\n4. Exit"
		"\n\n Solve with (Type 1, 2 or 3):  ")
		if option == "1":
			print("\nHEURISTIC A\n")
			items_sort.sort(key=itemgetter(1),reverse=True) # Sort by higher Vi
			k = objective_f(w,items_sort,n) 


		elif option == "2":
			print("\nHEURISTIC B\n")
			items_sort.sort(key=itemgetter(2)) # Sort [items_sort] by higher Wi
			k = objective_f(w,items_sort,n)  


		elif option == "3":
			print("\nHEURISTIC C\n")
			items_sort = calculate_b(items_sort,n) # Returns [items_sort] a sorted array by higher bi
			k = objective_f(w,items_sort,n)  


		elif option == "4":
			
			break;
		else:
			print("Please type a number from 1 to 3")
        


def generate_instace(items,capacity,min_capacity,max_capacity,min_value,max_value): #Function that create instance
	file.write(str(itemsAmount)+"\t"+str(capacity)+"\n") 
	for i in range(0,itemsAmount): #Bucle for random numbers
		for j in range(0,2):
			if(j==0):
				value = str(random.randint(min_value+1,max_value+1)) 
			else:
				value = str(random.randint(min_capacity,max_capacity)) 
			file.write(value+str("\t")) #Write in file the generated numbers
		file.write("\n")

print("Fill the values") #Gets the intervals for the random numbers
minValue = get_data("\nMinimum Value")
maxValue = get_data("\nMaximum Value")
minWeight = get_data("\nMinimum Weight")
maxWeight = get_data("\nMaximum Weight")



if(minWeight>=maxWeight): #Validate that the intervals arent wrong
	print("\nPlease correct the intervals minimum weight can´t be >= than maximum weight.")
	sys.exit()

itemsAmount = get_data("\nNumber of items") # Gets the number of items for the instances (itemsAmount)
m = get_data("\n Number of instances") # Gets the number of instances to create (m)
knapsackCapacity = int((((float(minWeight)+float(maxWeight))/2.0)*float(itemsAmount)*0.3)) # Calculates the capacity (knapsackCapacity)

print("\nKnapsack Capacity = "+str(knapsackCapacity))
start_time = time.time() #Start the timer
for i in range(0,m): 
	items.clear() 
	file = open("instance"+str(i+1)+".txt",'w') 
	generate_instace(itemsAmount,knapsackCapacity,minWeight,maxWeight,minValue,maxValue) 
	file.close() #

print("\nRUNNING TIME: --- %s seconds ---" % (time.time() - start_time)) #Running time

