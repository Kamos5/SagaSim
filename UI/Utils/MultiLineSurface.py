from UI.Utils.Label import Label
from UI.Utils.MultiLineLabel import MultiLineLabel


def MultiLineSurface(string, width, height, font, offSetX, offSetY, screenSurface, writeLineLevel):
    lineHeight = height
    screenSurface = screenSurface
    writeLineLevel = writeLineLevel
    words = [word.split(' ') for word in string.splitlines()]
    tempLine = ""
    lineTypeIndex = 0
    lineCount = 0
    sumOfWordSizes = 0

    for line in words:
        for word in line:
            tempLine += word + " "
            for letter in word:
                sumOfWordSizes += font.size(letter)[0]
            sumOfWordSizes += font.size(" ")[0]
            if sumOfWordSizes >= width:
                if lineTypeIndex == 2:
                    lineTypeIndex = 1
                tempLine = tempLine[:-len(word) - 1].rstrip()
                label = MultiLineLabel(str(tempLine), width, height, font, lineTypeIndex)
                screenSurface.blit(label.localSurface, (offSetX, offSetY + lineCount * lineHeight))
                writeLineLevel += 1
                lineCount += 1
                tempLine = word + " "
                lineTypeIndex += 1
                sumOfWordSizes = 0
                for letter in word:
                    sumOfWordSizes += font.size(letter)[0]
                sumOfWordSizes += font.size(" ")[0]

    if lineTypeIndex == 0:
        label = Label(str(tempLine), width, height, font, lineTypeIndex)
        screenSurface.blit(label.localSurface, (offSetX, offSetY + lineHeight * lineCount))
        writeLineLevel += 1
        return writeLineLevel
    if lineTypeIndex == 1:
        label = MultiLineLabel(str(tempLine), width, height, font, lineTypeIndex + 1)
        screenSurface.blit(label.localSurface, (offSetX, offSetY + lineHeight * lineCount))
        writeLineLevel += 1
        return writeLineLevel
    if lineTypeIndex == 2:
        label = MultiLineLabel(str(tempLine), width, height, font, lineTypeIndex)
        screenSurface.blit(label.localSurface, (offSetX, offSetY + lineHeight * lineCount))
        writeLineLevel += 1
        return writeLineLevel