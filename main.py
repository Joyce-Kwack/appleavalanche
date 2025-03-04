#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple_x = rand.randint(-40,50)
apple_y = rand.randint(-40,50)
letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
apples = []
random_number = rand.randint(0,8)
random_letter = letters.pop(random_number)
print(random_letter)
number_of_apples = len(letters)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  if letters:
    active_apple.shape(apple_image)
    active_apple.penup()
    active_apple.goto(apple_x,apple_y)
  wn.update()
def draw_letter():
  apple.color("white")
  apple.penup()
  apple.goto(apple_x,apple_y)
  apple.write(random_letter, font=("Arial", 20)) 
def falling_apple():
  apple.penup()
  apple.goto(apple_x,-150)
  apple.clear()
  apple.hideturtle()
def reset_apple():
  apple.goto(apple_x,apple_y)
  draw_apple(apple)

#-----function calls-----
draw_apple(apple)
wn.tracer(False)
draw_letter()
wn.tracer(True)
wn.onkeypress(falling_apple,random_letter)
reset_apple()

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 

#TODO Create a function that draws a new letter from the letter list.

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
'''for i in range(0, number_of_apples):'''
  #Your code here

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

wn.mainloop()