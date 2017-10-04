import os
import csv
import filecmp
from operator import itemgetter
#Adam Benson


def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	f = open(file, newline='')
	a = f.readlines()
	dlist = []
	for line in a[1:]:
		x = line.split(',')
		d = {}
		d["First"] = x[0]
		d["Last"] = x[1]
		d["Email"] = x[2]
		d["Class"] = x[3]
		d["DOB"] = x[4]
		dlist.append(d)
	return dlist

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	x = sorted(data, key=itemgetter(col))
	y = x[0]
	if col == 'Last':
		return y['First'] + " " + y[col]
	elif col == 'First':
		return y[col] + " " + y['Last']
	elif col == 'Email':
		return y['First'] + " " + y['Last']


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0
	for row in data:
		if row['Class'] == 'Freshman':
			freshman += 1
		elif row['Class'] == 'Sophomore':
			sophomore += 1
		elif row['Class'] == 'Junior':
			junior += 1
		elif row['Class'] == 'Senior':
			senior +=1 
		else:
			pass
		#print("No Grade Entered")
	#print(row)
	grades = [('Freshman', freshman), ('Sophomore', sophomore), ('Junior', junior), ("Senior", senior)]
	ordered = sorted(grades, key=lambda x: x[1], reverse=True)
	return(ordered)



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_count = {}
	for day in a:
		bd = day['DOB']
		day = bd.split('/')
		x = day[1]
		if x not in day_count:
			day_count[x] = 1
		else:
			day_count[x] += 1
	day_lst = []
	for key in day_count.keys():
		day_tup = (key, day_count[key])
		day_lst.append(day_tup)
	sorted_lst = sorted(day_lst, key = lambda x: x[1], reverse = True)
	return int(sorted_lst[0][0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	agedic = {}
	current = 2017
	totalage = 0
	numpeople = 0
	for line in a:
		x = line['DOB']
		o = x.split('/')
		p = o[2][:4]
		#print(int(p))
		totalage += int(p)
		numpeople += 1
	#print(totalage)
	#print(numpeople)

	mean = totalage / numpeople
	average = 2017 - mean
	return int(average)


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	data = sorted(a, key = lambda x: x[col])
	new = open(fileName, 'w')
	for t in data:
		new.write('{},{},{}\n'.format(t['First'], t['Last'], t['Email']))
	new.close()


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

