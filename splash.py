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
    print('''|________________________________|''')
    print(f'''|Great you chose: {opt}        |''')
    print('''|________________________________|''')


def correct():
    print('''__________________________________''')
    print('''|             Correct!           |''')
    print('''|________________________________|''')
    
def wrong():
    print('''__________________________________''')
    print('''|            Incorrect!          |''')
    print('''|________________________________|''')

def question(question):
    print('''__________________________________''')
    print(f"|            {question}          |")
    print('''|________________________________|''')

