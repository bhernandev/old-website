from flask import Flask
from flask import render_template

from .bean.views import bean

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(bean, url_prefix='/games/bean')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
