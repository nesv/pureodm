'''
examples/user.py

An small, but complete, example of creating a model.
'''

import pureodm
import pymongo

class User(pureodm.Model):
    fields = {
        'name': {
            'type': str,
            'required': True
        },
        'password': {
            'type': str,
            'required': True
        }
    }

if __name__ == '__main__':
    connection = pymongo.Connection(host='localhost', port=27017)
    database = connection['pureodmTest']
    users = database['users']

    user = User(name='stinky', password='none_of_yer_beeswax')
    print user.save_to(None)
    user.save_to(users)
    print 'successfully saved user'

    connection.close()
