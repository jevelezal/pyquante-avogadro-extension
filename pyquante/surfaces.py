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
import logging
from PyQt4.QtCore import QSettings

#import Avogadro
import numpy
from numpy import array
from mock import Mock

QSettings = Mock()
Avogadro=Mock()

class GlViewWrapper(object):
    def __init__(self, glwidget):
        self.glwidget = glwidget

    def get_engine(self, name):
        '''
        Looks for engines in the glwidget
        '''
        glwidget = self.glwidget
        for engine in glwidget.engines:
            if engine.name == name:
                surfaceEngine = engine  # This should work...
            logging.debug("Name %s, Alias %s, PrimitiveTypes %s"%(
                    engine.name, engine.alias, engine.primitiveTypes))
        return surfaceEngine

    def get_baricenter(self):
        '''
        get the approximate baricenter of the molecule
        '''
        ret = numpy.zeros(3)
        for atom in self.glwidget.molecule.atoms:
            ret += numpy.array(atom.pos) * atom.atomicNumber * 2
        return ret

    def create_cube(self, dim,max,min):
        cube = self.glwidget.molecule.addCube()
        
        cube.setLimits(min,max,dim)
        return cube
    
    def generate_mesh(self, cube):
        mesh = self.glwidget.molecule.addMesh()
        mesh.cube = cube.id
        return mesh
        
    def isosurface(self, func, iso,
                   dim = array([50,50,50]),
                   min = -array([10.0,10.0,10.0]),
                   max = array([10.0,10.0,10.0])):
        '''
        Generate an isosurface from the func (x,y,z) passed.
        '''
        # Create Cube (maybe extimate the size)
        center = self.get_baricenter() # Translating to the center of the molecule
        min+=center
        max+=center
        cube = self.create_cube(dim, min, max)

        # Fill Data in the cube
        x_min,y_min,z_min = min 
        x_max,y_max,z_max = max
        x_dim, y_dim, z_dim = dim
        
        # Creating a grid
        grid = numpy.ogrid[x_min:x_max:x_dim*1j,
                           y_min:y_max:z_dim*1j,
                           z_min:z_max:z_dim*1j]
        
        # Something like that, it has to produce a flattened list
        data = func(*grid)
        cube.setData(data)
        
        # Generate mesh
        mesh = self.generate_mesh(cube)
        mesh_gen = Avogadro.MeshGenerator()
        
        initialized = mesh_gen.initialize(cube,mesh,iso)
        mesh_gen.run()
        
        Avogadro.toPyQt(mesh_gen).wait()
        
        self.display_mesh(mesh)
    
    def display_mesh(self,mesh):
        
        surfaceEngine = self.get_engine("Surfaces")
        
        settings = QSettings()
        settings.setValue("mesh1Id", mesh.id)
        surfaceEngine.readSettings(settings)
        
        surfaceEngine.enabled = True
        self.glwidget.molecule.update()  


def get_glview_mock():
    glview = Mock()
    surfengine = Mock()
    surfengine.name = "Surfaces"
    glview.engines = [surfengine]
    return glview
    
def test():

    from numpy import array
    glview = get_glview_mock()
    wrapper = GlViewWrapper(glview)
    
    # Test calls
    
    # Get the engine named...
    wrapper.get_engine("Surfaces")
    
    # Create cube dim...
    dim = array([5,5,5])
    min = -array([10.0,10.0,10.0])
    max = array([10.0,10.0,10.0])
    wrapper.create_cube(dim,max,min)
    
    # Create isosurface from volumetric data...
    voldata = [0,1]
    wrapper.isosurface(voldata, iso = 0.1)
    #print glview.method_calls

if __name__ == '__main__':
    test()
