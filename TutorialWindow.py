import tkinter as tk

def DisplayTutorial() -> None:
    # Create a window
    tutorialWindow = tk.Tk()
    tutorialWindow.title("Tutorial")
    tutorialWindow.geometry("800x600")

    tutorialLabel = tk.Label(tutorialWindow, text="How to use QuickInvoice", font=("open sans", 20, "bold", "underline"))
    tutorialLabel.pack(side="top", padx=20, pady=20, anchor="nw")

    tutorialText = """
    This is just a test
    Please let me know if I have forgotten anythign. Blah blah blah, the fitness gram pacer test, I'm just testing the width"""
    bodyText = tk.Message(tutorialWindow, text=tutorialText, font=("open sans", 15), justify="left", width=500) # apparently justify adds first line indentation
    bodyText.pack(side="left", padx=20, pady=0, anchor="nw", expand=True)

    # Sustains the window
    tutorialWindow.mainloop()