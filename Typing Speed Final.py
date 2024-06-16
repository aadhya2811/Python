import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedTest:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = ''
        self.s = self.sentence_generator()
        self.input_text = ''
        self.start_time = 0
        self.end_time = 0

    def sentence_generator(self):
        with open("Sentences.txt", "r") as f:
            sentences = f.readlines()
        return random.choice(sentences)

    def intro(self):
        return f"Hello, {self.name}! welcome to typing speed test"

    def speed_test(self):
        self.start_time = time.time()

    def process_input(self, user_input):
        self.input_text = user_input
        self.end_time = time.time()

    def display_result(self):
        if self.input_text == '':
            result_text = "Test Failed."
        else:
            time_taken = self.end_time - self.start_time
            wpm = (len(self.s.split()) / time_taken) * 60
            result_text = f"Typing Speed: {wpm:.2f} words per minute\n"

            correct_characters = sum(c1 == c2 for c1, c2 in zip(self.s, self.input_text))
            total_characters = len(self.s)
            accuracy = (correct_characters / total_characters) * 100
            result_text += f"Accuracy: {accuracy:.2f}%\n"

            if wpm < 20 or accuracy < 20:
                result_text = "Test Failed."
            if wpm == 40 and accuracy > 50:
                result_text += "You've got average typing speed!"
            elif wpm > 40 and accuracy > 80:
                result_text += "Your typing speed is better than average!"
            else:
                result_text += "Your typing speed is below average!"

        return result_text

class TypingSpeedTestGUI:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")
        master.configure(bg='pink')

        custom_font = ("Helvetica", 14)

        self.typing_test = TypingSpeedTest()

        self.label = tk.Label(master, text="Welcome to the typing speed test!", bg='pink', font=custom_font)
        self.label.pack()

        self.name_label = tk.Label(master, text="Enter your name:", bg='pink', font=custom_font)
        self.name_label.pack()

        self.name_entry = tk.Entry(master, font=custom_font)
        self.name_entry.pack()

        self.start_button = tk.Button(master, text="Start Test", command=self.start_test, font=custom_font)
        self.start_button.pack()

        self.input_label = tk.Label(master, text="", bg='pink', font=custom_font)
        self.input_label.pack()

        self.entry = tk.Entry(master, font=custom_font)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.process_input, font=custom_font)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="", bg='pink', font=custom_font)
        self.result_label.pack()

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again, font=custom_font)
        self.play_again_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_program, font=custom_font)
        self.quit_button.pack()

    def start_test(self):
        self.typing_test.name = self.name_entry.get()
        intro_text = self.typing_test.intro()
        self.label.config(text=intro_text)

        
        sentence_text = f"Type the following sentence:\n{self.typing_test.s}"
        self.input_label.config(text=sentence_text)

        self.typing_test.speed_test()

    def process_input(self):
        user_input = self.entry.get()
        self.typing_test.process_input(user_input)
        
        
        result_text = self.typing_test.display_result()
        self.result_label.config(text=result_text)

    def play_again(self):
        self.typing_test.reset()
        self.label.config(text="Welcome to the typing speed test!")
        self.result_label.config(text="")
        self.input_label.config(text="")
        self.entry.delete(0, tk.END)

    def quit_program(self):
        messagebox.showinfo("Bye Bye!", "Thanks for playing! Bye Bye!")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestGUI(root)
    root.mainloop()
