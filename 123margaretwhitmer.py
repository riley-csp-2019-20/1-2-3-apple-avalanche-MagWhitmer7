#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

#apple = trtl.Turtle()

letter_list = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "x"]

current_letters = []

apple_list = []

number_of_apples = 5

# given a turtle, set that turtle to be shaped by the image file
#def draw_apple(active_apple):
  #active_apple.shape(apple_image)
  #wn.update()

#draw_apple(apple)

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")

def apple_fall():
  index = current_letters.index(letter)
  current_letters.pop(index)
  apple = apple_list.pop(index)
  apple.showturtle()
  apple.penup()
  apple.goto(0,-150)
  drawer.clear()
  corner_drawer.clear()
  apple.hideturtle()
  apple_list.append(apple)
  move_apple()


drawer = trtl.Turtle()
drawer.hideturtle()
# This function takes care of font and color.

def draw_the_letter():
  drawer.color("blue")
  drawer.penup()
  drawer.write(current_letters, font=("Arial", 74, "bold")) 

def reset_apple():
    new_xpos= rand.randint(-100,100)
    new_ypos= rand.randint(-50,50)
    apple.goto(new_xpos, new_ypos)

for i in range(number_of_apples):
  apple = trtl.Turtle(shape = apple_image)
  apple.penup()
  reset_apple()
  apple_list.append(apple)

# this tells the user what letter to type

corner_drawer = trtl.Turtle()
corner_drawer.hideturtle()
def letter_to_type():
  random = rand.randint(0, len(letter_list))
  current_letters.append(letter_list[random])
  corner_drawer.color("black")
  corner_drawer.penup()
  corner_drawer.goto(0,100)
  corner_drawer.write(current_letters, font=("Arial", 74, "bold"))

#TODO Create a function that draws a new letter from the letter list.


#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 

def move_apple():
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    letter_to_type()
    apple.showturtle()
    apple.penup()
    reset_apple()
      

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

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
'''
for i in range(0, number_of_apples):
  #Your code here
'''
#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter 
# to disappear. Call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.



#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.


wn.listen() 

trtl.mainloop()