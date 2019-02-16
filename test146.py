# http://tinyurl.com/gldykam

pop = []    #pop music list
jpop = []   #jpop list

def collect_songs():
    song = "input songs: "
    ask = "Please input p or j. quit q: "

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.append(j)

        else:
            print("value is not correct")

    print("pop songs: ", pop)
    print("jpop songs ", jpop)

collect_songs()
