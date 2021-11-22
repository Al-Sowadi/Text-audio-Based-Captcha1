from tkinter import *
import tkinter.messagebox
from captcha.image import ImageCaptcha
import string
import random
import os
import pyttsx3
# from tkinter import ttk
class audio:
    audio_captcha = ''
     # to generate audio captcha i.e 5698 , s1 will return the value
    def generate_digit_captcha(self):
        self.VAR2 = ''
        self.VAR1 = ''
        for i in range(5):
            self.randvalu = str(random.randint(0, 9))
            self.VAR1 = self.VAR1 +self. randvalu
            self.VAR2 = self.VAR2 + self.randvalu + " "
        # print(type(VAR1))
        self.audio_captcha
        self.audio_captcha = self.VAR1

        return self.VAR2

    def generate_audio_captcha(self):
        self.st = self.generate_digit_captcha()
        # print(st)

        self.voiceEngine = pyttsx3.init()  # object creation

        self.voiceEngine.setProperty('rate', 200)# getting details of current speaking rate
        self.voiceEngine.setProperty('volume', 1.00)#getting to know current volume level (min=0 and max=1


        self.voices = self.voiceEngine.getProperty('voices')#getting details of current voice
        self.voiceEngine.setProperty('voice', self.voices[1].id)#changing index, changes voices. o for male: 1 for female
        
        self.voiceEngine.say(self.st)  # saying value of s and runing 3 time 
        self.voiceEngine.runAndWait()
        self.voiceEngine.say(self.st)
        self.voiceEngine.runAndWait()
        # self.voiceEngine.say(self.st)
        # self.voiceEngine.runAndWait()
        """Saving Voice to a file"""
        """
        self.engine.save_to_file(self.st, 'test.mp3')
        self.engine.runAndWait()
        """

        # print("Audio Captcha Generated.\n\n")

    
    def regenerate_audio_captcha(self):
        self.generate_audio_captcha()

    # to return the value of audio capt so we will be able to chick weather audio capt value is mutch with user input

    def get_audio(self):
        return self.audio_captcha

    # to chick Captcha Code Matched for  audio .'messagebox' will display
    def check_audio_captcha(self):
        # answer = input("\nEnter Value : ")
        if self.ans.get() == self.get_audio():
            tkinter.messagebox.showinfo("SUCCESS!", "Captcha Code Matched.")
            self.ans.set("")

        else:
            tkinter.messagebox.showinfo("WRONG!", "Captcha Code does not Matched.")
            self.ans.set("")
class capt_img:
    
    image_captcha = ''
    # code for image captcha
    # to generate captcha value i.e sh5or6 ,s will return the value of capt
    def generate_captcha(self):
        self.data = list(string.ascii_letters + string.digits)  # a-z,A-Z,0-9
        self.VARBS = ''
        for i in range(6):
            self.VARBS1 = random.choice(self.data)
            self.VARBS = self.VARBS + self.VARBS1
            self.data.remove(self.VARBS1)

        self.image_captcha
        self.image_captcha = self.VARBS
        # print(self.VARBS)
        return self.VARBS
    # for image captchar file open from file
    def generate_image_captcha(self):
        # to open the image
        os.startfile('capt.png')
    # for generate image take value from global string "image_captcha"
    def generate_first_image(self):
        self.img = ImageCaptcha()
        # recursive function generate_captcha to give the value i.e hfjf4g
        self.st = self.generate_captcha()
        # print(s)
        # generate value capt
        self.value = self.img.generate(self.st)
        # generate img capt
        self.img.write(self.st, "capt.png")


    def regenerate_image_captcha(self):
        self.img = ImageCaptcha()

        self.st = self.generate_captcha()
        # print(s)
        self.value = self.img.generate(self.st)
        self.img.write(self.st, "capt.png")
        os.startfile('capt.png')
        # print("Image Captcha Generated.\n\n")

    # 
    def get_image(self):
        return self.image_captcha

    # to chick Captcha Code Matched for  image .'messagebox' will display
    def check_image_captcha(self):
        if self.ans1.get() == self.get_image():
            tkinter.messagebox.showinfo("SUCCESS!", "Captcha Code Matched.")
            self.ans1.set("")
        else:
            tkinter.messagebox.showinfo("WRONG!", "Captcha Code does not Matched.")
            self.ans1.set("")
class Root(Tk,capt_img,audio):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Text Based Captcha")
        # to specify height and width of interface window
        self.geometry("777x420")
        self.configure(background='#100457')
        self.ans = StringVar()
        self.ans1 = StringVar()
        # generate_first_image()
        self.colorbg='#390411'
        self.MainFrame = Frame( bg='Powder Blue', pady=2, width=1100, height=100, relief=RIDGE)
        self.MainFrame.grid(row=1, column=0)
        
    def Top(self):
        self.Tops = Frame( bg='#880325', pady=1, width=450, height=40, relief="ridge")
        self.Tops.grid(row=0, column=0)
        self.Title_Label = Label(self.Tops, font=('Comic Sans MS', 12, 'bold'),
                    text="             Text Based CAPTCHA Generation \t\t", bg='#031012',
                    fg='white', justify="center")
        self.Title_Label.grid(row=0, column=0)
        
    def img_part(self):
        self.LeftFrame = Frame(self.MainFrame, bd=10, width=150, height=150, pady=2, padx=8, bg=self.colorbg, relief=RIDGE)
        self.LeftFrame.pack(side=LEFT)

        self.Label_1 = Label(self.LeftFrame, font=('lato black', 30, 'bold'), text=" Image Captcha ", padx=2, pady=2,
                        fg="#310308")
        self.Label_1.grid(row=0, column=0, sticky=W)

        self.Label_2 = Label(self.LeftFrame, font=('arial', 17, 'bold'), text="", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_2.grid(row=1, column=0, sticky=W)

        self.Label_9 = Button(self.LeftFrame, font=('arial', 16, 'bold'), text="Show Image", padx=2, pady=2,  fg="#310308",
                        command=self.generate_image_captcha)
        self.Label_9.grid(row=4, column=0)

        self.Label_7 = Label(self.LeftFrame, font=('arial', 17, 'bold'), text="", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=2, column=0, sticky=W)

        self.Entry_1 = Entry(self.LeftFrame, font=('arial', 17, 'bold'), bd=2, fg="black", textvariable=self.ans1, width=12,
                        justify=LEFT).grid(row=5, column=0)

        self.Label_7 = Label(self.LeftFrame, font=('arial', 17, 'bold'), text="", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=6, column=0, sticky=W)

        self.Label_7 = Label(self.LeftFrame, font=('arial', 17, 'bold'), text="  ", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=6, column=1, sticky=W)

        self.Label_8 = Button(self.LeftFrame, font=('Arial', 20, 'bold'), text="Check", padx=2, pady=2, bg="white", fg="#310308",
                        command=self.check_image_captcha)
        self.Label_8.grid(row=9, column=0)

        self.Label_4 = Button(self.LeftFrame, font=('arial', 12, 'bold'), text="Regenerate", padx=2, pady=2, bg="white", fg="#310308",
                        command=self.regenerate_image_captcha)
        self.Label_4.grid(row=10, column=0)

        self.Label_7 = Label(self.LeftFrame, font=('arial', 17, 'bold'), text="      ", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=11, column=1, sticky=W)


    def audio_part(self):

        self.RightFrame = Frame(self.MainFrame, bd=10, width=150, height=150, padx=8, pady=2, bg=self.colorbg, relief=RIDGE)
        self.RightFrame.pack(side=RIGHT)
        
        self.LabelAudio_1 = Label(self.RightFrame, font=('lato black', 30, 'bold'), text=" Audio Captcha ", padx=2, pady=2,
                fg="#310308")
        self.LabelAudio_1.grid(row=0, column=0, sticky=W)

        self.LabelRightFrame_2 = Label(self.RightFrame, font=('arial', 17, 'bold'), text="", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.LabelRightFrame_2.grid(row=1, column=0, sticky=W)

        self.Label_9 = Button(self.RightFrame, font=('arial', 17, 'bold'), text="Play Audio", padx=2, pady=2, fg="#310308",
                 command=self.generate_audio_captcha)
        self.Label_9.grid(row=4, column=0)

        self.Label_7 = Label(self.RightFrame, font=('arial', 17, 'bold'), text="", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=2, column=0, sticky=W)

        self.Entry_1 = Entry(self.RightFrame, font=('arial', 17, 'bold'), bd=2, fg="black", textvariable=self.ans, width=12,
                justify=LEFT).grid(row=5, column=0)

        self.Label_7 = Label(self.RightFrame, font=('arial', 17, 'bold'), text="", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=6, column=0, sticky=W)

        self.Label_7 = Label(self.RightFrame, font=('arial', 17, 'bold'), text="  ", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=6, column=1, sticky=W)

        self.Label_8 = Button(self.RightFrame, font=('Arial', 17, 'bold'), text="Check", padx=2, pady=2, bg="white", fg="#310308",
                 command=self.check_audio_captcha)
        self.Label_8.grid(row=9, column=0)

        self.Label_4 = Button(self.RightFrame, font=('arial', 12, 'bold'), text="Regenerate", padx=2, pady=2, bg="white", fg="#310308",
                 command=self.regenerate_audio_captcha)
        self.Label_4.grid(row=10, column=0)

        self.Label_7 = Label(self.RightFrame, font=('arial', 17, 'bold'), text="      ", padx=2, pady=2, bg=self.colorbg, fg="black")
        self.Label_7.grid(row=11, column=1, sticky=W)




    def fun_call(self):
        self.Top()
        self.img_part()
        self.audio_part()

root=Root()
root.fun_call()
root.mainloop()