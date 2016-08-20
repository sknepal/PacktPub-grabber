# PacktPub Grabber

Grabs [https://www.packtpub.com/packt/offers/free-learning](Today's Free Learning eBook from PacktPub) & notifies you via Email.

## Dependencies

```sh
pip install beautifulsoup4
pip install mechanize
```

## Configuration
Steps to configure the script.

####PacktPub Account Information
Replace USERNAME and PASSWORD on line 8 and 9 with your packtpub username (email address) and password.

```python
    br.form["email"] = "USERNAME"
    br.form["password"] = "PASSWORD"
```

####Email Account Information

The script sends the email from a Gmail address you specify to your another email address. Note that, only Gmail account is accepted for sending email. I'd advise not to use your existing Gmail account since you need to enable access for less secure apps. 

* Create a new Gmail account.
* [https://support.google.com/accounts/answer/6010255?hl=en](Enable access for less secure apps) on the (new) sending Gmail account.
* Replace the "FROM", "TO", and "EMAIL PASSWORD" on the last line with your sending Gmail address, receiving Email address and the sending Gmail account's password respectively. 

```python
    send_email("FROM", "TO", "PacktPub Grabber", outcome, "EMAIL PASSWORD")
``` 
After each run, you'll receive an email in the "TO" address with the success/failure message.

## Run
Two ways to go about running the script.

####Manually
To run manually, simply go to the shell and type:

```python
    python /path/to/packtpub-grabber/packtpub-grabber.py
```
####Automatically
Since the purpose of the script is to automate the whole process of getting a free Ebook everyday, you should choose an automated way. So, put the script on your VPS and then setup a cron job so that the script runs everyday on the given time. 

Run _crontab -e_ and add the following lines to run the script everday at 6.30 PM. 

```
30 6 * * * python /path/to/packtpub-grabber/packtpub-grabber.py 2>>errors.log
```

The errors, if any, can be viewed on errors.log file.
