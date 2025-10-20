stu_details={"Akki":90,"Jags":100,"Ashish":95,"Sumit":99,"Vinod":100,"Shelly":98,"Ravi":97}
search=input("Enter the name of the students whose marks you want to see")
if search in stu_details:
    print("The student name is ",search,"and marks scored:",stu_details[search])
else:
    print("The student name",search,"does not exist in our records")
