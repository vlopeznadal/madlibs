"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


@app.route("/game")
def show_madlib_form():
    
    response = request.args.get("response")

    if response == "yes":
        return render_template("game.html")
    elif response == "no":
        return render_template("goodbye.html")

@app.route("/madlib", methods=['POST'])
def show_madlib():

    person = request.form.get("person")
    color = request.form.get("color")
    noun1 = request.form.get("noun1")
    noun2 = request.form.get("noun2")
    noun3 = request.form.get("noun3")
    adjective1 = request.form.get("adjective1")
    adjective2 = request.form.get("adjective2")
    adjective3 = request.form.get("adjective3")
    animal = request.form.get("animal")
    food = request.form.get("food")
    verb1 = request.form.get("verb1")
    verb2 = request.form.get("verb2")
    verb3 = request.form.get("verb3")
    pasttenseverb1 = request.form.get("pasttenseverb1")
    pasttenseverb2 = request.form.get("pasttenseverb2")
    pasttenseverb3 = request.form.get("pasttenseverb3")
    place = request.form.get("place")
    vehicle = request.form.get("vehicle")

    temps = ["madlib.html", "madlib-2.html", "madlib-3.html"]
    rand_templates = choice(temps)

    return render_template(rand_templates, person=person, color=color, noun1=noun1, noun2=noun2, noun3=noun3, adjective1=adjective1, adjective2=adjective2, adjective3=adjective3, animal=animal, food=food, verb1=verb1, verb2=verb2, verb3=verb3, pasttenseverb1=pasttenseverb1, pasttenseverb2=pasttenseverb2, pasttenseverb3=pasttenseverb3,place=place, vehicle=vehicle)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
