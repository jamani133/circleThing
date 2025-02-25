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
        self.wait()
        self.next_section()
        ax = Axes(
            axis_config={'tip_shape': StealthTip},
            x_length=7.8,
            y_length=7.8,
            x_range=(-1.2,1.2,0.5),
            y_range=(-1.2,1.2,0.5))
        self.play(Create(ax))
        self.next_section()


        c = Circle(radius=3.25,color=PURPLE)        
        self.play(Create(c))
        self.next_section()


        radius = Line(
            start=ax.coords_to_point(0,0),
            end=c.point_at_angle(0.6),
            stroke_width=8
        )
        self.play(Create(radius))
        self.next_section()



        self.play(Rotate(radius,about_point=ax.coords_to_point(0,0),angle=2*PI,run_time=2))
        self.next_section()



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
        self.next_section()


        cred = Arc(arc_center=[3,0,0],stroke_width=8,radius=3.25, start_angle=0, angle=PI,color=RED)
        cblue  = Arc(arc_center=[3,0,0],stroke_width=8,radius=3.25, start_angle=PI, angle=PI,color=BLUE)


        graphics = Group(ax,c,radius,xPart,yPart)
        graphics.generate_target()
        graphics.target.shift(3*RIGHT)
        self.play(MoveToTarget(graphics))
        self.next_section()
        eq1 = MathTex(r"a^{2}+b^{2}=c^{2}",color=RED)
        eq2 = MathTex(r"y^{2}+x^{2}=r^{2}")
        eq3 = MathTex(r"y^{2}=r^{2}-x^{2}")
        eq4 = MathTex(r"f\left(x\right)=\sqrt{r^{2}-x^{2}}",color=GREEN_C)
        equations = Group(eq1,eq2,eq3,eq4)
        equations.arrange_in_grid(rows=4,cols=1,buff=0.5,col_alignments="l")
        equations.shift(4*LEFT+1.5*UP)
        self.play(Create(eq1,run_time=0.25))
        self.next_section()
        self.play(Create(eq2,run_time=0.25))
        self.next_section()
        self.play(Create(eq3,run_time=0.25))
        self.next_section()
        self.play(Create(eq4,run_time=0.25))

        self.next_section()
        xPart.set_opacity(0.3)
        yPart.set_opacity(0.3)
        radius.set_opacity(0.3)
        self.play(Create(cred),Create(cblue))
        self.next_section()
        self.play(FadeOut(c),FadeOut(cblue),FadeOut(xPart),FadeOut(yPart),FadeOut(radius),FadeOut(equations,shift=LEFT))
        eqi1 = MathTex(r"V\left(r\right)=\pi\int_{-r}^{r}f\left(x\right)^{2}dx",color=RED,font_size=30)
        eqi2 = MathTex(r"V\left(r\right)=\pi\int_{-r}^{r}\left(\sqrt{r^{2}-x^{2}}\right)^{2}dx",font_size=30)
        eqi3 = MathTex(r"V\left(r\right)=2\pi\int_{-r}^{r}\left(r^{2}-x^{2}\right)dx",font_size=30)
        eqi4 = MathTex(r"V\left(r\right)=2\pi\cdot\left[r^{2}-\frac{1}{3}x^{3}\right]_{-r}^{r}",font_size=30)
        eqi5 = MathTex(r"V\left(r\right)=2\pi\cdot\left[r^{2}-\frac{1}{3}r^{3}\right]-\left[r^{2}+\frac{1}{3}r^{3}\right]",font_size=30)
        eqi6 = MathTex(r"V\left(r\right)=2\pi\cdot\left[-\frac{1}{3}r^{3}\right]-\left[\frac{1}{3}r^{3}\right]",font_size=30)
        eqi7 = MathTex(r"V\left(r\right)=\frac{4}{3}\pi r^{3}",color=GREEN_C)

        equationsi = Group(eqi1,eqi2,eqi3,eqi4,eqi5,eqi6,eqi7)
        equationsi.arrange_in_grid(rows=7,cols=1,buff=0.25,col_alignments="l")
        equationsi.shift(LEFT*3.5)
        self.next_section()
        self.play(Create(eqi1,run_time=0.25))
        self.next_section()
        self.play(Create(eqi2,run_time=0.25))
        self.next_section()
        self.play(Create(eqi3,run_time=0.25))
        self.next_section()
        self.play(Create(eqi4,run_time=0.25))
        self.next_section()
        self.play(Create(eqi5,run_time=0.25))
        self.next_section()
        self.play(Create(eqi6,run_time=0.25))
        self.next_section()
        self.play(Create(eqi7,run_time=0.25))

        self.next_section()

        self.play(FadeOut(ax),FadeOut(cred),FadeOut(equationsi,shift=LEFT))