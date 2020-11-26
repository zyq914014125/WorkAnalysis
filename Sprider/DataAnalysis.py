import csv
import random

#读csv
with open('java',"rt", encoding="utf-8") as file:
    reader=csv.DictReader(file)
    datas=[row for row in reader]
#随机data
random.shuffle(datas)
#取90%数据为训练集，剩余10%为测试集
n = len(datas)//10
train_list = datas[n:]
test_list = datas[0:n]

#KNN
def distance(k1,k2):
    length=0
    #总距离测试
    for key in ['experience','education','demand','treatment']:
        if k1[key]!='0' or k2[key]!='0':
          length+=(float(k1[key])-float(k2[key]))**2
        else:
            continue
    #距离开方
    # print(length**0.5)
    return length**0.5
# 算距离,排序,取k,加权平均
def knn(data,K):
    # for train in test_list:
    #     print(train)
    result=[
        {"salary":train['salary'],"distance":distance(data,train)}
        for train in train_list
    ]
    #排序
    result=sorted(result,key=lambda item:item['distance'])
    #取K个
    result2= result[0:K]
    #结果预测
    result3={"distance":0}
    #加权平均
      #总距离
    sum=0
    for re in result2:
       if re['salary']!=0:
         sum+=re['distance']
    #平均
    for re in result2:
        if re['distance']!=0:
         result3["distance"]+=1-re['distance']/sum
    for re in result2:
       if result3['distance']==re['distance']:
           return re['salary']

def Test(K):
    count=0
    all=0
    # 测试
    for test in test_list:
        result1=test['salary']
        result2=knn(test,K)
        if result2!=None and result1.find('0')!=-1:
            if result2.find('0')!=-1:
                all += 1
                if abs(float(result1) - float(result2))<1:
                    count+=1
    if count!=0 and all!=0:
        return count/all

print(Test(6))



