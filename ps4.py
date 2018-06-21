#Trevor Tomlin

alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

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

def main():
    while (True):
        print ("1. Encrypt")
        print ("2. Decrypt")
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
        else:
            print ("Invalid choice, try again.")


if __name__ == '__main__':
    main()
