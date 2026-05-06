# -----------------------------------
# This has functions for sending JS via button click
# -----------------------------------


from flask import Blueprint, jsonify, render_template, request

jsa_bp = Blueprint('jsa', __name__)

# Standard Route Entry Point


@jsa_bp.route('/jsa1')
def jsa1():
    return render_template('jsa.html')

# JS Wil go in here


@jsa_bp.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}!')

    return jsonify({'message': 'Data fucked now in file.txt'})
