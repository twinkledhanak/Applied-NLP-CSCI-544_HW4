# Importing all libraries
import re
import json

# Constants
input_file_path = "data/train_niu"
dev_file_path = "data/dev_niu"
test_file_path = "data/test"

## Creating all functions here -

# Function to sort dictionary in desc order
def orderDictionary(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

# Creating dictionary
def create_vocabulary(dictionary):
# We removed punctuations to increase accuracy
    train_file = open(input_file_path, "r")
    for line in train_file:
        # If line is not a blank line, do further processing  
        if(line.strip()):
            line = line.strip()
            word = line.split(" ")[2]
            if word in dictionary:
                dictionary[word] = dictionary[word] + 1
            else:
                dictionary[word] = 1
            

    # Order the dictionary in descending order
    sorted_dict = orderDictionary(dictionary, True)

    # @TODO - Check if we need unknown counts at all?

    return sorted_dict   





# Keep all word counts in a dictionary - This is for Vocab count 
dictionary = dict()

# Task1: Create Vocabulary
sorted_dict = create_vocabulary(dictionary) # This vocab file has punctuations and special characters too
print(len(sorted_dict)) ## There are 9 distinct tags in all 

## Step 1:
train_file = open(input_file_path, "r")
vocab = {'__PAD__': 0, '__</e>__': 1, '__UNK__': 2} 
for line in train_file:
    # If line is not a blank line, do further processing  
    if(line.strip()):
      line = line.strip()
      word = line.split(" ")[1].lower()
      # We send the line to training model
      if word not in vocab:
        vocab[word] = len(vocab)

print(len(vocab))

unk_token='__UNK__'
max_epochs = 1
for epoch in range(max_epochs):
  #bilstm.train()
    train_loss = 0.0
    sentence_tensor = []
    # take the __UNK__ value fro mthe vocabulary 
    unk_ID = vocab[unk_token]

    train_file = open(input_file_path, "r")
    for line in train_file:
        print("Line: ",line)  
        # If line is not a blank line, do further processing  
        if(line.strip()):
            line = line.strip()
            word = line.split(" ")[1].lower()
            
            # if the word is not in vocab_dict, then assign UNK
            word_ID = vocab.get(word, unk_ID)
            #print("Word::: ",word," and its ID: ",word_ID)
            # append to tensor list
            sentence_tensor.append(word_ID)

        else:
            print("Tensor for prev sentence: ",sentence_tensor)
            sentence_tensor = []
            
    
        