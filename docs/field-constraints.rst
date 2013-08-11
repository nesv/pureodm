.. _field-constraints:

Field constraints
=================

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
