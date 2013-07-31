'''
The ``pureodm.codecs`` module provides the :class:`~pureodm.codec.Codec` class
for creating your own field codecs.

A field codec is used to encode the data written to a field, and decode the
data when it is read from the field.

.. tip::

	When writing a codec, you should try to make sure that your ``encode()``
	and ``decode()`` methods can also work with lists.
'''

from base64 import b64encode, b64decode
from hashlib import sha1

class Codec(object):
	'''
	A mixin-style class that provides two methods:

	*	:meth:`pureodm.codec.Codec.encode`
	*	:meth:`pureodm.codec.Codec.decode`

	If :meth:`pureodm.codec.Codec.encode` is the only method that is required
	to be implemented by its inheritors; failure to do so will result in the
	method raising a :exc:`NotImplementedError`.
	'''

	def __init__(self):
		pass

	def encode(self, value):
		'''Returns the encoded version of ``value``.'''
		raise NotImplementedError('This method needs to be implemented.')

	def decode(self, value):
		'''Returns the decoded version of ``value``.

		.. note::

			In some occasions, this method may not need to be overwritten.
			For example, in the event of a hashed value, you cannot un-hash
			it. In which case, you would subclass :class:`pureodm.codec.Codec`
			but not override this method.

		'''
		return value

class Base64Codec(Codec):
	'''A very simple codec used for encoding data to, and decoding data from,
	base64.'''

	def __init__(self):
		pass

	def encode(self, value):
		'''
		Returns the contents of ``value`` base64-encoded. If ``value`` happens
		to be a list, then each element in the list will be encoded.
		'''
		if isinstance(value, list):
			return [b64encode(i) for i in value]

		return b64encode(value)

	def decode(self, value):
		'''
		Returns the decoded contents of ``value``. If ``value`` is a list,
		each element within the list will be decoded.
		'''
		if isinstance(value, list):
			return [b64decode(i) for i in value]

		return b64decode(value)

class SHA1Codec(Codec):
	'''
	Another simple codec that encodes a value, but does not (because it
	cannot) decode it.
	'''

	def __init__(self):
		pass

	def encode(self, value):
		'''
		Returns the contents of ``value`` hashed using the SHA-1 algorithm.
		'''
		if isinstance(value, list):
			return [sha1(i).hexdigest() for i in value]

		return sha1(value).hexdigest()
