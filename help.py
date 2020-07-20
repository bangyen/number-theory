import number_theory_essentials
import number_theory

print("This documentation can be accessed for specific packages by using the following commands:")
print("import xxx")
print("print(xxx.functions_in_this_package)")
x = number_theory_essentials.functions_in_this_package
for key in x:
    print("This function, "+key + " " + str(x[key]))
