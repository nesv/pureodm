# pureodm/models.py
#

import UserDict
import bson.objectid

class BaseModel(UserDict.IterableUserDict):

    fields = {}

    def __init__(self, **kwargs):
        '''All this simple constructor does is populate the instance's
        field values from any of the provided keyword arguments.'''
        self.data = {}
        for k in kwargs:
            self.__setitem__(k, kwargs[k])

    def __getitem__(self, key):
        '''
        Returns the value of the requested field, and will decode the data in
        the field if there is a codec associated with the field.
        '''
        return self.data[key]

    def __setitem__(self, key, value):
        '''
        Validates the value being set, as well as passes it through a
        codec, if one is defined, for the field.'''
        if key not in self.fields:
            if key == '_id' and isinstance(value, bson.objectid.ObjectId):
                self.fields[key] = {'type': bson.objectid.ObjectId,
                                    'required': True,
                                    'value': value}

            elif key != '_id' and not isinstance(value, bson.objectid.ObjectId):
                e = 'Value must be of type bson.objectid.ObjectId.'
                raise TypeError(e)
        
        elif key not in self.fields:
            raise KeyError('No such field "{0}".'.format(key))

        field_type = self.fields[key]['type']
        if isinstance(field_type, str) and isinstance(value, unicode):
            # Favour unicode, over regular strings.
            self.data[key] = value

        elif isinstance(field_type, unicode) and isinstance(value, str):
            # Upgrade to unicode, because reasons.
            self.data[key] = unicode(value)

        elif isinstance(field_type, list) and not isinstance(value, list):
            # The caller is trying to set the value of a list field to 
            # something other than a list.
            #
            # For shame...
            #
            e = '"{0}" is a list field of {1}.'.format(key, field_type[0])
            raise ValueError(e)

        elif isinstance(field_type, list) and isinstance(value, list):
            # Ensure that each element in the list ``value`` matches the
            # sub-type of the list field.
            for i in value:
                if not isinstance(i, field_type[0]):
                    e = '"{0}" is meant to hold {1}, not {2}.'
                    raise ValueError(e.format(key, field_type[0], type(i)))

            self.data[key] = value

        elif isinstance(value, field_type):
            # We were not passed a list, but the value the caller wants to set
            # is of the same type as that in the key definition.
            #
            self.data[key] = value

        elif isinstance(value, None):
            # In the event we are nullifying the value of a field, we want
            # this to pass.
            self.data[key] = None
        
        else:
            # Nope; type mismatch.
            #
            e = '{2}: Wanted {0}, got {1}.'
            raise ValueError(e.format(field_type, type(value), key))

    def __delitem__(self, key):
        '''Instead of removing the item from the dictionary, this method
        simply nullifies the value.

        To nullify the value, this method - in turn - just calls 
        :meth:`self.__setitem__()` so that all of the type-checking is done in
        one place.
        '''
        # Remember, this is a cleanliness thing.
        self.__setitem__(key, None)

class EmbeddedModel(BaseModel):

    pass

class Model(BaseModel):

    def save_to(self, collection, **kwargs):
        '''Does some remaining validation on the data in the model, then
        saves it.'''

        # Check to make sure an "_id" field was set. If one was not defined,
        # and/or it just never had a value assigned, do so now.
        #
        if '_id' not in self.fields:
            self.fields['_id'] = {
                'type': bson.objectid.ObjectId,
                'required': True
            }
            self.__setitem__('_id', bson.objectid.ObjectId())

        # Run through the fields, and see if any of them that have a "default"
        # callable set have been assigned a value, and if they haven't, then
        # call the callable.
        #
        for i in self.fields:
            if i not in self.data and 'default' in self.fields[i]:
                # No value has been set, but there is a default value.
                #
                self.__setitem__(i, self.fields[i]['default']())

        # Check to make sure none of the required fields have been left empty.
        #
        for i in self.fields:
            if i not in self.data and 'required' in self.fields[i]:
                if self.fields[i]['required']:
                    raise ValueError('"{0}" is a required field.'.format(i))

        # Now, generate an update spec.
        #
        spec = dict([(i, self.data[i]) for i in self.fields if i in self.data])

        # Do the update.
        #
        if collection is not None:
            collection.save(spec, **kwargs)

        else:
            return spec

    @classmethod
    def find_in(cls, collection, terms=None, **kwargs):
        '''Simply maps the keyword arguments to a call to `collection.find()`,
        but will try to map the data from each document to the model.'''
        results = collection.find(terms, **kwargs)
        for i in results:
            yield cls.map_from_result(i)

    @classmethod
    def find_one_in(cls, collection, terms=None, **kwargs):
        '''Practically identical to find_in(), but only returns a single
        object, as opposed to a list.'''
        result = collection.find_one(terms, **kwargs)
        if result is not None:
            result = cls.map_from_result(result)

        return result

    @classmethod
    def map_from_result(cls, result):
        '''Creates (and returns) an instance of this model, and does its best
        to map the fields in "result" to attributes in this class.'''

        model = cls()
        for field in result:
            model[field] = result[field]

        return model
