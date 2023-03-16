from flask import Flask, render_template, request
from creature import Creature, Ability

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/den")
def den():
    all_creatures = Creature.objects()
    return render_template("den.html",
                           all_creatures=all_creatures)


@app.route("/creature")
def creature():
    name = request.args.get("name")

    creature = Creature.objects.get(name=name)


    return render_template("creatures.html", name=name, creature=creature)




if __name__ == '__main__':
    app.run(debug=True)


