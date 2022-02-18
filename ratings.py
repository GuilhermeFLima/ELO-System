from ELO import update

# Below is the list of students in the club:
students = [
    'Anna',
    'Bob',
    'Charlie',
            ]

# The dictionary of ratings and number of games played by student. We start
# each student with an ELO of 1000 and 0 played games.
ELOratings = {s: (1000, 0) for s in students}

# Here is the list of games played, according to the following format:
# triples = (white player, black player, winner), winner is 'black'/'white'/'draw'.
games = [
        ('Anna', 'Bob', 'white'),
        ('Bob', 'Charlie', 'black'),
        ('Charlie', 'Anna', 'draw'),
        ]

# Loop that updates ELOs based on the games played.
for (whiteplayer, blackplayer, winner) in games:
    whiterating = ELOratings[whiteplayer][0]
    blackrating = ELOratings[blackplayer][0]
    whitenew, blacknew = update(whiterating, blackrating, winner)
    n = ELOratings[whiteplayer][1]
    m = ELOratings[blackplayer][1]
    ELOratings[whiteplayer] = (whitenew, n+1)
    ELOratings[blackplayer] = (blacknew, m+1)

# List of pairs (student, ELO), with ELOs computed from
# the list of games.
standings = [(s, ELOratings[s]) for s in students]

# getting the rankings based on ELO scores.
ranking = reversed(sorted(standings, key=lambda x: x[1][0]))

# Printing the rankings with ELOs and number of games played.
print("\n")
for (i, p) in enumerate(ranking):
    place = i + 1
    player = p[0]
    elorating = '{0:.0f}'.format(p[1][0])
    numberofgames = p[1][1]
    print('{:2}. {:>12}: {:>4}  ({})'.format(place, player, elorating, numberofgames))

