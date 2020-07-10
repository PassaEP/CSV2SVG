from pysvg.structure import Svg, G
from pysvg.text import *
from pysvg.builders import ShapeBuilder, TransformBuilder, StyleBuilder
from drawView import Honeycomb
from pysvg.shape import Rect, Circle
import math
xmove = 50*math.sqrt(3)
ymove = 50
newDoc = Svg()

a = Honeycomb(4, 6)
#circleStyle = StyleBuilder()
#circleStyle.setStrokeWidth(0.5)
#circleStyle.setStroke('orange')
#circleStyle.setFilling('#edd239')
newDoc.addElement(a.genHoneyRect())
newDoc.addElement(a.genHoneycomb())
#newTransform = TransformBuilder()
#newTransform.setTranslation(str(xmove) + ' ' + str(ymove))

#a = Circle(100, 100, 50)
#a.set_style(circleStyle.getStyle())
#b = a
#b.set_transform(newTransform.getTransform())



newDoc.save('testgeom.svg')
