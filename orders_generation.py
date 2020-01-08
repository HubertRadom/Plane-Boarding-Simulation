import random
number_of_rows = 16
columns = [-3,-2,-1,1,2,3]
def random_order():
    result =[]
    for row in range(1,number_of_rows+1):
        for col in columns:
            result.append([row,col])
    random.shuffle(result)
    return result

def back_to_front():
    result =[]
    for row in range(number_of_rows,0,-1):
        col_copy=columns.copy()
        random.shuffle(col_copy)
        for col in col_copy:
            result.append([row,col])
    return result

def front_to_back():
    result =[]
    for row in range(1,number_of_rows+1):
        col_copy=columns.copy()
        random.shuffle(col_copy)
        for col in col_copy:
            result.append([row,col])
    return result

def back_to_front_4():
    result =[]
    for group in range(3,-1,-1):
        group_arr=[]
        for sub_group in range(1,5):
            for col in columns:
                group_arr.append([4*group+sub_group,col])
        random.shuffle(group_arr)
        result+=group_arr
    return result

def front_to_back_4():
    result =[]
    for group in range(4):
        group_arr=[]
        for sub_group in range(1,5):
            for col in columns:
                group_arr.append([4*group+sub_group,col])
        random.shuffle(group_arr)
        result+=group_arr
    return result

def window_middle_isle():
    result =[]
    for col in range(3,0,-1):
        group=[]
        for row in range(1,number_of_rows+1):
            group.append([row,col])
            group.append([row,-col])
        random.shuffle(group)
        result+=group
    return result

def steffen_perfect():
    result =[]
    columns=[3,2,1]
    for col in columns:
        for row in range(number_of_rows,0,-2):
            result.append([row,-col])
        for row in range(number_of_rows,0,-2):
            result.append([row,col])
        for row in range(number_of_rows-1,0,-2):
            result.append([row,-col])
        for row in range(number_of_rows-1,0,-2):
            result.append([row,col])
    return result

def steffen_modified():
    result =[]
    group_1=[]
    for row in range(number_of_rows,0,-2):
        for col in [-3,-2,-1]:
            group_1.append([row,col])
    random.shuffle(group_1)
    result+=group_1
    group_2=[]
    for row in range(number_of_rows,0,-2):
        for col in [3,2,1]:
            group_2.append([row,col])
    random.shuffle(group_2)
    result+=group_2
    group_3=[]
    for row in range(number_of_rows-1,0,-2):
        for col in [-3,-2,-1]:
            group_3.append([row,col])
    random.shuffle(group_3)
    result+=group_3
    group_4=[]
    for row in range(number_of_rows-1,0,-2):
        for col in [3,2,1]:
            group_4.append([row,col])
    random.shuffle(group_4)
    result+=group_4
    return result

def shuffle_keeping_order(tabs):
    result =tabs[0].copy()
    for  i in range(1,len(tabs)):
        last_insert_id=-1
        for element in tabs[i]:
            random_id = random.randint(last_insert_id+1,len(result))
            result=result[:random_id]+[element]+result[random_id:]
            last_insert_id=random_id
    return result
        
def random_without_shuffle():
    result =[]
    for row in range(1,number_of_rows+1):
        result.append([[row,3],[row,2],[row,1]])
        result.append([[row,-3],[row,-2],[row,-1]])
    return shuffle_keeping_order(result)


def back_to_front_4_without_shuffle():
    result =[]
    for group in range(3,-1,-1):
        group_arr=[]
        for sub_group in range(1,5):
            row = 4*group+sub_group
            group_arr.append([[row,3],[row,2],[row,1]])
            group_arr.append([[row,-3],[row,-2],[row,-1]])
        result+=shuffle_keeping_order(group_arr)
    return result

