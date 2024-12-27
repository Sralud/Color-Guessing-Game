import random
from tkinter import Tk, Canvas, Label, Button

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_code = f"#{r:02x}{g:02x}{b:02x}"
    return r, g, b, hex_code

def new_round():
    global correct_hex, options, result_label, next_button, color_canvas

    r, g, b, correct_hex = generate_random_color()
    options = [correct_hex]
    while len(options) < 4:
        _, _, _, fake_hex = generate_random_color()
        if fake_hex not in options:
            options.append(fake_hex)
    random.shuffle(options)

    color_canvas.config(bg=correct_hex)

    result_label.config(text="")

    next_button.pack_forget()

    for button in hex_buttons:
        button.pack_forget()
    for option in options:
        button = Button(root, text=option, font=("Arial", 12),
                        command=lambda opt=option: check_guess(opt))
        button.pack(pady=5)
        hex_buttons.append(button)

def check_guess(user_guess):
    if user_guess == correct_hex:
        result_label.config(text="🎉 Correct! Well done! Click 'Next Color' to continue.", fg="green")
        next_button.pack(pady=10)
    else:
        result_label.config(text=f"❌ Wrong! The correct code was {correct_hex}.", fg="red")

def color_code_guessing_game():
    global root, color_canvas, result_label, next_button, hex_buttons

    root = Tk()
    root.title("Color Code Guessing Game")

    color_canvas = Canvas(root, width=300, height=200, bg="white")
    color_canvas.pack(pady=20)

    instruction_label = Label(root, text="Guess the hex code of the displayed color:")
    instruction_label.pack()

    result_label = Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=10)

    next_button = Button(root, text="Next Color", font=("Arial", 12), command=new_round)
    next_button.pack_forget()

    hex_buttons = []

    new_round()

    root.mainloop()

if __name__ == "__main__":
    color_code_guessing_game()