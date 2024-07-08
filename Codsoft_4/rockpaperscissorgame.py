import random
from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk   

def computer_input():
    computer_choice = ["rock", "paper", "scissor"]
    return random.choice(computer_choice)

def game_logic(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("draw game")
        return "Draw!"
    elif (user_choice=="rock" and computer_choice=="scissor") or (user_choice=="scissor" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock"):
        print("you win")
        return "You Win"
    else:
        print("computer wins")
        return "Computer Win"

def play_game(user_choice):
          
        global player_score, computer_score
        computer_choice = computer_input()
        print(f"You Choose: {user_choice}")
        print(f"Computer Choose: {computer_choice}")
        result = game_logic(user_choice.lower(), computer_choice)
        result_label.config(text=f"Computer Chose: {computer_choice}\n {result}")

        
        if result == "You Win":
            player_score.set(player_score.get() + 1)
        elif result == "Computer Win":
            computer_score.set(computer_score.get() + 1)
        player_score_label.config(text=f"Player Score: {player_score.get()}")
        computer_score_label.config(text=f"Computer Score: {computer_score.get()}")
        
root = Tk()
root.geometry("400x500")
root.title("Rock Paper Scissor Game")
root.wm_iconbitmap("game.ico")
root.config(background="light pink")


image = Image.open("C:\\Users\\hp\\Downloads\\image2.jpg")
image = image.resize((150, 100))
photo_image = ImageTk.PhotoImage(image)
label = Label(root, image=photo_image, background="light pink")
label.grid(row=10, column=3, rowspan=2, padx=10, pady=10)    


label = Label(root, text="Rock Paper Scissor Game", font="boulder 20 bold", background="light pink")
label.grid(row=0, column=0, columnspan=5, pady=20, sticky="nsew")

player_score = IntVar()
player_score.set(0)

computer_score = IntVar()
computer_score.set(0)


player_score_label = Label(root, text="Player Score: 0", font="italic 16", background="light pink")
player_score_label.grid(row=1, column=0, columnspan=5, pady=10)


computer_score_label = Label(root, text="Computer Score: 0", font="italic 16", background="light pink")
computer_score_label.grid(row=2, column=0, columnspan=5, pady=10)


result_label = Label(root, text="Result: ", font="italic 16", background="light pink")
result_label.grid(row=3, column=0, columnspan=5, pady=20)

rock_button = Button(root, text="Rock", command=lambda: play_game("Rock"), width=5, height=3, font="italic 16 bold", background="light blue")
rock_button.grid(row=4, column=2, padx=10, pady=10)

paper_button = Button(root, text="Paper", command=lambda: play_game("Paper"), width=5, height=3, font="italic 16 bold", background="light blue")
paper_button.grid(row=4, column=3, padx=10, pady=10)

scissor_button = Button(root, text="Scissor", command=lambda: play_game("Scissor"), width=6, height=3, font="italic 16 bold", background="light blue")
scissor_button.grid(row=4, column=4, padx=10, pady=10)

player_score_label.config(text=f"player score: {player_score.get()}")
computer_score_label.config(text=f"computer score: {computer_score.get()}")
root.mainloop()



    

