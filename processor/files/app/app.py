from flask import Flask, request, jsonify
import redis
import psycopg2
from bs4 import BeautifulSoup
import os

app = Flask(__name__)


# Connect to Redis
r = redis.Redis(
    host=os.environ["REDIS_HOST"],
    port=6379,
    password=os.environ["REDIS_PASSWORD"],
    decode_responses=True
)

# Connect to Postgres
conn = psycopg2.connect(
    dbname=os.environ["POSTGRES_DB"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.getenv("DB_HOST", "db"),
    port=5432
)
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS html_titles (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL
    );
""")
conn.commit()


@app.route('/processor', methods=['POST'])
def parse():
    # Read raw HTML from request body
    html = request.data.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else 'No title'

    # Store in Redis and Postgres
    r.set('last_title', title)
    cur.execute("INSERT INTO html_titles (title) VALUES (%s)", (title,))
    conn.commit()

    return jsonify({"stored_title": title})
