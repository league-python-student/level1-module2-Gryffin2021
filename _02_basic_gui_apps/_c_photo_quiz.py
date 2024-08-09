"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class
class Quiz(tk.Tk):
    # TODO 2) Create a constructor
    def __init__(self):
        # TODO 3) call Tk's constructor
        super().__init__()
        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.
        self.label = tk.Label()
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)

# TODO 5) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    # TODO 6) Create an object of the tkinter class
    quiz = Quiz()
    # TODO 7) Set the app window width and height using geometry()
    quiz.geometry("1000x1000")
    # TODO 8) Declare and initialize a score variable
    score = 0
    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable
    baguette = create_image('carrots.jpg', 1000, 1000)
    fossil = create_image('fossil.jpg', 1000, 1000)
    penguin = create_image('download.jpg', 1000, 1000)
    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)
    quiz.label.configure(image=baguette)
    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.
    q1 = simpledialog.askinteger(title='Q1', prompt='How many baguettes are present in the photo?')
    if q1 == 0:
        messagebox.showinfo(title='Correct!', message="Correct! +1 point")
        score += 1
    else:
        messagebox.showinfo(title='Incorrect!', message="Incorrect! There are 0 baguettes in the image. Those are carrots. Can you not distinguish a bread from a vegetable?")
    # TODO 12) If the answer is correct, increase the score by 1

    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question
    quiz.label.configure(image=fossil)
    q2 = simpledialog.askstring(title='Q2', prompt='Is this a dinosaur fossil?')
    if q2 == 'Yes':
        messagebox.showinfo(title='Correct!', message="Correct! +1 point")
        score += 1
    else:
        messagebox.showinfo(title='Incorrect!', message="Incorrect! If you look at the fossil for more than your dwindling attention span allows you to, you will be able to make the observation that this is in fact a fossil created by a dinosaur.")
    quiz.label.configure(image=penguin)
    q3 = simpledialog.askstring(title='Q3', prompt='Macaroni')
    if q3 == 'No':
        messagebox.showinfo(title='Correct!', message="Correct! +1 point")
        score += 1
    else:
        messagebox.showinfo(title='Incorrect!', message="Incorrect! It is simply quite obvious that this is a Macaroni Penguin and not just a piece of macaroni. If you were not such a feeble minded being you would know that. If anyone is paying school tuition for you, they are wasting time and money.")
    # TODO 14) Display the score to the user after asking the last question
    messagebox.showinfo(title='Score', message='Score = ' + str(score) + '!')
