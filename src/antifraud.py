#!/usr/bin/env python3
# program that detects suspicious transactions

import sys
import argparse
import csv

# fraud detection algorithm

#Helper function for determining if two id's are second neighbors
def check_second_neighbors(dictionary,id1,id2):
    #initialize the returned value
    return_tf=False
    
    #Need to find id2 in the vectors of id1's links
    #For each of the first neighbors of id1 then look for id2 in that
    #friend's dictionary value
    for friend in dictionary[id1]:
        #print(id2)
        #print(dictionary[friend])
        if id2 in dictionary[friend]:
            return_tf=True
            break

    return return_tf

#Helper function for determining if two id's are third neighbors
#Already know that they they're not neighbors or second neighbors
def check_third_neighbors(dictionary,id1,id2):
    #initialize the returned value
    return_tf=False
    
    #Note that the third neighbors of an id is a second neighbor
    #of the neighbors an id
    for friend in dictionary[id1]:
        if check_second_neighbors(dictionary,friend,id2):
            return_tf=True
            break

    return return_tf

#Helper function for determining if two id's are 4th neighbors
#Already know that they are not first, second, or third neighbors
#Note that the 4th neighbors of person A is the second neighbors 
#of the second neighbors of person A
def check_fourth_neighbors(dictionary,id1,id2):
    #Initialize return value
    return_tf=False
    
    #For each of the second neighbors of id1, need to check if id2 is a second neighbor
    for first in dictionary[id1]:
        for second in dictionary[first]:
            if check_second_neighbors(dictionary,first,second):
                return_tf=True
                break

    return return_tf

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
    with open(args.output3_file, 'w') as output3_file:
        with open(args.output2_file, 'w') as output2_file:
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

                            #Output 1 constraints--two people had to have a past payment
                            #Also will satisfy the Output 2 and Output 3constraints if they are first-neighbors
                            #Test to see if the id2's are in value of the dictionary from id1.
                            #If so, then it's a trusted transaction
                            if id1 in id_vector.keys() and id2 in id_vector[id1]:
                                output1_file.write("trusted\n")
                                output2_file.write("trusted\n")
                                output3_file.write("trusted\n")
                            #If they're not first neighbors, then we have to check if they are 
                            #second neighbors or not--satisfies Output 2 and 3
                            elif check_second_neighbors(id_vector,id1,id2):
                                output2_file.write("trusted\n")
                                output3_file.write("trusted\n")
                            #Check the third neighbors first so we don't have to check the 4th neighbors if the condition is already satisfied
                            elif check_third_neighbors(id_vector,id1,id2):
                                output3_file.write("trusted\n")
                            #Final check for 4th neighbors--if the thwo are 4th neighbors then we can classify them as trusted in the output 3 file
                            elif check_fourth_neighbors(id_vector,id1,id2):
                                output3_file.write("trusted\n")
                            else:
                                output1_file.write("unverified\n")
                                output2_file.write("unverified\n")
                                output3_file.write("unverified\n")

                    except csv.Error as e:
                        sys.exit('file {}, line {}: {}'.format(args.batch_payment_file, reader.line_num, e))

    # with open(args.output1_file, 'w') as f:
        # pass # TODO
        # #f.write('Hello, World')

if __name__ == '__main__':
    main()
