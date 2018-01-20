django_app
===============
Django_app is a simple django application created for learning purposes. It features the user to search/save a location/direction on Google Maps Embeded API.

<img width="1274" alt="gm" src="https://user-images.githubusercontent.com/26566198/34909233-76444f3a-f89d-11e7-8181-0b880e31bbe3.png">

Table of Contents
=================

* <a name="features-content">[1 Main features](#features)</a>
* <a name="installation-content">[2  Installation](#installation)</a>
    * <a name="prerequisites-content">[2.1 Prerequisites](#prerequisites)</a>
    * <a name="download-content">[2.2 Download](#download)</a>
    * <a name="requirements-content">[2.3 Requirements](#requirements)</a>
    * <a name="sass-content">[2.4 Compile SASS](#sass)</a>
    * <a name="tweaks-content">[2.5 Tweaks](#tweaks)</a>
* <a name="usage-content">[3  Usage](#usage)</a>
* <a name="contributing-content">[4  Contributing](#contributing)</a>
* <a name="license-content">[5  License](#license)</a>

<a name="features">[1  Main features](#features-content)</a>
===============

* For Django 1.11
* Works with Python 2.7 or 3.5
* Django debug toolbar
* User Login/Registration
* Google maps embed API
* Google place autocomplete
* Location and direction search
* Saving and revisiting most recent locations
* SASS 
* Integration with travis CI
* Integration with Coveralls
* Code coverage up to 95 %
* Integration and unit tests
* Code quality up to 9/10 using Django-pylint



<a name="installation">[2  Installation](#installation-content)</a>
===============

<a name="prerequisites">[2.1 Prerequisites](#prerequisites-content)</a>
-----------------
- Python 2.7 or 3.5 https://www.python.org/downloads/
- SASS http://sass-lang.com/install 


<a name="download">[2.2 Download](#download-content)</a>
-----------------
Now, you need the *django-sample-app* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone https://github.com/BorisBesker/django_app.git projectname && cd projectname


<a name="requirements">[2.3 Requirements](#requirements-content)</a>
-----------------
Right there, you will find the *requirements.txt* file that has all requirement packages, django helpers and some other cool stuff. To install them, simply type:

`$ pip install -r requirements.txt`


<a name="sass">[2.4 Compile SASS](#tweaks-sass)</a>
-----------------
Before application usage you need to compile Sass to CSS using the sass command. 
Navigate to directory where the main.scss is located: 

`cd accounts/static/accounts/sass.scss`

 Execute the command:
 
`sass main.scss main.css`

 You can also tell Sass to watch the file and update the CSS every time the Sass file changes:
 
`sass --watch main.scss:main.css`


<a name="tweaks">[2.5 Tweaks](#tweaks-content)</a>
-----------------

#### SECRET_KEY
Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open your `projectname/settings.py`, find `SECRET_KEY` line, paste your secret key.

```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR SECRET KEY THERE'
```

#### Initialize the database
In your settings files; `projectname/settings.py` the default database settings is set to sqlite3. 

```python
  DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'my_database',
        }
    }
```
If you want to use an another database set the database engine (PostgreSQL, MySQL, etc..). Of course, remember to install necessary database driver for your engine. Then define your credentials as well. Time to finish it up:

`./manage.py migrate`

### Ready? Go!

`./manage.py runserver`

<a name="usage">[3  Usage](#usage-content)</a>
===============



<a name="contributing">[4  Contributing](#usage-content)</a>
===============

*. If you find some bug or have an new idea to implement(feature), or just want to write tests for JS. code.
*. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
*. Write a test which shows that the bug was fixed or that the feature works as expected.
*. Send a pull request.


<a name="license">[5  License](#license-content)</a>
===============

This project is licensed under the MIT License - see the LICENSE.md file for details



Section 1.1 Title
-----------------



2
===============




dsasad 

```python
mystery_int = 50
sum1 = 0

for i in range(2, mystery_int):
    if i % 2 != 0:
        sum1 += i
print(sum1 + 1)

```



21312312312312Subsection 1.1.1 Title
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




