from UI.Utils.Label import Label


def SingleLineSurface(string, width, height, font, offSetX, offSetY, screenSurface, writeLineLevel):

    writeLineLevel = writeLineLevel
    label = Label(string, width, height, font)
    screenSurface.blit(label.localSurface, (offSetX, offSetY))

    writeLineLevel += 1
    return writeLineLevel