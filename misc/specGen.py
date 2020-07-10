from pysvg.builders import ShapeBuilder
from pysvg.text import *
from pysvg.structure import Svg
from drawView import *

def specGenerate(input):
    fileName = 'design_' + str(input[0]) + '.svg'


    newDocument = Svg()
    # make title, labels of svg document
    title = Text('Design ' + str(input[0]), 20, 0)
    type = Text('p' + str(input[1]), 0, 0)
    newDocument.addElement(title)
    newDocument.addElement(type)
    # call method to draw x,y slice
    xySlice = Slice(input[5],input[7],input[3],'x', 'y')
    xySlice.calcPositionXY()
    newDocument.addElement(xySlice.draw())

    xyComponents = xySlice.genAxis()
    for stuff in xyComponents:
        newDocument.addElement(stuff)
    # call method to draw x,z slice
    xzSlice = Honeycomb(int(input[2]), int(input[4]), xySlice.gridCoord, float(input[5]),float(input[7]), float(input[3]))
    newDocument.addElement(xzSlice.genHoneyRect())
    newDocument.addElement(xzSlice.genHoneycomb())

    #for stuff in xzComponents:
    #    newDocument.addElement(stuff)
    # call method to draw y,z slice
    yzSlice = Slice(input[7],input[3],input[5],'y','z')
    yzSlice.calcPositionYZ()
    newDocument.addElement(yzSlice.draw())
    yzComponents = yzSlice.genAxis()
    for stuff in yzComponents:
       newDocument.addElement(stuff)
    # call method to draw prism views
    prism = Prism(input[5], input[7], input[3], yzSlice.gridCoord)
    newDocument.addElement(prism.draw())
    #prismComponents = prism.drawPrism()
    #for stuff in prismComponents:
    #    newDocument.addElement(stuff)
    # call method to arrange
    # save to svg file
    newDocument.save(fileName)
