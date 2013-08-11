Quick tutorial
==============

PureODM is not a large library, and would not be well-served by a large
tutorial. This tutorial is going to be a very "quick and dirty" tutorial,
and will show you how to get writing models in short order. Extra detail will
be provided where it is due.


Creating a model
----------------

If you look at the API, you will notice that the :py:class:`Model` class is
actually defined in :py:mod:`pureodm.models`, however, it has been imported
into the :py:mod:`pureodm` module for convenience. So, let's define a simple
model that would hold a blog post::

  import pureodm
  import bson.objectid
  
  class Post(pureodm.Model):
      fields = {'_id': {'type': bson.objectid.ObjectId,
                        'default': bson.objectid.ObjectId(),
			'required': True},
                'title': {'type': unicode,
                          'required': True},
                'author': {'type': unicode,
		           'required': True},
	        'body': {'type': unicode}}

Unlike other object-document/relational mappers (like MongoEngine, or
SQLAlchemy), you do not define your fields as individual class attributes. When
you define your model in PureODM, you specify one class attribute: ``fields``.
The ``fields`` attribute is a dictionary where each key is the name of the
field in the document. The value-portion of each key-value pair in the
dicitonary is another dictionary, holding the constraints for each field.

.. note::

   Fun fact, you do not need to specify the ``_id`` field! That does not mean
   you should never declare the ``_id`` field, though. In the event you forget 
   to declare the ``_id`` field, the :py:meth:`~pureodm.models.Model.save_to()`
   method will add it to your model before serializing your data, and committing
   it to the database.

For more information on the various, available field constraints, browse through
the :ref:`field-constraints` section.

Past this point, your model is ready to use!


Setting values
--------------

First, a teeny-tiny bit of history. The initial implementation of PureODM
tried to be an actual object-document mapper, where fields were accessed as
instance attributes of the model. This resulted in some exceptionally messy
handling of instance attributes and class attributes. 

As of PureODM 0.3, the models look (and feel) more like a dictionary.

So, we have already defined a model that represents holding a blog post; let's
build on this and actually set some values for that model::

  first_blog_post = Post(title=u'My first blog post',
                         author=u'Me',
			 body=u'Yippee!')

It's that simple! However, this is just a shortcut. If you wish to be a 
little more verbose in your assignment, you could also populate this model like so::

  first_blog_post = Post()
  first_blog_post['title'] = u'My first blog post'
  first_blog_post['author'] = u'Me'
  first_blog_post['body'] = u'Yippee!'


Saving your data
----------------

At this point, we have defined a model, created a new instance of our model, and
populated it with some data. Let's commit it to the database. Before we do that
though, we are going to establish a connection to the database (just to make this
example complete)::

  from pymongo.connection import Connection
  
  conn = Connection('localhost')
  db = conn['myBlog']
  posts = db['posts']

  first_blog_post.save_to(posts)

Oooh, but wait a minute, we didn't set the ``_id`` field of our model! No
worries! While there are very few things PureODM does for you, there are some
conveniences that have been put into it. Before, we mentioned that if you didn't
specify the ``_id`` field when you were defining your model, PureODM would add
it in for you. The same goes for the occasion where you may forget to assign a
value to the ``_id`` field: PureODM will quickly create a new
:py:class:`~bson.objectid.ObjectId` for you, and set it before the document gets
written to the database.


Retrieving your data
--------------------


Updating a document
-------------------
