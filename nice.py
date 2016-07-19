from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

RUDENESS = ['big fat stupid jerk', 'slob', 'snobby', 'lazy', 'cruel', 'rude', 'stinky']

@app.route('/')
def start_here():
    """Home page."""

    return """
           Hi! This is the home page.
           Go to <a href="/hello">hello</a>.
           """


def make_options(list_of_options):
    option_parts = ['<option value="%s">%s</option>' % (choice, choice)
                          for choice in list_of_options]
    options = " ".join(option_parts)
    return options


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    compliments = make_options(AWESOMENESS)
    insults = make_options(RUDENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <label for="field-compliment">Choose a compliment:</label>
          <select name="compliment" id="field-compliment">
            %s
          </select>
          <input type="submit">
        </form>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <label for="field-insult">Choose an insult:</label>
          <select name="insult" id="field-insult">
            %s
          </select>
          <input type="submit">
        </form>
      </body>
    </html>
    """ % (compliments, insults)

@app.route('/diss')
def diss_person():
    """Get user name and diss them """

    player = request.args.get("person")
    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
