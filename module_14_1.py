import sqlite3


conection = sqlite3.connect('not_telegram.db')
cursor = conection.cursor()

cursor.execute("""                          
CREATE TABLE IF NOT EXISTS Users_(
id INTEGER PRIMERY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

for i in range(10):
    cursor.execute('INSERT INTO Users_ (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1)*10}', '1000'))

for i in range(1,11,2):
    cursor.execute("UPDATE Users_ SET balance = ? WHERE username = ?", ("500", f"User{i}"))

for i in range(1,11,3):
    cursor.execute("DELETE FROM Users_  WHERE username = ?", (f"User{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users_ WHERE age != ?", ("60",))
users = cursor.fetchall()
for user in users:
    print(user)

conection.commit()
conection.close()