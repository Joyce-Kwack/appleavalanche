#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
# makes lists of letters and apples
letters = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
apples = []
number_of_apples = 5
random_letter = letters.pop(rand.randint(0,len(apples)))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  active_apple.penup()
  active_apple.goto(rand.randint(-200,200),rand.randint(-40,200))
  wn.update()

def draw_letter():
  apple.color("white")
  apple.penup()
  apple.goto(apple.xcor(),apple.ycor()-20)
  apple.write(random_letter, font=("Arial", 20)) 

def falling_apple():
  apple.penup()
  apple.goto(apple.xcor(),-150)
  apple.clear()
  apple.hideturtle()

def reset_apple():
  if letters:
    apple.goto(rand.randint(-200,200),rand.randint(-40,200))
  else:
    print("No letters left :(")

#-----function calls-----
for i in range(0, number_of_apples):
  apple = trtl.Turtle()
  apples.append(apple)
  draw_apple(apple)
  wn.tracer(False)
  draw_letter()
  wn.tracer(True)
  wn.onkeypress(falling_apple,random_letter)
  reset_apple()

wn.listen()

wn.mainloop()

'''make an apple
get a random letter from the list that still exists
draw that letter in the apple
repeat 5 times with different letters and positions
if user presses the right letter, apple falls
a new apple resets and goes to a new position with a new letter
if letters run out, no more apples'''
