from flask import Flask, jsonify
import redis
import os
import psycopg2

app = Flask(__name__)

# Redis config
redis_host = os.environ["REDIS_HOST"]
redis_password = os.environ["REDIS_PASSWORD"]
r = redis.Redis(host=redis_host, port=6379, password=redis_password)

# Postgres config
pg_conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "db"),
    dbname=os.environ["POSTGRES_DB"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"]
)

@app.route("/")
def index():
    r.set("hello", "world")
    return jsonify({
        "message": r.get("hello").decode()
    })

@app.route("/db")
def db_test():
    with pg_conn.cursor() as cur:
        cur.execute("SELECT current_date;")
        result = cur.fetchone()
    return jsonify({"date_from_db": result[0].isoformat()})
