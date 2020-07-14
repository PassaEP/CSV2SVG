SCALING_FACTOR = 2
FRAMELEN = 200
AXIS_LENGTH = 35
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
    def __init__(self, x, y, z, frame, angle):
        self.x = SCALING_FACTOR*float(x)
        self.y = SCALING_FACTOR*float(y)
        self.z = SCALING_FACTOR*float(z)
        self.angle = float(angle)

        self.frame = frame
        self.out = G()
        # figure out the aspect ratio stuff
        self.syms = {'red': 'x', 'blue': 'y', 'green': 'z'}
        self.dimDict = {'red': self.x / SCALING_FACTOR, 'blue': self.y / SCALING_FACTOR, 'green': self.z/SCALING_FACTOR}
        dims = [self.x, self.y, self.z]
        areas = [self. x * self.z, self.x * self.y, self.y*self.z]
        dimPairs = [[self.x, self.z], [self.x, self.y], [self.y,self.z]]
        colors = ['blue', 'green', 'red']
        largestFace = max(areas)
        index = areas.index(largestFace)
        self.topDims = dimPairs[index]
        dims.remove(self.topDims[0])
        dims.remove(self.topDims[1])
        self.height = dims[0]
        self.topColor = colors[index]
        self.sideColors = colors[areas.index(self.height*self.topDims[0])]
        self.frontColors = colors[areas.index(self.height*self.topDims[1])]
        # initializing transformation matrices

        a = math.cos(self.angle)
        b = math.sin(self.angle)
        c = math.tan(self.angle)

        
        self.transformMatrix = np.matrix([[0.866, -0.866, 0], [0.5, 0.5, 0], [0,0,1]])
        self.invtransform = np.linalg.inv(self.transformMatrix)
        self.topDownTransform = TransformBuilder()
        self.topDownTransform.setMatrix('0.866','0.5','-0.866','0.5','0','0')



    def CalcStart(self):
        transformedMidpoint = np.array([[self.frame[0] + FRAMELEN/2], [self.frame[1] + FRAMELEN/2], [1]])
        untransformedMidpoint = self.invtransform * transformedMidpoint

        # getting bottom left to start initializing rectangle
        self.startCoords = [float(untransformedMidpoint[0]) - 0.5*self.topDims[0], float(untransformedMidpoint[1]) - 0.5*self.topDims[1]]





    def makeFaces(self):
        #wantedCoords = np.array([[self.start[0]],[self.start[1]],[1]])
        #self.startCoords = self.invtransform * wantedCoords
        topFace = Rect(float(self.startCoords[0]), float(self.startCoords[1]), self.topDims[0], self.topDims[1])

        vertTransform = np.matrix([[1, 0, 0], [0.577,1,0], [0,0,1]])

        oldYLength = np.matrix([[0],[self.height],[1]])
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
            self.transformedBottom.append([float(self.transformedTop[i][0]),float(self.transformedTop[i][1]) + self.height])
            i+=1

    def genAxisLabels(self):
        outLabel = G()
        leftArmStart = [self.frame[0] + 0.8*FRAMELEN, self.frame[1] + 0.1*FRAMELEN]
        # setting style
        leftStyle = StyleBuilder()
        leftStyle.setStroke(self.sideColors)
        leftStyle.setStrokeWidth(0.5)
        downStyle = StyleBuilder()
        downStyle.setStroke(self.topColor)
        downStyle.setStrokeWidth(0.5)
        rightStyle = StyleBuilder()
        rightStyle.setStroke(self.frontColors)
        rightStyle.setStrokeWidth(0.5)

        labelStyle = StyleBuilder()
        labelStyle.setTextAnchor('middle')
        labelStyle.setFontSize(10)

        # building axis
        leftArmEnd = [leftArmStart[0] +  AXIS_LENGTH*math.cos(self.angle), leftArmStart[1] + AXIS_LENGTH*math.sin(self.angle)]
        downArmEnd =  [leftArmEnd[0], leftArmEnd[1] + AXIS_LENGTH]
        rightArmEnd = [leftArmEnd[0] + AXIS_LENGTH*math.cos(self.angle), leftArmEnd[1] - AXIS_LENGTH*math.sin(self.angle)]

        # drawing lines and labels
        leftAxis = Line(leftArmStart[0], leftArmStart[1], leftArmEnd[0], leftArmEnd[1])
        leftT = Text(self.syms[self.sideColors], leftArmStart[0], leftArmStart[1] - 5)
        downAxis = Line(leftArmEnd[0], leftArmEnd[1], downArmEnd[0],downArmEnd[1])
        downT = Text(self.syms[self.topColor], downArmEnd[0], downArmEnd[1] + 6)
        rightAxis = Line(leftArmEnd[0], leftArmEnd[1], rightArmEnd[0], rightArmEnd[1])
        rightT = Text(self.syms[self.frontColors], rightArmEnd[0], rightArmEnd[1] - 5)

        leftAxis.set_style(leftStyle.getStyle())
        rightAxis.set_style(rightStyle.getStyle())
        downAxis.set_style(downStyle.getStyle())
        leftT.set_style(labelStyle.getStyle())
        rightT.set_style(labelStyle.getStyle())
        downT.set_style(labelStyle.getStyle())

        outLabel.addElement(leftAxis)
        outLabel.addElement(leftT)
        outLabel.addElement(rightAxis)
        outLabel.addElement(rightT)
        outLabel.addElement(downAxis)
        outLabel.addElement(downT)
        return outLabel

    def Render(self):
        topStyle = StyleBuilder()
        topStyle.setFilling(self.topColor)
        topStyle.setFillOpacity(.75)
        topFace = Rect(float(self.startCoords[0]), float(self.startCoords[1]), self.topDims[0],self.topDims[1])
        topFace.set_transform(self.topDownTransform.getTransform())
        topFace.set_style(topStyle.getStyle())
        self.out.addElement(drawFrontFacePair(self.transformedTop, self.transformedBottom,self.frontColors))
        self.out.addElement(drawSideFacePair(self.transformedTop, self.transformedBottom,self.sideColors))
        self.out.addElement(topFace)
        return self.out
