# http://tinyurl.com/gnjvep7

songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"
         }

n = input("Please input value:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("NOT found")
