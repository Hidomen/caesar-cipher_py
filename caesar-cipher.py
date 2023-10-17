alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# shifting left for encode , shifting right for decode

def main():
    print("""                                                                                                                             
                                                                               88             88                                 
                                                                               ""             88                                 
                                                                                              88                                 
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         ,adPPPPP88 8PP           Y8ba,  ,a PPPPP88 88            8b         88 88       d8 88       88 8PP******  88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88             `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                  88                                             
                                                                                  88                                                  
""")

    while True :
        direction = input("Type 'encode' for encrypt, type 'decode' for decrypt. \n").lower()
        if direction == "encode" :
            shift_left = get_shift()
            encrypter(shift_left)
            break
        elif direction == "decode" :
            shift_right = get_shift()
            decrypter(shift_right)
            break

def get_shift():
        while True:
            try:
                shift = int(input(("Type your shift number.\n")))
                return shift
            except ValueError:
                print("NUMBER PLZ")

def encrypter(shift):
    print("encoding -", shift)
    plain_text = input("MESSAGE > ")
    cipher_text = ""
    for letter in plain_text :

        
        if letter in alphabet_list:    
            index_of_letter = alphabet_list.index(letter)
            new_position = index_of_letter + shift
            
            cipher_text += crypt_cycler(new_position)
        else :
            cipher_text += letter

    print(cipher_text)

def decrypter(shift):
    print("decoding -", shift)
    cipher_text = input("MESSAGE > ")
    plain_text = ""
    for letter in cipher_text :
        
        if letter in alphabet_list:
            index_of_letter = alphabet_list.index(letter)
            new_position = index_of_letter - shift
            
            plain_text += crypt_cycler(new_position)
        else :
            plain_text += letter
    
    print(plain_text)

def crypt_cycler(new_position):
    while new_position > 27 :
        new_position -= 26
    
    while new_position < 0 :
        new_position += 26
        
    return alphabet_list[new_position]


main()