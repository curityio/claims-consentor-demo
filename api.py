import json
import re

from flask import Flask, jsonify, abort
from flask import request
from flask import g
from oauth.oauth_filter import OAuthFilter

app = Flask(__name__)
_refOauth = OAuthFilter(verify_ssl=False)
transactions=[]


@app.route("/", methods=["PUT", "POST"])
def create_product():
    data = request.get_json()
    transaction_id = len(transactions)

    transactions.append(dict(currency=data["currency"], amount=data["amount"], product=data["product"]))

    return jsonify(dict(transactionId=transaction_id))


@app.route('/', methods=["GET"])
def lookup_product():
    return jsonify(_lookup_product(request.args.get('transactionId', default=0, type=int)))


def _lookup_product(transaction_id):
    if 0 <= transaction_id < len(transactions):
        result = transactions[transaction_id]
    else:
        result = dict(product="Unknown", amount=0, currency="Unknown")

    return result


@app.route('/<int:transaction_id>', methods=["GET"])
@_refOauth.protect(scopes=["transactionId"], isPrefix=True)
def get_product(transaction_id):
    authorized_transaction_id = -1

    for scope in re.split("\\s+", g.scope):
        if scope.startswith("transactionId"):
            authorized_transaction_id = int(scope.replace("transactionId", ""))
            break

    if authorized_transaction_id == transaction_id:
        data = _lookup_product(transaction_id)

        return "Thank you for purchasing a %s for %s %s" % (data["product"], data["amount"], data["currency"])
    else:
        abort(401)


_refOauth.configure_with_opaque("https://localhost:8443/introspection", "test_gateway_client", "changeme")

if __name__ == '__main__':
    app.run('0.0.0.0', debug=False, port=8080)
