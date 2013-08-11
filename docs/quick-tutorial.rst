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
dicitonary is another dictionary, holding the definition for your field.

In your field's definition, you can use the following key-value pairs to define
your field (you could also refer to them as "field constraints"):

+-----------------+------------------------------------------------------------+
| Constraint      | Explanation                                                |
+=================+============================================================+
| codec           | A reference to a class that inherits from                  |
|                 | :py:class:`~pureodm.codecs.Codec`. Field codecs are used   |
|                 | to encode values when they are set, and decode them when   |
|                 | they are retrieved. For more details, please read the      |
|                 | :ref:`codecs` section.                                     |
+-----------------+------------------------------------------------------------+
| default         | A default value that can be set for the field, should no   |
|                 | other value be specified.                                  |
+-----------------+------------------------------------------------------------+
| required        | ``True`` or ``False``, indicating whether or not the field |
|                 | is required to have a value set, before the model          |
|                 | generates the document and commits it to the database.     |
+-----------------+------------------------------------------------------------+
| type            | A class that can be passed to :py:func:`isinstance()` for  |
|                 | validating the value set for the field. This is the only   |
|                 | field constraint that is required to be provided when      |
|                 | defining the model.                                        |
+-----------------+------------------------------------------------------------+
