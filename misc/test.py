from pysvg.structure import Svg, G
from pysvg.text import *
from pysvg.builders import ShapeBuilder, TransformBuilder, StyleBuilder
from drawView import Honeycomb
from pysvg.shape import Rect

cat = Svg()


testRect = ShapeBuilder()
a = testRect.createRect(100, 100, 50, 50, strokewidth=2, fill='#edd239', stroke='black')

move = TransformBuilder()
move.setTranslation('50 50')

styleSet = StyleBuilder()
styleSet.setStrokeWidth(2)
styleSet.setStroke('black')
styleSet.setFilling('blue')
r = Rect(100, 100, 50, 50)


r.set_style(styleSet.getStyle())
r.set_transform(move.getTransform())
styleSet.setFilling('red')
move.setTranslation('0 50')
s = Rect(100, 100, 50, 50)
#s.set_style(styleSet.getStyle())
s.set_transform(move.getTransform())







cat.addElement(a)
cat.addElement(s)
cat.addElement(r)




cat.save('transform.svg')
