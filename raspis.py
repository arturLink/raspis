from tkinter import *
def descrpt(): pass
tunniplaan={}

aken=Tk()
aken.title("Расписание")
aken.geometry("1280x720")
#dni
Ep=Label(aken,text="Esmaspäev",font="Calibri 17",relief="solid").grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
Tp=Label(aken,text="Teisipäev",font="Calibri 17",relief="solid").grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
Kp=Label(aken,text="Kolmapäev",font="Calibri 17",relief="solid").grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
Np=Label(aken,text="Neljapäev",font="Calibri 17",relief="solid").grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
Rd=Label(aken,text="Reede",font="Calibri 17",relief="solid").grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)
#numUrokov
t0=Label(aken,text="0",width=5,font="Calibri 17",relief="solid").grid(row=0,column=1,sticky=N+S+W+E)
t1=Label(aken,text="1",width=5,font="Calibri 17",relief="solid").grid(row=0,column=2,sticky=N+S+W+E)
t2=Label(aken,text="2",width=5,font="Calibri 17",relief="solid").grid(row=0,column=3,sticky=N+S+W+E)
t3=Label(aken,text="3",width=5,font="Calibri 17",relief="solid").grid(row=0,column=4,sticky=N+S+W+E)
t4=Label(aken,text="4",width=5,font="Calibri 17",relief="solid").grid(row=0,column=5,sticky=N+S+W+E)
t5=Label(aken,text="5",width=5,font="Calibri 17",relief="solid").grid(row=0,column=6,sticky=N+S+W+E)
t6=Label(aken,text="6",width=5,font="Calibri 17",relief="solid").grid(row=0,column=7,sticky=N+S+W+E)
t7=Label(aken,text="7",width=5,font="Calibri 17",relief="solid").grid(row=0,column=8,sticky=N+S+W+E)
t8=Label(aken,text="8",width=5,font="Calibri 17",relief="solid").grid(row=0,column=9,sticky=N+S+W+E)
t9=Label(aken,text="9",width=5,font="Calibri 17",relief="solid").grid(row=0,column=10,sticky=N+S+W+E)
t10=Label(aken,text="10",width=5,font="Calibri 17",relief="solid").grid(row=0,column=11,sticky=N+S+W+E)
#uroki
#esmaspaev
MultE1=Button(aken,text="Multimeedia",font="Calibri 17",bg="blue").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
ProgramE2=Button(aken,text="Programeerimise alused",font="Calibri 17",bg="lightblue").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
ProgramE1=Button(aken,text="Programeerimise alused",font="Calibri 17",bg="lightblue").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
MultE2=Button(aken,text="Multimeedia",bg="blue",font="Calibri 17").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
KlHour=Button(aken,text="Rühmahataja tund",bg="lightblue",font="Calibri 17").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)
#teisipaev
IngKeel1=Button(aken,text="Inglise keel",font="Calibri 17",bg="lightgrey").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
IngKeel2=Button(aken,text="Inglise keel",font="Calibri 17",bg="pink").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
OS=Button(aken,text="Operatsioonisüsteemide alused",font="Calibri 17",bg="purple").grid(row=3,column=4,rowspan=2,columnspan=2,sticky=N+S+W+E)
KK=Button(aken,text="Kehaline kasvatus",font="Calibri 17",bg="#DB7093").grid(row=3,column=7,rowspan=2,columnspan=2,sticky=N+S+W+E)
EstKeelT1=Button(aken,text="Eesti keel",bg="#BA55D3",font="Calibri 17").grid(row=3,column=9,sticky=N+S+W+E)
EstKeelT2=Button(aken,text="Eesti keel",bg="#D8BFD8",font="Calibri 17").grid(row=4,column=9,sticky=N+S+W+E)
ajalugT=Button(aken,text="Ajalugu",bg="#F0E68C",font="Calibri 17").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)
#kolmapaev
ProgramK1=Button(aken,text="Programeerimise alused",font="Calibri 17",bg="lightblue").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
MultK2=Button(aken,text="Multimeedia",font="Calibri 17",bg="blue").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
ProgramK2=Button(aken,text="Programeerimise alused",font="Calibri 17",bg="lightblue").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
MultK1=Button(aken,text="Multimeedia",font="Calibri 17",bg="blue").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
Kunst=Button(aken,text="Kunstiained",font="Calibri 17",bg="#9932CC").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)
#neljapaev
AndBasSys=Button(aken,text="Andmebaasisüsteemide alused",font="Calibri 17",bg="#DC143C").grid(row=7,column=2,rowspan=2,columnspan=5,sticky=N+S+W+E)
ajalugN=Button(aken,text="Ajalugu",font="Calibri 17",bg="#F0E68C").grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
EstKeelN1=Button(aken,text="Eesti keel",font="Calibri 17",bg="#BA55D3").grid(row=7,column=8,sticky=N+S+W+E)
EstKeelN2=Button(aken,text="Eesti keel",font="Calibri 17",bg="#D8BFD8").grid(row=8,column=8,sticky=N+S+W+E)
#reede
KlJaKir=Button(aken,text="Keel ja kirjandus",font="Calibri 17",bg="#ADFF2F").grid(row=9,column=3,rowspan=2,columnspan=2,sticky=N+S+W+E)
Mat=Button(aken,text="Matemaatika",font="Calibri 17",bg="#DB7093").grid(row=9,column=6,rowspan=2,columnspan=2,sticky=N+S+W+E)
SuhKlient=Button(aken,text="Suhtlemine ja klienditeenindus",font="Calibri 17",bg="#7B68EE").grid(row=9,column=8,rowspan=2,columnspan=2,sticky=N+S+W+E)
ajalugN=Button(aken,text="Ajalugu",font="Calibri 17",bg="#F0E68C").grid(row=9,column=10,sticky=N+S+W+E)


aken.mainloop()