from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from ai import *
from back import *
from quiz import *
from info import *
import time
from pathlib import Path

BG_GRAY = "#D6CBBF"
BG_COLOR = "#97B3AE"
TEXT_COLOR = "#000001"
BORDER_COLOR = "#748f8a"
BUTTON_COLOR = "#8be0a4"
SEND_COLOR = "#a4c3ad"

USER_MESSAGE = "#010979"
TEACHER_MESSAGE = "#241104"

NOTES_FILE_NAME = "language_learning_notes.txt"
NOTES_FILE_PATH = Path(NOTES_FILE_NAME)

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 13 bold"
FONT_BOLD_SMALL = "Helvetica 10 bold"

previous_questions_and_answers = [] # Used by ai to store its previous questions and answers
previous_suggestions = [] # Used by ai to store its previous suggestions

SUGGESTION_PROMPT = "Reply only with the question you are suggesting. Keep the questions less than 10 words but understandable by you. Create 1 suggestion for me the user to ask you to teach me learn german. " \
"I am a novice and want to learn german. Keep each question different from ones you have already made. Vary the topics your asking. You should reply in english."

class LanguageApplication(Tk):

    def __init__(self):
        super().__init__()
        self._setup_main_window()

    def run(self):
        self.mainloop()

    def _setup_main_window(self):
        self.title("Language Teacher")
        self.configure(width="1280",height="720",bg=BORDER_COLOR)

        # Creates the header label area for placing labels and buttons
        self.header = Label(self, bg=BG_GRAY, fg=TEXT_COLOR, font=FONT_BOLD_SMALL, padx=2, pady=2)
        self.header.place(relheight=0.195, relwidth=1)

        #header
        title_label = Label(self.header, bg=SEND_COLOR, fg=TEXT_COLOR, font=FONT_BOLD_SMALL,borderwidth=2.8,relief=RAISED, padx=10, text="Hallo! I am your personal language teacher, please ask me questions to help you pass your test. " \
        "You can also click some of the prompts provided.")
        title_label.place(relwidth=0.758, relheight=0.25, relx=-0.001,rely=-0.005)
        
        # Test button on the header
        test_button = Button(self.header, text="Test", font=FONT_BOLD, bg=SEND_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=15, height=1,command=lambda:quiz.setup_quiz_window())
        test_button.place(relwidth=0.1, relheight=0.24, relx=0.780)

        # Info button on the header
        info_button = Button(self.header, text="Info", font=FONT_BOLD, bg=SEND_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=15, height=1,command=lambda:info.setup_info_window())
        info_button.place(relwidth=0.1, relheight=0.24, relx=0.895)

        # Middle section Label to hold Text widget
        self.middle = Label(self, bg=BORDER_COLOR, fg=TEXT_COLOR, font=FONT, padx=2, pady=2)
        self.middle.place(relheight=0.75, relwidth=1, rely=0.051)

        # Text widget
        self.text_widget = Text(self.middle, bg=BG_COLOR, fg=TEXT_COLOR, wrap=WORD, font=FONT, padx=20, pady=10)
        self.text_widget.place(relheight=1, relwidth=0.695, rely=0.007)
        self.text_widget.insert(END, "In here you can see the questions asked as well as the assistant replies\n\n")
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Configures tags for the text widget to change the colours depending on who is sending the message
        self.text_widget.tag_config('user_message', foreground=USER_MESSAGE)
        self.text_widget.tag_config('teacher_message', foreground=TEACHER_MESSAGE)

        #scroll bar
        scrollbar = Scrollbar(self.text_widget, orient='vertical')
        scrollbar.place(relheight=1, relx= 1)
        
        # Used to configure the scroll to scroll with more text
        scrollbar.configure(command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=scrollbar.set)

        # notes widget
        self.notes_widget = Text(self.middle, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, wrap=WORD, font=FONT, padx=10, pady=10)
        self.notes_widget.place(relheight=1, relwidth=0.295, relx=0.7, rely=0.007)
        self.notes_widget.configure(cursor="arrow", state=NORMAL)
        

        # Save button
        self.save_button = Button(self.notes_widget, text="Save Notes", font=FONT_BOLD, bg=SEND_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=15, height=1,command=lambda:self.save_notes())
        self.save_button.place(relheight=0.1, relwidth=0.4, rely=0.9, relx=0.595)
        self.protocol('WM_DELETE_WINDOW', self.save_and_quit) # Adds the protocol to save and quit when window is closed

        # Adds notes into
        self.set_notes(NOTES_FILE_NAME) # Sets notes from the file 
        self.notes_widget.insert(END, self.notes_content) # Displays in notes box

        # Bottom label area for widgets to be placed
        self.bottom_label = Label(self, bg=BG_GRAY, height= 40)
        self.bottom_label.place(relwidth=1, rely=0.815)

        # Entry title
        self.entry_label = Label(self.bottom_label,text="Enter Here:", fg=TEXT_COLOR, font=FONT_BOLD, bg=SEND_COLOR,borderwidth=0.52, relief=RAISED)
        self.entry_label.place(relwidth=0.095, relheight=0.06, rely=0.008, relx=0.011)

        # Entry box
        self.msg_entry = Entry(self.bottom_label, bg=SEND_COLOR, fg=TEXT_COLOR, font=FONT, borderwidth=0.9, relief=SUNKEN)
        self.msg_entry.place(relwidth=0.495, relheight=0.06, rely=0.008, relx=0.12)

        self.msg_entry.focus() # Focus on the entry box when application opened
        self.msg_entry.bind("<Return>",self.on_enter_press) # When enter/return key is pressed submit the message in the box
    
        # Send button widget
        self.send_button = Button(self.bottom_label, text="Send or press Enter", font=FONT_BOLD, width=20, bg=SEND_COLOR,
                                borderwidth=3,relief=RAISED, command=lambda:self.on_enter_press(None))
        self.send_button.place(relx=0.630, rely=0.008, relheight=0.06, relwidth=0.145)

        # Refresh button widget
        self.refresh_button = Button(self.bottom_label, text="👉 Refresh Suggestions 👈", font=FONT_BOLD, width=20, bg=SEND_COLOR, borderwidth=3,relief=RAISED)
        self.refresh_button.configure(command=lambda:self.refresh_suggestions(self.refresh_button))
        self.refresh_button.place(relx=0.811, rely=0.008, relheight=0.06, relwidth=0.18)

        # Suggestion label area for buttons to be placed
        suggestion_label = Label(self, bg=BG_GRAY, height= 40)
        suggestion_label.place(relwidth=1, rely=0.885)

        self.suggestion_button1 = Button(suggestion_label, text=self.get_suggestion(SUGGESTION_PROMPT), font=FONT, bg=BG_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=20, height=3, wraplength=220, padx=15 )
        self.suggestion_button1.configure(command=lambda:self.on_suggestion_press(self.suggestion_button1))
        self.suggestion_button1.place(relx=0.011, rely=0.008, relheight=0.11, relwidth=0.18)

        self.suggestion_button2 = Button(suggestion_label, text=self.get_suggestion(SUGGESTION_PROMPT), font=FONT, bg=BG_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=20, height=3, wraplength=220, padx=15)
        self.suggestion_button2.configure(command=lambda:self.on_suggestion_press(self.suggestion_button2))
        self.suggestion_button2.place(relx=0.211, rely=0.008, relheight=0.11, relwidth=0.18)

        self.suggestion_button3 = Button(suggestion_label, text=self.get_suggestion(SUGGESTION_PROMPT), font=FONT, bg=BG_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=20, height=3, wraplength=220, padx=15)
        self.suggestion_button3.configure(command=lambda:self.on_suggestion_press(self.suggestion_button3))
        self.suggestion_button3.place(relx=0.411, rely=0.008, relheight=0.11, relwidth=0.18)

        self.suggestion_button4 = Button(suggestion_label, text=self.get_suggestion(SUGGESTION_PROMPT), font=FONT, bg=BG_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=20, height= 3, wraplength=220, padx=15)
        self.suggestion_button4.configure(command=lambda:self.on_suggestion_press(self.suggestion_button4))
        self.suggestion_button4.place(relx=0.611, rely=0.008, relheight=0.11, relwidth=0.18)
        
        self.suggestion_button5 = Button(suggestion_label, text=self.get_suggestion(SUGGESTION_PROMPT), font=FONT, bg=BG_COLOR, borderwidth=3,relief=RAISED, fg=TEXT_COLOR, width=20, height=3, wraplength=220, padx=15)
        self.suggestion_button5.configure(command=lambda:self.on_suggestion_press(self.suggestion_button5))
        self.suggestion_button5.place(relx=0.811, rely=0.008, relheight=0.11, relwidth=0.18)

        # Adds all the suggestion buttons to a list
        self.suggestion_buttons = [self.suggestion_button1,self.suggestion_button2,self.suggestion_button3,self.suggestion_button4,self.suggestion_button5]

    def on_suggestion_press(self, button):
        msg = button.cget('text')
        button.configure(state=DISABLED) # Configures the button to be disabled
        self.update()
        self.user_message(msg)
        button.configure(state=NORMAL)

    def on_enter_press(self, event):
        msg = self.msg_entry.get() #Gets message entered into the entry
        self.user_message(msg)

    # Calls when either Enter is pressed from function on_enter_press or on_suggestion_press
    # Puts the user message in the text box and calls teacher_message to get the response
    # Buttons, labels and entry are disabled to give some the user action feedback
    # Then reenabled to return to normal
    def user_message(self, msg):
        if not msg: #If nothing in entry box then do nothing
            return
        
        self.msg_entry.delete(0, END) #Deletes whats in the entry box

        # Configures the send button to disabled and changes the text
        self.send_button.configure(text="Loading Response...",state=DISABLED)
        self.entry_label.configure(text="Loading..")
        self.msg_entry.configure(state=DISABLED)
        self.update()

        msg1 = f"👋 -- User: {msg} -- 👋\n\n"
        self.text_widget.configure(state=NORMAL) #Enables 
        self.text_widget.insert(END, msg1, 'user_message')
        self.text_widget.configure(state=DISABLED)

        self.teacher_message(msg)

        # Change the states back after ai has given a response
        self.send_button.configure(text="Send or press Enter",state=NORMAL)
        self.entry_label.configure(text="Enter here:")
        self.msg_entry.configure(state=NORMAL)

    # Asks the AI to create a response using the user input
    # Then it writes it to the text widget to display the output
    def teacher_message(self, user_message):
        msg2 = f"🤖 -- Teacher: -- 🤖 {self.ask_ai(user_message)} -- 👇\n\n"
        self.text_widget.configure(state=NORMAL) 
        self.text_widget.insert(END, msg2, 'teacher_message')
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

    # Used to use the ai functions and add it to the list of responses and text {returns: string response}
    def ask_ai(self, new_question):
        response = teacher.get_response(INSTRUCTIONS, previous_questions_and_answers, new_question)
        # add the new question and answer to the list of previous questions and answers
        previous_questions_and_answers.append((new_question, response))
        return response
    
    # Only gets suggestion and appends to the suggestions list
    def get_suggestion(self, suggestion_prompt):
        response = teacher.get_response(INSTRUCTIONS, previous_suggestions, suggestion_prompt)
        previous_suggestions.append((suggestion_prompt, response))
        return response

    # Function is called when Refresh button is clicked
    # Uses the AI to create Suggestions using a different prompt
    def refresh_suggestions(self, refresh_button):
        
        # Disables the refresh button when clicked
        refresh_button.configure(state=DISABLED)
        self.update()
        
        for button in self.suggestion_buttons:
            button.configure(state=DISABLED) # Disables the suggestion buttons
            self.update()
        
        for button in self.suggestion_buttons:
            button.configure(text=self.get_suggestion(SUGGESTION_PROMPT)) # Ask the ai to make questions to ask itself
            button.configure(state=NORMAL) # Enables the the suggestion back
        
        # Reenables the refresh button
        refresh_button.configure(state=NORMAL)

    
    # Gets the string of what has been put in the notes
    def get_notes(self):
        return self.notes_widget.get("1.0", "end-1c")
    
    # Reads language_learning_notes.txt file if it already exists and sets it to a variable
    # If it cant read the file (Doesn't exist) it will create one
    # First time users will create a file and it will save it with a little text
    def set_notes(self, file):
        try:
            self.notes_content = back.read_from_file(file)
        except:
            self.notes_content = "Please use this box to write any notes you want"
            self.save_notes()

    # Uses the Backend class in back.py to save to file
    def save_notes(self):
        back.save_to_file(NOTES_FILE_NAME,self.get_notes())
        
        # Added to give user feed back on their button click
        self.save_button.configure(state=DISABLED)
        self.update()
        time.sleep(0.25)
        self.save_button.configure(state=NORMAL)
    
    # Saves the notes then quits out of the window when X button on window is clicked
    def save_and_quit(self):
        self.save_notes()
        self.quit()

if __name__ == "__main__":
    teacher = Teacher()
    back = Backend()
    quiz = Quiz()
    app = LanguageApplication()
    info = Info()
    app.lower() # Puts the application window lower so the info page is on the top
    app.run()
