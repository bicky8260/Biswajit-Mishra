import random

i=1
won=0
lose=0
draw=0
while i<=11:
   Your_choice=input("Please enter a name what you want to choose:snake or water or gun:")
   List=['Snake','Water','Gun']
   Opponent_choice=random.choice(List)

   if Your_choice.lower() == "snake" and Opponent_choice.lower() == "water":
      print(f"Opponent choice is:{Opponent_choice}")
      print("Congrats..You won..")
      won=won+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   elif Your_choice.lower() == "snake" and Opponent_choice.lower() == "gun":
      print(f"Opponent choice is:{Opponent_choice}")
      print("Sorry..You lose..")
      lose=lose+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   elif Your_choice.lower() == "gun" and Opponent_choice.lower() == "snake":
      print(f"Opponent choice is:{Opponent_choice}")
      print("Congrats..You won..")
      won=won+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   elif Your_choice.lower() == "gun" and Opponent_choice.lower() == "water":
      print(f"Opponent choice is:{Opponent_choice}")
      print("Sorry..You lose..")
      lose=lose+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   elif Your_choice.lower() == "water" and Opponent_choice.lower() == "gun":
      print(f"Opponent choice is:{Opponent_choice}")
      print("Congrats..You won..")
      won=won+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   elif Your_choice.lower() == "water" and Opponent_choice.lower() == "snake":
      print(f"Opponent choice is:{Opponent_choice}")
      print("Sorry..You lose..")
      lose=lose+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   elif Your_choice.lower() == Opponent_choice.lower():
      print(f"Opponent choice is:{Opponent_choice}")
      print("Opps...Draw..")
      draw=draw+1
      print(f"{11-i} steps remaining.")
      print("-------------------------------------------")
   else:
      print("Invalid input..Please choose a name like snake,water or gun.")
      print(f"{11-i+1} steps remaining.")
      print("-------------------------------------------")
      i=i-1

   i=i+1
print("Game over.")
print(f"You have won {won} rounds.")
print(f"Opponent have won {lose} rounds.")
print(f"Total {draw} draws.")
print(f"Total {won+lose+draw} rounds you and your Opponent have played.")
print("THANK YOU FOR PLAYING THIS GAME.")
