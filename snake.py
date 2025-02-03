from turtle import Turtle
import time

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        #segment.speed("slow")
        segment.penup()
        segment.goto(position)
        self.all_segments.append(segment)

    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
