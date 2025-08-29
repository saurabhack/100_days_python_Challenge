

def ceaser(original_text,shift_amount,encoded_or_decoded):
    output_text=""
    for letter in original_text:
        if encoded_or_decoded=="decode":
            shift_amount+=-1
        
        shifted_position=alphabet.index(letter)-shift_amount
        shifted_position%=len(alphabet)
        print("shifted position=",shifted_position)
        output_text+=alphabet[shifted_position]
    print(f"Here is encoded result: {output_text}")

def yess_or_no():
    yorno=input("do you want to play again ? if you want to play again please enter yess or no").lower()
    return yorno
restart=True
while restart == True:
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    fruits=["Apple","Pear","Organge"]
    fruits.index("Pear")
    def encode(text,shift):
        new_string=""
        for let in text:
            number=alphabet.index(let)
            number=number%len(alphabet)
            new_string=new_string+alphabet[number+shift]
        print("here is encoded result : ",new_string)

    def dcrypt(text,shift):
        new_string=""
        for let in text:
            number=alphabet.index(let)
            number=number%len(alphabet)
            new_string=new_string+alphabet[number-shift]
        print(f"here is dcrypted result :",new_string)

    if direction=="encode":
        encode(text,shift)
    elif direction=="decode":
        dcrypt(text,shift)
    else:
        print("envalid input please try again !")
    yorno=yess_or_no()
    if yorno=="yes":
        restart=True
    elif yorno=="no":
        restart=False
    elif yorno is not "yes" or yorno is not "no":
        print("you enter invalid keyword please try again !")
        yorno=yess_or_no()

# if(direction=="encode"):
#     encode(text,shift)
# else:
#     dcrypt(shift=shift,text=text)




ceaser(text,shift,direction)