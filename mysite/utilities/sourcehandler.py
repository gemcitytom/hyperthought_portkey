import os

def __init__(self):
    pass


# PortKey home
def sourceList():
    basename=r"C:\Users\horntr\Documents\Repos\AFRL\PortKey"

    sourceDirectory =  basename+os.sep+".."+os.sep+"FullData"

    sourceList = os.listdir(sourceDirectory)

    return sourceList