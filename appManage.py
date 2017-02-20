from tkinter import*
lista=[[" "," "," "," "," "," "," "," "," "]]
m=0
def a():
    global lista
    global m
    o=True
    i=0
    while i<len(lista):
        if lista[i][0]==str(eafm.get()):
            print("Yπαρχει ηδη το ΑΦΜ:",str(eafm.get()))
            o=False
            break
        elif lista[i][7]==str(eari8thl.get()):
            print("Υπαρχει ηδη o αριθμος:",str(eari8thl.get()))
            o=False
            break
        i=i+1
    if o==True:
        afm=str(eafm.get())
        eponimo=str(eeponimo.get())
        onoma=str(eonoma.get())
        polh=str(epolh.get())
        odos=str(eodos.get())
        ari8mos=str(eari8mos.get())
        tk=str(etk.get())
        ari8mthl=str(eari8thl.get())
        ypol=str(eypol.get())
        x=afm
        x=Customer(afm,eponimo,onoma,polh,odos,ari8mos,tk,ari8mthl,ypol)
        x.listop()
        lista[m]=x.lista
        lista=lista+[[" "," "," "," "," "," "," "," "," "]]
        m=m+1
        print("O πελατης με ΑΦΜ:",afm,"δημιουργηθηκε")
        
    
    
    
    

def b():
    x=str(e10.get())
    global lista
    i=0
    k=False
    while i<len(lista):
        if lista[i][0]==x:
            print("AΦΜ|Επώνυμο|Όνομα|Πόλη|Οδός|Αριθμός|ΤΚ|Αριθμ.Τηλεφ|Υπόλοιπο")
            print(lista[i])
            k=True
        i=i+1
    if k==False:
        print("Δεν υπαρχει  πελατης με ΑΦΜ:",x)

def c():
    x=str(e14.get())
    global lista
    i=0
    k=False
    while i<len(lista):
        if lista[i][7]==x:
            print("Επώνυμο|Όνομα|")
            print(lista[i][1],lista[i][2])
            k=True
            
        i=i+1
    if k==False:
        print("Δεν υπαρχει πελατης με ΑΦΜ:",x)


def d():
    x=str(e18.get())
    global lista
    i=0
    k=False
    while i<len(lista):
        if lista[i][0]==x:
            k=True
            if lista[i][8]=="0":
                del lista[i]
                print("O πελατης με ΑΦΜ:",x,"διαγραφηκε")
            else:
                print("Πρεπει το υπολοιπο να ειναι 0")
        i=i+1
    if k==False:
        print("Δεν υπαρχει πελατης με ΑΦΜ:",x)

def e():
    x=str(e22.get())
    y=str(e23.get())
    global lista
    i=0
    k=False
    while i<len(lista):
        if lista[i][0]==x:
            k=True
            lista[i][8]=y
            print("To υπολοιπο του πελατη με ΑΦΜ:",x,"εγινε",y)
        i=i+1
    if k==False:
        print("Δεν υπαρχει πελατης με ΑΦΜ:",x)


class Address:
    def __init__(self,polh,odos,ari8mos,tk):
        self.polh=polh
        self.odos=odos
        self.ari8mos=ari8mos
        self.tk=tk
        
        

class Phone:
    def __init__(self,ari8mthl,dief8thl,ypol):
        self.ari8mthl=ari8mthl
        self.dief8thl=dief8thl
        self.ypol=ypol

class Customer:
    def __init__(self,afm,eponimo,onoma,polh,odos,ari8mos,tk,ari8mthl,ypol):
        self.afm=afm
        self.eponimo=eponimo
        self.onoma=onoma
        self.dief8=Address(polh,odos,ari8mos,tk)
        self.thlefsynd=Phone(ari8mthl,self.dief8,ypol)
    def listop(self):
        self.lista=[self.afm,self.eponimo,self.onoma,self.dief8.polh,
                    self.dief8.odos,self.dief8.ari8mos,
                    self.dief8.tk,self.thlefsynd.ari8mthl,
                    self.thlefsynd.ypol]




   
    

#########grafika#######
eisag=Tk()
Label(eisag,text="1)Δημιουργία νέου πελατη").grid(row=0,sticky=W)
Label(eisag,text="ΑΦΜ:").grid(row=1,sticky=W)
Label(eisag,text="Επώνυμο:").grid(row=2,sticky=W)
Label(eisag,text="Όνομα:").grid(row=3,sticky=W)
Label(eisag,text="Διεύθυνση αποστολης λογ/μου}}     Πολη:").grid(row=4,sticky=W)
Label(eisag,text="Οδός:").grid(row=4,column=2,sticky=W)
Label(eisag,text="                                                          Αριθμος:").grid(row=5,sticky=W)
Label(eisag,text="TK:").grid(row=5,column=2,sticky=W)
Label(eisag,text="Τηλεφωνική σύνδεση}}      Aριθμός τηλ/νου:").grid(row=6,sticky=W)
Label(eisag,text="Υπολοιπο λογ/μου:").grid(row=6,column=2,sticky=W)

eafm=Entry(eisag)
eeponimo=Entry(eisag)
eonoma=Entry(eisag)
epolh=Entry(eisag)
eodos=Entry(eisag)
eari8mos=Entry(eisag)
etk=Entry(eisag)
eari8thl=Entry(eisag)
eypol=Entry(eisag)

eafm.grid(row=1,column=1)
eeponimo.grid(row=2,column=1)
eonoma.grid(row=3,column=1)
epolh.grid(row=4,column=1)
eodos.grid(row=4,column=3)
eari8mos.grid(row=5,column=1)
etk.grid(row=5,column=3)
eari8thl.grid(row=6,column=1)
eypol.grid(row=6,column=3)

b1=Button(eisag,text="|Δημιουργια|",fg='red',command=a)
b1.grid(row=7,sticky=W)

Label(eisag,text="").grid(row=8,sticky=W)
Label(eisag,text="2)Αναζητηση ενος πελατη(βαση ΑΦΜ)").grid(row=9,sticky=W)
Label(eisag,text="ΑΦΜ:").grid(row=10,sticky=W)
e10=Entry(eisag)
e10.grid(row=10,column=1)
b2=Button(eisag,text="|Αναζήτηση|",fg='blue',command=b)
b2.grid(row=11,sticky=W)


Label(eisag,text="").grid(row=12,sticky=W)
Label(eisag,text="3)Αναζητηση μιας τηλ/κης συνδεσης").grid(row=13,sticky=W)
Label(eisag,text="(βαση αριθμου τηλ/νου)    Aριθμος:").grid(row=14,sticky=W)
e14=Entry(eisag)
e14.grid(row=14,column=1)
b3=Button(eisag,text="|Αναζητηση|",fg="brown",command=c)
b3.grid(row=15,sticky=W)



Label(eisag,text="").grid(row=16,sticky=W)
Label(eisag,text="4)Kαταργηση-Διαγραφη πελατη(βαση ΑΦΜ)").grid(row=17,sticky=W)
Label(eisag,text="(μονο οταν υπολοιπο=0)     ΑΦΜ:").grid(row=18,sticky=W)
e18=Entry(eisag)
e18.grid(row=18,column=1)
b4=Button(eisag,text="|Καταργηση|",fg="green",command=d)
b4.grid(row=19,sticky=W)


Label(eisag,text="").grid(row=20,sticky=W)
Label(eisag,text="5)Εισαγωγή νέου πολοίπου λογ/μου").grid(row=21,sticky=W)
Label(eisag,text="(βαση ΑΦΜ)    ΑΦΜ:").grid(row=22,sticky=W)
e22=Entry(eisag)
e22.grid(row=22,column=1)
Label(eisag,text="Nέο υπόλοιπο:").grid(row=22,column=2,sticky=W)
e23=Entry(eisag)
e23.grid(row=22,column=3)
b5=Button(eisag,text="|Εισαγωγή|",fg="purple",command=e)
b5.grid(row=23,sticky=W)
b6=Button(eisag,text="|Έξοδος|",fg="red",command=eisag.destroy)
b6.grid(row=24,column=1)
      


eisag.mainloop()
