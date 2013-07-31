'''
examples/user.py

An small, but complete, example of creating a model.
'''

import pureodm, pureodm.codecs
import pymongo

class User(pureodm.Model):
    fields = {
        'name': {
            'type': unicode,
            'required': True
        },
        'password': {
            'type': unicode,
            'required': True,
            'codec': pureodm.codecs.SHA1Codec
        }
    }

if __name__ == '__main__':
    connection = pymongo.Connection(host='localhost', port=27017)
    database = connection['pureodmTest']
    users = database['users']

    for result in User.find_in(users, {'name': 'stinky'}):
        for field in result.fields:
            print('{0:>12}\t{1}'.format(field, result[field]))

    connection.close()
