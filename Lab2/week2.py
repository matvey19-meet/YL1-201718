numlist1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numlist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def exercise3():
	ex3list=[]
	for index in range(len(numlist1)):
 		for index in range(len(numlist2)):
 			if(numlist1==numlist2):
 				ex3list.append(index)
	return(ex3list)
print(exercise3())
