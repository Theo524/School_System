from SchoolSystem import school_system
from MovieManager import movies
# code
choice = input('school system or movie manager?')

school = ['School system', '1', 'school']
movie = ['movie manager', '2', 'movie ']

if choice in school:
    school_system.loginMenu()

if choice in movie:
    movies.loginMenu()
