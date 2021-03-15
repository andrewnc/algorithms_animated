import manim


class SquareToCircle(manim.Scene):
    def construct(self):
        circle = manim.Circle()
        square = manim.Square()
        square.flip(manim.RIGHT)
        square.rotate(-3 * manim.TAU / 8)
        circle.set_fill(manim.PINK, opacity=0.5)

        self.play(manim.ShowCreation(square))
        self.play(manim.Transform(square, circle))
        self.play(manim.FadeOut(square))
