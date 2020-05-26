import sqlite3

conn = sqlite3.connect('blog.db')
# c = conn.cursor()
c.execute("""CREATE TABLE blog_post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title text NOT NULL,
                subtitle text NOT NULL,
                author text NOT NULL,
                date_posted text NOT NULL,
                content text NOT NULL
                )""")

print(c.fetchall())
conn.commit()
conn.close()