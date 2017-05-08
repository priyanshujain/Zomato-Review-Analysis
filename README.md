# Zomato Review Analysis
Sentiement analysis of reviews of restaurent by users on Zomato. Also it send email alert to restaurents for negative reviews.

## Dependencies

* MySQLdb (https://pypi.python.org/pypi/MySQL-python)
* textblob (https://textblob.readthedocs.io/en/dev/)
* sendgrid (https://pypi.python.org/pypi/sendgrid)
* nltk (http://www.nltk.org/)
* sklearn (http://scikit-learn.org/)
* csv (https://pypi.python.org/pypi/csv)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

## Usage
* Create database and table using
```
mysql -u root -p < db.sql
```
* Run
```
python review.py
```


##### For more information on Zomato API and Zomato API key
Visit : https://developers.zomato.com/api
