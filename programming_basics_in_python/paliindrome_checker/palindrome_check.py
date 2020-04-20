#Implementation to check whether the number is palindrome or not.
from flask import Flask
from flask import request
from flask import url_for
import os

import urllib.request
from subprocess import Popen

from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

# Define the flask app
app = Flask(__name__)
app.secret_key = "dev"

# Main template
@app.route('/')
def upload_form():
	return render_template('upload.html')

# Function that checks whether the given number is alindrome or not
@app.route('/', methods=['GET', 'POST'])
def check_palindrome():
    
    #get input from user from the form
    if request.method == 'POST':
        number = None
        try:
            number = request.form["number"]
        except Exception as e:
            print(e)
      
        # Assign to the local variable
        inp_num = number
        
        #check the entire number by reversing it in the list.
        if inp_num[::] == inp_num[::-1]:

        #if the reversed number matches original it is palinrome
            #abc = "Voila! It is palindrome"
            print("Voila! It is palindrome")
            flash("Voila! It is palindrome")
            
            return redirect(url_for('check_palindrome'))
            #return render_template('results.html', abc=abc)

        else:
            
            print("Well, why not try again")
            flash("Beep Bop, Well, why not try again with an actual palindrome!!!")
            return redirect(url_for('check_palindrome'))
            #return render_template('results.html', abc=msg)
    else:
        return render_template(upload_form)



# Run the app.
if __name__ == "__main__":
    app.run(port=5555, debug=True)