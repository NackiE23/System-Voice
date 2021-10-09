import mysql.connector

mydb = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "1111",
  database = "system_voice_db"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE users (user_id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(25) NOT NULL, login VARCHAR(25) NOT NULL, passwd VARCHAR(25) NOT NULL, is_voted BIT DEFAULT 0)")
# mycursor.execute("CREATE TABLE candidates (candidate_id INT PRIMARY KEY AUTO_INCREMENT, candidate_name VARCHAR(25) NOT NULL, number_of_votes INT DEFAULT 0)")
# mycursor.execute("INSERT INTO candidates (candidate_name) VALUES ('Peter')")
# mycursor.execute("INSERT INTO candidates (candidate_name) VALUES ('Amy')")
# mycursor.execute("INSERT INTO candidates (candidate_name) VALUES ('Hannah')")
# mycursor.execute("INSERT INTO candidates (candidate_name) VALUES ('Michael')")
# mycursor.execute("INSERT INTO candidates (candidate_name) VALUES ('Sandy')")
# sql = "INSERT INTO users (username, login, passwd) VALUES (%s, %s, %s)"
# val = [
#   ('Igor', '1111', '1111'),
#   ('Lesha', '1112', '1112'),
#   ('Dima', '1122', '1122'),
#   ('Stas', '1222', '1222'),
#   ('Tolik', '2222', '2222'),
#   ('Betty', '2223', '2223'),
#   ('Richard', '2233', '2233'),
#   ('Susan', '2333', '2333')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()


