import numpy as np
import os
import random

def read(file):
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

def schottky(data, concentration):
    
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

def frenkel(dataset, concentration):
    pass

def dopant(dataset, atom, charge, concentration):
    pass

def write_output(data, directory):
    os.mkdir(directory)
    out = str(directory) + "/input.txt" 
    output = open(out, "w")
    output.write("LATT\n")
    output.write("          21.8560000000         0.0000000000         0.0000000000\n")
    output.write("           0.0000000000        21.8560000000         0.0000000000\n")
    output.write("           0.0000000000         0.0000000000        21.8560000000\n")
    output.write("BASI\n")
    for i in range(0, data["Cation"][:,0].size):
        var = str("CA    " + "CORE     " + data["Cation"][i][2] + "     " + data["Cation"][i][3] + "     " + data["Cation"][i][4] + "\n")
        output.write(var)
    for i in range(0, data["Anion"][:,0].size):
        var = str("F    " + "CORE     " + data["Anion"][i][2] + "     " + data["Anion"][i][3] + "     " + data["Anion"][i][4] + "\n")
        output.write(var)    
        
    output.write("ends\n")
    output.write("potential\n")
    output.write("species\n")
    output.write("Ca 2.0 Ca2+\n")
    output.write("F -1.0 F-\n")
    output.write("ends\n")
    output.write("Buckingham\n")
    output.write("Ca F 797.42 0.3179 0.0 0.0 20.0\n")
    output.write("F F 1127.7 0.2753 15.83 0.0 20.0\n")
    output.write("ends\n")
    output.write("ends\n")
    output.write("check\n")
    output.write("stop\n")
    output.write("print dlpoly 1\n")
    output.write("start\n")
    output.write("stop\n")
    output.write("stop\n")
    output.close()