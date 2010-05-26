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
import Avogadro

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
    def create_cube(self, dim,max,min):
        cube = self.glwidget.molecule.addCube()
        
        cube.setLimits(min,max,dim)
        return cube
    def generate_mesh(self, cube):
        mesh = self.glwidget.molecule.addMesh()
        mesh.cube = cube.id
        return mesh
    
    def isosurface(self, voldata, iso):
        '''
        Generate an isosurface
        '''
        # Create Cube (maybe extimate the size)
        cube = self.create_cube()
        # Fill Data in the cube
        
        # Generate mesh
        mesh = self.generate_mesh(cube)
        
        mesh_gen = Avogadro.MeshGenerator()
        
        initialized = mesh_gen.initialize(cube,mesh,iso)
        mesh_gen.run()
        
        Avogadro.toPyQt(mesh_gen).wait()
        
        self.display_mesh(mesh)
    
    def display_mesh(mesh):
        
        surfaceEngine = self.get_engine("Surfaces")
        
        settings = QSettings()
        settings.setValue("mesh1Id", mesh.id)
        surfaceEngine.readSettings(settings)
        
        surfaceEngine.enabled = True
        self.glwidget.molecule.update()  


def test():
    from mock import Mock
    from numpy import array
    glview = Mock()
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
    wrapper.isosurface()
    
