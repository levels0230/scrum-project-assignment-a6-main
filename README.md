# Group 6

Setting up Python virtual environment

```
$ python -m venv myENV
```
Activate the environment 

```
$ source myENV/bin/activate
```

install flask and update pip

```
$ pip install flask
$ pip install --upgrade pip
```

manage packages installed:

```
$ pip freeze > requirements.txt
```

Later when you clone or start fresh, you can install packages:

```
$ pip install -r requirments.txt
```

### updates to the application run 

setup the __init__py
then setup the routes.py

Follow the tutorial:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

