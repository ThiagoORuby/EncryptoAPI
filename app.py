from flask import Flask, render_template, url_for, redirect, request, jsonify, flash, make_response
from rsa_crypto import RSA

def create_app():

    app = Flask(__name__)

    # Instancing a rsa
    rsa = RSA()

    @app.route('/generate_key', methods=['POST'])
    def generate_key():
        values = request.json
        n, e = RSA().generatePublicKey(values['p'], values['q'], values['e'])
        resp = {"n" : n, "e" : e}
        return make_response(
            jsonify(resp)
        )
    
    @app.route("/encrypting", methods=['POST'])
    def encrypting_message():
        values = request.json
        crypted = RSA().encrypting(values['message'], values['n'], values['e'])
        resp = {"crypted" : crypted}
        return make_response(
            jsonify(resp)
        )

    @app.route("/decrypting", methods=['POST'])
    def decrypting_message():
        values = request.json
        message = RSA().decrypting(values['crypted'], values['p'], values['q'], values['e'])
        resp = {"message" : message}
        return make_response(
            jsonify(resp)
        )

    return app



