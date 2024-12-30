print("abubakar")

def bakar(n):
    print(n)

bakar("Python Function")

new12 = "abc"









# PS C:\Users\Lenovo\OneDrive\Desktop\Python_start> python
# Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> for a in "abubakar"
#   File "<stdin>", line 1 
#     for a in "abubakar"  
#                        ^ 
# SyntaxError: expected ':'
# >>> for a in "abubakar":
# ...     print(a)
# ... 
# a
# b
# u
# b
# a
# k
# a
# r
# >>> import os
# >>> os.getcwd
# <built-in function getcwd>
# >>> os.getcwd()
# 'C:\\Users\\Lenovo\\OneDrive\\Desktop\\Python_start'
# >>> import sys
# >>> sys.platform
# 'win32'
# >>> import intro
# abubakar
# Python Function
# >>> intro.bakar("bakkar")   
# bakkar
# >>> import intro
# >>> from importlib import reload
# >>> import intro
# >>> reload(bakar)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'bakar' is not defined
# >>> reload("bakar")
# Traceback (most recent call last):
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py", line 139, in reload
#     name = module.__spec__.name
#            ^^^^^^^^^^^^^^^
# AttributeError: 'str' object has no attribute '__spec__'. Did you mean: '__doc__'?

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py", line 142, in reload
#     name = module.__name__
#            ^^^^^^^^^^^^^^^
# AttributeError: 'str' object has no attribute '__name__'. Did you mean: '__ne__'?

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py", line 144, in reload
#     raise TypeError("reload() argument must be a module")
# TypeError: reload() argument must be a module
# >>> from importlib import reload
# >>> reload(new12) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'new12' is not defined
# >>> intro.bakar(new12)    
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'new12' is not defined
# >>> from inmportlib import reload
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'inmportlib'
# >>> from importlib import reloadd 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'reloadd' from 'importlib' (C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\importlib\__init__.py)
# >>> from importlib import reload 
# >>> reload(intro)
# abubakar
# Python Function
# <module 'intro' from 'C:\\Users\\Lenovo\\OneDrive\\Desktop\\Python_start\\intro.py'>
# >>> intro.bakar(new12)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'new12' is not defined
# >>> intro.new12
# 'abc'




# Datatypes
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> import random
# >>> random.random()
# 0.268019269998081
# >>> username = "Abubakar"
# >>> len(username)
# 8
# >>> username[0]
# 'A'

                # muteable
# >>> username[0] = "a"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# dictionary also add index name(key) unlike array/list
# t = (1, 2, 3)  # Tuple
# l = [1, 2, 3]  # List
# l = [1, 2, 3]  # Array
# l = ['a':1, 'b':2, 'c':3]  # Dictinonary