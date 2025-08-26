import random
word_list=["aardvark","baboon","camel"]
lives=4
stages=['''
       _______
     |/   |
     |   (_)
     |   \|/
     |    |
     |   | |
     |
    _|___
''','''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
''',
'''
        _______
     |/    |
     |    (_)
     |     |
     |     |
     |      
     |
    _|___
'''
,'''
       _______
     |/   |   
     |   (_)
     |
     |       
     |      
     |
     |___
''','''
      _______
     |/   |   
     |   
     |
     |       
     |      
     |
     |___
''']
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                   ''')



random_word=random.choice(word_list)

player_name=input("enter player name :").lower()
print(f"Hii, {player_name}, welcome to hangman challenge . all the best !")

action=len(random_word)
game_over=False
correct_letter=[]
while not game_over:
    print(f'''*********************************************{lives}/4 LIVES LEFT********************************''')
    spaces="_"*len(random_word)
    print(spaces)
    user_guess_letter=input("Guess a letter : ").lower()
    display=""
    index=len(stages)-1
    for i in random_word:
        if i == user_guess_letter:
            display+=i
            correct_letter.append(user_guess_letter) 
        elif i in correct_letter:
            display+=i
        else:
            display+="_"
    
    print(display)
    
            
    if "_" not in display:
        game_over=True
        print(f"congratualations  {player_name} You win .")
    
    
    if user_guess_letter not in random_word:
        lives-=1
        print(f"You guessed {user_guess_letter}, that's npt in the word. you lose a life.")
        if lives==0:
            game_over=True
            print( f"********************************** IT WAS {user_guess_letter}! {player_name} YOU LOSE ****************************************")
    print(stages[lives])