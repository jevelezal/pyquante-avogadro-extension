import numpy
class MolecularOrbital(object):
    def __init__(self, scf, index):
        """
        
        Arguments:
        - `scf`:
        """
        self.coefs = scf.solver.orbs[:,index]
        self.cgtos = scf.basis_set.get()
    def __call__(self,x,y,z):
        amp = lambda x,y,z : sum( cgto.amp(x,y,z) * coef for (cgto,coef) in zip(self.cgtos,self.coefs) )
        return numpy.array(numpy.frompyfunc(amp,3,1)(x,y,z),dtype=numpy.float32)
