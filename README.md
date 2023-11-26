Project Title
- HW4 CSCI544 - BiLSTM model

Description
- This project has code and output files for BiLSTM model, BiLSTM model with Glove, along with other tasks for HW4


Author
- Twinkle Dhanak (5150891285)


Getting Started

###############################################
A. Libraries
###############################################
1. Python3.6
2. torch 
3. numpy, pandas
4. perl

###############################################
B. Program Input files
###############################################

1. data/train - This file is used to train model for Task1
2. data/dev - We evaluate the performance of both models on this file and determine accuracy
3. data/test - We predict the NER tags for sentences in this file
4. data/glove.6B.100d.gz - Glove embeddings
5. conll03eval

###############################################
C. Program Code files
###############################################

1. HW4-CSCI544-TwinkleD.py - This file caters to following:
- Task1
- Task2

###############################################
D. How to run the code files
###############################################

1. Keep all the data files - train , dev and test under same folder -> data
2. Ensure that the file paths are data/train , data/dev and data/test as they have been hardcoded in the program
3. Keep files HW4-CSCI544-TwinkleD.py outside 'data' directory
4. To execute , run below commands - 
python3 hw4_csci544_twinkled.py 


###############################################
E. Outputs
###############################################

Following files will be generated :
1. blstm1.pt
2. blstm2.pt
3. dev1.out
4. test1.out
5. dev2.out
6. test2.out

###############################################
F. Additional files
###############################################

1. PDF report
