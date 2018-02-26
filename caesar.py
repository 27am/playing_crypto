import string
import sys



alphabet = tuple(string.printable)


def crypt(plaintext, key = 0):
    
    ciphertext = []
    
    for char_plaintext in plaintext:
        numeric_position = alphabet.index(char_plaintext) # get the numeric position of the character
        
        char_ciphertext = alphabet[(numeric_position + key) % len(alphabet)] # substitution
        ciphertext.append(char_ciphertext)
        
    return "".join(ciphertext)


def decypt(ciphertext, key = 0):
    
    plaintext = []
    
    for char_ciphertext in ciphertext:
        numeric_position = alphabet.index(char_ciphertext) # get the numeric position of the character
        
        char_plaintext = alphabet[(numeric_position - key) % len(alphabet)] # substitution
        plaintext.append(char_plaintext)
        
    return "".join(plaintext)



def main():

	if (sys.argv[1] == "c"):
		txt = sys.argv[2]
		print(crypt(txt, int(sys.argv[3]))

	if (sys.argv[1] == "d"):
		txt = sys.argv[2]
		print(decypt(txt, int(sys.argv[3]))

	else:
		print("Missing proper input arguments")

	



if __name__ == "__main__":
    main()