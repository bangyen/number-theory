import __init__
import number_theory

print("This documentation can be accessed for specific packages by using the following commands:")
print("import xxx")
print("print(xxx.functions_in_this_package)")
x = __init__.functions_in_this_package
for key in x:
    print("This function, "+key + " " + str(x[key]))
