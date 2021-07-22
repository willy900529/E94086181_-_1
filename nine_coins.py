class Nine_Coins: #construct a class
    list_original = []  #construct a list to save the result of coin
    decimal_number=0 #construct a number to save its state,its range is from 0 to 511
    def __init__(self,number):  #initialize
        self.number=number
    def toss(self):  #toss function
        from random import randint
        for i in range(0,self.number):
            self.list_original.append(randint(0,1)) #choose 0 or 1 randomly
        for i in range(0,9):
            self.decimal_number +=(int(self.list_original[i]))*(2**(8-i)) #convert state
    def __repr__(self):
        self.list_repr=self.list_original
        for i in range(0,9):
            if self.list_repr[i]==1:  #change 1 to T
                self.list_repr[i]="T"
            elif self.list_repr[i]==0:  #change 0 to H
                self.list_repr[i]="H"
        string_repr='%s'*len(self.list_repr)%tuple(self.list_repr) #convert list to string
        return f"Nine_coin:{string_repr}"  #it can help us to print out
    def __str__(self):
        for i in range(0,9):
            if self.list_repr[i]=="T":  #change T to 1
                self.list_repr[i]="1"
            elif self.list_repr[i]=="H":  #change H to 0
                self.list_repr[i]="0"
        string_str='%s'*len(self.list_original)%tuple(self.list_original) #convert list to string
        del self.list_original[:]   #delete this coin,for let another coin in
        return f"binary:{string_str} and decimal:{self.decimal_number}" #it can help us to print out

