#Trevor Tomlin

alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
WORDLIST_FILENAME = "words.txt"

def loadwords():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return (wordlist)

def encryptor(data, shift):
    cypher = []
    for letter in data:
        if letter in alphabet:
            index = alphabet.index(letter)
            cypher.append(alphabet[(index + shift) % 26])
    return (cypher)

def decryptor(data, shift):
    cypher = []
    for letter in data:
        if letter in alphabet:
            index = alphabet.index(letter)
            cypher.append(alphabet[(index - shift) % 26])
    return (cypher)

def codebreaker(wordlist, data):
    data = list(data)
    for i in range(0,25):
        for index, letter in enumerate(data):
            alphaIndex = alphabet.index(letter)
            newLetter = alphabet[(alphaIndex + 1) % 26]
            data[index] = newLetter
            dataStr = "".join(data)
        if dataStr.lower() in wordlist:
            return (dataStr)

def main():
    while (True):
        print ("1. Encrypt")
        print ("2. Decrypt")
        print ("3. Code Breaker")
        choice = input()
        if choice == '1':
            data = input("Enter the cypher: ")
            while(True):
                try:
                    shift = int(input("Enter the number of shifts: "))
                    break
                except ValueError:
                    pass
                print ("Not an integer")
            data = data.upper()
            data_new = list(data)
            cypher = encryptor(data, shift)
            print (cypher)
            break
        elif choice == '2':
            data = input("Enter the cypher: ")
            while(True):
                try:
                    shift = int(input("Enter the number of shifts: "))
                    break
                except ValueError:
                    pass
                print ("Not an integer")

            data = data.upper()
            data_new = list(data)
            decyphered = decryptor(data, shift)
            print (decyphered)
            break
        elif choice == '3':
            wordlist = loadwords()
            data = input("Enter your data:")
            data = data.upper()
            word = codebreaker(wordlist, data)
            print (word)
            break
        else:
            print ("Invalid choice, try again.")


if __name__ == '__main__':
    main()
