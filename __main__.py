from utils.rendering import Window
from utils import statics

win = Window()
win.add_bar(statics.PRIGHT)

r = True
while r:
    r = win.update()
win.quit()
