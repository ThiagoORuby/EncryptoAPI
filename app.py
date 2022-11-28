from flask import Flask, render_template, url_for, redirect, request, jsonify, flash, make_response
from rsa_crypto import RSA
import re

def create_app():

    app = Flask(__name__)

    # Instancing a rsa
    rsa = RSA()

    @app.route('/generate-page', methods=['GET', 'POST'])
    def generate_page():
        keys = ''
        if request.method == 'POST':
            p = request.form['p']
            q = request.form['q']
            e = request.form['ege']
            #print(values)
            try:
                keys = RSA().generatePublicKey(int(p), int(q), int(e))
            except:
                keys = ("Certify that P and Q are prime numbers", "Check if E is coprime with (p - 1) x (q - 1)")
            print(len(keys))
        return render_template('generate.html', keys = keys)

    @app.route('/encrypting-page', methods=['GET', 'POST'])
    def encrypting_page():
        crypted = ''
        if request.method == 'POST':
            message = request.form['message']
            message = re.sub('[^a-zA-z ]', '', message)
            print(message)
            n = request.form['n']
            e = request.form['eenc']
            #print(values)
            try:
                crypted = RSA().encrypting(message, int(n), int(e))
            except:
                crypted = "There are something wrong with your keys"
            print(crypted)
        return render_template('encrypting.html', message = crypted)
    
    @app.route('/decrypting-page', methods=['GET', 'POST'])
    def decrypting_page():
        decrypted = ''
        if request.method == 'POST':
            crypted = request.form['crypted']
            crypted = re.sub('[^0-9 ]', '', crypted)
            p = request.form['p']
            q = request.form['q']
            e = request.form['edec']
            #print(values)
            try:
                decrypted = RSA().decrypting(crypted, int(p), int(q), int(e))
            except:
                crypted = "There are something wrong with your keys or crypted message"
            print(decrypted)
        return render_template('decrypting.html', message = decrypted)

    @app.route('/generate_key', methods=['POST'])
    def generate_key():
        values = request.json
        n, e = RSA().generatePublicKey(int(values['p']), int(values['q']), int(values['e']))
        resp = {"n" : str(n), "e" : str(e)}
        return make_response(
            jsonify(resp)
        )
    
    @app.route("/encrypting", methods=['POST'])
    def encrypting_message():
        values = request.json
        crypted = RSA().encrypting(values['message'], int(values['n']), int(values['e']))
        resp = {"crypted" : crypted}
        return make_response(
            jsonify(resp)
        )

    @app.route("/decrypting", methods=['POST'])
    def decrypting_message():
        values = request.json
        message = RSA().decrypting(values['crypted'], int(values['p']), int(values['q']), int(values['e']))
        resp = {"message" : message}
        return make_response(
            jsonify(resp)
        )

    return app



