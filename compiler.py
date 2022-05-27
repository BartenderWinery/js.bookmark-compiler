import sys,re
with open(sys.argv[1]) as file:
    def compile(data):
        def _replacer(match):
            if match.group(2) is None:
                return match.group(1)
        return " ".join(re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE|re.DOTALL).sub(_replacer, data).replace("\n",";").replace(":;",": ").replace("{;","{").split()).replace("; ",";")
    with open("compiled.js","a") as f:
        f.write("(()=>{"+compile(file.read())+"})()")
    