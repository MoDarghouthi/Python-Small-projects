import csv
from email import message
from email.message import EmailMessage
import smtplib


def get_credentials(credentialsFile):
    with open("credentials.txt","r") as f:
        email_address = f.readline()
        password = f.readline()
    return (email_address,password)

def login(email_address,password,s):
    s.ehlo()

    s.starttls()
    s.ehlo()

    s.login(email_address, password)

    print("login")


def sendEmail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    email_address, password = get_credentials("./credentials.txt")
    login(email_address, password, s)
    subject = "Broadcast Email"
    body = """This is a generated email for all our subscribers"""
    message = EmailMessage()

    message.set_content(body)

    message["subject"] = subject
    with open("emails.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for email in spamreader:
            s.send_message(email_address, email[0], message)
            print("Send To " + email[0])

    s.quit()
    print("sent")


if __name__ == "__main__":

    sendEmail()