from mechanize import Browser
from bs4 import BeautifulSoup
import re

def login(br, url):
    page = br.open(url)
    br.select_form(nr=1)
    br.form["email"] = "USERNAME"
    br.form["password"] = "PASSWORD"
    br.submit()
    
def browse(br, url):
    page = br.open(url)
    soup = BeautifulSoup(page.read())
    title_div = soup.find("div", class_="dotd-title")
    title = title_div.get_text()
    return title
  
def click(br):
    req = br.click_link(url_regex=re.compile("freelearning-claim"))
    br.open(req)
    
def send_email(send_from, send_to, subject, body, password):      
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    fromaddr = send_from 
    toaddr = send_to 
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject 
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit() 
    
br = Browser()
success=True

try:
    login(br, "http://www.packtpub.com")
    book_title = browse(br, "http://www.packtpub.com/packt/offers/free-learning")
    click(br)
except:
    success=False
    error_message = str(err)
    
if(success): outcome = "Success: Grabbed the book " + book_title.strip() + " for free!"
else: outcome = "Failure: " + error_message
    
send_email("FROM", "TO", "PacktPub Grabber", outcome, "EMAIL PASSWORD")