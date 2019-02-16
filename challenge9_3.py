import csv

movies = [["topgun", "risky business", "minorit report"], ["titanic", "the revenant", "inseptipn"], ["trainigday", "man on fire", "flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
