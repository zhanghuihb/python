from fontTools.ttLib import TTFont
def read():
    font_name = {}
    font_list = ["74ff4990.woff"]
    for item in font_list:
        font = TTFont(item)
        # font_names = font.getGlyphOrder()
        font_names = font.getGlyphNames()
        print(font_names)
        # getXml(item)

def getXml(item):
    font = TTFont(item)
    font.saveXML('74ff4990.xml')

if __name__ == "__main__":
    read()