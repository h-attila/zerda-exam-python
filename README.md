# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

Define 'count_letter_in_string' function with 'string', 'letter' parameters
    If 'string' type is not string:
        Set return value to 0 and exit from function
    Define 'count' variable by starting value 0
    Iterating on the 'sting' characters
        If current letter (=the actual character in the string) equals to the searched 'letter'
            Increment 'count' by 1
    Return the 'count' value


### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

Wee need to do the following steps:
1. First we need import the Python Tkinter drawing module: 'from tkinter import *'

2. need to create a blank canvas. It has three steps: (1) creating a root variable for graphics, (2) define the canvas, (3) draw it (or create it)

    root = Tk()
    my_canvas = Canvas(root, width=300, height=300, bg='white')
    my_canvas.pack()


3. need to draw someting, eg. a rectancle:
    my_canvas.create_rectangle(x1, y1, x2, y2, fill='white', width='1')

4. need update the graphics to show:
    my_canvas.update()

5. and finally we have to keep the canvas visible. Without this the canvas will shown only few moments:

    my_canvas.mainloop()



### What does V stand for in MVC? [2p]
#### Your answer:

V is the name os View module on MVC. It is responsible for the the graphical interface that the user can see on the screen.
It contains graphical functions, elements (eg. canvas, button, displax boxes, etc)
It gets all the information from the Controller module, and typically not contains business logic calculation inside or only
minimal which is neccessary for the graphical design.
