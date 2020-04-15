# *************************************************************************
# John Wolz
# CWID: 102-51-920
# Date: Febuary 7th, 2018
# Assigment 4: The purpose of this assignment was to implement 3 lighting
# and 3 shading models
# *************************************************************************

import math
from tkinter import *


CanvasWidth = 400
CanvasHeight = 400
d = 500

"""
# ***************************** Initialize Pyramid Object ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [-50,-50,50]
base2 = [50,-50,50]
base3 = [50,-50,150]
base4 = [-50,-50,150]
center = [0, 0, 100] # center of the pyramid

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside
frontpoly = [apex,base2,base1]
rightpoly = [apex,base3,base2]
backpoly = [apex,base4,base3]
leftpoly = [apex,base1,base4]
bottompoly = [base4,base1,base2,base3]

# Definition of the object
Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]

# Definition of the Pyramid's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4, center]

# ***************************** Initialize Cube Object *****************************
# Definition of 8 underlying points. BRF stands for Bottom-right Front, etc.
pointBRF = [200, 100, 100]
pointBRB = [200, 100, 200]
pointBLF = [100, 100, 100]
pointBLB = [100, 100, 200]
pointTLF = [100, 200, 100]
pointTLB = [100, 200, 200]
pointTRF = [200, 200, 100]
pointTRB = [200, 200, 200]
centerC = [150,150,150] # center of the cube

# Definition of 6 Polygon faces
frontpolyC = [pointTLF, pointTRF, pointBRF, pointBLF]
rightpolyC = [pointTRF, pointTRB, pointBRB, pointBRF]
backpolyC = [pointTRB, pointTLB, pointBLB, pointBRB]
leftpolyC = [pointTLB, pointTLF, pointBLF, pointBLB]
toppolyC = [pointTLB, pointTRB, pointTRF, pointTLF]
bottompolyC = [pointBLF, pointBRF, pointBRB, pointBLB]

# Definition of the object
Cube = [bottompolyC, toppolyC, frontpolyC, rightpolyC, backpolyC, leftpolyC]

# Definition of the Cube's point cloud
CubePointCloud = [pointBRF, pointBRB, pointBLF, pointBLB, pointTLF, pointTLB, pointTRF, pointTRB, centerC]

# ************************* Initializing Triangular Pyramid Object *******************
# Definition of 4 underlying points. named similar to pyramid but with T at the end for Triangular
apexT = [-150, 150, 117]
base1T = [-100, 75, 100]
base2T = [-200, 75, 100]
base3T = [-150, 75, 150]
centerT = [-150, 100, 117] # center of trian. pyramid

#Definition of 4 polygon faces
frontpolyT = [apexT, base2T, base1T]
leftpolyT = [apexT, base3T, base2T]
rightpolyT = [apexT, base1T, base3T]
bottompolyT = [base1T, base2T, base3T]

# Def of object
TriangularPyramid = [frontpolyT, leftpolyT, rightpolyT, bottompolyT]

# Def of point cloud
TriangularPyramidPointCloud = [apexT, base1T, base2T, base3T, centerT]

#************************************************************************************
"""
# ************************* Initializing Cylinder Object *******************
# Definition of 4 underlying points. named similar to pyramid but with T at the end for Triangular
base1B=[-50,-100,100]
base1T=[-50,100,100]
base2B=[-120,-100,170]
base2T=[-120,100,170]
base3B=[-120,-100,240]
base3T=[-120,100,240]
base4B=[-50,-100,310]
base4T=[-50,100,310]
base5B=[50,-100,310]
base5T=[50,100,310]
base6B=[120,-100,240]
base6T=[120,100,240]
base7B=[120,-100,170]
base7T=[120,100,170]
base8B=[50,-100,100]
base8T=[50,100,100]
center=[0 , 0 , 205] 

#Definition of 4 polygon faces
poly1= [base1B, base2B, base2T, base1T]
poly2= [base2B, base3B, base3T, base2T]
poly3= [base3B, base4B, base4T, base3T]
poly4= [base4B, base5B, base5T, base4T]
poly5= [base5B, base6B, base6T, base5T]
poly6= [base6B, base7B, base7T, base6T]
poly7= [base7B, base8B, base8T, base7T]
poly8= [base8B, base1B, base1T, base8T]

# Def of object
Cylinder = [poly1,poly2,poly3,poly4,poly5,poly6,poly7,poly8]

# Def of point cloud
CylinderPointCloud = [base1B,base1T,base2B,base2T,base3B,base3T,base4B,base4T,base5B,base5T,base6B,base6T,base7B,base7T,base8B,base8T,center]

#************************************************************************************

# Lighting Variables for Object and Light Source
start_R = 255
start_G = 51
start_B = 200
# normalize rgb
RGB_Magnitude = math.sqrt(start_R*start_R+start_G*start_G+start_B*start_B)
Kdr = start_R/RGB_Magnitude
Kdg = start_G/RGB_Magnitude
Kdb = start_B/RGB_Magnitude
Iar = 1
Iag = .3
Iab = .9
# normalize ambient intensity
Ia_Magnitude = math.sqrt(Iar*Iar+Iag*Iag+Iab*Iab)
Iar /= Ia_Magnitude
Iag /= Ia_Magnitude
Iab /= Ia_Magnitude
Lx = 1
Ly = 1
Lz = -1
#normalized L
L_length = math.sqrt(Lx*Lx+Ly*Ly+Lz*Lz)
Lx = Lx/L_length
Ly = Ly/L_length
Lx = Lz/L_length
Nx = 0
Ny = 0
Nz = 0
Ipr = 1
Ipg = 1
Ipb = 1
#normalize point intensity
Ip_Magnitude = math.sqrt(Ipr*Ipr+Ipg*Ipg+Ipb*Ipb)
Ipr /= Ip_Magnitude
Ipg /= Ip_Magnitude
Ipb /= Ip_Magnitude
Ksr = 1
Ksg = 1
Ksb = 1

#normalize ksr
Ks_Magnitude = math.sqrt(Ksr*Ksr+Ksg*Ksg+Ksb*Ksb)
Ksr /= Ks_Magnitude
Ksg /= Ks_Magnitude
Ksb /= Ks_Magnitude
ViewX = 0
ViewY = 0
ViewZ = -1
n = 300

#************************************************************************************

#objects = [Pyramid, Cube, TriangularPyramid] # initilizes array of objects
objects = [Cylinder]
selection = objects[0] # the pyramid is initially selected
backface_culling = True # backface culling is turned on by default
fill_toggle = 0 # Polygon filling starts off
filling = False # Filling is off
lines = True # Lines are on
depthbuffer = [[999999999 for x in range(CanvasWidth)] for y in range(CanvasHeight)] # Creates depth buffer
buffer = True # z buffering starts on
lighting = 0 # only ambient diffuse to start
shading = 0 # lambert shading to start with

# This function resets the all objects to their original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud
def resetObjects():
    # reset object point clouds to initial values
    CylinderPointCloud[0][0] = -50
    CylinderPointCloud[0][1] = -100
    CylinderPointCloud[0][2] = 100

    CylinderPointCloud[1][0] = -50
    CylinderPointCloud[1][1] = 100
    CylinderPointCloud[1][2] = 100

    CylinderPointCloud[2][0] = -120
    CylinderPointCloud[2][1] = -100
    CylinderPointCloud[2][2] = 170
     
    CylinderPointCloud[3][0] = -120
    CylinderPointCloud[3][1] = 100
    CylinderPointCloud[3][2] = 170

    CylinderPointCloud[4][0] = -120
    CylinderPointCloud[4][1] = -100
    CylinderPointCloud[4][2] = 240

    CylinderPointCloud[5][0] = -120
    CylinderPointCloud[5][1] = 100
    CylinderPointCloud[5][2] = 240

    CylinderPointCloud[6][0] = -50
    CylinderPointCloud[6][1] = -100
    CylinderPointCloud[6][2] = 310
 
    CylinderPointCloud[7][0] = -50
    CylinderPointCloud[7][1] = 100
    CylinderPointCloud[7][2] = 310

    CylinderPointCloud[8][0] = 50
    CylinderPointCloud[8][1] = -100
    CylinderPointCloud[8][2] = 310

    CylinderPointCloud[9][0] = 50
    CylinderPointCloud[9][1] = 100
    CylinderPointCloud[9][2] = 310
 
    CylinderPointCloud[10][0] = 120
    CylinderPointCloud[10][1] = -100
    CylinderPointCloud[10][2] = 240

    CylinderPointCloud[11][0] = 120
    CylinderPointCloud[11][1] = 100
    CylinderPointCloud[11][2] = 240

    CylinderPointCloud[12][0] = 120
    CylinderPointCloud[12][1] = -100
    CylinderPointCloud[12][2] = 170

    CylinderPointCloud[13][0] = 120
    CylinderPointCloud[13][1] = 100
    CylinderPointCloud[13][2] = 170

    CylinderPointCloud[14][0] = 50
    CylinderPointCloud[14][1] = -100
    CylinderPointCloud[14][2] = 100

    CylinderPointCloud[15][0] = 50
    CylinderPointCloud[15][1] = 100
    CylinderPointCloud[15][2] = 100

    CylinderPointCloud[16][0] = 0
    CylinderPointCloud[16][1] = 0
    CylinderPointCloud[16][2] = 205

# This function translates an object by some displacement.  The displacement is a 3D 
# vector so the amount of displacement in each dimension can vary.
def translate(object, displacement):
    
    for i in range(len(object)): # iterates over 2d array object
        for j in range(len(object[i])):
            object[i][j] += displacement[j] # increases each point vector component by corresponing displacement component
    
# This function performs a simple uniform scale of an object assuming the object is 
# centered at the origin.  The scalefactor is a scalar.
def scale(object,scalefactor):

    # sets the origin point to be the center point of the object being scaled
    # this works by creating a copy of the selected object's center point list
    origin = CylinderPointCloud[16][:]

    neg_origin = [-x for x in origin] # inverse origin used to translate back to 0,0,0
    translate(object, neg_origin)
    
    for i in range(len(object)): #i iterates ovrt 2d array object
        for j in range(len(object[i])):
            object[i][j] *= scalefactor # multiplies point vector component by scale factor

    translate(object, origin) # translates object back to its original position

# This function performs a rotation of an object about the Z axis (from +X to +Y) 
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]
def rotateZ(object,degrees):

    # sets the origin point to be the center point of the object being scaled
    # this works by creating a copy of the selected object's center point list
    origin = CylinderPointCloud[16][:]

    neg_origin = [-x for x in origin] # inverse origin used to translate back to 0,0,0
    translate(object, neg_origin)

    for i in range(len(object)): #i iterates over points
        x = object[i][0]
        y = object[i][1]
        object[i][0] = x*math.cos(math.radians(degrees)) - y*math.sin(math.radians(degrees)) # formula for x coord change of z-axis rotation
        object[i][1] = x*math.sin(math.radians(degrees)) + y*math.cos(math.radians(degrees)) # formula for y coord change of z-axis rotation
        # z coord does not change

    translate(object, origin) # translates object back to its original position
    
# This function performs a rotation of an object about the Y axis (from +Z to +X) 
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
def rotateY(object,degrees):

    # sets the origin point to be the center point of the object being scaled
    # this works by creating a copy of the selected object's center point list
    origin = CylinderPointCloud[16][:]

    neg_origin = [-x for x in origin] # inverse origin used to translate back to 0,0,0
    translate(object, neg_origin)

    for i in range(len(object)): #i iterates over points
        x = object[i][0]
        z = object[i][2]
        object[i][0] = x*math.cos(math.radians(degrees)) + z*math.sin(math.radians(degrees)) # formula for x coord change of y-axis rotation
        # y coord does not change
        object[i][2] = -x*math.sin(math.radians(degrees)) + z*math.cos(math.radians(degrees)) # formula for z coord change of y-axis rotation

    translate(object, origin) # translates object back to its original position

# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
def rotateX(object,degrees):

    # sets the origin point to be the center point of the object being scaled
    # this works by creating a copy of the selected object's center point list
    origin = CylinderPointCloud[16][:]

    neg_origin = [-x for x in origin] # inverse origin used to translate back to 0,0,0
    translate(object, neg_origin)

    for i in range(len(object)): #i iterates over points
        y = object[i][1]
        z = object[i][2]
        # x coord does not change
        object[i][1] = y*math.cos(math.radians(degrees)) - z*math.sin(math.radians(degrees)) # formula for y coord change of x-axis rotation
        object[i][2] = y*math.sin(math.radians(degrees)) + z*math.cos(math.radians(degrees)) # formula for z coord change of x-axis rotation

    translate(object, origin) # translates object back to its original position

# This function draws the scene as a whole by calling drawObject on each object
# The selected object is drawn in different color
def Draw():
    global depthbuffer
    global current_lighting
    global current_shading

    # reset the depth buffer after everydraw
    depthbuffer = [[999999999 for x in range(CanvasWidth)] for y in range(CanvasHeight)]
    
    for i in range(len(objects)):
        if (objects[i] == selection): # the selected object is marked as selected
            drawObject(objects[i], True) 
        else:
            drawObject(objects[i], False)

    w.create_text(10,10,anchor=W,text=current_lighting)
    w.create_text(10,20,anchor=W,text=current_shading)
        
# The function will draw an object by repeatedly callying drawPoly on each polygon in the object 
def drawObject(object, selected):
    global backface_culling
    global filling
    global Nx
    global Ny
    global Nz
    i = 0
    while i < len(object):

        # only does back face culling if it is enabled
 
        p0x = object[i][0][0] #object[poly][point][coord]
        p0y = object[i][0][1]
        p0z = object[i][0][2]
        p1x = object[i][1][0]
        p1y = object[i][1][1]
        p1z = object[i][1][2]
        p2x = object[i][2][0]
        p2y = object[i][2][1]
        p2z = object[i][2][2]

        # calculates surface normal
        A = ((p1y-p0y)*(p2z-p0z)-(p2y-p0y)*(p1z-p0z))
        B = -((p1x-p0x)*(p2z-p0z)-(p2x-p0x)*(p1z-p0z))
        C = ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))

        Nx = A
        Ny = B
        Nz = C
        
        D = p0x * A + p0y * B + p0z * C

        # determines if the poly is visible by taking the dot prod. of the surface norm, and the camera's location at 0,0,-d
        visibility_result = A * 0 + B * 0 + C * -d - D
        
        if (visibility_result > 0):
            drawPoly(object[i], selected, filling) #draws poly for every poly

        if not backface_culling:
            drawPoly(object[i], selected, False) #draws poly for every poly

        i += 1 

# This function will draw a polygon by repeatedly callying drawLine on each pair of points 
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly, selected, filling):

    if filling:
        fill(poly)
    
    i = 0

    if lines:
        while i < len(poly) - 1:
            drawLine(poly[i], poly[i + 1], selected) # calls draw line for every point pair except last and first
            i+=1
        drawLine(poly[-1], poly[0], selected) # draws line between last point and first point

# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project' 
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start,end,selected):

    startdisplay = project(start) # projects start point to get start display coordinates
    enddisplay = project(end) # projects end point to get end display coordinates
    startdisplay = convertToDisplayCoordinates(startdisplay) # coords are converted 
    enddisplay = convertToDisplayCoordinates(enddisplay)

    w.create_line(startdisplay[0],startdisplay[1],enddisplay[0],enddisplay[1]) # the line is drawn

    #if (selected):
    #    w.create_line(startdisplay[0],startdisplay[1],enddisplay[0],enddisplay[1], fill = 'grey') # the line is drawn
        
# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it 
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    ps = []
    ps.append(d*point[0]/(d+point[2])) # uses project formula to convert 3d point to 2d point. this is for x coord
    ps.append(d*point[1]/(d+point[2])) # does same for y coordinate
    ps.append(point[2]/(d+point[2])) # and the z

    return ps

# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a 
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    displayXY = []

    displayXY.append(point[0] + CanvasWidth/2) # x coord adds a 200 px cushion to center it in the viewing window
    displayXY.append(CanvasHeight/2 - point[1]) # subracting the y coord from 200 will center it
    displayXY.append(point[2])
    return displayXY

# This function fills the polygon by creating a table of the edges and filling each pixel between the edges
# This function also handles coloring of the pixels, and z buffering
def fill(poly):
    global depthbuffer
    global buffer
    global start_R
    global start_G
    global start_B
    global Kdr
    global Kdg
    global Kdb
    global Iar
    global Iag
    global Iab
    global Lx
    global Ly
    global Lz
    global Nx
    global Ny
    global Nz

    # instantiates the needed lists
    xpoints = []
    ypoints = []
    projected_poly = []
    edges = []
    unprojected_edges = []
    edge_table = []

    i = 0
    # converts points of the poly to display coordinates
    # and stores new points in the proper list
    while i < len(poly):
        projected_poly.append(convertToDisplayCoordinates(project(poly[i])))
        xpoints.append(projected_poly[i][0])
        ypoints.append(projected_poly[i][1])
        i += 1

    # sets y_min and y_max
    y_min = min(ypoints)
    y_max = max(ypoints)

    i = 0
    # adds edges to the edge list
    while i < len(projected_poly) - 1:
        edges.append([projected_poly[i], projected_poly[i+1]])
        unprojected_edges.append([poly[i],poly[i+1]])
        i+=1
    edges.append([projected_poly[-1], projected_poly[0]])
    unprojected_edges.append([poly[-1],poly[0]])

    i = 0
    # fills edge table with proper values
    while i < len(edges):
        # sorts by smallest y
        if edges[i][0][1] < edges[i][1][1]:
            x_start = edges[i][0][0]
            x_end = edges[i][1][0]
            y_start = edges[i][0][1]
            y_end = edges[i][1][1]
            z_start = edges[i][0][2]
            z_end = edges[i][1][2]

            vertex1 = unprojected_edges[i][0]
            vertex2 = unprojected_edges[i][1]
            # checks if y_end - y_start is not 0
            try:
                z_slope = (edges[i][1][2]-edges[i][0][2])/(y_end-y_start)
            except:
                z_slope = (edges[i][1][2]-edges[i][0][2])
        else:
            x_start = edges[i][1][0]
            x_end = edges[i][0][0]
            y_start = edges[i][1][1]
            y_end = edges[i][0][1]
            z_start = edges[i][1][2]
            z_end = edges[i][0][2]

            vertex1 = unprojected_edges[i][1]
            vertex2 = unprojected_edges[i][0]
            try:
                z_slope = (edges[i][0][2]-edges[i][1][2])/(y_end-y_start)
            except:
                z_slope = (edges[i][0][2]-edges[i][1][2])

        # determines normals for both vertices
        vertex1_normal = getNormal(vertex1)
        Vx = vertex1_normal[0]
        Vy = vertex1_normal[1]
        Vz = vertex1_normal[2]

        #projected_vertex1 = project(vertex1)

        vertex1_I = Light(vertex1[0],vertex1[1],Vx,Vy,Vz)

        vertex2_normal = getNormal(vertex2)
        Vx2 = vertex2_normal[0]
        Vy2 = vertex2_normal[1]
        Vz2 = vertex2_normal[2]

        #projected_vertex2 = project(vertex2)

        vertex2_I = Light(vertex2[0],vertex2[1],Vx2,Vy2,Vz2)

        if vertex2_I[0] < 0: vertex2_I[0] = 0
        if vertex2_I[1] < 0: vertex2_I[1] = 0
        if vertex2_I[2] < 0: vertex2_I[2] = 0

        # the following determines the delta I values for gourard shading
        try:
            dIr = (vertex2_I[0] - vertex1_I[0]) / (y_end-y_start) # delta Ir
            dIg = (vertex2_I[1] - vertex1_I[1]) / (y_end-y_start)# delta Ig
            dIb = (vertex2_I[2] - vertex1_I[2]) / (y_end-y_start)# delta Ib
        except:
            dIr = (vertex2_I[0] - vertex1_I[0]) 
            dIg = (vertex2_I[1] - vertex1_I[1])
            dIb = (vertex2_I[2] - vertex1_I[2])

        # the following code calculates the delta normals of the vertices for phong shading
        try:
            dVx = (vertex2_normal[0] - vertex1_normal[0]) / (y_end-y_start)
            dVy = (vertex2_normal[1] - vertex1_normal[1]) / (y_end-y_start)
            dVz = (vertex2_normal[2] - vertex1_normal[2]) / (y_end-y_start)
        except:
            dVx = (vertex2_normal[0] - vertex1_normal[0]) 
            dVy = (vertex2_normal[1] - vertex1_normal[1]) 
            dVz = (vertex2_normal[2] - vertex1_normal[2])
        
        # if the inverse slope is infinite, there is no need to store it in the table
        try:
            inverse_slope = (x_end - x_start) / (y_end - y_start)
            edge_table.append([x_start, y_start, y_end, inverse_slope, z_start, z_slope,\
                               vertex1_I[0],vertex1_I[1],vertex1_I[2],dIr,dIg,dIb,\
                               Vx,Vy,Vz,dVx,dVy,dVz])                                    
        except:
            pass

        i += 1

    edge_table = sort(edge_table) # sorts the edge table

    first_edge = edge_table[0]
    second_edge = edge_table[1]
    edge_index = 2 # index of next available edge

    first_edge_x = first_edge[0]
    second_edge_x = second_edge[0]

    first_edge_z = first_edge[4]
    second_edge_z = second_edge[4]

    # starting intensities for first and second edge
    # used for gouraurd shading
    first_edge_Ir = first_edge[6]
    first_edge_Ig = first_edge[7]
    first_edge_Ib = first_edge[8]

    second_edge_Ir = second_edge[6]
    second_edge_Ig = second_edge[7]
    second_edge_Ib = second_edge[8]

    # starting normals for first and second edge
    # used for phong shading
    first_edge_Px = first_edge[12]
    first_edge_Py = first_edge[13]
    first_edge_Pz = first_edge[14]

    second_edge_Px = second_edge[12]
    second_edge_Py = second_edge[13]
    second_edge_Pz = second_edge[14]

    # Determines fill color based on object
    if poly in objects[0]:
        fill_color = 1
    elif poly in objects[1]:
        fill_color = 2
    else:
        fill_color = 3

    # Normalizes N
    # used for faceted shading
    N_length = math.sqrt(Nx*Nx+Ny*Ny+Nz*Nz)
    Nx = Nx/N_length
    Ny = Ny/N_length
    Nz = Nz/N_length

    # FILL LOOP BEGINS ------------------------------------
    y = y_min
    while y <= y_max:

        # changes the first edge if y extends first_edges y_end
        if y >= first_edge[2]:
            first_edge = edge_table[edge_index]
            first_edge_x = first_edge[0]
            edge_index += 1

        # changes the second edge if y extends second_edges y_end
        if y >= second_edge[2]:
            second_edge = edge_table[edge_index]
            second_edge_x = second_edge[0]
            edge_index += 1

        # sets current x and z values
        x = first_edge_x
        z = first_edge_z

        Ir = first_edge_Ir
        Ig = first_edge_Ig
        Ib = first_edge_Ib

        Px = first_edge_Px
        Py = first_edge_Py
        Pz = first_edge_Pz

        if Ir < 0: Ir = 0
        if Ig < 0: Ig = 0
        if Ib < 0: Ib = 0
        
        # loops through rows
        while x < second_edge_x:

            # will only run if the z is closer than what is stored in the depth buffer
            # or if depth buffering is turned off
            if (depthbuffer[int(x)][int(y)] > z or not buffer):

                if shading == 0: # Lambert Shading
                    Intensity = Light(x,y,Nx,Ny,Nz)

                elif shading == 1: # Gouraurd Shading
                    Intensity = [Ir, Ig, Ib]

                else: # Phong Shading
                    Intensity = Light(x,y, Px, Py, Pz)
                
                R = int(start_R*Intensity[0])
                G = int(start_G*Intensity[1])
                B = int(start_B*Intensity[2])
                # choose proper fill color based on the object
                hex_value = '#%02x%02x%02x' % (R, G, B)

                # draws the pixel
                w.create_rectangle(x,y,x,y,width=0, fill=hex_value)
                w.create_rectangle(x+1,y,x+1,y,width=0, fill=hex_value)

                depthbuffer[int(x)][int(y)] = z

            # updates x and z values
            z += (second_edge_z - first_edge_z) / (second_edge_x - first_edge_x)

            # updates rgb intensities
            Ir += (second_edge_Ir - first_edge_Ir) / (second_edge_x - first_edge_x)
            Ig += (second_edge_Ig - first_edge_Ig) / (second_edge_x - first_edge_x)
            Ib += (second_edge_Ig - first_edge_Ig) / (second_edge_x - first_edge_x)

            # updates normals
            Px += (second_edge_Px - first_edge_Px) / (second_edge_x - first_edge_x)
            Py += (second_edge_Py - first_edge_Py) / (second_edge_x - first_edge_x)
            Pz += (second_edge_Pz - first_edge_Pz) / (second_edge_x - first_edge_x)

            x += 1
            
        # updates the start and end points of the line
        first_edge_x = first_edge_x + first_edge[3]
        second_edge_x = second_edge_x + second_edge[3]

        # changes z values based on z slope
        first_edge_z += first_edge[5]
        second_edge_z += second_edge[5]

        # changes rgb intensity based on dI
        first_edge_Ir += first_edge[9]
        first_edge_Ig += first_edge[10]
        first_edge_Ib += first_edge[11]

        second_edge_Ir += second_edge[9]
        second_edge_Ig += second_edge[10]
        second_edge_Ib += second_edge[11]

        # changes normals based on dV
        first_edge_Px += first_edge[15]
        first_edge_Py += first_edge[16]
        first_edge_Pz += first_edge[17]

        second_edge_Px += second_edge[15]
        second_edge_Py += second_edge[16]
        second_edge_Pz += second_edge[17]
        
        y += 1 

# The following function sorts edge tables based on y_start,
# x_start, slopem and y_end 
def sort(table):
    
    sorted_table = []

    # loops as long as there are values in the unsorted table
    while table:
        i = 0
        smallest = 9999999 # init smallest to be a large num
        # loops over the values in the unsorted table
        while i < len(table):
            # if the table's y_start is < smallest, it is the new smallest
            if table[i][1] < smallest:
                smallest = table[i][1]
                smallest_row = table[i]

            # tie on y_start
            elif table[i][1] == smallest:
                if table[i][0] < smallest_row[0]:
                    smallest_row = table[i]

                # tie on x_start
                elif table[i][0] == smallest_row[0]:
                    if table[i][3] < smallest_row[3]:
                        smallest_row = table[i]

                    # tie on slope
                    elif table[i][3] == smallest_row[3]:
                        if table[i][2] < smallest_row[2]:
                            smallest_row = table[i]
                
                
            i += 1

        # the smallest row is appended to the sorted table and removed from the unsorted
        sorted_table.append(smallest_row)
        table.remove(smallest_row)

    return sorted_table

def Light(x,y,Fx,Fy,Fz):
    global Kdr
    global Kdg
    global Kdb
    global Iar
    global Iag
    global Iab
    global Lx
    global Ly
    global Lz
    global ViewX
    global ViewY
    global ViewZ
    global n
    global Ksr
    global Ksg
    global Ksb
    
    I=[0,0,0]
    if True: # Ambient only
        # Ambient Diffuse
        I[0] = Kdr * Iar
        I[1] = Kdg * Iag
        I[2] = Kdb * Iab

        # Point Diffuse
        if lighting > 0: # lighting is either level 1 or 2
            I[0] += Ipr * Kdr * (Fx*Lx+Fy*Ly+Fz*Lz)
            I[1] += Ipg * Kdg * (Fx*Lx+Fy*Ly+Fz*Lz)
            I[2] += Ipb * Kdb * (Fx*Lx+Fy*Ly+Fz*Lz)

            if I[0] < 0: I[0] = 0
            if I[1] < 0: I[1] = 0
            if I[2] < 0: I[2] = 0

            # Point Specular
            if lighting == 2:
                # determines reflection vector
                tcphi = 2*(Fx*Lx+Fy*Ly*Fx*Lz)

                if tcphi > 0:
                    Rx = Fx-Lx/tcphi
                    Ry = Fy-Ly/tcphi
                    Rz = Fz-Lz/tcphi
                elif tcphi == 0:
                    Rx = -Lx
                    Ry = -Ly
                    Rz = -Lz
                else:
                    Rx = -Fx + Lx/tcphi
                    Ry = -Fy + Ly/tcphi
                    Rz = -Fz + Lz/tcphi

                # normalize R
                a = math.sqrt(Rx*Rx+Ry*Ry+Rz*Rz)
                Rx /= a
                Ry /= a
                Rz /= a
                
                I[0] += Ipr * Ksr * (Rx*ViewX+Ry*ViewY+Rz*ViewZ) ** n
                I[1] += Ipg * Ksg * (Rx*ViewX+Ry*ViewY+Rz*ViewZ) ** n
                I[2] += Ipb * Ksb * (Rx*ViewX+Ry*ViewY+Rz*ViewZ) ** n

        return I

def getNormal(point):
    i = 0
    point_normal = [0,0,0]
    while i < len(Cylinder):
        if point in Cylinder[i]:
            p0x = Cylinder[i][0][0] #object[poly][point][coord]
            p0y = Cylinder[i][0][1]
            p0z = Cylinder[i][0][2]
            p1x = Cylinder[i][1][0]
            p1y = Cylinder[i][1][1]
            p1z = Cylinder[i][1][2]
            p2x = Cylinder[i][2][0]
            p2y = Cylinder[i][2][1]
            p2z = Cylinder[i][2][2]

            # calculates surface normal
            A = ((p1y-p0y)*(p2z-p0z)-(p2y-p0y)*(p1z-p0z))
            B = -((p1x-p0x)*(p2z-p0z)-(p2x-p0x)*(p1z-p0z))
            C = ((p1x-p0x)*(p2y-p0y)-(p2x-p0x)*(p1y-p0y))

            point_normal[0] += A
            point_normal[1] += B
            point_normal[2] += C

        i += 1
    magnitude = math.sqrt(point_normal[0]*point_normal[0]+point_normal[1]*point_normal[1]+point_normal[2]*point_normal[2])
    if (magnitude != 0):
        point_normal[0] = point_normal[0]/magnitude
        point_normal[1] = point_normal[1]/magnitude
        point_normal[2] = point_normal[2]/magnitude
    return point_normal
    

# **************************************************************************
# Everything below this point implements the interface
def cycle():
    global selection
    current_index = objects.index(selection)
    
    if (objects[current_index] == objects[-1]): #if the current index is the last in the list, go to first index
        selection = objects[0]
    else:
        selection = objects[current_index + 1]
    Draw()

def reset():
    w.delete(ALL)
    resetObjects()
    scale(CylinderPointCloud, 1.5)
    Draw()

def backface():
    w.delete(ALL)
    global backface_culling
    backface_culling = not backface_culling
    Draw()

def filltoggle():
    w.delete(ALL)
    global fill_toggle
    global filling
    global lines
    
    if fill_toggle + 1 < 3:
        fill_toggle += 1
    else:
        fill_toggle = 0

    if fill_toggle == 0:
        filling = False
        lines = True
    elif fill_toggle == 1:
        filling = True
        lines = True
    else:
        filling = True
        lines = False
        
    Draw()

def buffertoggle():
    w.delete(ALL)
    global buffer

    buffer = not buffer
    Draw()

def lightingtoggle():
    global lighting
    global current_lighting
    
    w.delete(ALL)

    if lighting + 1 < 3:
        lighting += 1
    else:
        lighting = 0

    if lighting == 0:
        current_lighting = "Ambient Diffuse Only"
    elif lighting == 1:
        current_lighting = "Ambient Diffuse & Point Diffuse"
    else:
        current_lighting = "Ambient Diffuse, Point Diffuse, & Point Specular"

    Draw()

def shadingtoggle():
    global shading
    global current_shading
    
    w.delete(ALL)

    if shading + 1 < 3:
        shading += 1
    else:
        shading = 0

    if shading == 0:
        current_shading = "Faceted"
    elif shading == 1:
        current_shading = "Gouraurd"
    else:
        current_shading = "Phong"

    Draw()
    

def larger():
    w.delete(ALL)
    scale(CylinderPointCloud, 1.1)
    Draw()

def smaller():
    w.delete(ALL)
    scale(CylinderPointCloud, .9)
    Draw()

def forward():
    w.delete(ALL)
    translate(CylinderPointCloud,[0,0,5])
    Draw()

def backward():
    w.delete(ALL)
    translate(CylinderPointCloud,[0,0,-5])
    Draw()

def left():
    w.delete(ALL)
    translate(CylinderPointCloud,[-5,0,0])
    Draw()

def right():
    w.delete(ALL)
    translate(CylinderPointCloud,[5,0,0])
    Draw()

def up():
    w.delete(ALL)
    translate(CylinderPointCloud,[0,5,0])
    Draw()

def down():
    w.delete(ALL)
    translate(CylinderPointCloud,[0,-5,0])
    Draw()

def xPlus():
    w.delete(ALL)
    rotateX(CylinderPointCloud,5)
    Draw()

def xMinus():
    w.delete(ALL)
    rotateX(CylinderPointCloud,-5)
    Draw()

def yPlus():
    w.delete(ALL)
    rotateY(CylinderPointCloud,5)
    Draw()

def yMinus():
    w.delete(ALL)
    rotateY(CylinderPointCloud,-5)
    Draw()
    
def zPlus():
    w.delete(ALL)
    rotateZ(CylinderPointCloud,5)
    Draw()
    
def zMinus():
    w.delete(ALL)
    rotateZ(CylinderPointCloud,-5)
    Draw()

root = Tk()
outerframe = Frame(root)
outerframe.pack()

# selection code ---------------------------------
selection = objects[0] #pyramid

scale(CylinderPointCloud, 1.5)
current_lighting = "Ambient Diffuse Only"
current_shading = "Faceted"

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)

Draw()

w.pack()

w.create_text(10,10,anchor=W,text=current_lighting)
w.create_text(10,20,anchor=W,text=current_shading)

controlpanel = Frame(outerframe)
controlpanel.pack()

cyclecontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
cyclecontrols.pack(side=LEFT)

cyclecontrolslabel = Label(cyclecontrols, text="Cycle")
cyclecontrolslabel.pack()

cycleButton = Button(cyclecontrols, text="Cycle", fg="green", command=cycle)
cycleButton.pack(side=LEFT)

resetcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="red", command=reset)
resetButton.pack(side=LEFT)

backfacecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
backfacecontrols.pack(side=LEFT)

backfacecontrolslabel = Label(backfacecontrols, text="Backface")
backfacecontrolslabel.pack()

backfaceButton = Button(backfacecontrols, text="Toggle", fg="Blue", command=backface)
backfaceButton.pack(side=LEFT)

fillcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
fillcontrols.pack(side=LEFT)

fillcontrolslabel = Label(fillcontrols, text="Fill")
fillcontrolslabel.pack()

fillButton = Button(fillcontrols, text="Toggle", fg="blue", command=filltoggle)
fillButton.pack(side=LEFT)

zbuffercontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
zbuffercontrols.pack(side=LEFT)

zbuffercontrolslabel = Label(zbuffercontrols, text="Z Buffer")
zbuffercontrolslabel.pack()

zbufferButton = Button(zbuffercontrols, text="Toggle", fg="blue", command=buffertoggle)
zbufferButton.pack(side=LEFT)

lightingcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
lightingcontrols.pack(side=LEFT)

lightingcontrolslabel = Label(lightingcontrols, text="Lighting")
lightingcontrolslabel.pack()

lightingButton = Button(lightingcontrols, text="Toggle", fg="blue", command=lightingtoggle)
lightingButton.pack(side=LEFT)

shadingcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
shadingcontrols.pack(side=LEFT)

shadingcontrolslabel = Label(shadingcontrols, text="Shading")
shadingcontrolslabel.pack()

shadingButton = Button(shadingcontrols, text="Toggle", fg="blue", command=shadingtoggle)
shadingButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="DN", command=down)
upButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

root.mainloop()
