def home():
    print('''__________________________________''')
    print('''|           Welcome to           |''')
    print('''|             Trivia!            |''')
    print('''|________________________________|''')

def options():
    print('''__________________________________''')
    print('''|  Choose your trivia category!  |''')
    print('''|         Type: Animal           |''')
    print('''|         Type: History          |''')
    print('''|         Type: Locations        |''')
    print('''|________________________________|''')

def youChose(opt):
    print('''__________________________________''')
    print(f'''|Great you chose: {opt}        |''')
    print('''|________________________________|''')

def userName():
    print('''__________________________________''')
    print('''|   Please enter your user name  |''')
    print('''|________________________________|''')

def correct():
    print('''__________________________________''')
    print('''|             Correct!           |''')
    print('''|________________________________|''')
    
def wrong():
    print('''__________________________________''')
    print('''|            Incorrect!          |''')
    print('''|________________________________|''')

# ANIMAL TRIVIA

def animal_question0():
    print('''_____________________________________''')
    print(f"|  What Mammal has the Thickest Fur? |")
    print('''|           A: Sea Otter            |''')
    print('''|           B: Moose                |''')
    print('''|           C: Bear                 |''')
    print('''|___________________________________|''')

    # Answer Sea Otter

def animal_question1():
    print('''_____________________________________________''')
    print(f"|  What Animal Has The Highest Blood Pressue? |")
    print('''|               A: Rabbits                   |''')
    print('''|               B: Giraffe                   |''')
    print('''|               C: Cows                      |''')
    print('''|____________________________________________|''')
# Anser Giraffe

def animal_question2():
    print('''_____________________________________''')
    print(f"|  What is a group of cats called?    |")
    print('''|           A: Clowder               |''')
    print('''|           B: Murder                |''')
    print('''|           C: Huddle                |''')
    print('''|____________________________________|''')
    # clowder

def animal_question3():
    print('''_______________________________________________''')
    print(f"| What mammal has the most powerful bite force? |")
    print('''|               A: Hippo                       |''')
    print('''|               B: Gater                       |''')
    print('''|               C: Snaping Turtle              |''')
    print('''|______________________________________________|''')
    #hippo

def animal_question4():
    print('''_________________________________________________________________''')
    print(f"| What of the animals below does not die soon after giving birth? |")
    print('''|               A: Octopus                                       |''')
    print('''|               B: Salmon                                        |''')
    print('''|               C: Cicadas                                       |''')
    print('''|________________________________________________________________|''')
# Cicadas

def animal_question5():
    print('''__________________________________________________''')
    print(f"| What animals have teeth that never stop growing? |")
    print('''|               A: gaters                         |''')
    print('''|               B: rodents                        |''')
    print('''|               C: sharks                         |''')
    print('''|_________________________________________________|''')

#HISTORY
def history_questions0():
    print('''__________________________________''')
    print(f"| When was the Battle of Yorktown? |")
    print('''|        A: 1781                  |''')
    print('''|        B: 1783                  |''')
    print('''|        C: 1779                  |''')
    print('''|_________________________________|''')
    #1781

def history_questions1():
    print('''________________________________________________________________________________________''')
    print(f"| What is not the name of the period of starvation lasting from 1845 to 1852 in Ireland? |")
    print('''|                           A: The Irish Potato Famine                                  |''')
    print('''|                           B: Great Leap Forward                                       |''')
    print('''|                           C: The Great Hunger                                         |''')
    print('''|_______________________________________________________________________________________|''')
    #Great Leap Forward

def history_questions2():
    print('''____________________________________________________''')
    print(f"| What year did Australia stop being a penal colony? |")
    print('''|                    A: 1868                        |''')
    print('''|                    B: 1879                        |''')
    print('''|                    C: 1867                        |''')
    print('''|___________________________________________________|''')
    # 1868

def history_questions3():
    print('''_______________________________________________________________''')
    print(f"| How many US vice presidents have gone on to become president? |")
    print('''|                        A: 3                                  |''')
    print('''|                        B: 20                                 |''')
    print('''|                        C: 15                                 |''')
    print('''|______________________________________________________________|''')
# 15

def history_questions4():
    print('''_____________________________________________________''')
    print(f"| Which Greek goddess was the Parthenon dedicated to? |")
    print('''|                  A: Athena                         |''')
    print('''|                  B: Artims                         |''')
    print('''|                  C: Circe                          |''')
    print('''|____________________________________________________|''')
    #Athena

def history_questions5():
    print('''_________________________________________________________________________''')
    print(f"| Which of the following men did NOT sign the Declaration of Independence |")
    print('''|                      A: Thomas Jefferson                               |''')
    print('''|                      B: Alexander Hamilton                             |''')
    print('''|                      C: Benjamin Franklin                              |''')
    print('''|________________________________________________________________________|''')
    #Alexander Hamilton

#LOCATION
def location_questions0():
    print('''__________________________________________''')
    print(f"| What river is the longest in the world?  |")
    print('''|             A: The Nile River           |''')
    print('''|             B: The Mississipi           |''')
    print('''|             C: Amason                   |''')
    print('''|_________________________________________|''')
    #The Nile River

def location_questions1():
    print('''___________________________________________''')
    print(f"| Which country has the most natural lakes? |")
    print('''|               A: China                   |''')
    print('''|               B: Canada                  |''')
    print('''|               C: America                 |''')
    print('''|__________________________________________|''')
    #canada

def location_questions2():
    print('''_________________________________________________''')
    print(f"| What ocean is the largest and deepest on Earth? |")
    print('''|              A: The Pacific Ocean              |''')
    print('''|              B: The Alantic Ocean              |''')
    print('''|              C: The Indian Ocean               |''')
    print('''|________________________________________________|''')
#The Pacific Ocean

def location_questions3():
    print('''______________________________________________''')
    print(f"| What is the only continent without any bees? |")
    print('''|            A:  Antartica                    |''')
    print('''|            B:  Australia                    |''')
    print('''|            C:  South America                |''')
    print('''|_____________________________________________|''')

def location_questions4():
    print('''_______________________________________________________________________''')
    print(f"| What is the name of the highest uninterrupted waterfall in the world? |")
    print('''|                      A: Niagra Falls                                 |''')
    print('''|                      B: Angel Falls                                  |''')
    print('''|                      C: Gravity Falls                                |''')
    print('''|______________________________________________________________________|''')

def location_questions5():
    print('''_________________________________________________''')
    print(f"| Where is the largest volcano on Earth located? |")
    print('''|             A: Pompeii                        |''')
    print('''|             B: America/Canada                 |''')
    print('''|             C: Hawaii                         |''')
    print('''|_______________________________________________|''')

