from tkinter import *
from app import *
from tkinter import messagebox

BG_GRAY = "#D6CBBF"
BG_COLOR = "#97B3AE"
TEXT_COLOR = "#000001"
BORDER_COLOR = "#748f8a"
BUTTON_COLOR = "#8be0a4"
SEND_COLOR = "#a4c3ad"

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 13 bold"
FONT_BOLD_SMALL = "Helvetica 10 bold"

class Quiz():

    def setup_quiz_window(self):
        self.quiz_win = Toplevel()
        self.quiz_win.title("Quiz window")
        self.quiz_win.configure(width="800",height="600",bg=BORDER_COLOR)
        self.quiz_win.resizable(width=False, height=False)

        background_filler = Label(self.quiz_win,background=BG_GRAY)
        background_filler.place(relheight=1, relwidth=1)
        
        correct_answers = []

        q1_val1 = IntVar()
        q2_val1 = IntVar()
        q3_val1 = IntVar()
        q4_val1 = IntVar()
        q5_val1 = IntVar()

        q1_val2 = IntVar()
        q2_val2 = IntVar()
        q3_val2 = IntVar()
        q4_val2 = IntVar()
        q5_val2 = IntVar()

        q1_val3 = IntVar()
        q2_val3 = IntVar()
        q3_val3 = IntVar()
        q4_val3 = IntVar()
        q5_val3 = IntVar()

        #Q 1

        q1_label = Label(background_filler,background=BG_COLOR,fg=TEXT_COLOR,font=FONT,height=4, width=5,text="1. What does - Ich heiße Anna - mean?")
        q1_label.place(relheight=0.185, relwidth=0.395, relx=0.008,rely=0.008)
        
        q1_option1 = Checkbutton(background_filler, variable=q1_val1,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="I like Anna")
        q1_option1.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.008)

        q1_option2 = Checkbutton(background_filler, variable=q1_val2,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="I hate Anna")
        q1_option2.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.07)

        q1_option3 = Checkbutton(background_filler, variable=q1_val3,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="My name is Anna")
        q1_option3.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.135)

        #Q 2

        q2_label = Label(background_filler,background=BG_COLOR,fg=TEXT_COLOR,font=FONT,height=4, width=5, wraplength=280,text="2. How do you say Goodbye in German?")
        q2_label.place(relheight=0.185, relwidth=0.395, relx=0.008,rely=0.208)

        q2_option1 = Checkbutton(background_filler, variable=q2_val1,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Guten Abend")
        q2_option1.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.208)

        q2_option2 = Checkbutton(background_filler, variable=q2_val2,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Auf Wiedersehen")
        q2_option2.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.27)

        q2_option3 = Checkbutton(background_filler, variable=q2_val3,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Tschüss Morgen")
        q2_option3.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.335)

        #Q 3

        q3_label = Label(background_filler,background=BG_COLOR,fg=TEXT_COLOR,font=FONT,text="3. What is the German word for milk?")
        q3_label.place(relheight=0.185, relwidth=0.395, relx=0.008,rely=0.408)

        q3_option1 = Checkbutton(background_filler, variable=q3_val1,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Milch")
        q3_option1.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.408)

        q3_option2 = Checkbutton(background_filler, variable=q3_val2,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Molk")
        q3_option2.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.47)

        q3_option3 = Checkbutton(background_filler, variable=q3_val3,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Mülch")
        q3_option3.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.535)


        #Q 4

        q4_label = Label(background_filler,background=BG_COLOR,fg=TEXT_COLOR,font=FONT,text="4. What does Danke schön mean?")
        q4_label.place(relheight=0.185, relwidth=0.395, relx=0.008,rely=0.608)

        q4_option1 = Checkbutton(background_filler, variable=q4_val1,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="You're welcome")
        q4_option1.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.608)

        q4_option2 = Checkbutton(background_filler, variable=q4_val2,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Thank you very much")
        q4_option2.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.67)

        q4_option3 = Checkbutton(background_filler, variable=q4_val3,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Please")
        q4_option3.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.735)

        #Q 5

        q5_label = Label(background_filler,background=BG_COLOR,fg=TEXT_COLOR,font=FONT,text="5. How do you say I love you in\nGerman?")
        q5_label.place(relheight=0.185, relwidth=0.395, relx=0.008,rely=0.808)

        q5_option1 = Checkbutton(background_filler, variable=q5_val1,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Ich bin dich")
        q5_option1.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.808)

        q5_option2 = Checkbutton(background_filler, variable=q5_val2,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Ich mag dich")
        q5_option2.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.87)

        q5_option3 = Checkbutton(background_filler, variable=q5_val3,background=BG_COLOR,fg=TEXT_COLOR,font=FONT, text="Ich liebe dich")
        q5_option3.place(relheight=0.055, relwidth=0.29, relx=0.41,rely=0.935)

        q5_check = Button(background_filler, text="Final results", font=FONT_BOLD, width=20, bg=SEND_COLOR, command=lambda: check_answer_all())
        q5_check.place(relx=0.71, rely=0.873, relheight=0.055, relwidth=0.265)

        def check_answer(answer):
            if answer.get() == 1:
                correct_answers.append(answer)
            else: 
                pass
        
        def check_answer_all():
            check_answer(q1_val3)
            check_answer(q2_val2)
            check_answer(q3_val1)
            check_answer(q4_val2)
            check_answer(q5_val3)
            messagebox.showinfo("Yay", f"Final score is {len(correct_answers)}")


