import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = 'https://en.wikipedia.org/wiki/Project_governance'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

title = soup.find(id="firstHeading").get_text()
print(title)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Your emzil id','Your password')


    subject = 'Project Governance'
    body = 'Hey check this, https://en.wikipedia.org/wiki/Project_governance'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Senders Email id',
        'Recievers Email id',
        msg)

send_mail()
print("Email has been sent")
