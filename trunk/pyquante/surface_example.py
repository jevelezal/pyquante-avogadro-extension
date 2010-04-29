from PyQt4.QtCore import *
from PyQt4.QtGui import *
from numpy import *
import Avogadro

# always use 'Extension' for class name
class Extension(QObject):
  def __init__(self):
    QObject.__init__(self)

  def name(self):
    return "Surface example"

  def description(self):
    return "Example extension for surfaces."

  def actions(self):
    actions = []

    action = QAction(self)
    action.setText("Python Surface")
    actions.append(action)

    return actions

  def performAction(self, action, glwidget):
    
    for i,engine in enumerate(glwidget.engines):
      if engine.name == "Surfaces":
        surfaceEngine = engine  # This should work...
      print "Name",engine.name       # Bug, it gives nothing intelligible
      print "Alias",engine.alias     # Bug, same as before  
      print "Primitives", engine.primitiveTypes # Gives Surface, 3, Atoms etc...
      print "index",i

    cube = glwidget.molecule.addCube()

    dim = array([5,5,5])
    min = -array([10.0,10.0,10.0])
    max = array([10.0,10.0,10.0])
    cube.setLimits(min,max,dim)

    data = []
    for i in range(125):
      data.append(sin(i/5.0))
    cube.setData(data)

    mesh = glwidget.molecule.addMesh()
    ID = mesh.id

    mesh.cube = cube.id

    iso = 1.0
    mesh_gen = Avogadro.MeshGenerator()
    initialized = mesh_gen.initialize(cube,mesh,iso)
    mesh_gen.run()

    Avogadro.toPyQt(mesh_gen).wait()

    print "finished"  

    #settings = QSettings("mesh1Id", ID)   This doesn't set values!!
    settings = QSettings()
    settings.setValue("mesh1Id", ID)
    surfaceEngine.readSettings(settings)

    surfaceEngine.enabled = True
    glwidget.molecule.update()  
