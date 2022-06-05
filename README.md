# Selenium-Grabify-Mass-Mailer
Automated Chrome Selenium Grabify link creator for Email List...
1. Must have a gmail!
2. Must Have Selenium!
3. Must have an email list!
4. Must have a grabify Account!

## Download Selenium
```pip install selenium```
## Upgrade
```pip install selenium -U```

## Download the Chrome Driver and place the location in the code
https://chromedriver.chromium.org/downloads

## Create a grabify account
The program must be supplied the credentials
Supply all details including the email list.

## Will loop over captchas on grabify
I tested this program for a while and I found that there are captchas on grabify, so I decided to deal with the problem by instituting a try loop in case of selenium failure.
