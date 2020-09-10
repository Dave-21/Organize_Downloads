from glob import glob
import os

fldr_path = 'C:/Users/Dave/Downloads/'

while True:
    try:
        # gets directory of each .exe files
        # myFilesPaths, myFilesPaths2 = glob(fldr_path + r'\*.exe' ), glob(fldr_path + r'\*.msi')
        fullPaths = glob(fldr_path + r'\*.exe') + glob(fldr_path + r'\*.msi') + glob(fldr_path + r'\*.txt')# myFilesPaths + myFilesPaths2
        for i in fullPaths:
            print(i)
            i = i.replace("\\", "/")
            r = i.replace(fldr_path, "C:/Users/Dave/Documents/.exe/")
            os.rename(i, r)
    except Exception:
        pass