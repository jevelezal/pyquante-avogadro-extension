# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pyquante import PyQuanteController
import Avogadro
import logging

# always use 'Extension' for class name
class Extension(QObject):
    def __init__(self):
        QObject.__init__(self)

    def name(self):
        return "pyquante Integration Extension"

    def description(self):
        return "Computes the HF energy of the molecule"

    def actions(self):
        """
        Menu entry:
        - HF Energy
        """
        actions = []
        
        action = QAction(self)
        action.setText("HF Energy")
        actions.append(action)

        return actions

    def menuPath(self, action):
        return "Scripts"

    def performAction(self, action, glwidget):
        """
        Simply computes the energy and display the results somewhere
        """
        self.contr = PyQuanteController(glwidget)
        return None

    def readSettings(self, settings):
        pass
        #self.foo = settings.value("foo", QVariant(42))

    def writeSettings(self, settings):
        #settings.setValue("foo", self.foo)
        pass
