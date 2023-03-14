#to count the no of vowels and consonants

count_vowel=0
count_con=0
var=input("enter the word: ")
vowels='AEIOUaeiou'

for i in var:
    if i in vowels:
        count_vowel=count_vowel+1
    else:
        count_con=count_con+1


print('count_vowel:', count_vowel)
print('count_con:', count_con)

