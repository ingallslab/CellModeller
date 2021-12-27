import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy
import math

cell_cols = {0:[0,1.0,0], 1:[1.0,0,0], 2:[0,0,1.0]} #RGB cell colours
cell_lens = {0:3.5, 1:3.5, 2:3.5} #target cell lengths
cell_growr = {0:1, 1:1, 2:1.05} #growth rates

#Geometry
min_x = 0.0
max_x = 20.0
min_y = -0.1
max_y = 20.0

def setup(sim):
    # Set biophysics, signalling, and regulation models
    biophys = CLBacterium(sim, jitter_z=False, max_planes=2)

    # use this file for reg too
    regul = ModuleRegulator(sim, sim.moduleName)
    # Only biophys and regulation
    sim.init(biophys, regul, None, None)
 
    planeWeight = 1.0
    biophys.addPlane((min_x,0,0), (1,0,0), planeWeight) 		    # left side
    biophys.addPlane((max_x,0,0), (-1,0,0), planeWeight) 		# right side
    #biophys.addPlane((0,0,0), (0,0,+1), planeWeight) 			# base
 
    # Specify the initial cell and its location in the simulation
    sim.addCell(cellType=0, pos=(0,1,0), dir=(1,0,0))
    sim.addCell(cellType=1, pos=(6,1,0), dir=(1,0,0))
    sim.addCell(cellType=2, pos=(12,1,0), dir=(1,0,0))


    # Add some objects to draw the models
    therenderer = Renderers.GLBacteriumRenderer(sim)
    sim.addRenderer(therenderer)
    sim.pickleSteps = 20

def init(cell):
    # Specify mean and distribution of initial cell size
    cell.targetVol = cell_lens[cell.cellType] + random.uniform(0.0,0.5)
    # Specify growth rate of cells
    cell.growthRate = cell_growr[cell.cellType]
    cell.color = cell_cols[cell.cellType]

'''
cells = sim.cellStates
'''
def update(cells):
    #Iterate through each cell and flag cells that reach target size for division
    for (id, cell) in cells.items():
        if cell.pos[1] > max_y or cell.pos[1] < min_y:
            cell.removeFlag = True
        if cell.volume > cell.targetVol and cell.removeFlag == False:
            cell.divideFlag = True

def divide(parent, d1, d2):
    # Specify target cell size that triggers cell division
    d1.targetVol = cell_lens[parent.cellType] + random.uniform(0.0,0.5)
    d2.targetVol = cell_lens[parent.cellType] + random.uniform(0.0,0.5)
