# Number of Even in list

list = []
lis_len = int(input("Total element you want in the list : "))

for i in range(0,lis_len):
		if i == 0:
			lis_element = int(input("Pass a element: "))
			
		else:
			lis_element = int(input("Pass another element: "))

		list.append(lis_element)


ev,od = 0,0

for e in list:
    if e%2 == 0:
        ev+=1
    else:
        od+=1

print(f"In list {list} : ")
print(f"Total even numbers are {ev}, total odd numbers are {od}")
