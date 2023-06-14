from tinydb import TinyDB
from tinydb.table import Document


db = TinyDB('db.json', indent=4)

users = db.table(name='users')

# print(db.tables())

doc = Document(
    value={"name": "Ali", "age": 19},
    doc_id=4
)

users.insert(doc)