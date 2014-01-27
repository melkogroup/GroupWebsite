import os  
import fileinput

for root, dirs, files in os.walk('.'):
    #for line in fileinput.FileInput("Lauren.html",inplace=1):
    #for line in fileinput.input( (os.path.join(root,name) for name in files), inplace=True, backup='_bak'):
    for line in fileinput.input( (os.path.join(root,name) for name in files), inplace=True):
        #line = line.replace("Code We've Built","Code We've Built")
        #line = line.replace("Awkward Group Photos","Awkward Group Photos")
        #line = line.replace("Computational quantum many-body research","Computational quantum many-body research")
        #line = line.replace('<li><a href="https://www.dropbox.com/sh/kex0ui4f78ypzxd/PN641UnjIv">Online Material</a></li>','<li><a href="https://www.dropbox.com/sh/kex0ui4f78ypzxd/PN641UnjIv">Online Material</a></li>')
        line = line.replace('<a href="http://uwaterloo.ca/physics-astronomy/">','<a href="http://uwaterloo.ca/physics-astronomy/">')

        print line,
