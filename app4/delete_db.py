import os
db_path = 'instance/data.sqlite3'
if os.path.exists(db_path):
    os.remove(db_path)
    print('Database deleted')
else:
    print('Database not found')
