from flask import Flask, request, jsonify, render_template, url_for
import sqlite3 as sqlite
import sys
import os
app = Flask(__name__,template_folder='templates')



def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    

##This loads the index page
@app.route('/', methods=['GET'])
def home():
    ##Connect to the OnlyCompDB and get the browse pop fields
    conn = sqlite.connect('../data/OnlyComp.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_data = cur.execute("SELECT * FROM Address;").fetchall()
    #jsonify(all_data)
    ################################
    ##Testing Index

    content = all_data
    y=1
    for x in content:
        
        x["index"] = y
        y+=1
     
    #return render_template('test_temp.html', content=content)



    ##return stadared index
    return render_template('index.html', content=content)



@app.route('/browse', methods=['GET'])
def browse():

    return render_template('browse.html')

@app.route('/search', methods=['GET'])
def search(address):
    conn = sqlite.connect('../data/AddressToDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute("SELECT * FROM Address WHERE street_address=%s" %str(address)).fetchall()
    return jsonify(all_books)



@app.errorhandler(404)
def page_not_found(e):
    return "render_template('404.html'), 404"

# A route to return all of the available entries in our catalog.
@app.route('/test_db', methods=['GET'])
def api_all():
    conn = sqlite.connect('../data/OnlyComp.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_data = cur.execute("SELECT LAT ,LNG FROM Address;").fetchall()
    return jsonify(all_data)

@app.route("/api/v1/resources/books", methods=['GET'])
def api_filter():
    query_parameters = request.args
    
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    to_filter = []
    query = build_select_books_query(author, id, published, to_filter)
    conn = sqlite.connect('../data/AddressToDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    
    results = cur.execute(query, to_filter).fetchall()
    
    return jsonify(results)

@app.route("/api/v1/resources/books/json", methods=['GET'])
def api_filter_json():
    books = request.get_json()
    results = [] 
    for book in books['books']:
        to_filter = []

        id = book['id']
        published = book['published']
        author = book['author']
        query = build_select_books_query(author, id, published, to_filter)

        conn = sqlite.connect('../data/books.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results.append(cur.execute(query, to_filter).fetchall()[0])

    return jsonify(results)


def build_select_books_query(author, id, published, to_filter):
    query = "SELECT * FROM Address"
    return query


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

