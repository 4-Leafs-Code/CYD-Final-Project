from database import *
from flask import *

app = Flask(__name__)
app.secret_key = 'CorrectionsSecureKey'  # you can set any secret key but remember it should be secret

@app.route('/')
def Access():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("Home.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return render_template("Access.html")

@app.route('/login', methods=['POST', 'GET'])
@app.route('/login/<message>', methods=['POST', 'GET'])
def login(message=''):
    if message or request.method == 'GET':
        # show the user the login page
        return render_template("login.html", message=message, session=session)
    else:
        # the user is trying to log in
        username = request.form['username']
        password = request.form['password']

        # NEW STEP: USE DATABASE!
        if authenticate(username, password):
            # login successful!
            # save user to session & redirect to their Account
            session['username'] = username
            return redirect('/Home')

        # failed login, redirect to login page
        message = "Wrong username or password. Try again."
        return redirect(url_for('login', message=message))

@app.route('/Home')
def Home():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("Home.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/UMA')
def UMA():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("UMA.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/WCCC')
def WCCC():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("WCCC.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/MCCWRS')
def MCCWRS():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("MCCWRS.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/News_Letter')
def News_Letter():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("News_Letter.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/Womens_Center')
def Womens_Center():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("Womens_Center.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/SMWRC')
def SMWRC():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template("SMWRC.html", user=user)
    # user is not yet logged in
    message = "You must login to access this site."
    return redirect("/")

@app.route('/Account')
def Account():
    if 'username' in session:
        # if the user is logged in (a.k.a. in session)
        username = session['username']
        user = get_user_from_database(username)
        return render_template('Account.html', user=user)
    # user is not yet logged in
    message = "You must login to access your Account."
    return render_template("login.html", message=message)\

@app.route('/admin')
def admin():
    if 'username' in session:
        username = session['username']
        user = get_admin_from_database(username)
        if user == True:
            return render_template("admin.html")
        else:
            return redirect('/Home')

@app.route('/logout')
def logout():
    # remove the session from the browser
    session.pop('username')
    return redirect('/')

@app.route('/signup', methods=['POST', 'GET'])
@app.route('/signup/<message>', methods=['POST', 'GET'])
def signup(message=''):
    if request.method == 'GET':
        print(session)
        # show the user the login page
        return render_template("signup.html", session=session, message=message)
    else:
        # the user is trying to sign up
        # get user information from request.form dictionary
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        # check if username is already taken
        if is_username_taken(username):
            message = "Username already taken; please choose a different one."
            return redirect(url_for('signup', message=message))

        # add user information to database
        add_user(name, username, password)

        # save user to session & redirect to their Account
        session['username'] = username
        return redirect(url_for('Home', message=message))

if __name__ == '__main__':
    app.run(debug=True)
