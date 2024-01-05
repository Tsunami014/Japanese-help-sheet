import pygame
from utils import statics

class Bar:
    def __init__(self, position, win, colour=(155, 155, 155), thickness=50, callback=None, add=True):
        """
        _summary_

        Parameters
        ----------
        position : utils.statics.P_____
            The position of the bar
        win : utils.rendering.Window
            The window to add this bar to
        colour : tuple, optional
            The colour of the bar, by default (155, 155, 155)
        thickness : int, optional
            The thickness of the bar, by default 50
        callback : function, optional
            When this bar is updated, calls this function so you can do things like add buttons and stuff to the bar, by default None
            this function is called as follows: `func(events, barRect, winSurface)`
        add : bool, optional
            Whether or not to add this bar to the window so it can actually GET updated in the FIRST PLACE, by default True
        """
        assert position in [statics.PTOP, statics.PBOTTOM, statics.PLEFT, statics.PRIGHT], "Invalid position, must be utils.statics.P_____"
        self.win = win
        self.colour = colour
        self.position = position
        self.thickness = thickness
        self.callback = callback
        if add:
            self.win.bars.append(self)
    
    def update(self, events):
        if self.position == statics.PTOP:
            r = pygame.Rect(0, 0, self.win.win.get_width(), self.thickness)
        elif self.position == statics.PBOTTOM:
            r = pygame.Rect(0, self.win.win.get_height() - self.thickness, self.win.win.get_width(), self.thickness)
        elif self.position == statics.PLEFT:
            r = pygame.Rect(0, 0, self.thickness, self.win.win.get_height())
        elif self.position == statics.PRIGHT:
            r = pygame.Rect(self.win.win.get_width() - self.thickness, 0, self.thickness, self.win.win.get_height())
        self.win.win.fill(self.colour, r)
        if self.callback != None: self.callback(events, r, self.win.win)

class Window:
    def __init__(self, size=(0, 0), win=None):
        """
        This is a class that holds a window

        Parameters
        ----------
        size : tuple, optional
            The size of the window, by default (0, 0), only used if win is None
        win : pygame.Surface, optional
            If this is None it initialises pygame and creates a window of size `size`, else it uses this, by default None
        """
        if win is None:
            pygame.init()
            self.win = pygame.display.set_mode(size)
        else:
            self.win = win
        self.bars = []
    
    def add_bar(self, position, colour=(155, 155, 155), thickness=50, callback=None):
        """
        Adds a bar to the window

        Parameters
        ----------
        position : utils.statics.P_____
            The position of the bar
        colour : tuple, optional
            The colour of the bar, by default (155, 155, 155)
        thickness : int, optional
            The thickness of the bar, by default 50
        callback : function, optional
            When this bar is updated, calls this function so you can do things like add buttons and stuff to the bar, by default None
            this function is called as follows: `func(events, barRect, winSurface)`
        """
        self.bars.append(Bar(position, self, colour, thickness, callback, False))
    
    def update(self):
        """
        Updates the window

        Returns
        -------
        bool
            Whether the loop should continue or not (e.g. user closed window)
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        self.win.fill((255, 255, 255))
        for bar in self.bars:
            bar.update(events)
        pygame.display.update()
        return True
    
    def quit(self):
        pygame.quit()
