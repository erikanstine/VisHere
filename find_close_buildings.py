import csv
import pandas as pd
from math import sqrt

kHowManyBlocks = 10
kHowManyBuildings = 25
#Remove placeholder/island data, sorts in order of BBL
manhat = pd.read_csv('/Users/erikanstine/Code/VisHere_Project_Folder/VisHere/bldgquery/manhattan_coords.csv')
manhat = manhat.sort_values(by='BBL')
manhat.drop('Unnamed: 0',axis = 1, inplace = True)
manhat = manhat[manhat['BBL'] > 1000019999]
manhat = manhat[manhat['BBL'] < 1022510000]
unique_BBL = pd.unique(manhat.BBL.ravel())

#Inst. dictionary of BB:center point and BB:distance from coords [replace later with Block object creation?]
BB_center = {}
BB_dist = {}

#Instantiate 'shortened' array (array of first 6 digits of BBLs, aka BB, the 'Borough/Block num')
shortened = []
for i in unique_BBL:
    a = str(i)[0:6] #takes first 6 digits
    if a not in shortened:
        shortened.append(a)

def swap_latlon_xy(point):
    return [float(point[1]),float(point[0])]

def format_coords(longstr,append_array):
    s = longstr.strip('MULTIPOLYGON (((').rstrip('))))')
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.split(',')
    ls = len(s)
    a = 0
    while a < ls:
        s[a] = s[a].split()
        s[a] = swap_latlon_xy(s[a])
        append_array.append(s[a]) #<------------------IMPORTANT
        a += 1
    #return s

def find_center(array):
    if len(array) != 4:
        print('Incorrect array. Must have 4 terms.')
    else:
        centroid1 = [(array[0][0] + array[1][0] + array[3][0])/3,(array[0][1] + array[1][1] + array[3][1])/3]
        centroid2 = [(array[2][0] + array[1][0] + array[3][0])/3,(array[2][1] + array[1][1] + array[3][1])/3]

        center = [(centroid1[0] + centroid2[0])/2,(centroid1[1] + centroid2[1])/2]

        return center

def find_distance(pt1,pt2):
    dx = pt1[0] - pt2[0]
    dy = pt1[1] - pt2[1]
    return sqrt(dx**2 + dy**2)

#find_maxes now returns centroid
def find_maxes(array):
    ew_array = []
    ns_array = []
    alen = len(array)
    p = 0
    while p < alen:
        ew_array += [array[p][1]]
        ns_array += [array[p][0]]
        p += 1
    n_max = max(ns_array)
    n_max_index = ns_array.index(n_max)
    n = array[n_max_index]

    s_max = min(ns_array)
    s_max_index = ns_array.index(s_max)
    s = array[s_max_index]

    e_max = max(ew_array)
    e_max_index = ew_array.index(e_max)
    e = array[e_max_index]

    w_max = min(ew_array)
    w_max_index = ew_array.index(w_max)
    w = array[w_max_index]

    max_array = [n,s,e,w]

    return find_center(max_array)

def find_close_blocks(coord):
    close_blocks = []
    for b, c in BB_center.items():
        BB_dist[b] = find_distance(BB_center[b],coord)

    for i in sorted(BB_dist, key = BB_dist.__getitem__)[:kHowManyBlocks]:
        close_blocks.append(i)

    return close_blocks

def close_bldg(array, coord, numBuildings):
    #for BB, find closest 10 bldg centers from manhat geo data
    block_bldgs = []
    block_bldg_center = {}
    block_bldg_dist = {}
    close_array = []

    # Creates array of BBLs for a given block
    for h in array:
        for i in unique_BBL:
            if str(i).startswith(h):
                block_bldgs.append(i)

    # Finds centroid for all buildings
    for j in block_bldgs:
        temp_array = []
        t = manhat[manhat['BBL'] == j].the_geom.iloc[0]
        format_coords(t,temp_array)
        block_bldg_center[j] = find_maxes(temp_array)

    # Writes distance values to block_bldg_center
    for k, l in block_bldg_center.items():
        block_bldg_dist[k] = find_distance(block_bldg_center[k],coord)

    # Prints out the top 20 closest buildings/info
    for m in sorted(block_bldg_dist, key = block_bldg_dist.__getitem__)[:numBuildings]:
        close_array.append(int(m))
    # return the array of BBLs
    return close_array

#BEGIN FLOW: Instantiate BB_center [Can be saved to .csv/other DB?

with open('/Users/erikanstine/Code/VisHere_Project_Folder/VisHere/bldgquery/BB_centers.csv','rt') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        s = row[1]+','+row[2]
        s = s.strip("|['").rstrip("']|").split(',')
        s[0] = float(s[0])
        s[1] = float(s[1])
        BB_center[row[0]] = s

def building_finder(lat, lon, numBuildings):
    BIN_array = []
    BBL_BIN = pd.read_pickle('/Users/erikanstine/Code/VisHere_Project_Folder/VisHere/bldgquery/BBL_BIN.pickle')
    coord = [lat, lon]
    BBL_array = close_bldg(find_close_blocks(coord), coord, numBuildings)

    # for BBL in BBL_array, BIN_array.append(corresponding BIN)
    for bbl in BBL_array:
        vals = BBL_BIN[BBL_BIN['BBL'] == bbl]['BIN']
        for i in vals:
            BIN_array.append(i)

    return BIN_array
