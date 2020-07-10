from pysvg.structure import Svg, G
from pysvg.text import *
from pysvg.builders import ShapeBuilder, TransformBuilder, StyleBuilder
from drawView import Honeycomb
from pysvg.shape import Rect, Circle
import math
xmove = 50*math.sqrt(3)
ymove = 50
newDoc = Svg()

#a = Honeycomb(4, 18, 37.8, 13.5)
circleStyle = StyleBuilder()
#circleStyle.setStrokeWidth(0.5)
circleStyle.setStroke('orange')
circleStyle.setFilling('#edd239')
#newDoc.addElement(a.genHoneycomb())
newTransform = TransformBuilder()
newTransform.setTranslation(str(xmove) + ' ' + str(ymove))

a = Circle(100, 100, 50)
a.set_style(circleStyle.getStyle())
b = Circle(100 + math.sqrt(3)*50,150,50)
#c = Circle
#b.set_transform(newTransform.getTransform())


newDoc.addElement(a)
newDoc.addElement(b)

newDoc.save('testgeom.svg')
