import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['s3']

studentdetails=db.students

student1={"regd":"111","name":"Aman"}
student2=[{"regd":"222","name":"ammm"},
          {"regd":"333","name":"eeee"}]
studentdetails.insert_one(student1)
studentdetails.insert_many(student2)

a={"name":"Aman"}
for x in studentdetails.find(a):
    print(x)

    #delete single documents
    b= {"reg":"222"}
    studentdetails.delete(b)
    d={"name":"eeee"}
    studentdetails.delete(d)

    #update documents


