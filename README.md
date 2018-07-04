Chatting System Between different Systems
===

Project Source Code Can be Downloaded from the github repository ykaran86/chat
---

Author
---

Yogesh Karan  
Email address:- ykaran86@gmail.com


**created and tested on Ubuntu 16.04 LTS with Python 3.6**

An Attempt to make a very simple, chatting system that makes it possible to make conversations between more than 2 systems at a time.

Once you have cloned the directory to your local machine, follow the directions below:
---
Prerequisites:-  
1. python 3.6 as default python version.  
2. google chrome as default browser.  
3. install pip  

The procedure mentioned here is taken from *Django girls tutorial* so you can take the help from
there too.

**Follow These Steps**

1. Download the code from the github repository ykaran86/chat and extract it.

2. Make a new folder/directory and give it a name(for example, chat) or run the following
command:-  
	` ~$ mkdir chat`  
this is the directory where you are going to add files from the downlaoded code

3. now create a virtual environment(name it as ‘myvenv’) inside that directory  
	` $ cd chat `  
	` ~/chat$ python3 -m venv myvenv `  
if you get error that virtual environment was not created then run the following command:-  
	` ~/chat$ sudo apt-get install python3-venv `  
	 		or  
	` ~/chat$ sudo apt install python3-venv `  
if still getting error in creating virtual environment checkout steps from *Django girls Tutorial*  
finally create the virtual environment:  
	` ~/chat$ python3 -m venv myvenv `

4. now start the virtual environment:-  
	` ~/chat$ source myvenv/bin/activate `

5. installing Django:-  
	` (myvenv) ~/chat$ python3 -m pip install --upgrade pip `  
	` (myvenv) ~/chat$ pip install django~=1.11.0 `

6. start the project:-  
	` (myvenv) ~/chat$ django-admin startproject login . `  
	**NOTE:-** “.” at the last is compulsary.

7. now you will have login directory inside the chat
directory.  
In that you will find **settings.py** file.  
In that you will find **ALLOWED_HOSTS** list.  
Add **'127.0.0.1','localhost'** in that list it will look like:-  
` ALLOWED_HOSTS = ['127.0.0.1','localhost'] `  
make changes in Internationalization as:-  
```

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

```  
and add a line after STATIC_URL  
```

STATIC_URL = '/static/'  
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

```
add three lines after the **INSTALLED_APPS** like this:  
```
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
]

LOGIN_URL='login'  
LOGOUT_URL='logout'  
LOGIN_REDIRECT_URL='home'

```

8. creating database:-  
run the command:  
	` (myvenv) ~/chat$ python manage.py migrate `  
if this gives any error like  
    1) No module named *apt_pkg*  
    then run:-  
	` (myvenv)~/chat$ sudo apt-get update `  
	` (myvenv)~/chat$ sudo apt-get dist-upgrade `  
    this may take a while.  
    In the root directory run the following command:-  
	` ~$ sudo ln -s apt_pkg.cpython-{35m,36m}-x86_64-linux-gnu.so `  
    you can search this solution in the stackOverflow also,i found there.  
    2) if error comes like No module named *django*  
    then run:-  
	` (myvenv)~/chat$ python -m pip install django `  
		 or use python3 in place of python  
    now finally run migrate command:-  
	` (myvenv) ~/chat$ python manage.py migrate `

Now, you can see a database file **db.sqlite3** in the chat directory which is the default database provided by django  
and here it will be used for creating users and their chats.
 
9. now check whether the website is running  
start the server:-  
	` (myvenv)~/chat$ python manage.py runserver `  
if no error shows up and a link(http://127.0.0.1:8000/) is  
provided then open that link in chrome.  
If It worked! is displayed then you are on right track.  

10. creating an application:-  
	` (myvenv)~/chat$ python manage.py startapp index `  
add ‘index’ in **INSTALLED_APPS** list in **login/settings.py**  
**INSTALLED_APPS** list will look like:-
```

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'index',
]

```

11. now replace the **models.py** in the index directory with the  
**models.py** in the **index directory from the downloaded code**.  
models.py is used to create the user and chats.

12. 1)now replace the **login/urls.py** with **login/urls.py** from
**downloaded code.**  
2)Copy **urls.py** in the **index directory from the downloaded code**
and paste in the **index directory in the chat directory**.

13. replace **views.py** in the **index directory** with the **views.py in**
**the index directory from the downloaded code.**  
**Views.py** is the main file which actually takes the chat
and gives to a javascript file which displays to HTML
file.

14. copy **static and templates directory in index directory** from
the **downloaded code** and paste in the **index folder of your chat**
directory  
**static directory contains chat.js and dialog.js** which takes chats from the
HTML file , sends to views.py and then views.py returns the chat
and it displays it to home.html  
**templates directory contains home.html,Dialogue.html,home.html,login.html,messages.html,signup.html**

15. copy the **forms.py from index directory of the downloaded code** and paste it in the **index directory of your chat directory**

16. for making changes in the database  
run the following commands:-  
	` (myvenv)~/chat$ python manage.py makemigrations index `  
	` (myvenv)~/chat$ python manage.py migrate index `  
	` (myvenv)~/chat$ python manage.py createsuperuser `  
now provide username,email,password

17. installing speech recoginition:-  
run following commands:-  
1) ` (myvenv)~/chat$ sudo apt-get install portaudio19-dev `  
2) ` (myvenv)~/chat$ pip install pyaudio `  
3) ` (myvenv)~/chat$ sudo pip install SpeechRecognition `

18. now you are all set to use the library dialogue system using
microphone  
start the Server  
	` (myvenv)~/chat$ python manage.py runserver `  	
go to the link http://127.0.0.1:8000/
