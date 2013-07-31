'''
examples/change_password.py

An small, but complete, example of creating a model.
'''

import pureodm
import pymongo

class User(pureodm.Model):
    fields = {
        'name': {
            'type': unicode,
            'required': True
        },
        'password': {
            'type': unicode,
            'required': True
        }
    }

if __name__ == '__main__':
    connection = pymongo.Connection(host='localhost', port=27017)
    database = connection['pureodmTest']
    users = database['users']

    result = User.find_one_in(users, {'name': 'stinky'})
    if result is not None:
        new_password = u'supers3cret!'
        print 'changing password from "{0}" to "{1}"'.format(result['password'],
                                                             new_password)
        result['password'] = new_password
        result.save_to(users)
        print 'saved user'

    connection.close()
