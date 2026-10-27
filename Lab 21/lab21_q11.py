#Write a program to concatenate a list of strings to make a sentence using reduce function.
from functools import reduce
words=["Python","is","easy","language"]
sentence=reduce(lambda a,b:a+" "+b,words)
print(sentence)