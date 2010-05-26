class GlViewMock(object):
    """
    """
    
    def __init__(self):
        """
        """
        self.molecule = MolecMock(AtomMock(6,(0,0,0)),
                                   AtomMock(6,(0,1,0))
                                   ) 
        
 
class MolecMock(object):
    """
    """
    
    def __init__(self,*atoms):
        """
        """
        
        self.atoms = atoms

class AtomMock(object):
    """
    """
    
    def __init__(self, atomicNumber, pos):
        """
        """
        
        self.atomicNumber = atomicNumber
        self.pos = pos
