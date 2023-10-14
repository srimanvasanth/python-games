import random

def rword(mlen):
    word_pros = 0
    global cword
    cword = None
    with open("text.txt") as x:
        for word in x:
            word = word.strip().lower()
            if len(word) < mlen:
                continue
            word_pros += 1
            if random.randint(1, word_pros) == 1:
                cword = word
    return cword

def att():
    while True:
        global att
        att = input("How many attempts do you want? ")
        try:
            att = int(att)
            if 1 <= att <= 25:
               return att
            else:
                print("You can't have more than 25 attempts")
                continue
        except:
            print("Enter numeric values only")
            continue

def mwl():
    global mlen
    while True:
        mlen = input("Enter minimum word length: ")
        try:
            mlen = int(mlen)
            if 4 <= mlen <= 12:
                return mlen
            else:
                print("Enter values between 4 and 12")
                continue
        except:
            print("Enter numeric values only")
            continue

print("The minimum word length is ",mwl())
print("Number of attempts: ",att())
rword(mlen)
word = ""

while att >= 0:
    z = 0
    print("Guessing word: ", end="")
    for letter in cword:
        if letter in word:
            print(letter, end="")
        else:
            z += 1
            print("_", end="")
    if att == 0:
        print("\nYou have 0 attempts left. You lose.")
        break
    if z == 0:
        print("\nYou win. The word is ",cword)
        break
    char = input("\nEnter a character: ")
    if len(char) != 1:
        print("Enter one character at a time")
        continue
    word += char
    if char not in cword:
        att -= 1
        print("{0} is not present in the word".format(char))
        print("You have ", +att ," attempts left")
    print("\n")






