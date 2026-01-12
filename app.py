from flask import Flask, render_template

app = Flask(__name__)

@app.route(rule="/")
def get_homepage():
    return render_template(template_name_or_list="home.html")

# @app.route(rule="/")
def route_not_found():
    return "<p>Sorry, route not found</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
