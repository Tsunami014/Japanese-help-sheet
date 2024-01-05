import pygame

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
    
    def update(self):
        """
        Updates the window

        Returns
        -------
        bool
            Whether the loop should continue or not (e.g. user closed window)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        self.win.fill((255, 255, 255))
        pygame.display.update()
        return True
    
    def quit(self):
        pygame.quit()
