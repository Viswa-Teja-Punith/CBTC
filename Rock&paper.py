import maskpass

class rps():
    print("lets start the game ")
    print("ROCK\nPAPER\nSCISSOR\n")
    choice=["rock","roc","ro","r","rk","paper","pape","pap","pa","p","pr","scissor","scisso","sciss","scis","sci","sc","s","sr"]
    player1=maskpass.askpass(prompt="player1 enter your choice from above:")

    def fun1(self):
    
    
        if self.player1.lower()in self.choice:
            if self.player1[0].lower()=="r":
                    self.player1="Rock"
                    #return fun2()
            elif self.player1[0].lower()=="s":
                        self.player1="Scissor"
                        #return fun2()
            elif self.player1[0].lower()=="p":
                    self.player1="Paper"
                    #return fun2()
        else:
            print("Invalid choice by player1")
            self.player1=maskpass.askpass(prompt="player1 enter your choice from above:")
            return obj.fun1()

        print(self.player1)

    player2=maskpass.askpass(prompt="player2 enter your choice from above:")
    def fun2(self):
        
        if self.player2.lower() in self.choice:
            if self.player2[0].lower()=="r":
                self.player2="Rock"
                #return fun1()
            elif self.player2[0].lower()=="s":
                    self.player2="Scissor"
                    #return fun1()
            elif self.player2[0].lower()=="p":
                self.player2="Paper"
                #return fun1()
        else:
            print("Invalid choice by the player2")
            self.player2=maskpass.askpass(prompt="player2 enter your choice from above:")
            return(obj.fun2())
        print(self.player2)
    def output(self):
          
         
          if ((self.player1=="Rock") &(self.player2=="Paper")) or ((self.player2=="Rock") &(self.player1=="Paper")):
                if self.player1=="Paper":
                    print("Paper covers rock! ",self.player1,"wins the match")
                elif  self.player2=="Paper":
                    print("Paper covers rock! ",self.player2,"wins the match")
          elif ((self.player1=="Scissor") &(self.player2=="Paper")) or ((self.player2=="Scissor") &(self.player1=="Paper")):
                if self.player1=="Scissor":
                    print("Scissor cuts paper ",self.player1,"wins the match")
                elif  self.player2=="Scissor":
                    print("Scissor cuts paper ",self.player2,"wins the match")
          elif ((self.player1=="Rock") &(self.player2=="Scissor")) or ((self.player2=="Rock") &(self.player1=="Scissor")):
                if self.player1=="Rock":
                    print("Rock smashes scissors! ",self.player1,"wins the match")
                elif  self.player2=="Rock":
                    print("Rock smashes scissors! ",self.player2,"wins the match")
          elif self.player1==self.player2:
               print("Both opted the same ,so its draw")
          #return obj.recurce()
    #def recurce(self):
         #self.player1=maskpass.askpass(prompt="player1 enter your choice from above:")
         #self.player2=maskpass.askpass(prompt="player2 enter your choice from above:")
         #if self.player1 !="":
              #return obj.fun1()
        #elif self.player2!="":
              #return obj.fun2()
         #else:

             #pass


obj=rps()
obj.fun1()
obj.fun2()
obj.output()