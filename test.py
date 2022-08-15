mainList = [5,4,5,2,1,3,5,6,7,8,5,4,3,2,3,4,5,9] #18 numbers
tempList = []

print("Before Algorithm")
print(f"mainList {mainList}")    
print(f"tempList {tempList}\n")

mainLength = int(len(mainList))
print(f"Lengh of mainList: {len(mainList)}")
j=int(mainLength/2)
print(f"Half length mainList: {j}")

#0-17
#index 9 to index 18
for i in range(int(mainLength/2), mainLength):
    tempList.append(mainList[i])
    #print(i, end= " ")
    #print(j, end= " ")


for j in range(int(mainLength/2), mainLength):
    mainList.pop()

print("\nAfter Algorithm")
print(f"mainList {mainList}")    
print(f"tempList {tempList}\n")








