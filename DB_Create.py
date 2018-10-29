import pandas as pd

#df = pd.DataFrame(columns = ['UId','Name','Age','Phone No','Email Address'])
#df.to_csv("data/DBNames.csv", index = False)

Uid = input("Enter your UserId : ")
name = input("Enter your name : ")
age = input("Enter your age : ")
phone = input("Enter your Phone No. : ")
email = input("Enter your Email Address : ")

rawData = {
    'UId' : [Uid],
    'Name' : [name],
    'Age' : [age],
    'Phone No' : [phone],
    'Email Address' : [email]
}
df2 = pd.DataFrame(rawData)

with open("data/DBNames.csv",'a') as file:
    df2.to_csv(file,index = False,header = False)