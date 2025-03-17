import psycopg2
import json

# Database connection details
DB_CONFIG = {
    "host": "localhost",
    "database": "nexirift",
    "user": "username",
    "password": "password",
}

# Connect to PostgreSQL and fetch posts
try:
    print("Connecting to database...")
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    print("Fetching posts...")
    cur.execute("SELECT id, content FROM post")  # Modify table/column names as needed
    posts = cur.fetchall()

    print(f"Retrieved {len(posts)} posts.")
    
    # Convert to JSON format
    post_data = [
        {"post_id": post_id, "post_text": content}
        for post_id, content in posts
    ]

    # Convert to JSON string
    input_json = json.dumps(post_data, ensure_ascii=False, indent=4)

    print("Generated JSON input:")
    print(input_json)  # For debugging
    
    # Save JSON to file (optional)
    with open("posts.json", "w", encoding="utf-8") as json_file:
        json.dump(post_data, json_file, ensure_ascii=False, indent=4)

    print("Saved posts to posts.json")

    # Close database connection
    cur.close()
    conn.close()
    print("Database connection closed.")

except Exception as e:
    print(f"Error: {e}")
