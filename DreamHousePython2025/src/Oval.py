import tkinter as tk
from tkinter import Canvas
from Shape import Shape


class Oval(Shape):
    def __init__(self, canvas: Canvas, x: int = 20, y: int = 60, width: int = 30, height: int = 60, color: str = "blue", fill: str = None, line: int = 2, tag: str = None):
        super().__init__(canvas=canvas, x=x, y=y, color=color, fill=fill, line=line)
        self.width = width
        self.height = height

    def draw(self):
        if self.is_visible:
            print(f"Drawing Oval at ({self.x_position},{self.y_position}) width {self.width} height {self.height} color {self.color} fill {self.fill} line {self.line}")
            self.shape_id = self.canvas.create_oval(
                self.x_position, self.y_position,
                self.x_position + self.width, self.y_position + self.height,
                outline=self.color, fill=self.fill, width=self.line
            )

    def erase(self):
        if self.is_visible:
            print("Erasing Oval")
            super().erase()
