from flask import Flask, render_template

from controllers.makes_controller import makes_blueprint
from controllers.cameras__controller import cameras_blueprint

app = Flask(__name__)

app.register_blueprint(makes_blueprint)
app.register_blueprint(cameras_blueprint)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)