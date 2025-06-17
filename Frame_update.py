import tkinter as tk

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, radius=25, **kwargs):
        super().__init__(parent, **kwargs)
        self.radius = radius
        self.create_rounded_rectangle(0, 0, self.winfo_reqwidth(), self.winfo_reqheight(), self.radius, fill=kwargs.get('bg'))

    def create_rounded_rectangle(self, x1, y1, x2, y2, r, **kwargs):
        # Создаем закругленный прямоугольник
        self.create_arc(x1, y1, x1 + r * 2, y1 + r * 2, start=90, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
        self.create_arc(x2 - r * 2, y1, x2, y1 + r * 2, start=0, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
        self.create_arc(x1, y2 - r * 2, x1 + r * 2, y2, start=180, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
        self.create_arc(x2 - r * 2, y2 - r * 2, x2, y2, start=270, extent=90, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
        self.create_rectangle(x1 + r, y1, x2 - r, y2, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
        self.create_rectangle(x1, y1 + r, x2, y2 - r, fill=kwargs.get('fill'), outline=kwargs.get('outline'))
