from flask import Flask,render_template

#render_template---->flask
app=Flask(__name__)


@app.route('/wish/<n>')
def wish(n):
    return 'hai how r u {}'.format(n)

@app.route('/something/')
def hai():
    return 'This is an hypelinked page'

@app.route('/temp/')
def template1():
    return render_template('h1.html',name='Harshad',phone=8985338755)


if __name__=='__main__':
    app.run(debug=True)
