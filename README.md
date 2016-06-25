# PAYMENT SYSTEM #
### This is a web service for depositing, withdrawing, transfering money between user! ###

**Running Locally**

```
#!script

* $ git clone https://nhat2008@bitbucket.org/nhat2008/payment_system.git
* $ cd payment_system
* $ pip install -r requirements.txt
* $ python manage.py migrate
* $ python manage.py customer migrate
* $ python manage.py payment migrate
* $ python manage.py runserver
```

This webservice will be run on http://127.0.0.1:8000/

This project is hosted online in Heroku, https://payment-system-v1.herokuapp.com/admin
