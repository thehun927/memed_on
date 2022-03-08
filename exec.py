# exec.py
# will restart the main.py if encountering an error (bruh)

def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)


# run the script

try:
    execfile("main.py")
except:
    pass
