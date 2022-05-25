import sys,os
with open(sys.argv[1]) as file:
    with open("compiled.js","a") as f:
        f.write("(()=>{"+file.read()+"})()")
    