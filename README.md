
## Todo list using Django

- clone the repository 
- run the following command in your terminal


  ```sh
  python manage.py runserver
  ```
- checkout my project 

# Installation of Django

- run the following command in your terminal

```sh
	pip3 install Django
 ```
- Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/juanifioren/django-project-template/master/requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```
# Installation of Django on Mac
- open your terminal
## virtualenv installation on mac
- run following command
```sh
  sudo pip install virtualenv
```
- Okay, after installing, we need to create a virtual environment. Now you will create this folder when you are putting your other projects. Mine is desktop >> code folder. So navigate to that and type the following command. In my case, My virtualenv folder name is virtualen
```sh
  virtualenv thanos
```
- Okay, so it will install the required folders. Now, go into that folder
```sh
  cd virtualenv
```
- Now, activate the virtual environment by typing the following command. Please Make sure you are in the virtual environment directory.
```sh
  source bin/activate
```
## django installation
  
```sh
  sudo pip install django==3.0.1
```
- to check the version of django
```sh
  python -m django --version
```
 - will deploy this project on heroku server soon!!
- HAPPY CODING!
