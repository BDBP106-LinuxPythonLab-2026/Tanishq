#Write a program to extract all vowels in a given string using list comprehension.
s=input("Enter a string:")
vowels=[ch for ch in s if ch in "aeiouAEIOU"]
print("Vowels:",vowels)