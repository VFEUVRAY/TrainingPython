languages = {
    'Python' : 'Guido van Rossum',
    'Ruby' : 'Yukihiro Matsumoto',
    'PHP' : 'Rasmus Lerdorf',
}

def kata01():
    for key, value in languages.items():
        print (key + " was created by " + value)

kata01()