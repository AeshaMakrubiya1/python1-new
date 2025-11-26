'''
write a program with two function: one to intialize a global variable and global variables with the same name.
'''

# Global variable (initialized later)
value = None

def init_global():
    global value           # Access the global variable
    value = 100            # Initialize global variable
    print("Global value initialized to:", value)

def local_variable():
    value = 50             # This is a LOCAL variable (same name)
    print("Local value inside function:", value)


# Calling both functions
init_global()
local_variable()

print("Global value after all functions:", value)
