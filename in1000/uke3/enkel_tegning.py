# 03.04: Enkel tegning

from ezgraphics import GraphicsWindow

window = GraphicsWindow()
nytt_canvas = window.canvas()
nytt_canvas.drawRect(50, 50, 50, 100) # x, y, width, height
window.wait()
