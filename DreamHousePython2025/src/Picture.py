import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from Oval import Oval
from RightTriangle import RightTriangle

class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='lightblue')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall1 = None
        self.wall2 = None
        self.window1 = None
        self.window2 = None
        self.roof = None
        self.sun = None
        self.garage = None
        self.garagewindow = None
        self.garageroof = None
        self.driveway = None
        self.car = None
        self.carwindow = None
        self.wheel1 = None
        self.wheel2 = None


        self.draw()

    def draw(self):
        self.wall1 = Square(canvas=self.canvas, size=100, color="black", fill="brown4", line=2)
        self.wall1.move_horizontal(237)
        self.wall1.move_vertical(200)
        self.wall1.make_visible()

        self.garage = Square(canvas=self.canvas, size=75, color="black", fill="antiquewhite", line=2)
        self.garage.move_horizontal(255)
        self.garage.move_vertical(250)
        self.garage.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=100, width=200, color="black", fill="burlywood4", line=2)
        self.roof.move_horizontal(44)
        self.roof.move_vertical(234)
        self.roof.make_visible()

        self.garageroof = Triangle(canvas=self.canvas, height=50, width=91, color="black", fill="burlywood4", line=2)
        self.garageroof.move_horizontal(253)
        self.garageroof.move_vertical(234)
        self.garageroof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=100, color="black", fill="yellow", line=1)
        self.sun.move_horizontal(500)
        self.sun.move_vertical(-50)
        self.sun.make_visible()

        self.wall2 = Rectangle (canvas=self.canvas, width=200, height=100, color="black", fill="brown4", line=1)
        self.wall2.move_horizontal(35)
        self.wall2.move_vertical(200)
        self.wall2.make_visible()

        self.window1 = Square(canvas=self.canvas, size=35, color="black", fill="snow", line=1)
        self.window1.move_horizontal(170)
        self.window1.move_vertical(221)
        self.window1.make_visible()

        self.window2 = Square(canvas=self.canvas, size=35, color="black", fill="snow", line=1)
        self.window2.move_horizontal(60)
        self.window2.move_vertical(221)
        self.window2.make_visible()

        self.garagewindow = Circle(canvas=self.canvas, diameter=20, color="black", fill="snow", line=1)
        self.garagewindow.move_horizontal(320)
        self.garagewindow.move_vertical(200)
        self.garagewindow.make_visible()

        self.door = Rectangle (canvas=self.canvas, width=30, height=50, color="black", fill="royalblue4", line=1)
        self.door.move_horizontal(116)
        self.door.move_vertical(250)
        self.door.make_visible()

        self.driveway = Rectangle (canvas=self.canvas, width=300, height=190, color="black", fill="gray67", line=1)
        self.driveway.move_horizontal(255)
        self.driveway.move_vertical(290)
        self.driveway.make_visible()

        self.car = Oval (canvas=self.canvas, width=100, height=50, color="black", fill="indianred", line=1)
        self.car.move_horizontal(400)
        self.car.move_vertical(230)
        self.car.make_visible()

        self.carwindow = RightTriangle(canvas=self.canvas, height=20, width=25, color="black", fill="antiquewhite", line=2)
        self.carwindow.move_horizontal(420)
        self.carwindow.move_vertical(300)
        self.carwindow.make_visible()

        self.wheel1 = Circle(canvas=self.canvas, diameter=20, color="black", fill="gray16", line=1)
        self.wheel1.move_horizontal(400)
        self.wheel1.move_vertical(265)
        self.wheel1.make_visible()

        self.wheel2 = Circle(canvas=self.canvas, diameter=20, color="black", fill="gray16", line=1)
        self.wheel2.move_horizontal(480)
        self.wheel2.move_vertical(265)
        self.wheel2.make_visible()

        self.grass = Rectangle (canvas=self.canvas, height=200, width=35000, color="springgreen4", fill="springgreen4", line=1)
        self.grass.move_horizontal(-56)
        self.grass.move_vertical(300)
        self.grass.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
