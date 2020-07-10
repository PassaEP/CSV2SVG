from pysvg.shape import Circle, Path, Rect, Polygon, Line  # Polyline
from pysvg.structure import G, Svg, Use
from pysvg.text import Text
from pysvg.builders import StyleBuilder

newDoc = Svg()
pathStyle = StyleBuilder()
pathStyle.setStrokeWidth(2)
pathStyle.setStroke('black')
pathStyle.setFilling('white')
pathLines = '50 50, 100 50, 80 80, 30 30'

samplePath = Path(pathLines)

samplePath.set_style(pathStyle.getStyle())
newDoc.addElement(samplePath)
newDoc.save('path.svg')
