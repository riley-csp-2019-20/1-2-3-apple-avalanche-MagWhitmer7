#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape

apple = trtl.Turtle()

letter_list = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "x"]

current_letters = []

apple_list = []

number_of_apples = 5

current_letter = "a"

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)


def reset_apple(apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0, length_of_list)
    current_letter = letter_list.pop(index)
    new_xpos= rand.randint(-100,100)
    new_ypos= rand.randint(-50,50)
    apple.goto(new_xpos, new_ypos)
    draw_apple(apple, current_letter)
    current_letters.append(current_letter)

def draw_apple(apple, letter):
  apple.shape(apple_image)
  draw_the_letter(letter, apple)
  apple.showturtle()
  wn.update()

def apple_fall():
  index = current_letters.index(letter)
  current_letters.pop(index)

  apple.apple_list.pop(index)

  apple.goto(-200,200)

  apple.clear()
  apple.hideturtle()
  reset_apple(apple)
  apple_list.append(apple)

# create writing turtle
drawer = trtl.Turtle()
drawer.hideturtle()

# This function takes care of font and color.
def draw_the_letter(letter, apple):
  drawer.color("blue")
  drawer.write(letter, font=("Arial", 74, "bold")) 


for i in range(number_of_apples):
  apple = trtl.Turtle(shape = apple_image)
  apple.penup()
  reset_apple(apple)
  apple_list.append(apple)

      

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.



def check_apple_a():
  if ("a" in current_letters):
    apple_fall()
def check_apple_s():
  if ("s" in current_letters):
    apple_fall()
def check_apple_d():
  if ("d" in current_letters):
    apple_fall()
def check_apple_f():
  if ("f" in current_letters):
    apple_fall()
def check_apple_g():
  if ("g" in current_letters):
    apple_fall()
def check_apple_h():
  if ("h" in current_letters):
    apple_fall()
def check_apple_j():
  if ("j" in current_letters):
    apple_fall()
def check_apple_k():
  if ("k" in current_letters):
    apple_fall()
def check_apple_l():
  if ("l" in current_letters):
    apple_fall()
def check_apple_x():
  if ("x" in current_letters):
    apple_fall()
wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_x, "x")

wn.onkeypress(apple_fall, "a")

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")

wn.listen() 

trtl.mainloop()