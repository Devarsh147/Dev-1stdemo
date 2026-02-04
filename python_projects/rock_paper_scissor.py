'''
Docstring for Dev-1stdemo.python_projects.rock_paper_scissor

workflow of projects
1 - input from user(rock, paper, scissor)
2 - computer choice
3- result printed

cases:
A- rock:
- rock vs paper -> paper wins
- rock vs scissor -> rock wins
- rock vs rock -> tie

B- paper:
- paper vs rock -> paper wins
- paper vs scissor -> scissor wins
- paper vs paper -> tie

C- scissor:
- scissor vs rock -> rock wins
- scissor vs paper -> scissor wins
- scissor vs scissor -> tie

'''

import random 
items = ["rock", "paper", "scissor"]
user_choice = input("Enter your choice (rock,paper,scissor): ")
cpu_choice = random.choice(items)

print(f"user choice: {user_choice}, cpu_choice: {cpu_choice}")

if user_choice == cpu_choice:
    print("Both choices are same: it is a Tie!")

elif user_choice == "rock":
    if cpu_choice == "paper":
        print("paper wins!, cpu wins!")
    else:
        print("rock wins!, you won!")

elif user_choice == "paper":
    if cpu_choice == "scissor":
        print("scissor wins!, cpu wins!")
    else:
        print("paper wins!, you won!")

elif user_choice == "scissor":
    if cpu_choice == "rock":
        print("rock wins!, cpu wins!")
    else:
        print("scissor wins! , you won!")

else:
    print("Invalid input! please enter rock, paper or scissor")

