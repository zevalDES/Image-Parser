import xml.etree.cElementTree as et
from lib.PIL import Image
import os
import io

curDir=os.path.dirname(__file__)
os.system("cd "+curDir)
os.system("pwd")
os.system("echo "+curDir)
txt=io.open("{dir}/input/list.txt".format(dir=curDir))
files=[]
while True:
    line=txt.readline()
    if line!="":
        files.append(line[0:len(line)-1])
        break
print(files)


if not os.path.exists("input"):
    os.system("mkdir input")
if os.path.exists("result"):
    os.system("rm -r result")
os.system("mkdir result")

for file in files:
    os.system("mkdir result/{fn}".format(fn=file))
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
            im.crop((x,y,x+w,y+h)).save("result/{fn}/{name}.png".format(fn=file,name=n),"PNG")
        x0=x
        y0=y