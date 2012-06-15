.. PureODM documentation master file, created by
   sphinx-quickstart on Thu Jun 14 15:34:38 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PureODM's pure documentation!
=============================

PureODM is an incredibly lightweight object-to-document mapper for Python
and MongoDB.

Where other ODMs like to do some tasks for you, PureODM does absolutely nothing
for you, other than map your query results to usable Python objects. I make
the following promises:

*   PureODM will always let you manage your connections to your database
*   PureODM will never create, or ensure the existence of, an index for you
*   PureODM will add absolutely nothing to your data; the data you define
    is the data that will be written to the database
*   PureDOM will always be supplemental; you should be able to remove it from
    your project at any time, without penalty

Contents:

.. toctree::
   :maxdepth: 2

   tutorial
   fields

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

