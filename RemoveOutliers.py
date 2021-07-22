remove_number=int(input("Enter the number of smallest and largest values to remove:"))
list1=[] #construct a list
number_input_check=1 #if number_input_check=1,code keep run. if number_input_check=0,code stop
while(number_input_check):
    number_input=input("Enter a value (q or Q to quit):")
    if(number_input=="q" or number_input=="Q"): #if user enter Q or q,number_input_check=0(code stop)
        number_input_check=0
    else:
        list1.append(int(number_input)) #put number to list1
print("The original data:",list1)
list1.sort()   #put list1 to rearrange
def remove_outliers(list,number):  #the function can remove value
    list_out=list[0:number]  #get list that user want to remove
    list_out.extend(list[len(list)-number:len(list)]) #get list that user want to remove
    return list_out
list_outliers=remove_outliers(list1,remove_number)  #call function
del list1[len(list1)-remove_number:len(list1)]  #remove it
del list1[0:remove_number]  #remove it
print("The data with the outliers removed",list1)
print("The outliers:",list_outliers)




