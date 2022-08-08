import sqlite3
import os
import time
import random




def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class User:
    def __init__(self, username = None, password =None, numWin = 0, numLose=0):
        self.username = username
        self.password = password
        self.numWin=numWin
        self.numLose=numLose
        self.winRate=None
        try:
            self.winRate= numWin / (numLose+numWin)
        except:
            print("An exception occurred")
class MY_GAME:

    def __init__(self):
        self.my_user = User()

    def login(self):
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()

        cls()
        username = input('username: ')
        password = input('password: ')


        c.execute('SELECT * FROM Userdata WHERE username = ? and password = ?', (username, password))
        data = c.fetchall()
        c.close()
        conn.close()
        if (len(data)) == 0:
            cls()
            print("worng username or password")
            time.sleep(1.5)
            cls()
            return False
        else:
            self.my_user = User(data[0][0],data[0][1],data[0][2],data[0][3])
            cls()
            print("Welcome " + data[0][0])
            time.sleep(1.5)
            cls()
            return True
    def signup(self):
        cls()
        username = input("username: ")
        password=input("password: ")
        lose = 0
        win = 0
        cls()









        cls()

        conn = sqlite3.connect('Users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Userdata WHERE username = ? ', (username,))
        data = c.fetchall()

        if (len(data)) == 0:
            print("sing up is succseeful")

            c.execute("INSERT INTO Userdata (username, password, win, lose) VALUES (?, ?, ?, ?)",
                  (username, password, win, lose))
            conn.commit()

            time.sleep(1.5)
        else:
            print("worng username")
            time.sleep(1.5)



        c.close()
        conn.close()

    def showScore(self):
        cls()

        conn = sqlite3.connect('Users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Userdata')
        data = c.fetchall()

        print("name     win    lose")

        for row in data:
            print(str(row[0])  +"   " +str(row[2])+"    "+str(row[3]))



        c.close()
        conn.close()


        inp=input("exit")

    def updateScore(self , user_winner):

        cls()


        conn = sqlite3.connect('Users.db')
        c = conn.cursor()

        if user_winner:
            self.my_user.numWin = self.my_user.numWin + 1
            c.execute('UPDATE Userdata SET win = ? WHERE username = ?', (self.my_user.numWin, self.my_user.username))

        else:
            self.my_user.numLose = self.my_user.numLose + 1
            c.execute('UPDATE Userdata SET lose = ? WHERE username = ?', (self.my_user.numLose, self.my_user.username))

        self.my_user.winRate = self.my_user.numWin / (self.my_user.numWin+self.my_user.numLose)

        conn.commit()

        conn.commit()

        c.close()
        conn.close()






# now, to clear the screen

def main_menu():
    exit = True
    while (exit):
        cls()
        print("1-login \n2-sign up \n3-table \n4-exit")

        inp = input(':')

        if inp =='1' :

            cls()
            if my_game.login():
                user_menu()

        if inp =='2':
            my_game.signup()

        if inp =='3':
            my_game.showScore()
        if inp =='4' :
            exit = False

def user_menu():

    exit = True
    while (exit):
        cls()
        print("1-play \n2-information \n3-exit")

        inp = input(':')

        if inp =='1' :

            cls()
            play_game()

        if inp =='2':
            print("Username : " +str( my_game.my_user.username))
            print("Win : " + str(my_game.my_user.numWin) )
            print("Lose : " + str(my_game.my_user.numLose) )
            print("Winrate : " + str(my_game.my_user.winRate) )

            print("enter 1 to exit")

            ii = input("::")


        if inp =='3' :
            exit = False
    print()

def play_game():
    cls()
    highscore = input("enter high score: ")


    score_user=0
    score_cmp=0
    while str(score_cmp) !=highscore and str(score_user)!=highscore:
        cls()

        print("user : " + str(score_user))
        print("computer : " + str(score_cmp))
        print("1-rock  2-paper  3-scissors")
        user_chose= input()
        cmp_chose=random.randint(1, 3)

        print("computer chose is :" + str(cmp_chose))


        if user_chose == str (cmp_chose):
            print("")
        if user_chose == '1' and str (cmp_chose)=='2':
            score_cmp +=1
        if user_chose == '1' and str (cmp_chose)=='3':
            score_user +=1
        if user_chose == '2' and str (cmp_chose)=='1':
            score_user +=1
        if user_chose == '2' and str (cmp_chose)=='3':
            score_cmp +=1
        if user_chose == '3' and str (cmp_chose)=='1':
            score_cmp +=1
        if user_chose == '3' and str (cmp_chose)=='2':
            score_user +=1

        time.sleep(2)



    if score_user>score_cmp:

        my_game.updateScore(True)
        print(" you win")
        time.sleep(2)

    else:
        my_game.updateScore(False)
        print(" you lose")
        time.sleep(2)





my_game = MY_GAME()


def main():


    main_menu()



if __name__ == "__main__":
    main()