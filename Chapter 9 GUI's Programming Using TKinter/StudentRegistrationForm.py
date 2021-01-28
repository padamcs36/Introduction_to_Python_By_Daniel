from tkinter import *
class StudentRegis:
    def __init__(self):
        root = Tk()
        root.geometry("300x300")
        root.title('Student Registration')

        Label(root, text='Student Registration', font='times 15 italic bold').grid(row=0, column=2)
        Label(root, text='Full Name', font='lucida 10 italic').grid(row=1,column=1, sticky=W, padx=10, pady=5)
        Label(root, text='Father Name', font='lucida 10 italic').grid(row=2,column=1, sticky=W, padx=10, pady=5)
        Label(root, text='Gender', font='lucida 10 italic').grid(row=3, column=1, sticky=W, padx=10, pady=10)
        Label(root, text='Roll Num:', font='lucida 10 italic').grid(row=4,column=1, sticky=W, padx=10, pady=5)
        Label(root, text='Deptt:', font='lucida 10 italic').grid(row=5,column=1, sticky=W, padx=10, pady=5)
        Label(root, text='Phone No:', font='lucida 10 italic').grid(row=6,column=1, sticky=W, padx=10, pady=5)
        Label(root, text='Address', font='lucida 10 italic').grid(row=7, column=1, sticky=W, padx=10, pady=5)

        self.name = StringVar()
        self.fname = StringVar()
        self.rollNo = StringVar()
        self.Deptt = StringVar()
        self.phoneN = StringVar()
        self.address = StringVar()
        self.rdgender = IntVar()

        maleRd = Radiobutton(root, text='Male', variable=self.rdgender, value=1, command=self.processRadioButton)
        femaleRd = Radiobutton(root, text='Female', variable=self.rdgender, value=2, command=self.processRadioButton)
        maleRd.grid(row=3, column=2,sticky=W,padx=20)
        femaleRd.grid(row=3, column=2,sticky=E)

        Entry(root, textvariable = self.name).grid(row=1, column=2)
        Entry(root, textvariable = self.fname).grid(row=2, column=2)
        Entry(root, textvariable = self.rollNo).grid(row=4, column=2)
        Entry(root, textvariable = self.Deptt).grid(row=5, column=2)
        Entry(root, textvariable = self.phoneN).grid(row=6, column=2)
        Entry(root, textvariable = self.address).grid(row=7, column=2)

        Button(root, text='Submit', font='lucida 10 bold', command=self.submit).grid(row=8, column=1,sticky=E)
        Button(root, text='Reset', font='lucida 10 bold', command=self.reset).grid(row=8, column=2,sticky=W)




        mainloop()
    def processRadioButton(self):
        if self.rdgender.get() == 1:
            return 'Male'
        elif self.rdgender.get() == 2:
            return 'Female'
    def submit(self):
        print(format(self.name.get(),'<15s'), format(self.fname.get(),'<15s'),format(self.processRadioButton(),'<10s'),
              format(self.rollNo.get(),'<10s'),format(self.Deptt.get(), '<15s'),format(self.phoneN.get(), '<15s'),
              format(self.address.get(), '<10s'))

        with open("StudentRegist.txt", mode="a") as f:
            f.write(f"{self.name.get(), self.fname.get(), self.processRadioButton(),self.rollNo.get(), self.Deptt.get(), self.phoneN.get(), self.address.get()}\n")

    def reset(self):
        self.name.set('')
        self.fname.set('')
        self.rdgender.set('')
        self.rollNo.set('')
        self.phoneN.set('')
        self.address.set('')
        self.Deptt.set('')

print(format('Name', '<15s'), format('Father Name', '<15s'),format('Gender', '<10s') ,format('Roll No:','<10s'),
              format('Department', '<15s'), format('Phone No', '<15s'),format('Address', '<10s'))
StudentRegis()

