#!/usr/bin/env python3
# program that detects suspicious transactions

import sys
import argparse
import csv

# fraud detection algorithm

def main():
    parser = argparse.ArgumentParser(description='program that detects suspicious transactions')
    parser.add_argument('batch_payment_file', help='path to batch_payment.txt')
    parser.add_argument('stream_payment_file', help='path to stream_payment.txt')
    parser.add_argument('output1_file', help='path to output1.txt')
    parser.add_argument('output2_file', help='path to output2.txt')
    parser.add_argument('output3_file', help='path to output3.txt')
    args = parser.parse_args()

	#initialize the id dictionary
    id_vector=dict.fromkeys(['first'])
	
    #print('Reading batch payment file: {}'.format(args.batch_payment_file))
    with open(args.batch_payment_file, encoding='utf-8') as f:
        reader = csv.reader(f, skipinitialspace=True, quoting=csv.QUOTE_NONE)
        next(reader) # skip header
        try:
            for row in reader:
                if len(row) >= 3:
                    id1 = row[1] #print(row) #print(id1)
                    id2 = row[2]
                    #Add each of the id's to it's own key
                    #If the key isn't there then add it, otherwise if the
                    #key-value pair is already present then don't do anything
                    if not(id1 in id_vector.keys()):
                        id_vector[id1]=[id2]
                    if not(id2 in id_vector.keys()):
                        id_vector[id2]=[id1]
                    if id1 in id_vector.keys() and not(id2 in id_vector[id1]):
                        id_vector[id1].append(id2)
                    if id2 in id_vector.keys() and not (id1 in id_vector[id2]):
                        id_vector[id2].append(id1)					
				
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(args.batch_payment_file, reader.line_num, e))

    #Close the file			
    f.close() #print('Reading stream payment file: {}'.format(args.stream_payment_file))
    #Need to open and classify the new data from the stream file
    with open(args.output1_file, 'w') as output1_file:
        with open(args.stream_payment_file, encoding='utf-8') as stream_file:
            reader = csv.reader(stream_file, skipinitialspace=True, quoting=csv.QUOTE_NONE)
            next(reader) # skip header
            try:
                for row in reader:
                    #Grab the id's from the row if possible
                    if len(row)>=3:
                        id1=row[1]
                        id2=row[2]
    
                    #Test to see if the id's are in the dictionary.
                    #If so, then it's a trusted transaction
                    if id1 in id_vector.keys() and id2 in id_vector[id1]:
                        output1_file.write("trusted\n")
                    else:
                        output1_file.write("unverified\n")

            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(args.batch_payment_file, reader.line_num, e))
    
    # with open(args.output1_file, 'w') as f:
        # pass # TODO
        # #f.write('Hello, World')

if __name__ == '__main__':
    main()
