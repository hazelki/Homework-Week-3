from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


    
@app.route("/application-form.html", method=["POST"])
def application_f():

    first_name = request.form.get("first")
    last_name = request.form.get("last")
    salary = request.form.get("salary")
    job = request.form.get("job")

    return render_template("application-response.html",
                            first_name=first_name,
                            last_name=last_name,
                            salary=salary,
                            job=job,)





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

