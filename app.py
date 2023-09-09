from flask import Flask

app = Flask(__name__)

import sqlite3


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return

@app.route('/cart/order', methods=['POST'])
def cart_order():
    return

@app.route('/cart/add', methods=['POST'])
def cart_add():
    return

@app.route('/user', methods=['GET', 'POST', 'DELETE'])
def user():
    return

@app.route('/user/register', methods=['POST'])
def user_register():
    return

@app.route('/user/sign_in', methods=['POST'])
def user_sign_in():
    return

@app.route('/user/logout', methods=['GET', 'POST'])
def user_logout():
    return

@app.route('/user/restore', methods=['POST'])
def user_restore():
    return

@app.route('/user/history', methods=['GET'])
def user_history():
    return

@app.route('/user/history/<id>', methods=['GET'])
def user_history_by_id():
    return

@app.route('/user/address', methods=['GET', 'POST'])
def user_address():
    return

@app.route('/user/address/<id>', methods=['GET', 'PUT'])
def user_address_by_id():
    return

@app.route('/menu', methods=['GET'])
def menu():
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute("SELECT * FROM Dishes")
    RESULTS = res.fetchall()
    return RESULTS

@app.route('/menu/<catname>', methods=['GET'])
def menu_catname():
    return

@app.route('/menu/<catname>/dish', methods=['GET'])
def menu_catname_dish():
    return

@app.route('/menu/<catname>/dish/review', methods=['GET'])
def menu_catname_dish():
    return

@app.route('/menu/search', methods=['GET'])
def menu_search():
    return

if __name__ == '__main__':
    app.run()