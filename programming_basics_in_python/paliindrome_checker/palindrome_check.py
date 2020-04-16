#Implementation to check whether the number is palindrome or not.
from flask import Flask
from flask import request
import os
#import magic
import urllib.request
from subprocess import Popen
#from webapp import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = "secret key"
#function to check whether the number is palindrome or not


@app.route('/')
def upload_form():
	return render_template('upload.html')


@app.route('/', methods=['GET', 'POST'])
def check_palindrome():
    #get input from user 

    if request.method == 'POST':
        number = None
        try:
            number = request.form["number"]
        except Exception as e:
            print(e)
      
        
        inp_num = number
    #check the entire number by reversing it in the list.
        if inp_num[::] == inp_num[::-1]:

        #if the reversed number matches original it is palinrome
            print("Voila! It is palindrome")
            
        #else not
        else:
            print("Well, why not try again")
    else:
        return render_template(upload_form)




if __name__ == "__main__":
    app.run(port=5555, debug=True)