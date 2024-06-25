import sympy as sp

def ask_coordinate_system():
    print("Which coordinate system would you like to use?")
    print("1) Cartesian coordinates")
    print("2) Cylindrical coordinates")
    print("3) Spherical coordinates")
    
    choice = input("Please enter the number of your choice: ")
    return choice

coordinate_system = ask_coordinate_system()

#data


if coordinate_system == '1':
    x, y, z = sp.symbols(' x y z')
    func_str1=input("Enter the function f(x,y,z): ")
    func=sp.sympify(func_str1)
    def gradient_cartesian(x,y,z):
        grad_func = sp.derive_by_array(func, (x, y, z))
        return grad_func
    
    gc= gradient_cartesian(x,y,z)
    print("f(x,y,z) = ", func)
    print("∇f =", gc)


elif coordinate_system == '2':
    r, theta, z_cyl= sp.symbols('r theta z')
    func_str2=input("Enter the function f(r,theta,z): ")
    func_cyl=sp.sympify(func_str2)
    grad_func_cyl = sp.derive_by_array(func_cyl, (r, theta, z_cyl))
    print("f(r, theta, z) = ", func_cyl)
    print("∇f =", grad_func_cyl)



elif coordinate_system == '3':
    rho, theta, phi = sp.symbols('rho theta phi')
    func_str3=input("Enter the function f(rho,theta,phi): ")
    func_sph=sp.sympify(func_str3)
    grad_func_sph = sp.derive_by_array(func_sph, (rho, theta, phi))
    print("f(rho, theta, phi) = ", func_sph)
    print("∇f =", grad_func_sph)
else:
    print("Invalid choice. Please select a valid coordinate system.")














