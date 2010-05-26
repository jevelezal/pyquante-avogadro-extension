# -*- coding: utf-8 -*-
"""
Module to compute pyquante properties

ToDo:
 - When clicking the `run` button, change the label in `stop`
 - In Avogadro the click doesn't go clicked
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQuante.hartree_fock import rhf
import PyQuante.Basis.Tools
from PyQuante.PyQuante2 import SCF
from pyquante_ui import Ui_Dialog
import logging
LOG = "/tmp/avogadro.log"
logging.basicConfig(filename=LOG, level=logging.DEBUG)

from PyQuante.logger import configure_output

pyquante_logger = logging.getLogger("pyquante")
configure_output(file="/tmp/pyquante.log")

class PyQuanteDialog(QDialog,Ui_Dialog):
    """
    Dialog to select pyquante settings
    """
    def __init__(self, *args,**kw):
        """
        """
        QDialog.__init__(self,*args,**kw)
        self.setupUi(self)

class PyQuanteController(QObject):
    """
    Controller to make calculation and stuff
    """
    def __init__(self,glwidget):
        """
        - glwidget: useful to set up as the parent for the dialog and to
            fetch info as molecule and atoms
        """
        super(PyQuanteController,self).__init__()
        self.gl = glwidget
        self.ui = PyQuanteDialog()
        basis_choices = PyQuante.Basis.Tools.basis_map.keys()
        
        # Basis set choices from pyquante
        self.ui.basis_set_select.addItems(basis_choices)
        
        # Connect signals
        
        QObject.connect(self.ui.run,SIGNAL("clicked()"),self, SLOT("on_run_click()"))
        self.ui.show()

    @pyqtSignature("")
    def on_run_click(self):
        # Fetching Molecule
        mol = self.gl.molecule
        #print "Here" #ok
        # Convert molecule in the pyquante format
        pyquante_mol = to_pyquante_molecule(mol)
        # Fetch settings
        basis_set = str(self.ui.basis_set_select.currentText())
        method = str(self.ui.method_select.currentText())
        #print "Here" #ok
        self.it=SCFTask( pyquante_mol,
                         basis=basis_set,
                         method=method )
        #print "Here" #ok
        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self, SLOT("update()"))
        self.it.start()
        self.timer.start(20)

    @pyqtSignature("")
    def update(self):
        if self.it.queue.empty():
            if not self.it.is_alive():
                self.timer.stop()
            return True
        else:
            msg = self.it.queue.get()
            self.ui.output.append('<p>'+msg+"</p>")

import multiprocessing

class QueueStream(object):
    def __init__(self,queue):
        self.queue = queue
    def write(self,text):
        self.queue.put(text)

class SCFTask(multiprocessing.Process):
    def __init__(self,*a,**opts):
        super(SCFTask,self).__init__()
        # Connection is done in the thread because of the message
        # passing mechanism, the communication with the main thread
        # is done with pyqtSignals
        self.a = a
        self.opts = opts
        self.queue = multiprocessing.Queue()
        stream = QueueStream(self.queue)
        logger = logging.getLogger("pyquante")
        logger.addHandler(logging.StreamHandler(stream))
    def run(self):
        scf = SCF(*self.a,**self.opts)
        scf.iterate()

def to_pyquante_molecule(avogadro_mol):
    """Convert from Avogadro format to pyquante format

    Arguments:
    - `avogadro_mol`: molecule in Avogadro format
    Returns:
    - pyquante_mol : molecule in pyquante format
    """
    from PyQuante.Molecule import Molecule

    atom_list = []
    for atom in avogadro_mol.atoms:
        atom_entry = (atom.atomicNumber, atom.pos)
        atom_list.append(atom_entry)

    pyquante_mol = Molecule("mol", atom_list)
    return pyquante_mol


def main():
    """
    """
    from mock import GlViewMock
    import sys
    app = QApplication(sys.argv)
    cont = PyQuanteController(GlViewMock())
    app.exec_()

if __name__ == '__main__':
    main()
