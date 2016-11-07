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

    #print('Reading batch payment file: {}'.format(args.batch_payment_file))
    with open(args.batch_payment_file, encoding='utf-8') as f:
        reader = csv.reader(f, skipinitialspace=True, quoting=csv.QUOTE_NONE)
        next(reader) # skip header
        try:
            for row in reader:
                print(row)
                # id1 = row[1]
                # id2 = row[2]
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(args.batch_payment_file, reader.line_num, e))

    #print('Reading stream payment file: {}'.format(args.stream_payment_file))

    with open(args.output1_file, 'w') as f:
        pass # TODO
        #f.write('Hello, World')

if __name__ == '__main__':
    main()
