import sys 

filennam=sys.argv[0]
print("Filename is:-",filennam)
v_radius = int(sys.argv[1])
print("Radius is:-",v_radius)
v_pi = float(sys.argv[2])
print("PI is:-",v_pi)
area=v_pi*v_radius*v_radius
print("Area of Circle is:-",area)