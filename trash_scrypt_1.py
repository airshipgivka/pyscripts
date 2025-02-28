from turtle import clear, goto, speed, hideturtle, penup, pendown
from tkinter import *

class Turtle:

    def sgoto(self, start_pos, final_pos):
        penup()
        goto(start_pos[0] + self.current_pos[0], start_pos[1] + self.current_pos[1])
        pendown()
        goto(final_pos[0] + self.current_pos[0], final_pos[1] + self.current_pos[1])

    def __init__(self):

        Tkinter_instance = Tkinter()

        while True:
            
            string = input()

            self.current_pos = [-(len(string) * 50 + (len(string) - 1) * 25) / 2, 0]
        
            hideturtle()
            speed(0)
            clear()
            penup()
            goto(self.current_pos[0], self.current_pos[1])
            pendown()

            for key in string:
                match key:
                    case 'a':
                        self.sgoto([0, 0], [25, 100])
                        self.sgoto([25, 100], [50, 0])
                        self.sgoto([12.5, 50], [37.5, 50])
                    case 'b':
                        self.sgoto([0, 0], [0, 100])
                        self.sgoto([0, 50], [50, 50])
                        self.sgoto([50, 0], [50, 50])
                        self.sgoto([0, 0], [50, 0])
                current_pos = [self.current_pos[0] + 75, self.current_pos[1]]

class Tkinter:

    def __init__(self):
        window = Tk()

Turtle_instance = Turtle()

# клетка - 50 п.
