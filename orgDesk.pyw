from glob import glob
import os

fldr_path = 'C:/Users/Dave/Desktop/'

while True:
    try:
        # gets directory of all .txt files
        myFilesPaths = glob(fldr_path + r'\*.txt')
        for i in myFilesPaths:
            r = i.replace("\\", "/test/")
            i = i.replace("\\", "/")
            os.rename(i, r)
    except Exception:
        pass