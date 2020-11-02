import sqlite3
conn = sqlite3.connect('email.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split('@')[1]
    index = pieces.find('@') + 1
    org = pieces[index:]
    print("org is ", org)
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (org,))
    row = cur.fetchone()
    # fetchone() => This method retrieves the next row of a query result set and returns a single sequence,
    # or None if no more rows are available.
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
print("select all from db")
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC '


for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
#This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e.domain name of the email address) using a database with the following schema to maintain the counts.
