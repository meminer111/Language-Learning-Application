from tkinter import *
from app import *

BG_GRAY = "#D6CBBF"
BG_COLOR = "#97B3AE"
TEXT_COLOR = "#000001"
BORDER_COLOR = "#748f8a"
BUTTON_COLOR = "#8be0a4"
SEND_COLOR = "#a4c3ad"
BUTTON_FONT = "Helvetica 14 bold"
FONT_BOLD = "Helvetica 20 bold"
FONT_TEXT_BOX = "Helvetica 12 bold"

class Info():
    # When class is created open the window
    def __init__(self):
        self.setup_info_window()

    # When info button is clicked window will open
    def setup_info_window(self):
        self.info_win = Toplevel()
        self.info_win.title("Information window")
        self.info_win.configure(width="1280",height="720",bg=BORDER_COLOR)
        self.info_win.resizable(width=False, height=False)

        # Filled for background
        background_filler = Label(self.info_win,background=BG_GRAY)
        background_filler.place(relheight=1, relwidth=1)

        # Header label
        header = Label(self.info_win,text="Any information on how to use the application is provided below",fg=TEXT_COLOR,font=FONT_BOLD,background=BG_GRAY)
        header.place(relheight=0.095, relwidth=1, rely=0.005)

        # Text widget with all the information
        self.text_widget = Text(background_filler, bg=BG_COLOR, fg=TEXT_COLOR, wrap=WORD, font=FONT_TEXT_BOX, padx=20, pady=10)
        self.text_widget.place(relheight=0.895, relwidth=1, rely=0.1)
        self.text_widget.insert(END, "1) In the middle of the application is the Assistant (Left side) as well as the Notes box (Right side) \n\n" \
        "   1a) You can type in the Notes box anything you want to save after you close the application. You can also click the save button to save notes as you go.\n\n" \
        "2) To ask your Assistant questions type in the box next to (Enter Here: ) at the bottom of the application. Alternatively you can also use the Suggestion Buttons at the bottom " \
        "of the screen. \n\n   2a) If you are not happy with the suggestions made for you, try clicking the (👉 Refresh Suggestions 👈) button. (This may take a little while dont panic! Just wait " \
        "for the button to go back to looking normal) \n\n3) Tips and Tricks for harnessing the Assistants full capabilities: \n\n   3a) Don't be ambiguous in your questions, it is important to " \
        "ask specifically for what you want. \n\n   3b) Learn new topics by asking (What are 5 common phrases used in a Restaurant?). \n\n   3c) Some words in German are spelt with special characters " \
        "that are not on english keyboards instead Umlauts (ä, ö, ü)" \
        "can be replaced with (ae, oe, and ue) respectively, as well as ( ß ) can be replaced with ( ss ). You can always ask the Assistant if you forget! \n\n" \
        "   3d) If you have asked the assistant about a new topic you can ask them to summarize what they have taught you. Also you can copy and paste their response    into the Notes Box by " \
        "selecting their response by holding left click and dragging over the words you want to copy. Then use the keys (Ctrl C) and then (Ctrl V) like you would in any application. \n\n" \
        "4) Close the Information window by clicking the button below or just minimize this window if you want to look at it while you write. This window can be re opened anytime " \
        "Just by clicking the info button on the main screen. Thank you and have fun learning German. ")

        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self.refresh_button = Button(self.text_widget, text="👉 I understand now 👈", font=BUTTON_FONT, width=20, bg=SEND_COLOR, borderwidth=3,relief=RAISED)
        self.refresh_button.configure(command=lambda:self.close_info())
        self.refresh_button.place(relx=0.35, rely=0.9, relheight=0.06, relwidth=0.3)

    def close_info(self):
        self.info_win.destroy()
