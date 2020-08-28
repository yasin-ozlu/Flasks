from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "Main Page"

@app.route("/search")
def search():
    return "Search Page"
@app.route("/delete/item")
def delete():
    return "Delete item"
@app.route("/delete/<string:id>")
def deleteID(id):
    return "ID:" + id 
    

if __name__ == "__main__":
    app.run(debug = True)