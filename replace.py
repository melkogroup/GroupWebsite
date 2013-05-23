import os  
import fileinput

for root, dirs, files in os.walk('.'):
    #for line in fileinput.FileInput("Lauren.html",inplace=1):
    #for line in fileinput.input( (os.path.join(root,name) for name in files), inplace=True, backup='_bak'):
    for line in fileinput.input( (os.path.join(root,name) for name in files), inplace=True):
        #line = line.replace("Code We've Built","Code We've Built")
        #line = line.replace("Awkward Group Photos","Awkward Group Photos")
        line = line.replace("Computational quantum many-body research","Computational quantum many-body research")
        print line,
