import numpy as np
import os
import random

def read(file):
    ''' read - function to read METADISE input file
    Parameters
    ----------
    file - input.txt file
    
    Returns
    -------
    data - Dictionary containing cation coordinates and anion coordinates
    '''
    cat = []
    an = []
    f = open(file, "r")
    
    for line in f:
        if line[1] == "C" and line[2] == "A":
            cat.append(line.split())
        elif line[1] == "F":
            an.append(line.split())
    cat = np.asarray(cat)
    an = np.asarray(an)
    data = {"Cation": cat, "Anion": an}
    
    return data

def get_cubes(dataset):
    '''get_cubes - Finds all available interstitial sites in fluorite material
    
    Parameters
    ----------
    dataset - cation xyz coordinates
    
    Returns 
    -------
    interstitial - interstitial sites xyz coordinates
    '''
    xdata = dataset[:,2].astype(float)
    ydata = dataset[:,3].astype(float)
    zdata = dataset[:,4].astype(float)

    interstitial = np.array([])
    for i in range(0, xdata.size):
        
        interstitial = np.append(interstitial, (xdata[i] + 2.732))
        interstitial = np.append(interstitial, ydata[i])
        interstitial = np.append(interstitial, zdata[i])
                
    d = interstitial.size / 3
    d = int(d)
    interstitial = np.reshape(interstitial, (d, 3))
    return interstitial 

def schottky(data, concentration):
    '''schottky - Add schottky defects to the input.txt file
    
    Parameters
    ----------
    data - dictionary of cation and anion coordinates
    concentration - concentration of schottky defects to be added
    
    Returns
    -------
    data - new dictionary - containing the schottky defects
    '''
    catrem = ( data["Cation"][:,0].size / 100 ) * concentration
    catrem = int(catrem)
    anrem = ( data["Anion"][:,0].size / 100 ) * concentration
    anrem = int(anrem)
    ar = random.sample(range(0, data["Anion"][:,0].size), anrem)
    cr = random.sample(range(0, data["Cation"][:,0].size), catrem)
    
    ar.sort(key=int)
    cr.sort(key=int)

    data["Cation"] = np.delete(data["Cation"], cr, 0)
    data["Anion"] = np.delete(data["Anion"], ar, 0)

    return data

def frenkel(data, concentration, atom):
    '''frenkel - Adds Frenkel defects
    Parameters
    ----------
    data - dictionary of cation and anion coordinates
    concentration - concentration of schottky defects to be added
    atom - atom that should be moved to the interstitial. 
    
    Returns
    -------
    data - new dictionary - containing the schottky defects
    '''
    cation_sites = get_cubes(data["Cation"])
    catrem = ( cation_sites[:,0].size / 100 ) * concentration
    catrem = int(catrem)

    cr = random.sample(range(0, cation_sites[:,0].size), catrem)
    cr.sort(key=int)
    data["Cation"] = np.delete(data["Cation"], cr, 0)
    
    ac = random.sample(range(0, cation_sites[:,0].size), catrem)
    ac.sort(key=int)
    for i in range(0, len(ac)):
        x = ac[i]
        data["Cation"] = np.append(data["Cation"], atom)
        data["Cation"] = np.append(data["Cation"], "CORE")
        data["Cation"] = np.append(data["Cation"], cation_sites[x, 0])
        data["Cation"] = np.append(data["Cation"], cation_sites[x, 1])
        data["Cation"] = np.append(data["Cation"], cation_sites[x, 2])

    x = data["Cation"].size / 5
    x = int(x)
    data["Cation"] = np.reshape(data["Cation"], (x, 5))
    return data
        
def dopant(dataset, atom, charge, concentration):
    '''dopant - Adds dopants to structure. 
    Parameters
    ----------
    data - dictionary of cation and anion coordinates
    atom - atom type to be added. 
    charge - charge of new atom.
    concentration - concentration of schottky defects to be added
    
    Returns
    -------
    data - new dictionary - containing dopants
    '''
    x = charge - 2.0
    
    p = data["Cation"][:,0].size
    catrem = ( data["Cation"][:,0].size / 100 ) * concentration
    catrem = int(catrem)
    cr = random.sample(range(0, data["Cation"][:,0].size), catrem)
    cr.sort(key=int)

    if x > 0.0:
        anrem = catrem * (x / 2)
        anrem = int(anrem)
        ar = random.sample(range(0, data["Cation"][:,0].size), anrem)
        ar.sort(key=int)
        data["Cation"] = np.delete(data["Cation"], ar, 0)

    cr = random.sample(range(0, data["Cation"][:,0].size), catrem)
    cr.sort(key=int)
    for i in range(0, len(cr)):
        data["Cation"][cr[i], 0] = atom

    
    if x == 0.0:    
        return data
        
    elif x < 0.0:
        anrem = len(cr)
        anrem = int(anrem)
        ar = random.sample(range(0, data["Anion"][:,0].size), anrem)
        ar.sort(key=int)
        data["Anion"] = np.delete(data["Anion"], ar, 0)
    
        return data
    
    return data

def write_output(data, directory):
    '''write_output - write out new input.txt file 
    Parameters
    ----------
    data - Dictionary containing cation and anion coordinates
    directory - directory that should be created for the new file. 
    '''
    os.mkdir(directory)
    out = str(directory) + "/input.txt" 
    output = open(out, "w")
    output.write("LATT\n")
    output.write("          21.8560000000         0.0000000000         0.0000000000\n")
    output.write("           0.0000000000        21.8560000000         0.0000000000\n")
    output.write("           0.0000000000         0.0000000000        21.8560000000\n")
    output.write("BASI\n")
    for i in range(0, data["Cation"][:,0].size):
        var = str(data["Cation"][i][0] + "    " + data["Cation"][i][1] + "     " + data["Cation"][i][2] + "     " + data["Cation"][i][3] + "     " + data["Cation"][i][4] + "\n")
        output.write(var)
    for i in range(0, data["Anion"][:,0].size):
        var = str(data["Anion"][i][0] + "    " + data["Anion"][i][1] + "     " + data["Anion"][i][2] + "     " + data["Anion"][i][3] + "     " + data["Anion"][i][4] + "\n")
        output.write(var)    
        
    output.write("ends\n")
    output.write("potential\n")
    output.write("species\n")
    output.write("Ca core 2,0\n")
    output.write("F core -1.0\n")
    
    output.write("ends\n")
    output.write("Buckingham\n")
    output.write("Ca F 797.42 0.3179 0.0 0.0 20.0\n")
    output.write("F  F 1127.7 0.2753 15.83 0.0 20.0\n")

    output.write("ends\n")
    output.write("ends\n")
    output.write("check\n")
    output.write("stop\n")
    output.write("print dlpoly 1\n")
    output.write("start\n")
    output.write("stop\n")
    output.write("stop\n")
    output.close()