import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import csv
train_csv=pd.read_csv('heart.csv', sep=',')
train_data=np.empty(10)
weight=np.zeros(10)
#train_data=np.empty(6)
target_list=np.zeros(0)

cross_validation=np.array([[0,30],[31,61],[62,92],[93,123],[124,154],[155,185],[186,216],[217,247],[248,278],[279,303]])
#print(cross_validation[0][2])


for data in train_csv.values:
    age=data[0]    
    cp=data[2]
    fbs=data[5]
    thal=data[12]
    thalach=data[7]
    oldpeak=data[9]
    restecg=data[6]
    slope=data[10]
    sex=data[1]
    thal_reversable_defect=0
    thal_fixed_defect=0
    thal_normal=0
    number_major_vessel=data[11]
    if(thal==3):
        thal_reversable_defect=1
    elif(thal==2):
        thal_fixed_defect=1
    elif(thal==1):
        thal_normal=1
    
    temp=np.array([sex,slope,restecg,oldpeak,number_major_vessel,thalach,thal_normal,thal_fixed_defect,thal_reversable_defect,1])
#    temp=np.array([sex,slope,restecg,oldpeak,thalach])
    train_data=np.vstack((train_data,temp))
    if(data[13]==1):
        target_list=np.append(target_list,1)
    else:
        target_list=np.append(target_list,-1)
    

#----------------------delete first zero row
train_data=np.delete(train_data,0,0)


# for index,x in enumerate(train_data):
#     answer=np.sign(weight.T.dot(x))
#     if(answer!=target_list[index]):
#         weight+=x*target_list[index]
# print(weight)




# right=0
# error=0
# for index,x in enumerate(train_data):
#    answer=np.sign(weight.T.dot(x))
#    if(answer!=target_list[index]):
#        error=error+1
#    else:
#        right=right+1
# print("right:",right)
# print("error:",error)
# print("accuracy:",round(right/(right+error),2))

#print(cross_validation[1][1])
#exit()
#--------------------------------------------test for cross validation
total_error=0
total_right=0
for i in range(0,10):
    error=0
    right=0
    for index,x in enumerate(train_data):
        if(index>=cross_validation[i][0] and index<=cross_validation[i][1]):
            continue
        else:
            answer=np.sign(weight.T.dot(x))
    #        print(weight)
            if(answer!=target_list[index]):
                weight+=x*target_list[index]
    print(weight)
    for index,x in enumerate(train_data):
        if(index>=cross_validation[i][0] and index<=cross_validation[i][1]):
            answer=np.sign(weight.T.dot(x))
            if(answer!=target_list[index]):
                error=error+1
            else:
                right=right+1
        else:
            continue
    print("right:",right)
    print("error:",error)
    print("accuracy:",round(right/(right+error),2))     
    total_right=total_right+right
    total_error=total_error+error
print("---------------------------------total-----------------------------------------------------------")
print("\tright:",total_right)
print("\terror:",total_error)
print("\taccuracy:",round(total_right/(total_right+total_error),2))     

