from flask import Flask, render_template, redirect, request, session, escape, flash
app = Flask(__name__)
app.secret_key = 'ThisIsASecretKey'
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/submit', methods=['POST'])
def success():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty")
		return redirect('/')
	else:
		session['name'] = escape(request.form['name'])
	if len(request.form['location']) < 1:
		flash("Location must be chosen")
		return redirect('/')
	else:
		session['location'] = escape(request.form['location'])
	if len(request.form['language']) < 1:
		flash("Language must be chosen")
		return redirect('/')
	else:
		session['language'] = escape(request.form['language'])
	if len(request.form['comment']) < 1:
		flash("Comment cannot be empty")
		return redirect('/')
	else:
		session['comment'] = escape(request.form['comment'])
	return redirect('/show')
@app.route('/show')
def show_success():
	return render_template('success.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])
@app.route('/back')
def go_back():
	session.clear()
	return redirect('/')
app.run(debug=True)