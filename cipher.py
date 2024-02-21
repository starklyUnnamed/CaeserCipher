from time import sleep
from tqdm import tqdm

key = ["U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

def main():
    start()
    plainText = input('What would you like to encrypt?: ')
    cipherText = encrypt(plainText.upper())
    print('Here is your encrypted text: ', cipherText)

def start():
    print("Starting Encryption Algorithm...")
    for i in tqdm(range(100)):
        sleep(.05)

def encrypt(plainText):
    cipherText = []
    for char in plainText:
        if char in key:
            i = key.index(char)
            char = key[i-6]
        cipherText.append(char)
    return ''.join(cipherText)

main()