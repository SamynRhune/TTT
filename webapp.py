from flask import Flask, request, jsonify, render_template
from flask_table import Table, Col
from markupsafe import Markup
from backend.game import game

game = game()

app = Flask(__name__)

def enumerate_list(lst):
    return list(enumerate(lst))

@app.template_filter('enumerate')
def jinja2_enumerate(lst):
    return enumerate_list(lst)


@app.route("/")
def index():
    # Create some items for the table
    items = game.get_board_2d()
    # Return the table's HTML and buttons
    return render_template('index.html',data=items)

@app.route('/player_move', methods=['POST'])
def player_move():
    data = request.get_json()  # Ontvang JSON-data van het verzoek
    index = data.get('index')
    sign = data.get('sign')
    

    # Roep de Python-functie aan met de ontvangen parameters
    result = game.move(sign,index)


    return jsonify({'result': result})

@app.route('/ai_move', methods=['POST'])
def ai_move():
    data = request.get_json()  # Ontvang JSON-data van het verzoek
    ai_sign = data.get('ai_sign')
    player_sign = data.get('player_sign')
    

    # Roep de Python-functie aan met de ontvangen parameters
    result = game.ai_move(ai_sign,player_sign)


    return jsonify({'result': result})

@app.route('/get_board', methods=['POST'])
def get_board():

    # Roep de Python-functie aan met de ontvangen parameters
    result = game.get_board().tolist()
    print(result)
    return jsonify({"result" :result})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)