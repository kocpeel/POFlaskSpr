from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)



#     Model użytkownika dodawany w aplikacji powinien być zgodny z następującym JSON:
# {
#     "firstName": str,
#     "lastName": str,
#     "birthYear": int,
#     "group": str, // jedynymi poprawnymi wartościami są napisy: "user", "premium", "admin"
   
# }

# Model użytkownika zwracany z aplikacji powinien być zgodny z następującym JSON:
# {
#     "id": int,
#     "firstName": str,
#     "lastName": str,
#     "age": int,
#     "group": str, // jedynymi poprawnymi wartościami są napisy: "user", "premium", "admin"
   
# }

users = {}
