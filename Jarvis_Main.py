import speedtest
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui_own import Ui_Dialog
import tkinter as tk
from tkinter import simpledialog
import pyttsx3
import speech_recognition as sr
import datetime
import psutil
import tkinter as tk
import os
import cv2
import PyPDF2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

system_dir = os.environ.get("SystemRoot", os.path.join(os.environ.get("SystemDrive"), "Windows"))

# Constructing the full path to Notepad
npath = os.path.join(system_dir, "system32", "notepad.exe")

def run_once(flag_file_path):
    """
    Check if a function has been run once by checking the existence of a flag file.
    
    Parameters:
        flag_file_path (str): The path to the flag file.
        
    Returns:
        bool: True if the function has not been run before and creates the flag file, False otherwise.
    """
    # Check if the flag file exists
    if os.path.exists(flag_file_path):
        print("User input has already been obtained. Skipping...")
        return False
    
    # If the flag file does not exist, proceed with getting user input
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt user for input
    global apath, music_dir, email_id, email_pwd, sendemail_id, News_Api, api_key
    apath = simpledialog.askstring("Input", "Enter path for apath:")
    music_dir = simpledialog.askstring("Input", "Enter path for music_dir:")
    email_id = simpledialog.askstring("Input", "Enter your email ID:")
    email_pwd = simpledialog.askstring("Input", "Enter your email password:", show="*")
    sendemail_id = simpledialog.askstring("Input", "Enter email ID to send to:")
    News_Api = simpledialog.askstring("Input", "Enter your News API key:")
    api_key = simpledialog.askstring("Input", "Enter your OpenWeatherMap API key:")
    
    # Destroy the root window after input is provided
    root.destroy()
    
    # Create the flag file to indicate that user input has been obtained
    with open(flag_file_path, "w") as f:
        f.write("User input has been obtained. This file prevents the function from running again.")
    
    return True

def get_user_input():
    flag_file_path = "get_user_input.flag"  # Specify the path to the flag file
    function_ran_first_time = run_once(flag_file_path)
    if function_ran_first_time:
        # Code to execute if the function ran for the first time
        print("User input obtained successfully!")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#text to speech
def speak(audio):
    # print(audio)
    engine.say(audio)
    engine.runAndWait()



def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning sir, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon sir, its {tt}")
    else:
        speak(f"good evening sir, its {tt}")
    speak("i am jarvis. please tell me how may i help you")

def news():
    main_url = f'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={News_Api}'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Prompt user for file location
    fil = filedialog.askopenfilename(title="Select PDF file")
    
    try:
        # Open the PDF file
        book = open(fil, 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f"Total number of pages in this book: {pages}")
        
        # Prompt user for page number
        pg = simpledialog.askinteger("Input", "Enter the page number to read:")
        if pg is None:
            speak("No page number provided. Exiting...")
            return
        
        # Read the specified page and extract text
        page = pdfReader.getPage(pg)
        text = page.extractText()
        
        # Speak the text
        speak(text)
    except Exception as e:
        speak("An error occurred while reading the PDF file.")
        print(e)


def Sweather():
    
    ipAdd = requests.get('https://api.ipify.org').text
    print(ipAdd)
    
    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    print(geo_data)
    
    city = geo_data['city']
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = (f'{city}')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    response = requests.get(complete_url)
    x = response.json()
    
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        
        r = ("Outside, the temperature is " +
              str(int(current_temperature - 273.15)) + " degrees Celsius, " +
              "atmospheric pressure " + str(current_pressure) + " hPa unit, " +
              "humidity is " + str(current_humidity) + " percent, " +
              "and " + str(weather_description))
        
        speak(r)
    else:
        speak("City Not Found")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        recognizer = sr.Recognizer()
        recognizer.dynamic_energy_threshold = False
        recognizer.energy_threshold = 35000
        recognizer.dynamic_energy_adjustment_damping = 0.03
        recognizer.dynamic_energy_ratio = 1.9
        recognizer.pause_threshold = 0.4
        recognizer.operation_timeout = None
        recognizer.phrase_threshold = 0.2
        recognizer.non_speaking_duration = 0.3

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)

            while True:
                print("Listening....", end='', flush=True)
                try:
                    audio = recognizer.listen(source, timeout=None)
                    print("\rRecognizing...   ", end='', flush=True)
                    recognized_text = recognizer.recognize_google(audio).lower()
                    if recognized_text:
                        return recognized_text
                    else:
                        return ""
                except sr.UnknownValueError:
                    recognized_text = ""
                finally:
                    print("\r", end='', flush=True)
                    os.system('cls' if os.name == 'nt' else 'clear')


    def TaskExecution(self):
        get_user_input()
        wish()
        while True:
            query = self.takecommand()

            if "open notepad" in query:
                os.startfile(npath)

            elif "open adobe reader" in query:
                os.startfile(apath)

            elif "open command prompt" in query:
                os.system("start cmd")

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in query:
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print("according to wikipedia ")
                print(results)
                speak("according to wikipedia")
                speak(results)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in query:
                webbrowser.open("www.facebook.com")

            elif "open stack  overflow" in query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in query:
                print("sir, what should i search on google")
                speak("sir, what should i search on google")
                cm = takecommand()
                webbrowser.open(f"{cm}")

            elif "song on youtube" in query:
                speak("sir, what should i search on youtube")
                cm = takecommand()
                kit.playonyt(f"{cm}")

            elif "whatsapp message" in query:
                speak("Enter the number to send the message")
                root = tk.Tk()
                root.withdraw()  # Hide the root window
                # Prompt user for phone number
                num = simpledialog.askstring("Input", "Enter phone number to send (without country code): ")
                num = "+91" + num  # Assuming the country code is fixed as +91 for India
                # Prompt user for message
                speak("Sir, please enter the message")
                mes = takecommand()
                # Get current time
                current_time = datetime.datetime.now()
                hour = current_time.hour
                minute = current_time.minute + 1
                # Send WhatsApp message
                kit.sendwhatmsg(num, mes, hour, minute)
                # Wait for message to be sent (optional)
                time.sleep(120)
                speak("Message has been sent")            

            elif "you can sleep" in query or "sleep now" in query:
                speak("okay sir, i am going to sleep you can call me anytime.")
                sys.exit()

            elif "close notepad" in query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "set alarm" in query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "shut down the system" in query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "hello" in query or "hey" in query:
                speak("hello sir, may i help you with something.")

            elif "how are you" in query:
                speak("i am fine sir, what about you.")

            elif "no thanks" in query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

            elif "thank you" in query or "thanks" in query:
                speak("it's my pleasure sir.")

            elif 'switch window' in query or "change screen" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in query:
                speak("please wait sir, feteching the latest news")
                news()

            elif "where i am" in query or "where we are" in query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass

            elif "take screenshot" in query or "take a screenshot" in query or "screenshot" in query:
                speak("sir, please tell me the name for this screenshot file")
                name = takecommand()
                speak("please sir hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

            elif "read pdf" in query:
                pdf_reader()

            elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = takecommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d")  # os module
                    speak("sir, all the files in this folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak(
                        "sir, all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif "weather" in query:
                Sweather()

            elif 'timer' in query or 'stopwatch' in query:
                speak("For how many minutes?")
                timing = takecommand()
                timing =timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')
                time.sleep(timing)
                speak('Your time has been finished sir')

            else:
                speak("i am unable to understand please say again")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("images/___3.gif")
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("images/64ebb007104825948e077233babe3fcb.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("images/initial.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("images/Iron_Template_1.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)

        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
mainWindow = Main()
mainWindow.show()
exit(app.exec_())
