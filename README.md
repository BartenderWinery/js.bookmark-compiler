# Simple JS.Bookmark compiler
###### How to use
- Python file: 
    1. Install the [python environment](https://www.python.org).
    2. Download/Copy the [source](https://github.com/BartenderWinery/js.bookmark-compiler/blob/main/compiler.py)
    3. Drag and drop any JS file to `compiler.py`.
    4. The compiled source will be created in the same directory.
- EXE file:
    1. Download the [release download](https://github.com/BartenderWinery/js.bookmark-compiler/releases/tag/exe)
    2. Drag and drop any JS file to `compiler.exe`.
    3. The compiled source will be created in the same directory.
###### Processing
The python script `[compiler.py](https://github.com/BartenderWinery/js.bookmark-compiler/blob/main/compiler.py)` calucates the source file in the following sequence:
1. Opens the source file and reads it.
> f.write("(()=>{"+compile(file.read())+"})()")
2. Compiles the source for any comments by using different markup syntaxes.
> re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
3. Replaces all newlines with a semicolon.
> re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE|re.DOTALL).sub(_replacer, data).replace("\n",";")
4. Replaces any `:;` with `: ` & `{;` with `{`.
> re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE|re.DOTALL).sub(_replacer, data).replace("\n",";").replace(":;",": ").replace("{;","{")
5. Combines a multitude of spaces with a singular space.
> " ".join(re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE|re.DOTALL).sub(_replacer, data).replace("\n",";").replace(":;",": ").replace("{;","{").split())
6. Replaces any `; ` with `;`.
> " ".join(re.compile(r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)", re.MULTILINE|re.DOTALL).sub(_replacer, data).replace("\n",";").replace(":;",": ").replace("{;","{").split()).replace("; ",";")
7. Returns to value to the orginial write function, compiling it to `compiled.js`.