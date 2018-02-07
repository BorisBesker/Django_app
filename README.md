django_app
===============
Django_app is a simple django application created for learning purposes. It features the user to search/save a location/direction on Google Maps Embeded API.

<img width="1274" alt="gm" src="https://user-images.githubusercontent.com/26566198/35930619-b2b2eadc-0c32-11e8-99e3-1cbf1c7136f5.png">


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
    * <a name="basicusage-content">[3.1 Basic usage](#basicusage)</a>
    * <a name="tests-content">[3.2 Tests](#tests)</a>



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
**Recommended**: Create virtual environment

      $ pip install --upgrade virtualenv
      $ virtualenv env
      $ source env/bin/activate

Right there, you will find the *requirements.txt* file that has all requirement packages, django helpers and some other cool stuff. To install them, simply type:

`(env) $ pip install -r requirements.txt`


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
<a name="basicusage">[3.1 Basic usage](#basicusage-content)</a>
-----------------
Once the server is up and running, create an account and login into the app. From there you can search for locations or directions.
<img width="1274" alt="gm" src="https://user-images.githubusercontent.com/26566198/35930530-7291b212-0c32-11e8-9c14-2728cb2e3cc3.png">

When searching google maps autocomplete is on to make it easy for you. 
If you want to save a location click the button "SAVE LOCATION". 
To see the list of saved locations click on button "Saved locations". You can revesit the saved location clicking on it.

<img width="1274" alt="gm" src="https://user-images.githubusercontent.com/26566198/35930601-a570d960-0c32-11e8-9807-723aabb74541.png">

<a name="tests">[3.1 Tests](#tests-content)</a>
-----------------
Django_app is covered with unit and integration tests. 
### Running tests
The easiest way to run all the tests is to use the command:

`python manage.py test`

This will discover all files named with the pattern test*.py under the current directory and run all tests defined using appropriate base classes. By default the tests will individually report only on test failures, followed by a test summary.

### Running specific tests

If you want to run a subset of your tests you can do so by specifying the full dot path to the package(s), module, TestCase subclass or method:

`python3 manage.py test accounts.tests`   # Run the specified package tests (django application) 

`python3 manage.py test accounts.tests.test_integration`  # Run the specified module integration tests

`python3 manage.py test accounts.tests.test_integration.LoginViewTest` # Run the specified class

`python3 manage.py test accounts.tests.test_integration.LoginViewTest.test_login_view_url_exists`  # Run the specified

method



<a name="contributing">[4  Contributing](#usage-content)</a>
===============

1. If you find some bug or have an new idea to implement(feature), or just want to write tests for JS. code.
2. Fork <a href="https://github.com/BorisBesker/django_app">the repository</a> on GitHub to start making your changes to the **master** branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request.


<a name="license">[5  License](#license-content)</a>
===============

This project is licensed under the MIT License - see the <a href="https://raw.githubusercontent.com/BorisBesker/django_app/391adcb2dda56f11fff8743950d9fd45e4ba6306/LICENSE">LICENSE.md<a/> file for details



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




