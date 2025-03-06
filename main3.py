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
apple_letters = {}
apple_x = rand.randint(-150,150)
apple_y = rand.randint(-40,180)
number_of_apples = 5

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(apple):
  apple.shape(apple_image)
  apple.penup()
  wn.tracer(False)
  apple.goto(apple_x,apple_y)
  apple.color("white")
  apple.penup()
  apple.goto(apple.xcor(),apple.ycor())
  apple.write(letter, font=("Arial", 20)) 
  apple.showturtle()
  wn.tracer(True)
  wn.update()

def falling_apple(letter):
    """Finds the apple with the corresponding letter and makes it fall"""
    if letter in apple_letters:
        apple = apple_letters[letter]
        apple.clear()
        apple.goto(apple.xcor(), -150)
        apple.hideturtle()
        del apple_letters[letter]  # Remove apple from dictionary

#-----function calls-----
for i in range(number_of_apples):
    letter = rand.choice(letters)  # Pick a random letter
    letters.remove(letter)  # Ensure each letter is unique

    apple_x = rand.randint(-150, 150)
    apple_y = rand.randint(-40, 180)

    apple = trtl.Turtle()
    apples.append(apple)
    apple_letters[letter] = apple  # Link apple to letter

    draw_apple(apple)

# Bind keypress events
for letter in apple_letters.keys():
  wn.onkeypress(lambda l=letter: falling_apple(l), letter)

wn.listen()

wn.mainloop()
