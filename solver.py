from io import open
import random
from iterations import *

if len(sys.argv)==2:
	file = sys.argv[1]
else:
	print("\nPlease type the name of the instance after 'solver.py' ")
	sys.exit()

items,itemsAmount,knapsackCapacity = read_instance(file)

menu(knapsackCapacity,itemsAmount,items)