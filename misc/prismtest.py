from pysvg.structure import Svg, G
from pysvg.text import *
from pysvg.builders import ShapeBuilder, TransformBuilder, StyleBuilder
from drawView import Honeycomb
from pysvg.shape import Rect, Polygon, Polyline, Line

cat = Svg()
a1 = Line(30, 30, 20, 20)
a2 = Line(30, 30, 35, 30)
a3 = Line(35, 30, 25, 20)
a4 = Line(25,20,20,20)

b = Polyline(a1)
c = Polyline(a2)
d = Polyline(a3)
e = Polyline(a4)

f = Polygon(b)


cat.addElement(f)
cat.save('prismtest.svg')
