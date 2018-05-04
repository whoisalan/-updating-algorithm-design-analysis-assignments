from PIL import Image
from PIL.ExifTags import TAGS
import os
import pygal


def get_exif_data(fname):
    f = open('./test.txt', 'w')

    for name in os.listdir(fname):
        if not name.startswith("."):
            path = fname + "//" + name
            img = Image.open(path)
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag,value in exifinfo.items():   
                    decoded = TAGS.get(tag, tag)
                    if(decoded == "Model"):
                        f.writelines(value+"\n")
    f.close()
    print("done")


#画图
def drawPic(ftxt):
    content = {}
    f = open(ftxt)
    line = f.readline()
    while line:
        a = line.strip("\n")
        if a not in content:
            content[a]= 0
        content[a] += 1
        line = f.readline()

    pie_chart = pygal.Pie()
    pie_chart.title = 'Phone model'

    for word, val in content.items():
        pie_chart.add(word,val)
    pie_chart.render_to_file('./a.svg')


if __name__ == '__main__':
    fileName = '/Users/iCloud/Desktop/作业/img'
    get_exif_data(fileName)
    drawPic("./test.txt")
