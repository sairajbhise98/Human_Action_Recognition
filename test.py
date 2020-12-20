from flask import Flask ,render_template
app = Flask(__name__)
answer = ''
@app.route('/', methods=['GET','POST'])
def index():
	answer = ''
	return render_template('index.html',answer=answer)

if __name__=='__main__':
	app.run(debug=True)