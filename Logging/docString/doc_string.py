def my_function():
    """Demonstrates triple double quotes
	docstrings and does nothing really."""

    return None


print("Using __doc__:")  # here we are using the _doc_ function to access it
print(my_function.__doc__)

print("Using help:")
help(my_function)  # here using help function
