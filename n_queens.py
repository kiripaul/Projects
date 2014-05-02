#This program is an example of the N Queens Problem
#in which given a normal Chess board, the program has to
#figure the most optimal way to place N Queens such that no
#Queens check one another.

import random as rnd
rnd.seed()

def Main():
    ####Setting up the Genotype
    N = 8  #Number of Queens and size of chessboard(NxN)
    Runs = 30
    
    
    #p = [[0 for i in range(N)] for j in range(N)] #Used for Testing
    #g = list(range(N))                             #Used for Testing

    #for n in range(len(g)): #Used for Testing
    #    p[n][g[n]] = 1

    #for i in range(N):
    #    print i,p[i]
    
    #Want fitness to be 0 so that number of conflicting placements is minimized
    for ii in range(Runs):
        count =0
        p,g=Evolve_Mutation(N)
        fit = Fitness(p)
        while fit != 0:
            p,g=Evolve_Mutation(N)
            fit = Fitness(p)
            print count,g,fit
            for i in range(N): #Printing chessboard congfiguration
                print p[i]
            count +=1
        #Writing solutions to file
        solution = open("N_Queens_Solutions_Mutation.txt",'a')
        print "HI"
        solution.write((str(g)+"--->"+str(count)+"\n"))
        solution.close()
   
    

def Fitness(phenotype):
    ####Evaluating the Phenotype
    #print(len(phenotype))
    slope_points=[]
    #If the slope of two positions equals 1 or -1,
    #it means they are diagonally checking.
    #Since we only care about positions that are directly, diagonally putting each other in check
    #we only need worry about slopes that are eqaul to 1 or -1.  Everything else may be diagonally
    #positioned compared to our pivot, but not putting the piece in check
    Fitness_Value = 0
    for i in range(len(phenotype)): #Rows
        for j in range(len(phenotype)): #Columns
            pivot = phenotype[i][j]#pivot point for comparison;checking all other rows compared to this piece for slope
            #print i,j
            if pivot==1: #Piece is found in row
                slope_points.append(i)#--->x1,Row
                slope_points.append(j)#--->y1,Col
                for k in range(len(phenotype)-1): #Rows-1 (done so that we can compare two rows at a time); Comparing all other rows to pivot
                    for l in range(len(phenotype)): #Columns
                        check = phenotype[(k+1)][l] #(k+1) Comparing next row
                        if check==1:#Found a queen at current position
                            slope_points.append(k+1)#--->x2,Row
                            slope_points.append(l)#--->y2,Col
                        if len(slope_points)==4:
                            #We now have four points with which to do the calculation...
                            m=0
                            #print "x1=",slope_points[0],"y1=",slope_points[1],"x2=",slope_points[2],"y2=",slope_points[3]
                            if slope_points[0]!=slope_points[2] and slope_points[1]!=slope_points[3]:
                                m = ((float(slope_points[3]-slope_points[1])/(slope_points[2]-slope_points[0]))*-1) #Slope = y2-y1/x2-x1  
                                #Multiplied slope by -1 so that it matches my conceptual representation of a negative slope/positive slope
                                #i.e a negative slope being "\" and not "/"
                                #print slope_points , "Slope=",m
                                if m ==1.0 or m==-1.0:
                                    #Fitness value needs to be minimized here so as to have the fewest number of conflicts
                                    Fitness_Value+=1
                            slope_points.pop() #Pop position 3 and 2 (last two points that are not the pivot)
                            slope_points.pop()
                slope_points.pop() #Pop positions 1 and 0; pop off the pivot
                slope_points.pop()
    return Fitness_Value
    
def Evolve_Mutation(N):
    #Current Strategy: Randomly permute each position in the genotype list
    g = list(range(N))
    rnd.shuffle(g)

    ####Setting up the Phenotype: Placing the queens on the board
    p = [[0 for i in range(N)] for j in range(N)]
    for n in range(len(g)):
        p[n][g[n]] = 1
    return p,g
    
def Evolve_Recombination(N):
    #Current Strategy: Randomly permute each position in the genotype list
    g1 = list(range(N))
    g2 = list(range(N))
    rnd.shuffle(g1)
    rnd.shuffle(g2)

    ####Setting up the Phenotype: Placing the queens on the board
    p1 = [[0 for i in range(N)] for j in range(N)]
    p2 = [[0 for i in range(N)] for j in range(N)]
    for n in range(len(g1)):
        p1[n][g1[n]] = 1            
    for n in range(len(g2)):
        p2[n][g2[n]] = 1
    return g1,g2,p1,p2   
                
            
                    
                
                


Main()