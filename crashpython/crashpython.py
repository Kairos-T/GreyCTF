 import ctypes
def segfault():
    # Access an invalid memory location
    ctypes.string_at(0)

segfault()
