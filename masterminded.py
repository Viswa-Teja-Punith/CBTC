import maskpass


class mastermind():
    player1=""
    player2=""
    count1=0
    count2=0
    count=0
    count0=0
    countin1=0
    countin2=0
    name=""
    player1name=input("enter your name player1:")
    player2name=input("enter your name player2:")
    def controls(self):
        #self.player1name=input("enter your name player1:")
        #self.player2name=input("enter your name player2:")
        #self.countin1=0
        #self.countin2=0

        print("choose who wants to start the program by entering name below")
        self.name=input("enter your name to start the game:")
        
        if self.countin2 & self.countin1==1:
             return obj.player1output()
        
        
             
        
                  
            
        elif self.name==self.player1name:
            self.countin1=self.countin1+1
            #if self.countin1 >1:
             #print("start your game by typing your name below",self.player2name)
             #return obj.controls()
            if self.countin1==1:
                self.m=maskpass.askpass(prompt="enter your number player1:")
            #m=self.player1
                self.player1=self.m
            #print(type(self.player1))
                return obj.correctinput()
            else:
                 print(' your turn is over',self.player1name)
                 self.countin1=self.countin1-1
                 print("start your game by typing your name below",self.player2name)
                 return obj.controls()
        elif self.name==self.player2name:
            self.countin2=self.countin2+1
            #if self.countin2>1:
             #self.countin2=self.countin2-1
             #print("start your game by typing your name below",self.player1name)
             #return obj.controls()
            if self.countin2==1:
                self.m=maskpass.askpass(prompt="enter your number player2:")
                #m=self.player1
                self.player2=self.m
                #print(type(self.player1))
                return obj.correctinput()
            else:
                print("your turn is over",self.player2name)
                self.countin2=self.countin2-1
                print("start your game by typing your name below",self.player1name)
                return obj.controls()
                #return obj.controls()
             
    def correctinput(self):
        if self.player1name==self.name:
            b=len(self.player1)
            self.value="please enter a value having "
            self.value=self.value+str(b)+" digits player2:"
            self.player2=maskpass.askpass(self.value)
            
            if len(self.player1)==len(self.player2):
                print(self.player2)
                return obj.func()
            else:
                print("playeer2 entered lesser number of digits than player1 ")
                return obj.correctinput()
        
        elif self.player2name==self.name:
            b=len(self.player2)
            self.value="please enter a value having "
            self.value=self.value+str(b)+" digits  player1:"
            self.player1=maskpass.askpass(self.value)
            
            if len(self.player1)==len(self.player2):
                print(self.player1)
                return obj.func1()
            else:
                print("playeer1 entered lesser number of digits than player1 ")
                return obj.correctinput()
       
    def func(self):
        
        self.countvalue=0
        #self.count0=0
        #print(self.value)
        
        
        if (self.player1)!=(self.player2):
                self.count0=self.count0+1
                #print(self.count2)
                for i in range (len(self.player1)):
                    
                    if self.player1[i]==self.player2[i]:
                            self.countvalue=self.countvalue+1
                            self.x=10**(len(self.player1)-(i+1))
                            print("the number that you enter in ",self.x,"s place is correct") 

                    
                    else:
                            continue
                #print(self.countvalue)
                if self.countvalue>=0:
                        return   obj.correctinput()  
        #elif self.player1 or self.player2 =="":
             #return obj.controls()
        else:
            self.count2= self.count0
            print(self.count2)
            print('player2 exactly guessed the value in ',self.count2,"attempts")
            if self.countin2 & self.countin1==1:
             return obj.player1output()
            else:
             return obj.controls()
                
    def func1(self):
        self.countvalue=0
        #self.count0=0
        #print(self.value)
        
        if (self.player1)!=(self.player2):
                self.count=self.count+1
                #print(self.count2)
                for i in range (len(self.player2)):
                    
                    if self.player1[i]==self.player2[i]:
                            self.countvalue=self.countvalue+1
                            self.x=10**(len(self.player2)-(i+1))
                            print("the number that you enter in ",self.x,"s place is correct") 

                    
                    else:
                            continue
                #print(self.countvalue)
                if self.countvalue>=0:
                        return   obj.correctinput()  
        else:
            self.count1= self.count
            print(self.count1)
            print('player1  exactly guessed the value in ',self.count1,"attempts")
            if self.countin2 & self.countin1==1:
             return obj.player1output()
            else:
                return obj.controls()
                 

    
     
    def player1output(self):
        if self.count1==0:
             return obj.func1()
        elif self.count2==0:
             return obj.func()
        elif self.count1>self.count2:
             print("===========0===========")
             print("winner is player2")
             print("player2 exactly guessed the value in ",self.count2," attempts")
             print("player2 won by ",self.count1-self.count2,"attempts")
        elif self.count1<self.count2:
             print("===========0===========")
             print("winner is player1")
             print("player1 exactly guessed the value in ",self.count1," attempts")
             print("player1 won by ",self.count2-self.count1,"attempts")
        else:
             print("both the players guessed the number in same attenmpts",self.count1,"-",self.count2)
obj=mastermind()
obj.controls()