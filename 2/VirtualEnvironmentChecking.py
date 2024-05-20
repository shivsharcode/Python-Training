import sys

def is_in_virtual_environment():
    """Check if the Python interpreter is running inside a virtual environment."""
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

if is_in_virtual_environment():
    print("You are in a virtual environment.")
else:
    print("You are not in a virtual environment.")