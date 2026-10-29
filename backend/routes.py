import os, json
from pathlib import Path
from urllib.parse import quote_plus
from flask import jsonify, request
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from . import app

host=os.environ.get('MONGODB_SERVICE','127.0.0.1:27018')
user,password=os.environ.get('MONGODB_USERNAME'),os.environ.get('MONGODB_PASSWORD')
auth=f'{quote_plus(user)}:{quote_plus(password)}@' if user and password else ''
client=MongoClient(os.environ.get('MONGODB_URI',f'mongodb://{auth}{host}'),serverSelectionTimeoutMS=5000)
db=client.songs
db.songs.create_index('id',unique=True)
if db.songs.count_documents({})==0:
    db.songs.insert_many(json.loads((Path(__file__).parent/'data/songs.json').read_text()))

def clean(song):
    return {k:v for k,v in song.items() if k!='_id'}

@app.get('/health')
def health():
    client.admin.command('ping')
    return jsonify(status='OK')

@app.get('/count')
def count():
    return jsonify(count=db.songs.count_documents({}))

@app.get('/song')
def songs():
    return jsonify([clean(s) for s in db.songs.find({})])

@app.get('/song/<int:id>')
def get_song(id):
    s=db.songs.find_one({'id':id})
    return (jsonify(clean(s)),200) if s else (jsonify(message='song with id not found'),404)

@app.post('/song')
def post_song():
    s=request.get_json(silent=True)
    if not isinstance(s,dict) or type(s.get('id')) is not int or not all(isinstance(s.get(k),str) for k in ('title','lyrics')):
        return jsonify(message='id, title and lyrics required'),400
    s={k:s[k] for k in ('id','title','lyrics')}
    try: db.songs.insert_one(s)
    except DuplicateKeyError: return jsonify(message='song already exists'),409
    return jsonify(clean(s)),201

@app.put('/song/<int:id>')
def put_song(id):
    s=request.get_json(silent=True)
    if not isinstance(s,dict) or not all(isinstance(s.get(k),str) for k in ('title','lyrics')):
        return jsonify(message='title and lyrics required'),400
    s={'id':id,'title':s['title'],'lyrics':s['lyrics']}
    if not db.songs.replace_one({'id':id},s).matched_count:
        return jsonify(message='song with id not found'),404
    return jsonify(s),201

@app.delete('/song/<int:id>')
def delete_song(id):
    if not db.songs.delete_one({'id':id}).deleted_count:
        return jsonify(message='song with id not found'),404
    return '',204
