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


#for index,x in enumerate(train_data):
#    answer_list=np.append(answer_list,np.sign(weight.T.dot(x)))


#print(train_csv)
#train_data=

# df_test=pd.read_csv('titanic/test.csv', sep=',')
# age_list=np.zeros(0)
# fare_list=np.zeros(0)
# survived_list=np.zeros(0)
# #---------------------------------------------none zero age input age list
# for idx,data in enumerate(df_train.values):
#     fare_list=np.append(fare_list,data[9])

#     if(math.isnan(data[5])==False):
#         age_list=np.append(age_list,data[5])
# #-------------------------------------------get the age median
# for data in df_test.values:
#     fare_list=np.append(fare_list,data[8])

# fare_list=pd.qcut(fare_list,6,labels=False)
# fare_train_list=fare_list[:len(df_train)]
# fare_test_list=fare_list[len(df_train):]
# #-----------------------------------------no use
# df_train["Fare_qcut"]=pd.qcut(df_train["Fare"],6,labels=False)
# #-----------------------------------------
# age_median=np.median(age_list)
# print("age:",age_median)
# #---------------------------------------input age median to original data
# for idx,data in enumerate(df_train.values):
#     if(data[1]==1):
#         survived_list=np.append(survived_list,1)
#     else:
#         survived_list=np.append(survived_list,-1)
#     if(math.isnan(data[5])):
#         df_train["Age"][idx]=age_median




# np_train_data=np.empty(5)

# #np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
# weight=np.zeros(5)
# #print(df_train["Sex"])
# for index,data in enumerate(df_train.values):
#     fare_price=fare_train_list[index]
#     if(data[4]=="female"):
#         sex=1
#     else:
#         sex=0
#     if(data[5]<16):
#         young=1
#     else:
#         young=0
#     np_train_data=np.vstack([np_train_data,[sex,young,data[2],fare_price,1]])
# #-----------------------------------------------------comaper every singal chance

# for i in range(1,5):
#     for index,x in enumerate(np_train_data):
#         answer=np.sign(weight.T.dot(x))
#         print(weight)
#         if(answer!=survived_list[index-1]):
#             weight+=x*survived_list[index-1]

# #-----------------------------------test data produce
# answer_list=np.empty(0)
# np_test_data=np.empty(5)

# df_test["Fare_qcut"]=pd.qcut(df_test["Fare"],6,labels=False)
# for index,data in enumerate(df_test.values):
#     fare_price=fare_test_list[index]
#     if(data[3]=="female"):
#         sex=1
#     else:
#         sex=0
#     if(data[4]<16):
#         young=1
#     else:
#         young=0
#     np_test_data=np.vstack([np_test_data,[sex,young,data[1],fare_price,1]])

# for index,x in enumerate(np_test_data):
#     answer_list=np.append(answer_list,np.sign(weight.T.dot(x)))



# right=0
# error=0
# df_answer=pd.read_csv('titanic/gender_submission.csv', sep=',')
# for index,compare in enumerate(df_answer.values):

#     if(answer_list[index+1]==-1):
#         answer_list[index+1]=int(0)
#     else:
#         answer_list[index+1]=int(1)
#     if(compare[1]==answer_list[index+1]):
#         right+=1
#     else:
#         error+=1
# print("right:",right)
# print("error:",error)
# print("accuracy:",right/(right+error))

# with open('submission.csv', 'w', newline='') as csvfile:
# # 建立 CSV 檔寫入器
#     writer = csv.writer(csvfile)

#     # 寫入一列資料
#     writer.writerow(['PassengerId', 'Survived'])
#     for index,compare in enumerate(df_answer.values):
# #        print(answer_list[index+1])
#         output_value=int(answer_list[index+1])
#         writer.writerow([compare[0],output_value])
