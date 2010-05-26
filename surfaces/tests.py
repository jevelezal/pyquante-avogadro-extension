from PyQuante import SCF,Molecule,configure_output
import numpy as np
import shelve
from chem import MolecularOrbital

def generate_data():
    mol = Molecule.from_file("eth.cml")
    scf = SCF(mol, basis="sto3g")
    scf.iterate()
    shelf = open_shelf()
    shelf["scf"]=scf
    shelf.close()


def open_shelf():
    return shelve.open("scf.dump")

shelf = open_shelf()

def mass_centre(mol):
    n=len(mol.atuples())
    return sum( atom.r for atom in mol )/n

def make_grid(maker = np.ogrid):
    mol = Molecule.from_file("eth.cml")
    mc = mass_centre(mol)
    x,y,z = mc
    DIM = 5
    grid = maker[-DIM + x :DIM +x:32j,-DIM +y:DIM+y:32j,-DIM+z:DIM+z:32j]
    return grid

def generate_points():

    x,y,z = make_grid(np.mgrid)
    shelf = open_shelf()
    scf = shelf["scf"]
    mo = MolecularOrbital(scf,15) # First orbital
    points = mo(x,y,z)
    return points

def display_points_func():
    from enthought.mayavi import mlab 
    scf = shelf["scf"]
    mo  = MolecularOrbital(scf,0)
    x,y,z = make_grid(np.mgrid)
    obj = mlab.contour3d(x,y,z,mo(x,y,z) )
    mlab.show()
def display_atoms():
    mol = Molecule.from_file("eth.cml")
    cords=[]
    power = []
    mc = mass_centre(mol)
    for atom in mol:
        cords.append(atom.r  )
        power.append(atom.atno)
    x,y,z = zip(*cords)
    from enthought.mayavi import mlab
    mlab.points3d(x,y,z,power,scale_mode='none')
    

def display_points(val=0.3):
    scalars = shelf["scalars"]
    scalars =  generate_points()
    shelf["scalars"] = scalars
    min = scalars.min()
    max = scalars.max()
    
    from enthought.mayavi import mlab
    x,y,z = make_grid(np.mgrid)
    contours = list(np.arange(-val,val,0.02))
    obj = mlab.contour3d(x,y,z,scalars,contours=contours,opacity=0.3,colormap="PRGn",transparent=True)

    display_atoms()
#    source = mlab.pipeline.scalar_field(x,y,z,scalars)
#    vol = mlab.pipeline.volume(source, vmin=min+0.65*(max-min), 
#                               vmax=min+0.9*(max-min))
#    mlab.view(132, 54, 45, [21, 20, 21.5])
    mlab.show()

    
display_points(0.2)
