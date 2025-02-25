from manim import *
#class DefaultTemplate(Scene):
#    def construct(self):
#        circle = Circle()  # create a circle
#        circle.set_fill(PINK, opacity=0.5)  # set color and transparency
#
#        square = Square()  # create a square
#        square.flip(RIGHT)  # flip horizontally
#        square.rotate(-3 * TAU / 8)  # rotate a certain amount
#
#        self.play(Create(square))  # animate the creation of the square
#        self.play(Transform(square, circle))  # interpolate the square into the circle
#        self.play(FadeOut(square))  # fade out animation

class CircleExplanation(Scene):
    def construct(self):
        
        ax = Axes(
            axis_config={'tip_shape': StealthTip},
            x_length=7.8,
            y_length=7.8,
            x_range=(-1.2,1.2,0.5),
            y_range=(-1.2,1.2,0.5))
        self.play(Create(ax))



        c = Circle(radius=3.25,color=PURPLE)        
        self.play(Create(c))



        radius = Line(
            start=ax.coords_to_point(0,0),
            end=c.point_at_angle(0.6),
            stroke_width=8
        )
        self.play(Create(radius))




        self.play(Rotate(radius,about_point=ax.coords_to_point(0,0),angle=2*PI,run_time=2))
        



        xPart = Line(
            start=ax.coords_to_point(0,0),
            end=[c.point_at_angle(0.6)[0],ax.coords_to_point(0,0)[1],0],
            color=RED,
            stroke_width=8
        )
        yPart = Line(
            start=xPart.end,
            end=[xPart.end[0],c.point_at_angle(0.6)[1],0],
            color=BLUE,
            stroke_width=8
        )
        self.play(Create(xPart),Create(yPart))


        graphics = Group(ax,c,radius,xPart,yPart)
        graphics.generate_target()
        graphics.target.shift(3*RIGHT)
        self.play(MoveToTarget(graphics))

        t = MathTex()
        #self.add(t)

        self.wait()