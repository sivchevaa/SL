word = str(input())
word.lower()
if word == word[::-1]:
    print("Word is a palindom.")
else:
    print("Word is not a palindrom.")