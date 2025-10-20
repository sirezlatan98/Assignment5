data=[1,2,3,4,5,6,7,8,9,10]
new_data=[]
for i in range(5):
    new_data.append(data[i])
print("The first five extracted elements are:",new_data)
new_data.reverse()
print("The reverse extracted list elements are:",new_data)