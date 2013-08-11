.. PureODM documentation master file, created by
   sphinx-quickstart on Sat Aug 10 14:51:43 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PureODM
=======

Welcome to PureODM's documentation! 


What is PureODM?
----------------

PureODM is an object-document mapper...sort of. PureODM provides you with a
convenient way to create models for your `MongoDB <http://www.mongodb.org>`_
data. And, actually, that's really all there is to it. Here is a list of things
that PureODM *does not* do:

*   It does not manage connections; more on this below
*   It does not create, or ensure, indexes for your data
*   It does not force a one-to-one, model-to-collection relationship; you can
    store the data from many different models in the same collection, or spread
    the data generated from the same model to many collections

All PureODM does, is map your data to a dictionary-like object so you can
easily store (and retrieve) data from MongoDB.


Seriously, *another* ORM, for MongoDB and Python?
-------------------------------------------------

*Working subtitle: A tale of long-standing connections*

Yes! In the previous sub-section, there is a mention of how PureODM does not
manage connections for you; it was the imposition of other Python/MongoDB ORMs
keeping your database connection a global thing, that spurred the creation of
this library. PureODM was also borne of a desire for a *much* simpler library 
for modeling data in MongoDB; the other ODMs just felt...heavy.

So, one project I was working on, was a high-traffic web API, that had to handle
serving data for multiple clients from the same process. In an attempt to
optimize the application, we thought it would be a good idea to move the
code that connected to our various MongoDB servers from our set-up functions, to
the section of code that ran while the application was starting up. Yes, this 
meant having to maintain long-standing connections to all of our database
servers, but at the same time, it was an optimization and proved to be a rather
decent one.

At the time, we were using `MongoEngine <http://mongoengine.org/>`_, which did
not allow us to maintain more than one connection to a MongoDB server at the
same time, as it kept the connection object in the global context (no bueno).
This was not an issue when we would connect to the database during the set-up
for the request handler, but in this situation where we would connect to the
database during the application's start-up, it was a serious show-stopper.

We ended up going back to just using plain, old
`pymongo <http://api.mongodb.org/python/current/>`_. From that situation though,
it seemed fitting to offer an alternative object-document mapper that did
nothing more than map documents, to objects (and vice versa). Why would we want
the ODM to manage our connections for us, as well?

Either way, we hope you enjoy using PureODM.


Development
-----------

The code for PureODM is kept on Github:
`nesv/pureodm <https://github.com/nesv/pureodm>`_.

If you would like to add a feature to PureODM, or just help out with the
project, create a fork, do your work, then submit a pull request. 

If you have an issue, a bug, or would like to make a feature request, please
create `an issue <https://github.com/nesv/pureodm/issues/new>`_.


Licensing
---------

PureODM is released under the terms of the MIT license.

What does this mean for you? Well, the MIT license is wonderfully permissive,
however if you would like to learn more about it, I recommend
`reading more about it <http://en.wikipedia.org/wiki/MIT_License>`_.


Contributing
------------

If you find PureODM useful, a tip on `Gittip <https://www.gittip.com/nesv/>`_ 
would be muchly appreciated!


Table of Contents
=================

.. toctree::
   :maxdepth: 2

   quick-tutorial
   field-constraints
   codecs
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

