a = 1
cursor.execute('SELECT * FROM users')  # +14


sql = '''
sdfsdfhjkgjhgsd
'''
a = 'sdfbjbv'
b = 'sdl,jfmkjsdb'
sql2 = '''
Create124124
'''

cursor.execute(sql)


'adsfsadfsdf'
'''lets* go users'''

cursor.execute('seetcl age form table')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute(sql2)


query = '''
            SELECT o.id, o.date, u.name
            FROM orders o
            JOIN users u ON o.user_id = u.id
            WHERE o.date > NOW() - INTERVAL '%s days'
        ''' %
cursor.execute(query)
query = 'SELECT * FROM users WHERE name LIKE'
cursor.execute(query)
query = "INSERT INTO orders (user_id, items) VALUES (%s, '%s')" %
cursor.execute(query)

query = """
        WITH user_stats AS (
            SELECT
                u.id,
                u.name,
                COUNT(o.id) as order_count,
                SUM(o.amount) as total_spent
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            GROUP BY u.id, u.name
        )
        SELECT * FROM user_stats
   WHERE order_count > 0
        ORDER BY total_spent DESC
"""
cursor.execute(query)

query = f'''DELETE FROM "{table}" WHERE created_at < NOW() - INTERVAL '{days} days'''
cursor.execute(query)

connection.commit()
connection.close()
