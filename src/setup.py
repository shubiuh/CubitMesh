import sys
import os
def start():
    try:
        sys.path.append("C:\\Program Files\\Trelis 17.0\\bin")
        import cubit
    except:
        print("Python version")
        print (sys.version)
        print("Version info.")
        print (sys.version_info)
        print("Error: Python version should >=3.8")
        sys.exit(1)



