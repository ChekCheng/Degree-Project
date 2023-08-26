from tkinter import *
from tkinter import PhotoImage
from tkinter import Frame
from tkinter import Label

mainWindow = Tk()

image1 = PhotoImage(file="C:\\Users\\acer\\Downloads\\FNIS(4).png")
background_label = Label(mainWindow, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


mainWindow.title("Balanced Vitamin C juicing recipe system")
mainWindow.geometry("800x600")

headingFrame1 = Frame(mainWindow,bg="#5ce1e6",bd=5)
headingFrame1.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Balanced Vitamin C juicing recipe system", bg='black', fg='white', font=('Courier',18))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

def user_guide():
    root3 = Toplevel()
    root3.title("User Guide")
    root3.resizable(False, False)
    root3.geometry("900x800")
    root3.config(bg='light blue')

    m1 = Frame(root3, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=850, height=250)
    m1.place(x=20, y=50)

    title = Label(m1, text="Function of each menu", font=("aria", 10, "bold"), fg="darkblue", bg="lightyellow")
    title.place(x=350, y=10)

    Label(m1, font=("aria", 10, "bold"), text="1.User's Guide-User can understand deeply in our system.", fg="skyblue2",
          bg="lightyellow").place(x=40, y=40)
    Label(m1, font=("aria", 10, "bold"),
          text="2.Nutrient info-User can know the vitamin c content in recommended fruit based on avergae size.",
          fg="skyblue2", bg="lightyellow").place(x=40, y=80)
    Label(m1, font=("aria", 10, "bold"),
          text="3.Calculate RDA- User can calculate thier vitamin c RDA based on their age and gender.", fg="skyblue2",
          bg="lightyellow").place(x=40, y=120)
    Label(m1, font=("aria", 10, "bold"),
          text="4.Try your recipe- User can make recipe by mixing different fruits and calculate the total vitamin c of user's juicing recipe.",
          fg="skyblue2", bg="lightyellow").place(x=40, y=160)

    m2 = Frame(root3, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=850, height=200)
    m2.place(x=20, y=320)

    title1 = Label(m2, text="Purpose of this system", font=("aria", 10, "bold"), fg="darkblue", bg="lightyellow")
    title1.place(x=350, y=10)

    Label(m2, font=("aria", 10, "bold"),
          text=" This system aims to provide a guide for a daily balanced vitamin c juicing recipe to different users ",
          fg="skyblue2", bg="lightyellow").place(x=85, y=60)
    Label(m2, font=("aria", 10, "bold"), text=" according to their calculated Recommendation Daily Allowance(RDA).  ",
          fg="skyblue2", bg="lightyellow").place(x=170, y=90)

    m3 = Frame(root3, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=850, height=200)
    m3.place(x=20, y=550)

    title2 = Label(m3, text="Why vitamin c is so important?", font=("aria", 10, "bold"), fg="darkblue",
                   bg="lightyellow")
    title2.place(x=350, y=10)

    Label(m3, font=("aria", 10, "bold"),
          text=" Vitamin C has been linked to many impressive health benefits, such as boosting antioxidant levels, ",
          fg="skyblue2", bg="lightyellow").place(x=85, y=50)
    Label(m3, font=("aria", 10, "bold"),
          text=" lowering blood pressure, protecting against gout attacks, improving iron absorption, ", fg="skyblue2",
          bg="lightyellow").place(x=135, y=75)
    Label(m3, font=("aria", 10, "bold"), text=" boosting immunity, and reducing heart disease and dementia risk.",
          fg="skyblue2", bg="lightyellow").place(x=165, y=100)

    back_button = Button(root3, text="Back to Main Menu", command=root3.destroy)
    back_button.config(bg='black', fg='white')
    back_button.place(x=10, y=20)


image2 = PhotoImage(file="C:\\Users\\acer\\Downloads\\FNIS(3).png")
def nutrient_info():
    root2 = Toplevel(mainWindow)
    root2.title("Fruit Nutrients Info")
    root2.geometry("800x600")
    root2.resizable(False, False)
    background_label2 = Label(root2, image=image2,bg='#3a7067')
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)

    headingFrame1 = Frame(root2, bg="#5ce1e6", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel = Label(headingFrame1, text="VITAMIN C CONTAIN IN YOUR\n FAVOURITE FRUITS", bg='#182e2a', fg='white',font=('Courier', 18,'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    apple = Label(root2,
        text="APPLE"
             "\n"
             "\n Size:"
             "\n Average - 4.1mg",
        fg='purple',
        bg='pink',
        width=18,
        height=8,
        font=('Times', 14))
    apple.place(relx=0.2,rely=0.3, relwidth=0.2,relheight=0.2)

    orange = Label(root2,
        text="ORANGE"
             "\n"
             "\n Size:"
             "\n Average - 30.6mg",
        fg='orange red4',
        bg='tan1',
        width=18,
        height=8,
        font=('Times', 14))
    orange.place(relx=0.4,rely=0.3, relwidth=0.2,relheight=0.2)

    kiwi = Label(root2,
        text="KIWI"
             "\n"
             "\n Size:"
             "\n Average - 69mg",
        fg='dark green',
        bg='pale green',
        width=18,
        height=8,
        font=('Times', 14))
    kiwi.place(relx=0.6,rely=0.3, relwidth=0.2,relheight=0.2)

    lemon = Label(root2,
        text="LEMON"
             "\n"
             "\n Size:"
             "\n Average - 58mg",
        fg='blue',
        bg='yellow',
        width=18,
        height=8,
        font=('Times', 14))
    lemon.place(relx=0.2,rely=0.5, relwidth=0.2,relheight=0.2)


    tomato = Label(root2,
        text="TOMATO"
             "\n"
             "\n Size:"
             "\n Average - 12.8mg",
        fg='red4',
        bg='light pink1',
        width=18,
        height=8,
        font=('Times', 14))
    tomato.place(relx=0.4,rely=0.5, relwidth=0.2,relheight=0.2)

    Grapefruit = Label(root2,
        text="GRAPEFRUIT"
             "\n"
             "\n Size:"
             "\n Average - 41.3mg",
        fg='blue4',
        bg='light sky blue2',
        width=18,
        height=8,
        font=('Times', 14))
    Grapefruit.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.2)

    papaya = Label(root2,
        text="PAPAYA"
             "\n"
             "\n Size:"
             "\n Average - 57.4mg",
        fg='saddle brown',
        bg='navajo white',
        width=18,
        height=8,
        font=('Times', 14))
    papaya.place(relx=0.4,rely=0.7, relwidth=0.2,relheight=0.2)

    back_button = Button(root2, text="Back to Main Menu", command=root2.destroy)
    back_button.config(bg='black', fg='white')
    back_button.place(x=335,y=550)

image3 = PhotoImage(file="C:\\Users\\acer\\Downloads\\Nutrient(2).png")
def calcRDA():
    root1 = Toplevel()
    root1.geometry("800x600")
    root1.configure(bg="#3a7067")
    root1.resizable(False, False)
    root1.title("Vitamin C RDA calculator")

    background_label2 = Label(root1, image=image3, bg='#3a7067')
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)


    frame = Frame(root1, padx=10, pady=10)
    frame.place(x=200, y=330)
    ageValue = StringVar()
    ageEntry = Entry(root1, textvariable=ageValue, width=30, bd=3, font=20)
    ageEntry.place(x=310, y=300)

    nameValue = StringVar()
    nameEntry = Entry(root1, textvariable=nameValue, width=30, bd=3, font=20)
    nameEntry.place(x=310, y=250)

    gender_button = IntVar()
    male = Radiobutton(frame, text="Male",bg='yellow', font=('bold', 12), variable=gender_button, value=0)
    female = Radiobutton(frame, text="Female",bg='pink' ,font=('bold', 12), variable=gender_button, value=1)
    male.grid(row=3, column=1, pady=3)
    female.grid(row=3, column=2, pady=3)
    gender_label = Label(frame, text='Enter your gender ',bg='light blue', font=('bold', 12))
    gender_label.grid(row=3, column=0, sticky=W)

    Label(root1,text="Name",bg='light blue' , font=23).place(x=210, y=250)
    Label(root1,text="Age",bg='light blue' ,font=23).place(x=210, y=300)



    def calculateRDA():
        if gender_button.get() == 0:
            if int(ageEntry.get()) <= 3:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for children 1-3 years old:15 mg/day.",font=30).place(x=70, y=490)
            elif int(ageEntry.get()) <= 8:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for children 4-8 years old:25 mg/day.",font=30).place(x=70, y=490)
            elif int(ageEntry.get()) <= 13:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for adolescents 9-13 years old:45 mg/day.",font=30).place(x=70, y=490)
            elif int(ageEntry.get()) <= 18:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for males 14-18 years old:75 mg/day.",font=30).place(x=70, y=490)
            else:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for males 19 years old and older:90 mg/day.",font=30).place(x=65, y=490)
        else:
            if int(ageEntry.get()) <= 3:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for children 1-3 years old:15 mg/day.",font=30).place(x=70, y=490)
            elif int(ageEntry.get()) <= 8:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for children 4-8 years old:25 mg/day.",font=30).place(x=70, y=490)
            elif int(ageEntry.get()) <= 13:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for adolescents 9-13 years old:45 mg/day.",font=30).place(x=70, y=490)
            elif int(ageEntry.get()) <= 18:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for females 14-18 years old:65 mg/day.",font=30).place(x=70, y=490)
            else:
                Label(root1,text=f"Hi {nameValue.get()} ^^", font=30).place(x=350, y=460)
                Label(root1,text=f"The Recommended Dietary Allowance (RDA) of vitamin C for females 19 years old and older:75 mg/day.",font=30).place(x=65, y=490)
                Label(root1,text=f"*Note* 1.🤰 Pregnancy:85 mg/day", font=30).place(x=320, y=520)
                Label(root1,text=f"*Note* 2.🍼 Lactation:120 mg/day", font=30).place(x=320, y=550)

    Button(root1,text="Calculate RDA", font=20, bg="black", fg="white", width=11, height=2, command=calculateRDA).place(x=340,y=390)
    back_button = Button(root1, text="Back to Main Menu", command=root1.destroy)
    back_button.place(x=650, y=550)

def try_recipe():
    root = Toplevel()
    root.geometry("1280x720+150+80")
    root.resizable(False, False)
    root.title("Balanced Vitamin C Juicing Recipe Calculator")

    def Reset():
        entry_apple.delete(0, END)
        entry_orange.delete(0, END)
        entry_kiwi.delete(0, END)
        entry_lemon.delete(0, END)
        entry_tomato.delete(0, END)
        entry_grapefruit.delete(0, END)
        entry_papaya.delete(0, END)

    def VitaminC():
        try:
            a = int(apple.get())
        except:
            a = 0

        try:
            o = int(orange.get())
        except:
            o = 0

        try:
            k = int(kiwi.get())
        except:
            k = 0

        try:
            l = int(lemon.get())
        except:
            l = 0

        try:
            t = int(tomato.get())
        except:
            t = 0

        try:
            g1 = int(grapefruit.get())
        except:
            g1 = 0

        try:
            p = int(papaya.get())
        except:
            p = 0

        n1 = 4.1 * a
        n2 = 30.6 * o
        n3 = 69 * k
        n4 = 58 * l
        n5 = 12.8 * t
        n6 = 41.3 * g1
        n7 = 57.4 * p

        display_Vc = Label(f2, font=('aria', 20, 'bold'), text="Total Vitamin C", width=22, fg="lightyellow",
                           bg="black")
        display_Vc.place(x=0, y=50)
        entry_Vc = Entry(f2, font=('aria', 20, 'bold'), textvariable=Total_vc, bd=6, width=14, bg="lightgreen")
        entry_Vc.place(x=80, y=100)

        totalVcvalue = n1 + n2 + n3 + n4 + n5 + n6 + n7
        string_Vc = str('%.2f' % totalVcvalue), "mg"
        Total_vc.set(string_Vc)

    Label(root, text="Vitamin C Juicing Recipe Calculator", bg="black", fg="white", font=("calibri", 33), width="300",
          height="4").pack()

    f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=370, height=400)
    f.place(x=30, y=250)

    f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=400, height=400)
    f.place(x=30, y=250)

    Label(f, text="Start Trying Different", font=("Gabriola", 19, "bold"), fg="black", bg="lightgreen").place(x=100,
                                                                                                              y=0)
    Label(f, text="Combination of juice!", font=("Gabriola", 19, "bold"), fg="black", bg="lightgreen").place(x=100,
                                                                                                             y=40)

    Label(f, font=("Lucida Calligraphy", 13, "bold"), text="Advise for balanced vitamin c intake", fg="blue4",
          bg="lightgreen").place(x=5, y=100)
    Label(f, font=("Lucida Calligraphy", 10, "bold"), text="1.Your RDA>Your Juicing Recipe Vitamin C", fg="black",
          bg="lightgreen").place(x=0, y=130)
    Label(f, font=("Lucida Calligraphy", 10, "bold"), text="Add More fruit for higher your vitamin c intake",
          fg="darkgreen", bg="lightgreen").place(x=5, y=150)
    Label(f, font=("Lucida Calligraphy", 10, "bold"), text="2.Your Recipe Vitamin C= ±5.0mg of Your RDA", fg="black",
          bg="lightgreen").place(x=0, y=180)
    Label(f, font=("Lucida Calligraphy", 10, "bold"), text="NICE! Your Juicing Recipe is well balanced", fg="darkgreen",
          bg="lightgreen").place(x=5, y=200)
    Label(f, font=("Lucida Calligraphy", 10, "bold"), text="3.Your RDA<Your Juicing Recipe Vitamin C", fg="black",
          bg="lightgreen").place(x=0, y=230)
    Label(f, font=("Lucida Calligraphy", 10, "bold"), text="Add Less fruit for lower your vitamin c intake",
          fg="darkgreen", bg="lightgreen").place(x=5, y=250)

    f2 = Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=370, height=400)
    f2.place(x=880, y=250)

    Recipe = Label(f2, text="Your Juicing Recipe", font=("calibri,20"), bg="lightyellow")
    Recipe.place(x=110, y=10)

    f1 = Frame(root, bd=5, height=400, width=450, relief=RAISED)
    f1.pack(pady=30)
    apple = StringVar()
    orange = StringVar()
    kiwi = StringVar()
    lemon = StringVar()
    tomato = StringVar()
    grapefruit = StringVar()
    papaya = StringVar()
    Total_vc = StringVar()

    display_apple = Label(f1, font=("aria", 20, "bold"), text="Apple", width=12, fg="blue4")
    display_orange = Label(f1, font=("aria", 20, "bold"), text="Orange", width=12, fg="blue4")
    display_kiwi = Label(f1, font=("aria", 20, "bold"), text="kiwi", width=12, fg="blue4")
    display_lemon = Label(f1, font=("aria", 20, "bold"), text="Lemon", width=12, fg="blue4")
    display_tomato = Label(f1, font=("aria", 20, "bold"), text="Tomato", width=12, fg="blue4")
    display_grapefruit = Label(f1, font=("aria", 20, "bold"), text="Grapefruit", width=12, fg="blue4")
    display_papaya = Label(f1, font=("aria", 20, "bold"), text="Papaya", width=12, fg="blue4")

    display_apple.grid(row=1, column=0)
    display_orange.grid(row=2, column=0)
    display_kiwi.grid(row=3, column=0)
    display_lemon.grid(row=4, column=0)
    display_tomato.grid(row=5, column=0)
    display_grapefruit.grid(row=6, column=0)
    display_papaya.grid(row=7, column=0)

    entry_apple = Entry(f1, font=("aria", 20, "bold"), textvariable=apple, bd=6, width=8, bg="lightpink")
    entry_orange = Entry(f1, font=("aria", 20, "bold"), textvariable=orange, bd=6, width=8, bg="lightpink")
    entry_kiwi = Entry(f1, font=("aria", 20, "bold"), textvariable=kiwi, bd=6, width=8, bg="lightpink")
    entry_lemon = Entry(f1, font=("aria", 20, "bold"), textvariable=lemon, bd=6, width=8, bg="lightpink")
    entry_tomato = Entry(f1, font=("aria", 20, "bold"), textvariable=tomato, bd=6, width=8, bg="lightpink")
    entry_grapefruit = Entry(f1, font=("aria", 20, "bold"), textvariable=grapefruit, bd=6, width=8, bg="lightpink")
    entry_papaya = Entry(f1, font=("aria", 20, "bold"), textvariable=papaya, bd=6, width=8, bg="lightpink")

    entry_apple.grid(row=1, column=1)
    entry_orange.grid(row=2, column=1)
    entry_kiwi.grid(row=3, column=1)
    entry_lemon.grid(row=4, column=1)
    entry_tomato.grid(row=5, column=1)
    entry_grapefruit.grid(row=6, column=1)
    entry_papaya.grid(row=7, column=1)

    b_reset = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Reset",
                     command=Reset)
    b_reset.grid(row=8, column=0)

    b_Total = Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Total",
                     command=VitaminC)

    b_Total.grid(row=8, column=1)

    back_button = Button(root, text="Back to Main Menu", command=root.destroy)
    back_button.config(bg='black', fg='white')
    back_button.place(x=635, y=650)


userGuide_frame = Frame(mainWindow, bg='#a9d696', bd=5)
userGuide_frame.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.14)
userGuideButton = Button(userGuide_frame, text="User Guide", bg='#39382e', fg='white', font=('Courier', 15,'bold'), command=user_guide)
userGuideButton.place(relx=0.0, rely=0, relwidth=1, relheight=1)

nutrientInfo_frame = Frame(mainWindow, bg='#a9d696', bd=5)
nutrientInfo_frame.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.14)
nutrientInfoButton = Button(nutrientInfo_frame, text="Nutrient Info", bg='#39382e', fg='white',font=('Courier', 15,'bold'), command=nutrient_info)
nutrientInfoButton.place(relx=0.0, rely=0, relwidth=1, relheight=1)

calcRDA_frame = Frame(mainWindow, bg='#a9d696', bd=5)
calcRDA_frame.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.14)
calcRDAButton = Button(calcRDA_frame, text="Calculate RDA(Vitamin C)", bg='#39382e', fg='white',font=('Courier', 15,'bold'), command=calcRDA)
calcRDAButton.place(relx=0.0, rely=0, relwidth=1, relheight=1)

tryRecipe_frame = Frame(mainWindow, bg='#a9d696', bd=5)
tryRecipe_frame.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.14)
tryRecipeButton = Button(tryRecipe_frame, text="Try Your Recipe", bg='#39382e', fg='white',font=('Courier', 15,'bold'), command=try_recipe)
tryRecipeButton.place(relx=0.0, rely=0, relwidth=1, relheight=1)

mainWindow.mainloop()