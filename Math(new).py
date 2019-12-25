from tkinter import *
import tkinter as TK
from tkinter import ttk
import time

players = 4
teams = {}
counter = 0

ques_no = 1
root = Tk()
root.configure(background='#fdcb6e')
root.wm_title("Math Game")
root.geometry("750x500")
current = 1

score={}
ans=['C','D','A','D','B','A','C','C','D','B']

Questions = [{'content': "      What's the maximum number of common chords a circle and a \nparabola have?", 'answer': 'C', 'A':'2', 'B':'4', 'C':'6','D':'8'},
             {'content': "For how many values of 'd' does 'x\u00b2 + 2dx + d\u00b2' have a common root?", 'answer': 'D', 'A':'1', 'B':'3', 'C':'5','D':'infinite'},
             {'content': "Find the sum of coffecients in the expansion of (x\u00b3-x\u00b2 + 1)\u00b9\u00b9\u00b9 :", 'answer': 'A', 'A':'1', 'B':'0', 'C':'1729','D':'17\u00b3'},
             {'content': "What's the dictionary rank of word 'RANDOM'?", 'answer': 'D', 'A':'390', 'B':'603', 'C':'613','D':'614'},
             {'content': "What's iⁱ(iota to exponent iota) ?", 'answer': 'B', 'A':'1', 'B':'-1', 'C':'0','D':'i'},
             {'content': "What's the integral of sin(a)cos(a).da ", 'answer': 'A', 'A':'-cos(2a)/4', 'B':'sin(2a)', 'C':'cos(2a)','D':'sin\u00b2a'},
             {'content': "  what's the angle between the pair of tangents drawn from the\n directix to the corresponding parabola(in degrees) ", 'answer': 'C', 'A':'30', 'B':'60', 'C':'90','D':'0'},
             {'content': "what's the maximum value of sin(a) +cos(a) : ", 'answer': 'C', 'A':'1/2', 'B':'1', 'C':'√2','D':'2'},
             {'content': "  Inside an ellipse a random point is taken what's the maximum \number of normals that may intersect at that point", 'answer': 'D', 'A':'2', 'B':'3', 'C':'5','D':'4'},
             {'content': "what's the sum of cubes of first 10 natural numbers : ", 'answer': 'B', 'A':'4755', 'B':'3025', 'C':'1743','D':'3443'},
             ]


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def next_ques():
    global counter,ques_no
    if counter == 9:
        evaluate()
        popup('finished')
    else:
        counter += 1
        ques_no += 1
        no.config(text="Question no. " + str(ques_no))
        ques.config(text=Questions[counter]['content'])
        C1.config(text='A)' + Questions[counter]['A'])
        C2.config(text='B)' + Questions[counter]['B'])
        C3.config(text='C)' + Questions[counter]['C'])
        C4.config(text='D)' + Questions[counter]['D'])



def create_vars(i):
    global players
    players = i
    global teams, score
    for x in range(1, i+1):
        teams['t'+str(x)] = []
        score['t'+str(x)] = 0


def popup(do=''):
    global score, players
    win = TK.Toplevel()
    if do == 'finished':

        win.wm_title("Result")
        win.configure(background='#fdcb6e')
        score_str=""
        for k,v in score.items() :
            score_str += k.replace('t','team') + ': '+ str(v) + '\n'

        l = TK.Label(win, text="Hope you had a good time playing!\n Your scores are:\n " + score_str, font='Arial 15 bold',
                     bg="#ecf0f1")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Play Again..", command=combine_funcs(win.destroy, reset), width=40)
        b.grid(row=1, column=0)

        q = ttk.Button(win, text="Quit", command=root.quit, width=40)
        q.grid(row=2, column=0)

        answers = ""
        for i in range(1,11):
            answers += str(i) +' '+ ans[i-1] +'\n'

        l2 = TK.Label(win, text="Answers :\n " + answers,font='Arial 10 bold',bg="#ecf0f1")
        l2.grid(row=3, column=0)

    elif do == 'rules':
        win.wm_title("Rules")
        win.configure(background='#fdcb6e')
        l = TK.Label(win, text="Mathematics Quiz\nRules:\nThere are 10 questions in total\nAnswer of the questions is supposed to be typed in the textbox with your team name for eg.\nIf you are the first team and answer is A the type 't1A , where 't1' represents \n the first team and 'A' the correct option \nClick on 'submit' to submit the answer and move to next question\nIncase no team is able to guess the right answer , then simply clik submit and the question will be skipped\nEnjoy!!\nNumber of teams:\n", font='Arial 15 bold',
                     bg="#ecf0f1")
        l.grid(row=0, column=0)

        e =TK.Entry(win)
        e.grid(row=1,column=0)

        b = ttk.Button(win, text="Start!", command=lambda : combine_funcs(create_vars(int(e.get())),win.destroy()), width=40)
        b.grid(row=2, column=0)


def evaluate():
    for key, value in teams.items() :
        for k in range(0,10):
            if value[k] == ans[k]:
                score[key] +=1


def reset():
    global counter,ques_no,current,score,teams,players
    counter = -1
    ques_no = 0
    current = 1
    create_vars(players)
    next_ques()


def check(ans):
    global current,score,teams
    for k,v in teams.items():
        if k == ans[0:2]:
            v.append(ans[2:])

        else:
            v.append(' ')

    e1.delete(0, END)
    next_ques()


ques = Label(root, text=Questions[counter]['content'], font='Comic 15 bold', bg='#fdcb6e')
ques.place(x=350, y=100 , anchor='center')

no = Label(root, text="Question no. 1", font='Comic 15 bold', bg="#ecf0f1")
no.place(x=0, y=0)

e1 = Entry(root, width=30)
e1.place(x=250, y=300)

submit = Button(root, command=lambda: check(e1.get()), text="Submit", bg="#ecf0f1", font='Comic 10 bold')
submit.place(x=330, y=430)

C1 = Label(root, text ='A) ' + Questions[counter]['A'],  font='Comic 15 bold')
C2 = Label(root, text ='B) ' + Questions[counter]['B'],  font='Comic 15 bold')
C1.place(x=40, y=350)
C2.place(x=240, y=350)
C3 = Label(root, text ='C) ' + Questions[counter]['C'],  font='Comic 15 bold')
C4 = Label(root, text = 'D)' + Questions[counter]['D'],  font='Comic 15 bold')
C3.place(x=400, y=350)
C4.place(x=560, y=350)
popup('rules')
root.mainloop()

