from time import sleep
from tqdm import tqdm

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]

def main():
    start()
    getShiftSuccess = False
    plainText = input('What would you like to encrypt?: ')
    while getShiftSuccess != True:
        shift, getShiftSuccess = getShift()
    cipherText = encrypt(plainText.upper(), shift)
    print('Here is your encrypted text: ', cipherText)

def start():
    print("Starting Encryption Algorithm...")
    for i in tqdm(range(100)):
        sleep(.05)

def getShift():
    shift = ''
    success = False
    shiftValues = [x+1 for x in range(25)]
    shiftTry = input('What would you like the shift to be?: ')
    try:
        if int(shiftTry) in shiftValues:
            shift = int(shiftTry)
            success = True
        else:
            print("Please select a number between one and twenty-five...")
            return shift, success
    except:
        print("Please ensure your selection is a NUMBER between one and twenty-five...")
    return shift, success

def encrypt(plainText, shift):
    cipherText = []
    for char in plainText:
        if char in alphabet:
            i = alphabet.index(char)
            char = alphabet[i - shift]
        cipherText.append(char)
    return ''.join(cipherText)

main()