#DOWNLOAD PIP FILE OF SPEECH RECOGNITION AND PYTTSX3 FROM GOOGLE.
print("code by UMER AADIL")
import smtplib
import speech_recognition as sr
import pyttsx3
from email.msg import Emailmsg

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(recev, subjt, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender', 'Sender_password')
    email = Emailmsg()
    email['From'] = 'Sender'
    email['To'] = recev
    email['subject'] = subjt
    email.set_content(msg)
    server.send_msg(email)


email_list = {
    'HELP': 'HELP',
    'book': 'abcdef@gmail.com',
    'umer': 'umer@abcd.com',
    'suhail': 'suhail@bro.com',
    'outlook': 'outlook@live.com'
}


def get_email_info():
    talk('Tell Me the sender email id')
    name = get_info()
    recev = email_list[name]
    print(recev)
    talk('Subject of your email')
    subjt = get_info()
    talk('Text of Your Email')
    msg = get_info()
    send_email(recev, subjt, msg)
    talk('Your email is send successfully')
    talk('Do you want send more emails')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
