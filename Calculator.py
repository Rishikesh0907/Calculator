from pathlib import Path
from tkinter import Button, Entry, Frame, GROOVE, Label, PhotoImage, StringVar, SUNKEN, Tk


class Calculator:
    def __init__(self):
        self.Data = ""
        self.win = Tk()
        self.win.title("Calculator")
        self.win.config(bg="skyblue")
        self.win.geometry("379x486+480+100")
        self.win.resizable(False, False)

        icon = PhotoImage(file=str(Path(__file__).with_name("logo.png")))
        self.win.iconphoto(False, icon)
        self.icon = icon

        brand_name = Label(self.win, text="TKINTER", font=("Arial Rounded MT Bold", 15),
                           fg="Black", bg="skyblue")
        brand_name.place(x=32, y=20)

        calculator_name = Label(self.win, text="Calculator", font=("Arial Rounded MT Bold", 10),
                                fg="Black", bg="skyblue")
        calculator_name.place(x=42, y=45)

        calculatorX_name = Label(self.win, text="GUI 380x490", font=("Arial", 8, "bold"),
                                 fg="black", bg="skyblue")
        calculatorX_name.place(x=276, y=70)

        brandTitle_name = Label(self.win, text="----- ", font=("Arial Rounded MT Bold", 8, "bold"),
                                fg="Black", bg="skyblue")
        brandTitle_name.place(x=170, y=158)

        self.var = StringVar()
        calculation_box = Entry(
            self.win, font=("Arial Rounded MT Bold", 25), relief=SUNKEN, bd=5,
            bg="#EEEEEE", fg="black", textvariable=self.var, cursor="none"
        )
        calculation_box.place(x=21, y=100, width=337, height=55)

        button_frame = Frame(self.win, relief=GROOVE, bd=2, bg="#FFFFFF")
        button_frame.place(x=22, y=180, width=335.49, height=266)

        ac_btn = Button(
            button_frame, text="AC", font=("Arial", 17, "bold"), bg="skyblue", fg="red",
            relief=GROOVE, bd=4, command=self.ACButton, cursor="hand2"
        )
        ac_btn.place(x=2, y=2, height=50, width=80)

        module_btn = Button(
            button_frame, text="%", bd=4, fg="red", bg="skyblue",
            font=("Arial Rounded MT Bold", 18, "bold"), relief=GROOVE,
            command=lambda: self.get_data("%"), cursor="hand2"
        )
        module_btn.place(x=84, y=2, height=50, width=80)

        back_btn = Button(
            button_frame, text="X", font=("Arial", 16, "bold"), bg="skyblue",
            relief=GROOVE, bd=4, fg="red", command=self.BackSpace, cursor="hand2"
        )
        back_btn.place(x=167, y=2, height=50, width=80)

        divid_btn = Button(
            button_frame, text="/", font=("Arial", 17, "bold"), bg="skyblue",
            relief=GROOVE, bd=4, fg="red", command=lambda: self.get_data("/"),
            cursor="hand2"
        )
        divid_btn.place(x=250, y=2, height=50, width=80)

        seven_btn = Button(
            button_frame, text="7", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("7"),
            cursor="hand2"
        )
        seven_btn.place(x=2, y=54, height=50, width=80)

        eight_btn = Button(
            button_frame, text="8", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("8"),
            cursor="hand2"
        )
        eight_btn.place(x=84, y=54, height=50, width=80)

        nine_btn = Button(
            button_frame, text="9", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("9"),
            cursor="hand2"
        )
        nine_btn.place(x=167, y=54, height=50, width=80)

        multiply_btn = Button(
            button_frame, text="*", font=("Arial", 22, "bold"), bg="skyblue",
            fg="red", relief=GROOVE, bd=4, command=lambda: self.get_data("*"),
            cursor="hand2"
        )
        multiply_btn.place(x=250, y=54, height=50, width=80)

        four_btn = Button(
            button_frame, text="4", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("4"),
            cursor="hand2"
        )
        four_btn.place(x=2, y=106, height=50, width=80)

        five_btn = Button(
            button_frame, text="5", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("5"),
            cursor="hand2"
        )
        five_btn.place(x=84, y=106, height=50, width=80)

        six_btn = Button(
            button_frame, text="6", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("6"),
            cursor="hand2"
        )
        six_btn.place(x=167, y=106, height=50, width=80)

        substraction_btn = Button(
            button_frame, text="-", font=("Arial", 24, "bold"), bg="skyblue",
            fg="red", relief=GROOVE, bd=4, cursor="hand2",
            command=lambda: self.get_data("-")
        )
        substraction_btn.place(x=250, y=106, height=50, width=80)

        one_btn = Button(
            button_frame, text="1", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("1"),
            cursor="hand2"
        )
        one_btn.place(x=2, y=158, height=50, width=80)

        two_btn = Button(
            button_frame, text="2", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("2"),
            cursor="hand2"
        )
        two_btn.place(x=84, y=158, height=50, width=80)

        three_btn = Button(
            button_frame, text="3", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("3"),
            cursor="hand2"
        )
        three_btn.place(x=167, y=158, height=50, width=80)

        plus_btn = Button(
            button_frame, text="+", font=("Arial", 18, "bold"), bg="skyblue",
            fg="red", relief=GROOVE, bd=4, command=lambda: self.get_data("+"),
            cursor="hand2"
        )
        plus_btn.place(x=250, y=158, height=50, width=80)

        double_zero_btn = Button(
            button_frame, text="00", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("00"),
            cursor="hand2"
        )
        double_zero_btn.place(x=2, y=210, height=50, width=80)

        zero_btn = Button(
            button_frame, text="0", font=("Arial", 18, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("0"),
            cursor="hand2"
        )
        zero_btn.place(x=84, y=210, height=50, width=80)

        dot_btn = Button(
            button_frame, text=".", font=("Arial", 25, "bold"), bg="skyblue",
            fg="black", relief=GROOVE, bd=4, command=lambda: self.get_data("."),
            cursor="hand2"
        )
        dot_btn.place(x=167, y=210, height=50, width=80)

        equal_btn = Button(
            button_frame, text="=", font=("Arial", 18, "bold"), bg="#FB7C14",
            fg="black", relief=GROOVE, bd=4, command=self.EqualButton,
            cursor="hand2"
        )
        equal_btn.place(x=250, y=210, height=50, width=80)

    def get_data(self, value):
        self.Data += str(value)
        self.var.set(self.Data)

    def EqualButton(self):
        try:
            total_data = str(eval(self.Data))
            self.var.set(total_data)
            self.Data = ""
        except Exception:
            self.var.set("Syntex Error:")

    def ACButton(self):
        self.Data = ""
        self.var.set("")

    def BackSpace(self):
        self.Data = self.Data[:-1]
        self.var.set(self.Data)

    def run(self):
        self.win.mainloop()


if __name__ == "__main__":
    Calculator().run()
