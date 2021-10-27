import math
from Schedule import Schedule
from itertools import permutations

"""
Notes:
    This is my blind attempt at coming up with a permutation algorithm
    Number of recursive loops is determined by the closest ceiling 2^x value
    After 16 (2^4) permutations the speed greatly drops
"""

def create_permutations(schedule, num_of_permutations, total_work_week_hours = 40):
       
    #calculate number of recursive loops needed 2^x
    max_layers = math.ceil(math.log(num_of_permutations,2))
    permutations_ = permutate(schedule.get_schedule()[:total_work_week_hours], max_layers, 0)
        
    #only select unique permutations
    unique_permutations = []
    for p in permutations_:
        if p not in unique_permutations:
            unique_permutations.append(p)
        if len(unique_permutations) == num_of_permutations:
            #end loop if required number of permutations are met
            break
    
    #return a list of Schedule objects
    return [Schedule(schedule.get_employees(),p) for p in unique_permutations]

def permutate(schedule, max_layers, current_layer):
    if len(schedule) <=1 or current_layer >= max_layers:
        #if schedule list cannot be divided furter or max recursive layers has been hit: exit recursive loops
        return [schedule]
    permutations = []
    #divide schedule into 2 parts
    slice1 = permutate(schedule[:int(len(schedule)/2)], max_layers, current_layer+1)
    slice2 = permutate(schedule[int(len(schedule)/2):], max_layers, current_layer+1)

    #combine 2 elements in both their possible combinations
    #eg: A,B -> A,B and B,A 
    if slice1 is not None and slice2 is not None:
        for x in slice1:
            for y in slice2:
                permutations.append(x + y)
                permutations.append(y + x)
                    
    return permutations




