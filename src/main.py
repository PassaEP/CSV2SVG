import csv
from page import RowFrame
from perpsview import IsometricView
from drawView import *
from pysvg.structure import *
newDoc = Svg()

csvfilename = str(input('Enter CSV file name:\n'))
csvtargetfile = str(input('Enter target file name:\n'))
with open(csvfilename, 'r', newline='') as csvfilename:
    specreader = csv.reader(csvfilename)
    next(specreader)
    count = 0
    for row in specreader:
        frames = RowFrame(count)
        newDoc.addElement(frames.makerow())
        xzSlice = Honeycomb(int(row[2]), int(row[4]), frames.rowCoords[0], row[6], row[3])
        newDoc.addElement(xzSlice.genHoneyRect())
        newDoc.addElement(xzSlice.genHoneycomb())
        newDoc.addElement(xzSlice.genLabels())
        xySlice = Slice(row[6], row[8], frames.rowCoords[1], 'green')
        xySlice.calcPosition()
        newDoc.addElement(xySlice.draw())
        newDoc.addElement(xySlice.genLabels())
        yzSlice = Slice(row[8], row[3], frames.rowCoords[2], 'red')
        yzSlice.calcPosition()
        newDoc.addElement(yzSlice.draw())
        newDoc.addElement(yzSlice.genLabels())
        isoView = IsometricView(row[6],row[8], row[3], frames.rowCoords[3])
        isoView.CalcStart()
        isoView.makeFaces()
        newDoc.addElement(isoView.Render())
        count += 1

newDoc.save(csvtargetfile)
