from collections import Counter
import os

def count_pal(l): #code for Palindrome with parameter list l of singel line
    pal_list=[]   #create empty list to store the palindromes in it.
    sentence = l.lower().split()
    for w in sentence:
        if len(w)>1 and w == w[::-1]:
            pal_list.append(w)
        else : None
    return pal_list

def count_rep(l):   #function to count repetition of words in a single line,with parameter as list l
    count = 0
    sentence = Counter(l.lower().split())      #converts all letters into lower case & split each word by space     #initialize counter variable
    for w,val in sentence.items(): 
        if val > 1:
            count += 1
        else: None
    return count

def write_to_file(pf,output_filename):      #write results to file function with two parameters
    with open(output_filename,'a') as output_file:
        output_file.write(pf)

def operation(l,output_filename):      #main function that calls other functions
    pal = count_pal(l)
    rep = count_rep(l)
    pf = f'{l} \n No.of words: {len(l.split())} , Palindrome : {len(pal)} , Repetition : {rep} \n' 
    write_to_file(pf,output_filename)


def check_file(file_name,output_filename):      #checks whether the input is valid or
    try:
        os.remove('outputs.txt')                        #not,and creates new one each time
        with open(file_name,'r') as input_file:
            paragraph = input_file.read()                 #reading all lines at once
            lines = paragraph.split('\n')                 #splitting into individual lines
            for l in lines:                                #iterating over every line
                operation(l,output_filename)                #calling main function

    except FileNotFoundError:
        print('File not found')

f_n = input('Enter input file name : ')
o_n = input("Enter the name of output file : ")
check_file(f_n,o_n)                                             # calling the function
