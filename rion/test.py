from rion import db

db.create_database("rion")
db.create_table("rion", "package", "name text, version text")
db.input_value("rion", "package", "('Test', 'v1.0')")
db.input_value("rion", "package", "('Tasdasfaasadd', 'v2.0')")
db.list_table("rion", "package", "name")
