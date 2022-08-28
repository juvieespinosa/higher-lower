from flask import Flask
import random



app = Flask(__name__)


#Generate a random number
random_number = random.randint(0, 9)
print(random_number)

#The website starts with a main page
@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 15</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


#detect number entered by the user and checks that number against the generated random number
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return '<h1 style="color: pink">Too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/IrwH4Vp5codA0HldUh/giphy.gif"/>'

    elif guess < random_number:
        return '<h1 style="color: teal">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/Bc4oup2pdP5iKFAYiF/giphy.gif"/>'

    else:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'



if __name__ == "__main__":
    app.run(debug=True)