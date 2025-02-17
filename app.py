from flask import Flask , render_template , redirect , url_for , session ,request 
from werkzeug.security import generate_password_hash , check_password_hash 
import sqlite3


app = Flask(__name__)
app.secret_key = "mongoniITF_club"

@app.route('/')
@app.route('/index')
def index():
   return render_template('frontEnd/index-mp-layout1.html')

##
# 
# gallery 
# 
@app.route('/gallery') 
def gallery():
    return render_template('frontEnd/page-gallery-3col.html')  
    

if __name__ == '__main__':
    app.run(debug=True)