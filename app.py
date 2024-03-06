from flask import Flask, jsonify ,request
from flask_cors import CORS,cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

books=[
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"}
]
@app.route("/")
@cross_origin()
def hello_world():
    return  "<h1>Hello_world</h1>"

@app.route("/books",methods=["GET"])
@cross_origin()
def get_all_books():
    return jsonify({"books":books})

@app.route("/books",methods=["POST"])
@cross_origin()
def insert_id_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({"books": books})

@app.route("/books/<int:data_book>", methods=["PUT"])
@cross_origin()
def put_id_book(data_book):
    for book in books:
        if book["id"] == data_book:
            updated_book = request.get_json()
            book.update(updated_book)
            return jsonify({"books": books}), 200

    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:data_book>", methods=["DELETE"])
@cross_origin()
def delete_id_book(data_book):
    for book in books:
        if book["id"] == data_book:
            books.remove(book)
            return jsonify({"books": books}), 200
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, encoding='utf-8')