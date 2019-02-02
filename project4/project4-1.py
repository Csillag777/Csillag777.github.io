from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

Session["username"] = "admin"
session.pop('username', None)


@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + \
      "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
   "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
   return redirect(url_for('index'))
   
   
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))   
   
   
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie('userID', user)
    
    return resp
   
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'  
   
if __name__ == "__main__":
   app.run(debug = True)
app.secret_key ="any random string"