Tutorial
========

Here is a really quick example to get you started (it will all be explained
afterwards)::

   >>> import pureodm
   >>> import pymongo

   >>> class User(pureodm.Model):
       fields = {
           'username': {
	       'type': unicode,
	       'required': True
	   },
	   'password': {
	       'type': unicode,
	       'required': True
    	   },
	   'comments: {
	       'type': [unicode]
	   }
        }

   >>> connection = pymongo.Connection(host='localhost', port=27017)
   >>> database = connection['test']
   >>> user = User(username='stinky')
   
   >>> from hashlib import sha512
   >>> user.password = unicode(sha512('some-password').hexdigest())

   >>> user.save_to(database['users'])

   >>> existing_user = User.find_one_in(database['users'], {'username': 'enid'})
   >>> print existing_user.comments[0]
   '...we never really knew each other, anyways.'



   
