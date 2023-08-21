import tkinter as tk
from nltk.chat.util import Chat, reflections
import pyttsx3
from ttkthemes import ThemedStyle

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        #self.root.configure(bg="#f0f0f0")

         # Create a themed style for the GUI
        self.style = ThemedStyle(self.root)
        self.style.set_theme("clam")  # You can try different themes
        
        self.pairs = [
            [
                r"(?i)hi|hello|hey",
                ["Hello!", "Hi there!", "Hey! How can I help you?"]
            ],
            [
        r"(?i)bye|goodbye",
        ["Goodbye!", "See you later!", "Have a great day!"]
    ],
    [
        r"(?i)good|very good|nice|wow",
        ["Thank you so much","Thanks buddy"]
    ],
    [
        r"(?i)how are you|how's it going",
        ["I'm just a chatbot, but I'm here to help!", "I'm doing well, thank you!"]
    ],
    [
        r"(?i)whats up|tell me something",
        ["Do you like songs?", "How is your mood? happy, sad, romantic or motivational?"]
    ],
    [ 
        r"(?i)what is your name",
        ["you can call me Sam,Thanks for asking"]
    ],
    [
        r"(?i)happy",
        ["If you are happy, try CRUISs Go For It Cyndi Laupes Girls Just Want to Have Fun. Songs like Walking on Sunshine by Katrina and the Waves and Here Comes the Sun by the Beatles might even inspire you to soak up some vitamin D outdoors."]
    ],
    [
        r"(?i)sad",
        ["If you are sad, try Lay Me Down By Sam Smith, Great American Novel By Max Jury, Would've Could've Should've By Taylor Swift, Don’t Watch Me Cry By Jorja Smith, Male Fantasy By Billie Eilish, Glimpse of Us in By Joji, Risk By FKJ & Bas, Wake Up Alone By Amy Winehouse; these might change your mood."]
    ],
    [
        r"(?i)motivational",
        ["There are some songs that might motivate you a bit more. I have made you a list of 20 Inspirational English songs that I hope will help you to get throughAin’t No Mountain High Enough by Marvin Gaye and Tammi Terrell I Will Survive by Gloria Gaynor Lose Yourself by Eminem Im Still Standing by Elton John Survivor by Destinys Child Harder, Better, Faster, Stronger by Daft Punk Your Love Keeps Lifting Me) Higher and Higher by Jackie Wilson Juicy’ by the Notorious BIG"]
    ],
    [
        r"(?i)romantic",
        ["I have made you short list of romantic songs, try these... We Found Love  by Rihanna and Calvin Harris, Alive With the Glory of Love by Say Anything, My Love by Justin Timberlake, Love Yourz  by J. Cole, How Deep is Your Love  by the Bee Gees, Love Story by Taylor Swift, Its the Falling in Love by Michael Jackson"]
    ],
    [
        r"(?i)yes",
        ["How is your mood? happy, sad, motivational or romantic?"]
    ],
    [
        r"(?i)no",
        ["How can i help you?"]
    ],
    [
    r"(.*)",
    [
        "I'm sorry, I didn't quite understand that. Could you please rephrase your question?",
        "I'm still learning and might not have an answer for that. Can you ask something else?",
        "I'm not sure I understand. Could you provide more context?",
    ]
],

            ]
        

        self.width = self.root.winfo_screenwidth()  # Get screen width
        self.height = self.root.winfo_screenheight()  # Get screen height
        self.root.geometry(f"{self.width}x{self.height}")

        #self.background_image = tk.PhotoImage(file=r"C:\Users\kiran\Downloads\download.gif")
        #self.background_image = self.background_image.subsample(int(self.background_image.width() / self.width))
        #self.background_label = tk.Label(self.root, image=self.background_image)
        #self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.chat_text = tk.Text(self.root, height=15, width=60, bg="white", wrap=tk.WORD, state=tk.DISABLED)
        self.chat_text.pack(padx=20, pady=(20, 10))

        self.scrollbar = tk.Scrollbar(self.root, command=self.chat_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_text['yscrollcommand'] = self.scrollbar.set

        self.clear_button = tk.Button(self.root, text="Clear Chat", command=self.clear_chat,
                                      bg="#F44336", fg="white", font=("Helvetica", 12, "bold"))
        self.clear_button.pack()

        self.engine = pyttsx3.init()

        self.entry = tk.Entry(self.root, width=60, font=("Helvetica", 12))
        self.entry.pack(padx=20, pady=(0, 20))

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message,
                                     bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.send_button.pack()

        self.root.bind("<Return>", self.send_message)

        self.chatbot = Chat(self.pairs, reflections)

        self.greet_and_speak("Hello! I'm your ChatBot. How can I assist you today?")

    def greet_and_speak(self, message):
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "Bot: " + message + "\n", "bot")
        self.chat_text.tag_config("bot", foreground="#4CAF50", font=("Helvetica", 12, "bold"))
        self.chat_text.config(state=tk.DISABLED)
        self.engine.say(message)
        self.engine.runAndWait()

    def clear_chat(self):
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.delete("1.0", tk.END)
        self.chat_text.config(state=tk.DISABLED)

    def bot_speaking(self, response):
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "Bot: ... (speaking)\n", "bot")
        self.chat_text.tag_config("bot", foreground="orange", font=("Helvetica", 12, "bold"))
        self.chat_text.see(tk.END)
        self.chat_text.config(state=tk.DISABLED)
        self.root.update()
        self.engine.say(response)
        self.engine.runAndWait()
        # Clear the "speaking" indicator after speech
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.delete("bot.last+1c", tk.END)
        self.chat_text.config(state=tk.DISABLED)


    def send_message(self, event=None):
        user_input = self.entry.get()
        response = self.chatbot.respond(user_input)
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "You: " + user_input + "\n", "you")
        self.chat_text.tag_config("you", foreground="#007acc", font=("Helvetica", 12, "bold"))
        self.chat_text.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)
        
        if "bye" in response.lower():
            self.root.destroy()
        self.bot_speaking(response)
        self.chat_text.config(state=tk.NORMAL)
        self.chat_text.insert(tk.END, "Bot: " + response + "\n", "bot")
        self.chat_text.tag_config("bot", foreground="#4CAF50", font=("Helvetica", 12, "bold"))
        self.chat_text.see(tk.END)
        self.chat_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()
