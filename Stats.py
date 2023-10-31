#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Baligh BABAALI
#
# Created:     26/03/2023
# Copyright:   (c) Baligh BABAALI 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import the necessary libraries
import nltk
import pandas as pd

#nltk.download('punkt')

def init_MADAR():
    MSA_df = pd.read_csv('MADAR\MADAR.corpus.MSA.tsv', sep='\t')
    # printing data
    #print(MSA_df)

    DZDA_df = pd.read_csv('MADAR\MADAR.corpus.Algiers.tsv', sep='\t')
    # printing data
    #print(DZDA_df)

    f_MSA = open("MSA.txt", "w")
    f_DZDA = open("DZDA.txt", "w")

    for index, row in DZDA_df.iterrows():
        print(index,' --------------------------------')
    #    print(index, row['sent'], row[0])
        f_DZDA.write(row['sent']+'\n')

        for i, x in MSA_df.iterrows():
            if x[0] == row[0]:
                f_MSA.write(x['sent']+'\n')
    #            print(i, x['sent'], x[0])
                break
    f_MSA.close()
    f_DZDA.close()

    return

def tokens_Stats(filename):
    # Load the dataset
    with open(filename+'.txt', 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
    with open(filename+'.txt', 'r') as f:
        data = f.read()
#        if data.startswith(BOM):
#            data = data[1:]

    # Tokenize the dataset
    tokens = nltk.word_tokenize(data)
    # Count the number of tokens
    num_tokens = len(tokens)
    # Print the result
    print("The number of tokens in "+filename+" is:", num_tokens)

    unique_tokens = set(tokens)
    num_unique_tokens = len(unique_tokens)
    # Print the result
    print("The number of unique tokens in the "+filename+" is:", num_unique_tokens)

    # Tokenize the dataset into sentences
    sentences = nltk.sent_tokenize(data)
    print("The number of sentences in "+filename+" is :", line_count)
    # Count the total number of words in the sentences
    total_words = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences)
    # Count the number of sentences
    num_sentences = len(sentences)
    # Calculate the average sentence length
    avg_sentence_length = total_words / num_sentences
    # Print the results
    print("The number of unique tokens in "+filename+" is:", num_unique_tokens)
    print("The average sentence length is:", avg_sentence_length)
    print('---------------------------------------------------------------------')

    return

def init_PADIC():

    return

#init_MADAR()
#tokens_Stats('MADAR_MSA')
#tokens_Stats('MADAR_DZDA')
#init_PADIC()
#tokens_Stats('PADIC_MSA')
#tokens_Stats('PADIC_DZDA')
#
#tokens_Stats('Tatoeba_MSA')
#tokens_Stats('Tatoeba_DZDA')
#
#tokens_Stats('MSA')
#tokens_Stats('DZDA')
#
#tokens_Stats('CC-MSA')
#tokens_Stats('CC-DZDA')

tokens_Stats('RR_MSA')
tokens_Stats('RR_DZDA')
