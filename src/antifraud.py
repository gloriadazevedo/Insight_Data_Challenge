#Python script to create 3 output files that have "trusted" or "unverified"
#Input is two .csv files--one of them has the past payment data that we use
#to train our routine/model and the second has the new test data that we want to predict

#libraries that we need
import csv

#Need to figure out how to grab the arguments from the command line run in .sh
#For now hard code
batch_filename='../paymo_input/batch_payment.csv'

#import the batch file which has the historical information and store the data somewhere
#initialize the matrix that we want to store things in
batch_data=[]
# with open(batch_filename) as csvfile:
	# line_reader=csv.reader(csvfile,delimiter=',')
	# for row in line_reader:
		# line_split=split(line_reader,',')
		# batch_data.append(line_split)[1]
		
	# print("Hello World")

open_file=open(batch_filename,'r')
print(open_file)

print(open_file.read(10))
#open_file.readline().split(str=',')
	
	
#import the stream file which has the new data which needs to be predicted

