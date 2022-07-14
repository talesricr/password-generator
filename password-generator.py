import sys
import random

symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+", "=", "-", "`", ":", ";" "." ">", "<", ","]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetalt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
password = [];
characters = sys.argv[1];
             
def append(num1, num2, type):
    while True:
            index = random.randint(num1, num2)
            if type[index] not in password:
                password.append(type[index])
                break

for x in range(int(characters)):
    randomizer = random.randint(0, 3)
    if randomizer == 0:
        append(0, 9, numbers)
    elif randomizer == 1:    
        append(0, 18, symbols)
    elif randomizer == 2:
        append(0, 25, alphabet)
    elif randomizer == 3:
        append(0, 25, alphabetalt)

printpassword = ''.join(password)    
print(printpassword)
