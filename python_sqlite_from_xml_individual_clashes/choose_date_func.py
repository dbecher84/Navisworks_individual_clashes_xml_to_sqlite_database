

import datetime
import re

def pick_date(users_option):
    date_match = '^[2][0-1]\d\d[.]([0-1][0-9])[.]([0-3][0-9])$'
    if users_option.lower() == 'y':
        now = datetime.datetime.now()
        picked_date = now.strftime('%Y.%m.%d')
        return picked_date
    else:
        user_date = input('Enter test date YYYY.MM.DD: ')
        if re.match(date_match, user_date):
            picked_date = user_date
            return picked_date
        else:
            print ('Not a valid Date')
