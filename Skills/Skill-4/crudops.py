from pymongo import MongoClient
client = MongoClient("mongodb+srv://pfsd123:pfsd123@cluster0.ujwlikz.mongodb.net/?retryWrites=true&w=majority")
db = client['Skill4']
studentdata=db.studentDetails
loop =True
while(loop):
    print("1. Insert Data\n2. Delete Data\n3. Update Data\n4. Search\n5. End\nPlease Select the Option : ")
    v=int(input())
    if(v==1):
        print("Enter the no of students you want to add")
        for i in range(int(input())):
            print("Please Enter Student Name : ")
            name=input()
            print("Please Enter Student Roll.No : ")
            roll=int(input())
            print("Please Enter Student Branch : ")
            branch=input()
            student={"Name": name,"Reg Num": roll, "Branch": branch}
            studentdata.insert_one(student)
        print("Data Inserted successfully...........")
    elif(v==2):
        print("Please enter the Student id you want to delete : ")
        id=int(input())
        todelete1 = {"Reg Num": id}
        studentdata.delete_one(todelete1)
        print("Data Deleted successfully...........")
    elif(v==3):
        print("Please enter the Student id you want to Update : ")
        id1 = int(input())
        filter = {'Reg Num': id1}
        print("Please Enter Updated Student Id : ")
        Id3= int(input())
        print("Please Enter Updated Student Name : ")
        name1=input()
        print("Please Enter Updated Student Branch : ")
        branch1=input()
        newvalues2 = {"$set": {"Reg Num": Id3}}
        newvalues = {"$set": {"Name":name1 }}
        newvalues1 = {"$set": {"Branch": branch1}}
        studentdata.update_one(filter, newvalues2)
        studentdata.update_one(filter, newvalues)
        studentdata.update_one(filter, newvalues1)
        print("Data Updated successfully...........")
    elif(v==4):
        print("Please enter the Student id you want to Search : ")
        id2 = int(input())
        tofind = {"Reg Num": id2}
        for x in tofind:
            print(studentdata.find_one(tofind))
        print("Data Found successfully...........")
    elif(v==5):
        print("Loop Terminated...........")
        loop=False
        break;
    else:
        print("!!!!!.....Please Enter a valid data.....!!!!!\n")