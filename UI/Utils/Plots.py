import matplotlib.pyplot
import pygame
import matplotlib.backends.backend_agg as agg
import pylab
from matplotlib.ticker import LinearLocator


class Plots:

    def __init__(self,  x, y, title, xLabel, yLabel, xAxisData, yAxisLabel, yAxisLabelColor, *yAxisData, dummyWeatherFlag=False):

        dpi = 100
        fig = pylab.figure(figsize=[x/dpi, y/dpi],  dpi=dpi, facecolor='#aaaaaa')
        ax = fig.gca()
        ax.set_facecolor('#221f22')
        i = 0

        if dummyWeatherFlag:
            dummy, = ax.plot([500, 501, 502, 503, 504], ['normal weather', 'mild cataclysm', 'medium cataclysm', 'strong cataclysm', 'extreme cataclysm'])
            dummy.remove()

        for data in yAxisData[0]:
            ax.plot(xAxisData, data, label='Label' + str(i), linestyle='--', color=yAxisLabelColor[i], linewidth=1)
            i += 1
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
        # ax.set_xticklabels(xAxisData, rotation=45)
        ax.get_xaxis().set_major_locator(LinearLocator(numticks=15))
        matplotlib.pyplot.xlabel(xLabel)
        matplotlib.pyplot.ylabel(yLabel)
        matplotlib.pyplot.title(title)
        if len(yAxisLabel) > 0:
            matplotlib.pyplot.legend(yAxisLabel)

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        size = canvas.get_width_height()

        self.surf = pygame.image.fromstring(raw_data, size, "RGB")

    def getPlotSurface(self):

        return self.surf

    def closePlot(self):
        matplotlib.pyplot.close()
