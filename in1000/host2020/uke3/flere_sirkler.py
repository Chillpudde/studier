# 03.09: Flere flere sirkler

from ezgraphics import GraphicsWindow

window = GraphicsWindow()
nytt_canvas = window.canvas()
nytt_canvas.drawOval(20, 20, 50, 50)
nytt_canvas.drawOval(120, 20, 50, 50)
nytt_canvas.drawOval(220, 20, 50, 50)
nytt_canvas.drawOval(320, 60, 50, 70)
window.wait()
