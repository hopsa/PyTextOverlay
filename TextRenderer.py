import cairo

class TextRenderer:
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        self.surface=cairo.SVGSurface("example.svg", cols, rows)
        return
    def printText(self):
        #generic cairo usage example
        context = cairo.Context(self.surface)
        x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
        x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
        context.scale(self.cols, self.rows)
        context.set_line_width(0.04)
        context.move_to(x, y)
        context.curve_to(x1, y1, x2, y2, x3, y3)
        context.stroke()
        context.set_source_rgba(1, 0.2, 0.2, 0.6)
        context.set_line_width(0.02)
        context.move_to(x, y)
        context.line_to(x1, y1)
        context.move_to(x2, y2)
        context.line_to(x3, y3)
        context.stroke()
        context.show_text("example")
        context.stroke()
