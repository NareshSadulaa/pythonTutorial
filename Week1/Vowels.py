char = ["A","a","e","E","i","I","o","O","u","U"]
alpha = input("Enter an Alphabet: ")
if alpha in char:
    print(alpha,"is a vowel")
else:
    print(alpha,"is a consonant")