import os

# PortKey home

basename=r"C:\Users\horntr\Documents\Repos\AFRL\PortKey"

sourceDirectory =  basename+os.sep+".."+os.sep+"FullData"

sourceList = os.listdir(sourceDirectory)

return sourceList