SECRET_INIT = ('mike', 'some-password', 'some-secret-key')
"""tuple containing username, password and secret session key"""


class Language:
    def __init__(self, name, flag, level):
        self.name = name
        self.flag = flag
        self.level = level


# TODO move into a db table
class MY:
    NAME = 'Tanja Savanin'
    EMAIL = 'savanin.tanja@gmail.com'
    TITLES = (
        ('MSc Corporate Management and Economics', 'http://google.com'),
        ('BSc Business Administration', 'http://google.com'),
    )
    DESCRIPTION = (
        'This is my personal online CV, designed with '
        'Python HTML, CSS and JavaScript.')
    PHONE = '+12 345 6789 1011'
    ADDRESS = [
        'Fallenbrunnen 19',
        'Zimmer 123',
        'Friedrichshafen',
        'Germany',
    ]
    SKILLS = [
        'HTML',
        'CSS',
        'JavaScript',
        'Ruby',
    ]
    LANGUAGES = [
        Language('German', 'germany', 100),
        Language('English', 'gb', 89),
        Language('Spanish', 'spain', 60),
        Language('French', 'france', 60),
        Language('Russian', 'russia ', 85),

    ]
