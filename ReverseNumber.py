def reverse(num):  #function:display an integer in reverse order
    while(num>=1):
        print(num%10,end="")  #print out the number that is in the rightest
        num=num//10
number=int(input("Enter an integer"))
reverse(number) #call function