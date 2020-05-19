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

# c.execute("INSERT INTO blog_post VALUES (2, 'Alfddff', 'Aedsdfg', 'Pista Jeno', '2019-25-21', 'sidjifgdjgidfjg') ")
# c.execute("SELECT id, title, subtitle, author, date_posted, content FROM blog_post ORDER BY date_posted DESC")
print(c.fetchall())
conn.commit()
conn.close()