#!/usr/bin/env bash

# example of the run script for running the fraud detection algorithm with a python file,
# but could be replaced with similar files from any major language

# I'll execute my programs, with the input directory paymo_input and output the files in the directory paymo_output
#python ./src/antifraud.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt

#Gloria D'Azevedo submission using R
#R script to yield output with the first type of constraint
R CMD BATCH output_1.R

#R script to yield output with the second type of constraint
R CMD BATCH output_2.R

#R script to yield output with the third type of constraint
R CMD BATCH output_3.R