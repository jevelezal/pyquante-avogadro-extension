from PyQt4.QtCore import *
from PyQt4.QtGui import *
from numpy import *
import Avogadro

from lib.surfaces import GlViewWrapper

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
            
            wrap = GlViewWrapper(glwidget)
            
            # Displaying a sphere centered in the current molecule
            
            center = wrap.get_baricenter()
            def sphere(x,y,z):
                return x**2 + y**2 + z**2 - center
            
            wrap.isosurface(sphere, 3)
            
