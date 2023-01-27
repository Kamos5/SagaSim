import pygame
import matplotlib.backends.backend_agg as agg
import pylab


class Plots:

    def __init__(self,  x, y, xAxisData, *yAxisData ):

        dpi = 100
        fig = pylab.figure(figsize=[x/dpi, y/dpi],  dpi=dpi)
        ax = fig.gca()
        i = 0
        legendArray = yAxisData[0][0]
        for data in yAxisData[0]:
            if i == 0:
                i += 1
                continue
            ax.plot(xAxisData, data)
            i += 1
        ax.get_title()
        ax.set_title('TITLE')
        ax.legend(legendArray)

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()

        self.surf = pygame.image.fromstring(raw_data, size, "RGB")


    def getPlotSurface(self):

        return self.surf