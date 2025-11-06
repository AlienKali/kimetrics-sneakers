import psycopg2

#Establecer una conexion
conn = psycopg2.connect(
    dbname="bdkimetrics",
    user="postgres",
    password="kimetrics123",
    host="awsrds-kimetrics.c9gciya28sq3.us-east-2.rds.amazonaws.com", # o la dirección de tu servidor
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT version();")

db_version = cur.fetchone()
print(db_version)

conn.commit()


cur.close()
conn.close()

