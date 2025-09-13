print('''
       _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
''')

def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def devide(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":devide
}

def calculation():    
    should_accumalate=True
    num1=float(input("enter first number = "))

    while should_accumalate:
        for symbol in operations:
            print(symbol)
        ops=input('Pick an operation = ')
        if(ops not in operations):
            print("please enter valid operations :")
            ops=input('enter your operation "+" , "-" , "*" , "/" ')
        num2=float(input("enter second number = "))
        answer=operations[ops](num1,num2)
        print(f"{num1} {ops} {num2} = {answer}")

        choice=input(f"Type 'Y' to continue calculationg with {answer} , or type 'n' to start a new calculation ").lower()

        if choice=="y":
            num1=answer
        if choice=="n":
            should_accumalate=False
            print("\n"*20)
            calculation()
calculation()