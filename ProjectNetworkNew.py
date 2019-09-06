import numpy as np
import array
from copy import copy, deepcopy
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.gamma = []

    def createWidgets(self):
        self.t1 = Text(self, width=20, height=10, wrap=WORD)
        self.b1 = Button(self, text='Matrix', command=self.matrixInput)
        self.b1.grid(row=0, column=0, sticky=E)
        self.t1.grid(row=0, column=1)

        self.t2 = Text(self, width=24, height=1, wrap=WORD)
        self.b2 = Button(self, text='Search Tr', command=self.searchTr)
        self.b2.grid(row=1, column=0, sticky=E)
        self.t2.grid(row=1, column=1)

        self.t3 = Text(self, width=24, height=1, wrap=WORD)
        self.b3 = Button(self, text='Search Tp', command=self.searchTp)
        self.b3.grid(row=2, column=0, sticky=E)
        self.t3.grid(row=2, column=1)

        self.t4 = Text(self, width=24, height=1, wrap=WORD)
        self.b4 = Button(self, text='Search reserves and critical way', command=self.searchRezAndCritway)
        self.b4.grid(row=3, column=0, sticky=E)
        self.t4.grid(row=3, column=1)

        self.t5 = Text(self, width=24, height=20, wrap=WORD)
        self.t5.grid(row=4, column=1)

    def matrixInput(self):
        A = []
        with open('matrix.txt', encoding='ascii') as fin:
            for line in fin:
                A.append(list(line.rstrip('\n')))
        for i in range(len(A)):  # преобразование элементов списков в int
            for j in range(len(A[i])):
                A[j][i] = int(A[j][i])
        self.t1.delete(0.0, END)
        self.t1.insert(0.0, A)

#поиск t ранних. записываются в массив
    def searchTr (self):

        A = []
        with open('matrix.txt', encoding='ascii') as fin:
            for line in fin:
                A.append(list(line.rstrip('\n')))
        for i in range(len(A)):  # преобразование элементов списков в int
            for j in range(len(A[i])):
                A[j][i] = int(A[j][i])

        global tr
        tr = []
        for i in range (len(A)):
            tr.append(0)
        for i in range(len(A)):
            currentcol = []
            for j in range(len(A)):
                currentcol.append(A[j][i])
            global maxtr
            maxtr = 0
            for j in range(len(A)):
                if A[j][i] > 0:
                    tr[i]=tr[j]+A[j][i]
                    if tr[i] > maxtr:
                        maxtr = tr[i]
            tr[i]= maxtr
        self.t2.delete(0.0, END)
        self.t2.insert(0.0, tr)
      #print (tr)
     #print()

    def searchTp (self):

        A = []
        with open('matrix.txt', encoding='ascii') as fin:
            for line in fin:
                A.append(list(line.rstrip('\n')))
        for i in range(len(A)):  # преобразование элементов списков в int
            for j in range(len(A[i])):
                A[j][i] = int(A[j][i])

        global tp
        tp = [] #считаем t поздние
        for i in range (len(A)):
            tp.append(0)
        i = len(A)-1
        mintp = maxtr
        tp[i] = mintp

        for i in range((len(A)-1),0,-1):
            currentrow = []
            for j in range (len(A)):
                currentrow.append(A[i][j])
            mintp = maxtr
            for j in range(len(A)):
                if A[i][j] > 0:
                    tp[i]=tp[j]-A[i][j]
                    if tp[i]<mintp:
                        mintp=tp[i]
                tp[i]=mintp
        self.t3.delete(0.0, END)
        self.t3.insert(0.0, tp)

    def searchRezAndCritway(self):

        A = []
        with open('matrix.txt', encoding='ascii') as fin:
            for line in fin:
                A.append(list(line.rstrip('\n')))
        for i in range(len(A)):  # преобразование элементов списков в int
            for j in range(len(A[i])):
                A[j][i] = int(A[j][i])

        rc = 0
        rn = 0
        critway = []
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j] > 0:
                    rc = 0
                    rn = 0
                    rc=tr[j]-tr[i]-A[i][j]
                    rn = tp[j] - tr[i] - A[i][j]
                    if rc==0 and rn==0:
                        critway.append(i+1)
                        critway.append(j+1)
                    reserves = "rc("+str(i+1)+","+str(j+1)+")="+str(rc)+" rn("+str(i+1)+","+str(j+1)+")="+str(rn)+"\n"
                    self.t5.insert(0.0, reserves)
        critway = list(set(critway))
        critway.sort()
        self.t4.delete(0.0, END)
        self.t4.insert(0.0, critway)

root = Tk()
root.title('Network')
root.geometry('500x600')
app = Application(root)

root.mainloop()