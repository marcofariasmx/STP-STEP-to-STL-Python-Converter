# New updated, simpler and more versatile version found here: https://github.com/marcofariasmx/STP-STEP-IGES-BREP-to-STL-Python-converter

# STP/STEP-to-STL-Python-Converter
Simple multithreaded Python script to convert STP/STEP to STL files based on Freecad.

This script should run on Windows, Linux and MacOS.

## Requisites

- [FreeCAD](https://www.freecadweb.org/downloads.php) installed
- Python 3.x installed

## How to run
Every file to convert must be in a directory called "3DModelsToConvert" in the root directory containing the STP-to-STL.py script. 

The script will create two new directories within "3DModelsToConvert", one called "Converted-STLs" with the converted files and anotherone called "OriginalFiles".

Simply execute it by the following command from the root directory:
```
python3 STP-to-STL.py
```

### Commments
This script becomes particularly useful when needed to convert a large batch of STP/STEP files to STL for further processing.

It is necessary to have FreeCAD installed in your OS. The main libraries used from the installation are the "Part" and "Mesh" libraries. I tried only abstracting those two libraries unsucessfully. It would be nice if someone finds a way to avoid having to install the whole program.

Blogpost to continue this conversation: https://marcofarias.com/stp-step-to-stl-python-converter/
