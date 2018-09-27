import numpy as np
import matplotlib.pyplot as plt
import os as os

from scipy import stats
from scipy.constants import codata

def read_history(file, atom):
    '''
    ReadHistory - Read a DL_POLY HISTORY file
    Parameters
    ----------
    file   : HISTORY filename                         : String
    atom   : Atom to be read                          : String
             
    Return
    ------
    data   : trajectories - Atomic trajectories       : Numpy array
           : lv           - Lattice Vectors           : Numpy array
           : timesteps    - Total number of timesteps : Integer
           : natoms       - Tital number of atoms     : Integer
    '''
    if os.path.isfile(file):
        trajectories = []
        timesteps = 0
        history = open(file, 'r')
        name = False
        count = 0
        tstep = False
        c = 0
        lv = []

        for line in history:
            if c == 3:
                c = 0
                tstep = False
            if c < 3 and tstep == True:
                lv.append(line.split())
                c = c + 1
            if name:
                name = False
                trajectories.append(line.split()) 
            if line[0] == atom[0]:
                name = True
                count = count + 1
            if line[0] =="t":
                timesteps = timesteps + 1
                tstep = True

        trajectories = np.asarray(trajectories, dtype=float)
        lv = np.asarray(lv, dtype=float)
        natoms = count / timesteps
        natoms = int(natoms)
        vec = np.array([])
        lv = np.split(lv, timesteps)

        for i in range(0, timesteps):

            vec = np.append(vec, (lv[i].sum(axis=0)))

        lv = np.reshape(vec, (timesteps, 3))
        data = {'trajectories':trajectories, 'lv':lv, 'timesteps':timesteps, 'natoms':natoms}
    else:
        print("File cannot be found")
        sys.exit(0)
    
    if natoms == 0:
        print("No Atoms of specified type exist within the selected HISTORY file")
        sys.exit(0)
        
    history.close() 
    return data

def pbc(rnew, rold, vec):
    '''
    pbc - Periodic boundary conditions for an msd calculation
    Parameters
    ----------
    rnew  : Value of current atomic position   : Float
    rold  : Value of previous atomic position  : Float
    vec   : Lattice vector at that timestep    : Float
    
    Return
    ------
    cross  : Result of PBC check - True if atom crosses the boundary   : Bool
    new    : New position                                              : Float
    '''
    shift = abs((rold - rnew) / vec)
    shift = round(shift, 0)
    shift = int(shift)

    cross = False
    if shift < 2:

        if (rnew - rold) > vec * 0.5:
            rnew = rnew - vec                    
            cross = True
        
        elif -(rnew - rold) > vec * 0.5:
            rnew = rnew + vec  
            cross = True
         
    else:
        
        if (rnew - rold) > vec * 0.5:
            rnew = rnew - (vec * shift)                    
            cross = True
        
        elif -(rnew - rold) > vec * 0.5:
            rnew = rnew + (vec * shift)  
            cross = True
    
    return cross, rnew

def distances(r1, r0):
    ''' 
    Simple subtraction 
    Parameters
    ----------
    r1       : numpy object
    r0       : numpy object
    
    Returns
    -------
    distance : Float
    '''
    return r1 - r0 
    
def square_distance(distance):
    '''
    Calculate the MSD for a series of distances 
    Parameters 
    ----------
    distance : Distance between atomic coordinates     : 2D Numpy object
    n        : 1 = 2D array, 0 = 1D array              : Integer
    Return
    ------
    msd      : squared displacement                    : Numpy object 
    '''
   
    return  ((distance[:,0] ** 2) + (distance[:,1] ** 2) + (distance[:,2] ** 2))

def run_msd(data):
    '''
    MSD calculator - Common to all the various funcitons that do some sort of MSD
    Parameters
    ----------
    data          :
    timestep      : Timestep of the simulation          : Integer
            
    Return
    ------
    msd_data : Dictionary {'msd': msd, 'xmsd': xmsd, 'ymsd': ymsd, 'zmsd': zmsd, 'time': time}    
    pmsd     : MSD arrays for every atom          :  1D numpy array
    '''
    timestep = 0.01
    trajectories = np.split(data['trajectories'], data['timesteps'])
    trajectories = np.asarray(trajectories)
    msd = np.array([])
    xmsd = np.array([])
    ymsd = np.array([])
    zmsd = np.array([])
    time = np.array([])

    r0 = trajectories[0]
    rOd = r0 

    for j in range(1, data['timesteps']):
        
        vec = data['lv'][j]
        r1 = trajectories[j]
        distance_new = distances(r1, r0)
        r1.tolist()
        rOd.tolist()    
      
        for k in range(0, distance_new[:,0].size):
            for i in range(0, 3):
                cross, r_new = pbc(r1[k,i], rOd[k,i], vec[i])
                if cross == True:
                    r1[k,i] = r_new
                    distance_new[k,i] = r_new - r0[k,i]

        distance = distance_new

        r1 = np.asarray(r1)
        rOd = np.asarray(rOd)
        rOd = r1    

        msd_new = square_distance(distance)
        msd_new = np.average(msd_new)
        msd = np.append(msd, (msd_new))
        time = np.append(time, ((j) * timestep))

        xmsd = np.append(xmsd, (np.average((distance[:,0] ** 2))))
        ymsd = np.append(ymsd, (np.average((distance[:,1] ** 2))))
        zmsd = np.append(zmsd, (np.average((distance[:,2] ** 2))))
        
        msd_data = {'msd': msd, 'xmsd': xmsd, 'ymsd': ymsd, 'zmsd': zmsd, 'time': time}

    return msd_data