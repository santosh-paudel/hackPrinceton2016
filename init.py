from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/AboutUs/')
def AboutUs():
	return render_template('AboutUs.html')

@app.errorhandler(404)
def page_not_found(e):
	return "<p>Page not found </p>"

if __name__=="__main__":
	app.run(debug=True)
