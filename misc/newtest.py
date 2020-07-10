# test script
# see how the class works

from drawView import *
from pysvg.structure import Svg
a = Slice(100, 100, 'x', 'y')
b = Slice(200, 200, 'x','z')
c = Slice(100, 200, 'y', 'z')
d = NewPrism(100, 100, 200)

a.calcPositionXY()
b.calcPositionXZ()
c.calcPositionYZ()

newDocument = Svg()
newDocument.addElement(a.draw())
newDocument.addElement(b.draw())
newDocument.addElement(c.draw())
views = a.genAxis()

for stuff in views:
    newDocument.addElement(stuff)
views = b.genAxis()
for stuff in views:
    newDocument.addElement(stuff)
views = c.genAxis()
for stuff in views:
    newDocument.addElement(stuff)
prism = d.drawPrism()
for stuff in prism:
    newDocument.addElement(stuff)

newDocument.save('newOne.svg')
