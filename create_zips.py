import os
import zipfile


for i in range(1,270634):
    zf = zipfile.ZipFile("Plugins_12345678987654321_0_213456"+str(i)+".zip", "w")
    zf.close()
