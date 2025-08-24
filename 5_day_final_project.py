import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1,','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many latters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like?\n"))

#Easy level
password=[]
for i in range(nr_letters):
    password.append(random.choice(letters))
    
for i in range(nr_symbols):
    password.append(random.choice(symbols))

for i in range(nr_numbers):
    password.append(random.choice(numbers))
    
#Hard level password
Hard_level_password=""
for i in range(len(password)):
    Hard_level_password+=random.choice(password)
print("Hard level Password")
print(f"Your Password : {Hard_level_password}")