str=input("enter the string:")
vowels=0
consonant=0
for ch in str:
    if ch in "aeiouAEIOU":
        vowels=vowels+1
    else:
        consonant=consonant+1
print(vowels)
print(consonant)