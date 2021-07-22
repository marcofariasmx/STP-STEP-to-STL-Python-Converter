import time
import multiprocessing
from functools import partial

import os
from os import listdir
from os.path import isfile, join
import platform
import sys
import glob

if platform.system() == 'Windows': 
    FREECADPATH = glob.glob(r"C:\Program Files\FreeCAD *\bin")
    FREECADPATH = FREECADPATH[0]
    #print(FREECADPATH) #in case needed to confirm, uncomment
    
elif platform.system() == 'Darwin': #MacOS
    FREECADPATH = '/Applications/FreeCAD.app/Contents/Resources/lib/'
elif platform.system() == 'Linux': 
    FREECADPATH = '/usr/lib/freecad-python3/lib/' # path to your FreeCAD.so or FreeCAD.dll file
else:
    print("Error: No recognized system available.")

sys.path.append(FREECADPATH)
import FreeCAD as App
import Part
import Mesh

def converter(filesPath, totalFiles, file):

    #totalFiles is unused, was not able to put current number of process.

    print("Converting File: " + file)
    shape = Part.Shape()
    shape.read(filesPath + "/" + file)
    doc = App.newDocument('Doc')
    pf = doc.addObject("Part::Feature","MyShape")
    pf.Shape = shape

    if not os.path.exists(filesPath + "/Converted-STLs"):
        os.makedirs(filesPath + "/Converted-STLs")

    if not os.path.exists(filesPath + "/OriginalFiles"):
        os.makedirs(filesPath + "/OriginalFiles")

    newName = filesPath + "/Converted-STLs/" + file + ".stl"
    Mesh.export([pf], newName)
    os.replace(filesPath + "/" + file, filesPath + "/OriginalFiles/" + file)

def main():

    filesPath = "./3DModelsToConvert"
    onlyfiles = [f for f in listdir(filesPath) if isfile(join(filesPath, f))]
    totalFiles = len(onlyfiles)
    
    start_time = time.time()
    
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    temp = partial(converter, filesPath, totalFiles)
    print("Pool info: ", pool)
    result = pool.map(func=temp, iterable=onlyfiles, chunksize=1)
    pool.close()
    pool.join()
    
    end_time = time.time()
    print('\n' + "Execution time: ")
    print(str(end_time-start_time) + " seconds" + '\n')

if __name__ == "__main__":
  main()