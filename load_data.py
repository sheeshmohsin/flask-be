import psycopg2
import random
import uuid


hostname = "dumbo.db.elephantsql.com"
port = 5432
username = "dkpfiyqb"
password = "INVgmukmKj85S0WWWn-KCkunxNMViXKF"
database = "dkpfiyqb"

conn = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname,
    port = port
)

cursor = conn.cursor()

uid = 1008
for y in range(0, 1003):
    query = "insert into poweruser (id, username, password, user_type) values "
    for x in range(1, 999):
        substring = "('%d', '%s', '%s', '%s')," % (uid, str(uuid.uuid4()), str(uuid.uuid4()), random.randint(1, 4))
        query += substring
        uid += 1

    query = query.rstrip(',')
    query += ';'

    cursor.execute(query)
    conn.commit()

conn.close()
