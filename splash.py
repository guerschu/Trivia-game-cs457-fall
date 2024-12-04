def home():
    return '''
    __________________________________
    |           Welcome to           |
    |             Trivia!            |
    |________________________________|
    '''

def lobby(user):
    return f'''
    ____________________________________________
    |                                          |
    |     {user} Welcome To The Lobby          |
    |__________________________________________|
    '''

def options():
    return '''
    __________________________________
    |  Choose your trivia category!  |
    |         Type: Animal           |
    |         Type: History          |
    |         Type: Location         |
    |________________________________|
    '''

def youChose(opt):
    return f'''
    __________________________________
    |Great you chose: {opt}          |
    |________________________________|
    '''

def userName():
    return '''
    __________________________________
    |   Please enter your user name  |
    |________________________________|
    '''

def correct():
    return '''
    __________________________________
    |             Correct!           |
    |________________________________|
    '''

def wrong():
    return '''
    __________________________________
    |            Incorrect!          |
    |________________________________|
    '''

def waiting():
    return '''
    _____________________________________
    | Waiting For Other Players To Join |
    |___________________________________|
    '''

def scoreBoard(players):
    
    scoreboard_str = "______________________SCOREBOARD___________________\n"
    for player in players:
        if player != "admin":
            scoreboard_str += f"{player}: {players[player]['GP']}\n"
    scoreboard_str += "___________________________________________________\n"
    return scoreboard_str

def winCondition(players):
    highest_score = 0
    highest_scorer = None
    win_str = "___________________________________________________________\n"
    for player in players:
        if player != "admin" and players[player]['GP'] > highest_score:
            highest_score = players[player]['GP']
            highest_scorer = player
    win_str += f"| {highest_scorer} Wins with a Score of: {highest_score}  |\n"
    win_str +=  "___________________________________________________________\n"
    return win_str

def thanksForPlaying():
    return f'''
    ____________________________________________________
    |                 Thanks For Playing               |
    |__________________________________________________|
    '''

def left(userName):
    return f'''
    ____________________________________________________
    |            {userName} has left the Game          |
    |__________________________________________________|
    '''

def howToAnswer():
    return '''
    _________________________________________________
    |         To Answer Only Put A, B, C            |
    |_______________________________________________|
    '''

# ANIMAL TRIVIA

def animal_question0():
    return '''
    _____________________________________
    |  What Mammal has the Thickest Fur? |
    |           A: Sea Otter            |
    |           B: Moose                |
    |           C: Bear                 |
    |___________________________________|
    '''

# Answer Sea Otter

def animal_question1():
    return '''
    _____________________________________________
    |  What Animal Has The Highest Blood Pressue? |
    |               A: Rabbits                   |
    |               B: Giraffe                   |
    |               C: Cows                      |
    |____________________________________________|
    '''
# Anser Giraffe

def animal_question2():
    return '''
    _____________________________________
    |  What is a group of cats called?    |
    |           A: Clowder               |
    |           B: Murder                |
    |           C: Huddle                |
    |____________________________________|
    '''
# clowder

def animal_question3():
    return '''
    _______________________________________________
    | What mammal has the most powerful bite force? |
    |               A: Hippo                       |
    |               B: Gater                       |
    |               C: Snaping Turtle              |
    |______________________________________________|
    '''
#hippo

def animal_question4():
    return '''
    _________________________________________________________________
    | What of the animals below does not die soon after giving birth? |
    |               A: Octopus                                       |
    |               B: Salmon                                        |
    |               C: Cicadas                                       |
    |________________________________________________________________|
    '''
# Cicadas

def animal_question5():
    return '''
    __________________________________________________
    | What animals have teeth that never stop growing? |
    |               A: gaters                         |
    |               B: rodents                        |
    |               C: sharks                         |
    |_________________________________________________|
    '''

#HISTORY
def history_questions0():
    return '''
    __________________________________
    | When was the Battle of Yorktown? |
    |        A: 1781                  |
    |        B: 1783                  |
    |        C: 1779                  |
    |_________________________________|
    '''
#1781

def history_questions1():
    return '''
    ________________________________________________________________________________________
    | What is not the name of the period of starvation lasting from 1845 to 1852 in Ireland? |
    |                           A: The Irish Potato Famine                                  |
    |                           B: Great Leap Forward                                       |
    |                           C: The Great Hunger                                         |
    |_______________________________________________________________________________________|
    '''
#Great Leap Forward

def history_questions2():
    return '''
    ____________________________________________________
    | What year did Australia stop being a penal colony? |
    |                    A: 1868                        |
    |                    B: 1879                        |
    |                    C: 1867                        |
    |___________________________________________________|
    '''
# 1868

def history_questions3():
    return '''
    _______________________________________________________________
    | How many US vice presidents have gone on to become president? |
    |                        A: 3                                  |
    |                        B: 20                                 |
    |                        C: 15                                 |
    |______________________________________________________________|
    '''
# 15

def history_questions4():
    return '''
    _____________________________________________________
    | Which Greek goddess was the Parthenon dedicated to? |
    |                  A: Athena                         |
    |                  B: Artims                         |
    |                  C: Circe                          |
    |____________________________________________________|
    '''
#Athena

def history_questions5():
    return '''
    _________________________________________________________________________
    | Which of the following men did NOT sign the Declaration of Independence |
    |                      A: Thomas Jefferson                               |
    |                      B: Alexander Hamilton                             |
    |                      C: Benjamin Franklin                              |
    |________________________________________________________________________|
    '''
#Alexander Hamilton

#LOCATION
def location_questions0():
    return '''
    __________________________________________
    | What river is the longest in the world?  |
    |             A: The Nile River           |
    |             B: The Mississipi           |
    |             C: Amason                   |
    |_________________________________________|
    '''
#The Nile River

def location_questions1():
    return '''
    ___________________________________________
    | Which country has the most natural lakes? |
    |               A: China                   |
    |               B: Canada                  |
    |               C: America                 |
    |__________________________________________|
    '''
#canada

def location_questions2():
    return '''
    _________________________________________________
    | What ocean is the largest and deepest on Earth? |
    |              A: The Pacific Ocean              |
    |              B: The Alantic Ocean              |
    |              C: The Indian Ocean               |
    |________________________________________________|
    '''
#The Pacific Ocean

def location_questions3():
    return '''
    ______________________________________________
    | What is the only continent without any bees? |
    |            A:  Antartica                    |
    |            B:  Australia                    |
    |            C:  South America                |
    |_____________________________________________|
    '''
    #A

def location_questions4():
    return '''
    _______________________________________________________________________
    | What is the name of the highest uninterrupted waterfall in the world? |
    |                      A: Niagra Falls                                 |
    |                      B: Angel Falls                                  |
    |                      C: Gravity Falls                                |
    |______________________________________________________________________|
    '''
    #B

def location_questions5():
    return '''
    _________________________________________________
    | Where is the largest volcano on Earth located? |
    |             A: Pompeii                        |
    |             B: America/Canada                 |
    |             C: Hawaii                         |
    |_______________________________________________|
    '''
    #C
