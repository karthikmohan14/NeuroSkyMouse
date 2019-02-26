# get data first as "__name__activity.csv" then create model based on it "__model__name.csv"
# model built with mean squared error ,, change map values from 1 to 100 to min to max from the model
# model ie "__model__name.csv" will store 3 vals "attention_min" "attention_max" "activity"

# when calibrate is run , ask for name and activity

# importing csv module 
import csv 

# csv file name 
filename = "./records/kabikabi_needles_.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = csvreader.__next__() 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 
