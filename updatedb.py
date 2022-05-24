import shelve

db = shelve.open('devicedb')

for key in sorted(db):
    print(key, '\=>', db[key])

fivpe016 = db['fivpe016']
fivpe016.RiseIsis(.10)
db['fivpe016'] = fivpe016
db.close
