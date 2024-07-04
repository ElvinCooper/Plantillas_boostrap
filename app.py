from flask import Flask, render_template, url_for

app = Flask('__name__')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('form.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



if app == '__main__':
    app.run(debug=True) 