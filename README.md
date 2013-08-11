pureodm
=======

A super-lightweight object-document mapper for Python and MongoDB.

It is so lightweight, all it does is provide a way for you to structure your
data, and that's it! It leaves all of the index creation, and connection 
management, to you. At some point in the future, however, there may be some
functionality added that provides you with some shortcuts to doing things like
creating indexes.

Why another ODM?
----------------

Basically, I am sick-n'-tired of other ODMs doing a ton of work behind the 
scenes, and making some jobs harder than they need to be. One of the main
reasons *pureodm* does not manage database connections for you, is because
that would duplicate the functionality provided by the pymongo driver, but
at the same time abstract away from it, and make certain tasks more difficult.

Which tasks am I referring to? Suppose you want to establish multiple
connections to multiple databases - from the same process - and while all of
their data may be identical in structure, it must be kept separate for one 
reason or another.

> In case you are wondering, yes, this has come up before, and no, there was
> no viable solution other than using just pymongo.

Now, it should be mentioned that using the term "ODM" here, is a serious 
misnomer. All *pureodm* does, is provide you with a way to declare your data
structures, and from that, generate `dict`s that can be passed directly to any 
of the methods of a `pymongo.collection.Collection` object.

What are the benefits?
----------------------

* You establish the connections to the databases
* Absolutely nothing is done behind your back - not even index creation

Dependencies
============

* `pymongo (>=2.4.1)`

Despite there having been almost an entire year since the last release of
`pureodm`, the version of [PyMongo](https://pypi.python.org/pypi/pymongo) 
does not need to change, and impose an artificial version number that 
`pureodm` does not realistically make use of.

That being said though, you should *really* be using the latest version of
PyMongo.

Contributions
=============

If you would like to contribute to PureODM's development by leaving a small,
monetary donation, you can do so, on [Gittip](https://www.gittip.com/nesv/).
