# s1=input("enter the first string:").lower()
# s2=input("enter the second string:").lower()
# if sorted(s1)==sorted(s2):
#     print("anangram")
# else:
#     print("not anagram")






s1 = input("Enter the first string: ").lower()
s2 = input("Enter the second string: ").lower()

if len(s1) != len(s2):
    print("Not anagram")
else:
    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch in freq:
            freq[ch] -= 1
        else:
            print("Not anagram")
            break
    else:
        for value in freq.values():
            if value != 0:
                print("Not anagram")
                break
        else:
            print("Anagram")
