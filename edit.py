import xml.etree.cElementTree as et
from lib.PIL import Image

file=input(":")
data=et.parse("input/{fn}.xml".format(fn=file)).getroot()
im=Image.open("input/{fn}.png".format(fn=file))
x0=-1
y0=-1
for i in data:
    x=int(i.attrib["x"])
    y=int(i.attrib["y"])
    w=int(i.attrib["width"])
    h=int(i.attrib["height"])
    n=i.attrib["name"]
    if x!=x0 or y!=y0:
        im.crop((x,y,x+w,y+h)).save("result/{name}/{name}.png".format(name=n),"PNG")
    x0=x
    y0=y