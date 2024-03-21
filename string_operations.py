from collections import Counter
sentence = input('Enter the sentence : ') #user will enter a string
words = Counter(sentence.lower().split())

print(f'Total no.of words in this sentence is {sum(words.values())}')
print("Palindrome words are : ")

for w,val in words.items():
    if len(w)>1 and w == w[::-1]:
        print(f'{w} : {val}')
print('Repetition are : ')    
for w,val in words.items():
    if val>1:
        print(f'{w} : {val} times')