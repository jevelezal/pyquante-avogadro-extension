'''
* Displaying surfaces
** Operations

- add a cube around a molecule,
- split the cube in little cubes,
- evaluate the function in each cube,
- fill the data

- generate the mesh
- wait for the mesh to be generated

- update the glwidget

'''

class AvogadroSurface(object):
    def __init__(self, function):
        self.function = function
    def display(self, glview):
        pass
