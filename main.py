
import random

print("Welcome to lock picking game")
choice = (input("ARE U A REAL LOCK PAPER?  Y/N:")).upper()

if choice == "Y" or choice == "YES":



    print("-----------------------------------------------------------------------------------------")


    print("WELCOME LOCK PICKER TO THE LOCK PICKING GAME")


    print("WELCOME TO THE LOCK PICKING GAME")




    print("RULES OF THE GAME ARE :------->")
    print("IN THIS GAME YOU WILL BE GIVEN 10 CHANCES TO PICK THE LOCK")
    print("IF YOU PICK THE LOCK WITHIN 10 CHANCES YOU WIN, IF NOT YOU LOSE")
    print("GOOD LUCK LOCK PICKER")
    
    print("-----------------------------------------------------------------------------------------")
elif choice == "N" or choice ==  "NO":
    print("GET OUT OF HERE, ONLY PICKER ARE ALLOWED")
    exit()

else:
    print("INVALID INPUT, PLEASE TRY AGAIN")

    print("-----------------------------------------------------------------------------------------")













print(''' lock art = 
      __________
     |  ______  |
     | |      | |
     | | LOCK | |
     | |______| |
     |          |
     |   ____   |
     |  /    \  |
     | |      | |
     |  \____/  |
     |__________|


key art = 
        ____
       |    |
   ____|    |____
  |              |
  |  __    __    |
  | |  |  |  |   |
  |_|  |__|  |___|
       |  |
       |__|
''')

    
lock_number = random.randint(1, 100)
chances = 10

while chances >= 0:
    print(f"you have {chances} chances left, DONT TRY TO WASTE IT")


    print("TRY TO PICK THE LOCK, GUESS THE NUMBER BETWEEN 1 AND 100")

    guess = int(input("ENTER YOUR GUESS: "))


    print("_-------------------------------------------------------------------------------------------------------------")

    if guess == lock_number:
        print("CONGRATS , YOU PICKED THE LOCK")

        print("YOU ARE A REAL LOCK PICKER")



        print(''' ⢸⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡷⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇ Are ya winning son?
⢸⠀⠀⠀⠀⠀⠖⠒⠒⠒⢤⠀⠀⠀⡇ 
⢸⠀⠀⣀⢤⣼⣀⡠⠤⠤⠼⠤⡄⠀⡇⠀
⢸⠀⠀⠑⡤⠤⡒⠒⠒⡊⠙⡏⠀⢀⡇⠀
⢸⠀⠀⠀⠇⠀⣀⣀⣀⣀⢀⠧⠟⠁⡇
⢸⠀⠀⠀⠸⣀⠀⠀⠈⢉⠟⠓⠀⠀⡇
⢸⠀⠀⠀⠀⠈⢱⡖⠋⠁⠀⠀⠀⠀⡇
⢸⠀⠀⠀⠀⣠⢺⠧⢄⣀⠀⠀⣀⣀⡇
⢸⠀⠀⠀⣠⠃⢸⠀⠀⠈⠉⡽⠿⠯⡆
⢸⠀⠀⣰⠁⠀⢸⠀⠀⠀⠀⠉⠉⠉⡇
⢸⠀⠀⠣⠀⠀⢸⢄⠀⠀⠀⠀⠀⠀⡇
⢸⠀⠀⠀⠀⠀⢸⠀⢇⠀⠀⠀⠀⠀⡇ ''')



        print("____________________________-------------------------___________________________------------------------------")
        break
    elif guess < lock_number:
        print("dig upper , you are going to the earth core")
    elif guess > lock_number:
        print("dig lower , you are going to the sky")

    
    if guess != lock_number:
        chances = chances - 1



        if chances == 0:
            print("SORRY GNG , YOU RAN OUT OF CHANCES AS U BROKE YOUR SHOVEL TRYING TO DIG THE LOCK ")


            print("--------------------------------------------------------------------------------------------------")

            print('''░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░
                          ▓▓░░░░░░▓▓                  
                        ▓▓  ░░░░░░▓▓                  
                      ▓▓░░░░░░░░░░▓▓                  
                        ▓▓░░░░░░▓▓                    
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
''')
            print("BYE BYE SHOVEL BREAKER, CUZ U DIDNT PICK THE LOCK , U ARE NOT A REAL LOCK PICKER GNG")

            exit()
 








































































































                                                                                        















            








































































  













  

                                    

                

