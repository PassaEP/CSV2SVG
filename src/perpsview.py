SCALING_FACTOR = 2
FRAMELEN = 200
from pysvg.builders import ShapeBuilder
from pysvg.text import *
from pysvg.structure import Svg
from pysvg.shape import *
from drawView import *
from page import *
import numpy as np
import math
from strgen import *

#check the bracket problem
class IsometricView:
    def __init__(self, x, y, z, frame):
        self.x = SCALING_FACTOR*float(x)
        self.y = SCALING_FACTOR*float(y)
        self.z = SCALING_FACTOR*float(z)
        self.frame = frame
        self.out = G()

    def CalcStart(self):
        self.start = [self.frame[0] + FRAMELEN*.4, self.frame[1] + FRAMELEN*.1]
    def makeFaces(self):
        self.transformMatrix = np.matrix([[0.866, -0.866, 0], [0.5, 0.5, 0], [0,0,1]])
        invtransform = np.linalg.inv(self.transformMatrix)
        self.topDownTransform = TransformBuilder()
        self.topDownTransform.setMatrix('0.866','0.5','-0.866','0.5','0','0')

        wantedCoords = np.array([[self.start[0]],[self.start[1]],[1]])
        self.startCoords = invtransform * wantedCoords
        topFace = Rect(float(self.startCoords[0]), float(self.startCoords[1]), self.x, self.z)

        vertTransform = np.matrix([[1, 0, 0], [0.577,1,0], [0,0,1]])

        oldYLength = np.matrix([[0],[self.y],[1]])
        # transform Y to get coords for bottom face parts
        #transformedYLengthV = vertTransform * oldYLength

        #transformedYLength = float(transformedYLengthV[1])
        points = topFace.getEdgePoints()

        self.transformedTop = []
        self.transformedBottom = []
        # get untransformed points of the top face
        i = 0
        for stuff in points:
            vector = np.matrix([[stuff[0]], [stuff[1]], [1]])
            self.transformedTop.append(self.transformMatrix * vector)
            self.transformedBottom.append([float(self.transformedTop[i][0]),float(self.transformedTop[i][1]) + self.y])
            i+=1

    def Render(self):
        XZStyle = StyleBuilder()
        XZStyle.setFilling('blue')
        XZStyle.setFillOpacity(.75)
        XZStyle.setStroke('black')
        topFace = Rect(float(self.startCoords[0]), float(self.startCoords[1]), self.x, self.z)
        topFace.set_transform(self.topDownTransform.getTransform())
        topFace.set_style(XZStyle.getStyle())
        self.out.addElement(drawSideFacePair(self.transformedTop, self.transformedBottom))
        self.out.addElement(drawFrontFacePair(self.transformedTop, self.transformedBottom))
        self.out.addElement(topFace)
        return self.out
