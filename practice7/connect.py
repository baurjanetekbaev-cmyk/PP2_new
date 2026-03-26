import psycopg2
import config 
def get():
    conn = psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    ) 
    return conn