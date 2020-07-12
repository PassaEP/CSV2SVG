# CSV2SVG

Tool to render SVG file of views and planes of basic DNA origami designs from a CSV file of specs.

### Features

- Generates XZ plane view, with the corresponding honeycomb lattice pattern.
- Generates XY, YZ views
- Generates pseudo-3D perspective views
- Annotated dimensions on the 2D slices

### In-Progress Features (as of 7/10/20)
- Need to add bounding boxes to pseudo-3d figures for framecentering.
- Need to lay figures down on the larger area faces
- Need to annotate dimensions on pseudo-3D perspective
- Need to render transformed faces in pseudo-3D using transformed figures instead of path-drawing.

### Dependencies
Need PySVG ported to Python 3 and Numpy.

`pip3 install pysvg-py3`

`pip3 install numpy`
