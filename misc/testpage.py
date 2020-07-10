from pysvg.builders import ShapeBuilder
from pysvg.text import *
from pysvg.structure import Svg
from pysvg.shape import *
from drawView import *
from page import *
import numpy as np
import math
from strgen import *

newfile = Svg()
topStyle = StyleBuilder()
topStyle.setStroke('black')
topStyle.setFilling('yellow')
topDownTransform = TransformBuilder()
topDownTransform.setMatrix('0.866','0.5','-0.866','0.5','0','0')
transformMatrix = np.matrix([[0.866, -0.866, 0], [0.5, 0.5, 0], [0,0,1]])
invtransform = np.linalg.inv(transformMatrix)
Obj = StyleBuilder()
Obj.setStrokeWidth(2)
Obj.setStroke('black')
wantedCoords = np.array([[30],[30],[1]])

startCoords = invtransform * wantedCoords
#print (startCoords)

#topDownTransform.setRotation('-30 60 58.66')
marker = Circle(30, 30, 2)



#newfile.addElement(frames.makerow())
TopDown = Rect(float(startCoords[0]), float(startCoords[1]), 20, 20)
TopDown.set_transform(topDownTransform.getTransform())
TopDown.set_style(topStyle.getStyle())
points = TopDown.getEdgePoints()
transformedPoints = []
transformMatrix2 = np.matrix([[0.866, -0.866], [0.5, 0.5]])



for stuff in points:
    vector = np.matrix([[stuff[0]], [stuff[1]], [1]])
    transformedPoints.append(transformMatrix * vector)


#marker2 = Circle(a[0], a[1], 2)
#xySlice = Slice(17.893, 6.75, frames.rowCoords[0], 'red')
#xySlice.calcPosition()
marker2 = Circle(float(transformedPoints[0][0]), float(transformedPoints[0][1]), 2)
marker3 = Circle(float(transformedPoints[1][0]), float(transformedPoints[1][1]), 2)
marker4 = Circle(float(transformedPoints[2][0]), float(transformedPoints[2][1]), 2)
marker5 = Circle(float(transformedPoints[3][0]), float(transformedPoints[3][1]), 2)
newTransformedPoints = transformedPoints.tolist()
pathString = strPathStart(transformedPoints[2])
newCoords = [float(transformedPoints[2][0]), float(transformedPoints[2][1]) + 10]

newString = pathString + strPathPoint(newCoords)
print(newString)

newObj = Path(newString)

newObj.set_style(Obj.getStyle())
#print(transformedPoints)
newfile.addElement(TopDown)
#newfile.addElement(marker)
newfile.addElement(marker2)
newfile.addElement(marker3)
newfile.addElement(newObj)
newfile.addElement(marker4)
newfile.addElement(marker5)
newfile.save('topdown.svg')
