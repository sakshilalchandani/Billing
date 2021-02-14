from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_colour = "#074463"
        title = Label(self.root, text="Billing software", bd=12, relief=GROOVE, bg=bg_colour, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # ==========Variables=============#
        # ==========Cosmetics=============#
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.lotion = IntVar()
        # ============groceries==============#
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.dal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # ===========coldrinks================#
        self.Pepsi = IntVar()
        self.Sprite = IntVar()
        self.Coke = IntVar()
        self.Mazza = IntVar()
        self.Fanta = IntVar()
        self.ThumbsUp = IntVar()

        # =======total product cost and tax variables========#
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ========CustomerDetailFrame======#

        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_colour)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_colour, fg="white",
                          font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cphn_lbl = Label(F1, text="Phone Number", bg=bg_colour, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                             column=3,
                                                                                                             pady=5,
                                                                                                             padx=10)

        cbill_lbl = Label(F1, text="Bill Number", bg=bg_colour, fg="white", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                  column=5,
                                                                                                                  pady=5,
                                                                                                                  padx=10)

        bill_btn = Button(F1, text="Search",command=self.find_bill, width=10, bd=7, font="Arial 12 bold").grid(row=0, column=6, padx=10,
                                                                                        pady=10)

        # ========CosmeticsFrame===============#
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_colour)
        F2.place(x=5, y=180, width=325, height=380)

        bath_lb = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(
            row=0, column=0, sticky="w")
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lb = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_colour,
                              fg="lightgreen").grid(row=1, column=0, sticky="w")
        face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5,
                               relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        face_w_lb = Label(F2, text="Face wash", font=("times new roman", 16, "bold"), bg=bg_colour,
                          fg="lightgreen").grid(row=2, column=0, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        hair_s_lb = Label(F2, text="hair shampoo", font=("times new roman", 16, "bold"), bg=bg_colour,
                          fg="lightgreen").grid(row=3, column=0, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        hair_w_lb = Label(F2, text="hair gel", font=("times new roman", 16, "bold"), bg=bg_colour,
                          fg="lightgreen").grid(row=4, column=0, sticky="w")
        hair_w_txt = Entry(F2, width=10, textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5,
                           relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        body_lb = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_colour,
                        fg="lightgreen").grid(row=5, column=0, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ========GroceriesFrame===============#
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Groceries", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_colour)
        F3.place(x=340, y=180, width=325, height=380)

        rice_lb = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(
            row=0, column=0, sticky="w")
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        food_oil_lb = Label(F3, text="Food oil", font=("times new roman", 16, "bold"), bg=bg_colour,
                            fg="lightgreen").grid(row=1, column=0, sticky="w")
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5,
                             relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        dal_lb = Label(F3, text="dal", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 sticky="w")
        dal_txt = Entry(F3, width=10, textvariable=self.dal, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        wheat_lb = Label(F3, text="wheat", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(
            row=3, column=0, sticky="w")
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        sugar_lb = Label(F3, text="sugar", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(
            row=4, column=0, sticky="w")
        sugar_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
                          relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        tea_lb = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=5,
                                                                                                                 column=0,
                                                                                                                 sticky="w")
        tea_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ========ColdrinksFrame===============#
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Coldrinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_colour)
        F4.place(x=670, y=180, width=325, height=380)

        c1_lb = Label(F4, text="Pepsi", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.Pepsi, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        c2_lb = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(
            row=1, column=0, sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.Sprite, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        c3_lb = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=2,
                                                                                                                 column=0,
                                                                                                                 sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.Coke, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        c4_lb = Label(F4, text="Mazza", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.Mazza, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        c5_lb = Label(F4, text="Fanta", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.Fanta, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        c6_lb = Label(F4, text="ThumbsUp", font=("times new roman", 16, "bold"), bg=bg_colour, fg="lightgreen").grid(
            row=5, column=0, sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.ThumbsUp, font=("times new roman", 16, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ==========billarea===========#
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ========ButtonFrame===============#
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_colour)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Cosmetic Price", bg=bg_colour, fg="lightgreen",
                       font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Groceries Price", bg=bg_colour, fg="lightgreen",
                       font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, widt=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Coldrinks Price", bg=bg_colour, fg="lightgreen",
                       font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, widt=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=1)

        t1_lbl = Label(F6, text="Cosmetic Tax", bg=bg_colour, fg="lightgreen",
                       font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        t1_txt = Entry(F6, widt=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=1)

        t2_lbl = Label(F6, text="Groceries Tax", bg=bg_colour, fg="lightgreen",
                       font=("times new roman", 15, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        t2_txt = Entry(F6, widt=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=1, column=3, padx=10, pady=1)

        t3_lbl = Label(F6, text="ColdDrink Tax", bg=bg_colour, fg="lightgreen",
                       font=("times new roman", 15, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        t3_txt = Entry(F6, widt=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                           font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white", bd=2,
                           pady=15, width=10, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data,bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                           font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command = self.Exit, bg="cadetblue", fg="white", bd=2, pady=15, width=10,
                          font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p = self.soap.get() * 40
        self.c_fc_p = self.face_cream.get() * 120
        self.c_fw_p = self.face_wash.get() * 60
        self.c_hs_p = self.spray.get() * 180
        self.c_hg_p = self.gell.get() * 140
        self.c_bl_p = self.lotion.get() * 180

        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p
        )

        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 80
        self.g_f_p = self.food_oil.get() * 180
        self.g_d_p = self.dal.get() * 60
        self.g_w_p = self.wheat.get() * 180
        self.g_s_p = self.sugar.get() * 45
        self.g_t_p = self.tea.get() * 150

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_p_d = self.Pepsi.get() * 50
        self.c_s_d = self.Sprite.get() * 50
        self.c_ola_d = self.Coke.get() * 45
        self.c_m_d = self.Mazza.get() * 40
        self.c_f_d = self.Fanta.get() * 45
        self.c_tu_d = self.ThumbsUp.get() * 50

        self.total_drinks_price = float(
            self.c_p_d +
            self.c_s_d +
            self.c_ola_d +
            self.c_m_d +
            self.c_f_d +
            self.c_tu_d
        )

        self.cold_drink_price.set("Rs. " + str(self.total_drinks_price))
        self.c_d_tax = round((self.total_drinks_price * 0.05), 2)
        self.cold_drink_tax.set("Rs. " + str(self.c_d_tax))

        self.Total_bill = float(
            self.total_cosmetic_price + self.total_grocery_price + self.total_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome webcode Retail")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END, f"\n======================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drink_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No products Purchased")

        else:
            self.welcome_bill()
            # =====cosmetics==========#
            if self.soap.get != 0:
                self.txtarea.insert(END, f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get != 0:
                self.txtarea.insert(END, f"\nFaceCream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get != 0:
                self.txtarea.insert(END, f"\nFaceWash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get != 0:
                self.txtarea.insert(END, f"\nSpray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gell.get != 0:
                self.txtarea.insert(END, f"\nGell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.lotion.get != 0:
                self.txtarea.insert(END, f"\nLotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            # =====groceriess==========#
            if self.rice.get != 0:
                self.txtarea.insert(END, f"\nRice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get != 0:
                self.txtarea.insert(END, f"\nFoodOil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.dal.get != 0:
                self.txtarea.insert(END, f"\nDal\t\t{self.dal.get()}\t\t{self.g_d_p}")
            if self.wheat.get != 0:
                self.txtarea.insert(END, f"\nWheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get != 0:
                self.txtarea.insert(END, f"\nSugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get != 0:
                self.txtarea.insert(END, f"\nTea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            # =====coldrinks==========#
            if self.Pepsi.get != 0:
                self.txtarea.insert(END, f"\nPepsi\t\t{self.Pepsi.get()}\t\t{self.c_p_d}")
            if self.Sprite.get != 0:
                self.txtarea.insert(END, f"\nSprite\t\t{self.Sprite.get()}\t\t{self.c_s_d}")
            if self.Coke.get != 0:
                self.txtarea.insert(END, f"\nFCoke\t\t{self.Coke.get()}\t\t{self.c_ola_d}")
            if self.Mazza.get != 0:
                self.txtarea.insert(END, f"\nMazza\t\t{self.Mazza.get()}\t\t{self.c_m_d}")
            if self.Fanta.get != 0:
                self.txtarea.insert(END, f"\nFanta\t\t{self.Fanta.get()}\t\t{self.c_f_d}")
            if self.ThumbsUp.get != 0:
                self.txtarea.insert(END, f"\nThumbsUp\t\t{self.ThumbsUp.get()}\t\t{self.c_tu_d}")

            self.txtarea.insert(END, f"\n--------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\ngrocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nColdrink Tax\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\nGrand Total:\t\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save bill", "do you want to save the bill?")
        if op==1:
            self.bill_data=self.txtarea.get('1.0', END)
            f1=open("bills/" + str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved", f"bill no.{self.bill_no.get()} saved successfully")
        else:
            return
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"
        if present=="no":
            messagebox.showerror("error","invalid bill no.")
    def clear_data(self):
        op = messagebox.askyesno("clear", "do you want to clear?")
        if op > 0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)
            # ============groceries==============#
            self.rice.set(0)
            self.food_oil.set(0)
            self.dal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # ===========coldrinks================#
            self.Pepsi.set(0)
            self.Sprite.set(0)
            self.Coke.set(0)
            self.Mazza.set(0)
            self.Fanta.set(0)
            self.ThumbsUp.set(0)

            # =======total product cost and tax variables========#
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit(self):
        op=messagebox.askyesno("exit","do you want to exit?")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()