import pygame
import matplotlib.backends.backend_agg as agg
import pylab


class Plots:

    def __init__(self, xAxisData, yAxisData , x, y):

        dpi = 100
        fig = pylab.figure(figsize=[x/dpi, y/dpi],  dpi=dpi)
        ax = fig.gca()
        ax.plot(xAxisData, yAxisData)

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()

        self.surf = pygame.image.fromstring(raw_data, size, "RGB")


    def getPlotSurface(self):

        return self.surf