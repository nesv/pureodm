# pureodm/models.py
#

class BaseModel:

    fields = {}

    _changed = []

    def __getattr__(self, attr):
        '''Allows obj.x type access to the fields of the model.'''

        if attr not in self.fields:
            # Oops, it looks like that field does not exist!
            #
            raise AttributeError('No such field "{0}".'.format(attr))

        elif 'value' not in self.fields[attr]:
            # If the field has no value, then just return None.
            #
            return None

        elif isinstance(self.fields[attr]['type'], list):
            # If the field holds a list, then return a generator.
            #
            return (v for v in self.fields[attr]['value'])

        else:
            # Otherwise, just return whatever the field holds.
            #
            return self.fields[attr]['value']

    def __setattr__(self, attr, value):
        '''Allows you to set a field by addressing it as an attribute.

        Additionally, setting a value to a field also validates the data being
        assigned.'''

        if attr not in self.fields:
            # Nope, she no exist.
            #
            raise AttributeError('No such field "{0}".'.format(attr))
        
        field_type = self.fields[attr]['type']
        if isinstance(field_type, list) and not isinstance(value, list):
            # The caller is trying to set the value of a list field to 
            # something other than a list.
            #
            # For shame...
            #
            e = '"{0}" is a list field of {1}.'
            raise ValueError(e.format(attr, field_type[0]))

        elif isinstance(field_type, list) and isinstance(value, list):
            # Make sure each element in the provided list matches the subtype
            # of the list field.
            #
            for i in value:
                if not isinstance(i, field_type[0]):
                    e = '"{0}" is meant to hold {1}, not {2}.'
                    raise ValueError(e.format(attr,
                                              field_type[0],
                                              type(i)))

            # Everything seems okay!
            #
            self.fields[attr]['value'] = value

        elif isinstance(value, field_type):
            # We were not passed a list, but the value the caller wants to set
            # is of the same type as that in the key definition.
            #
            self.fields[attr]['value'] = value
        
        else:
            # Nope; type mismatch.
            #
            e = 'Wanted {0}, got {1}.'
            raise ValueError(e.format(field_type, type(value)))
            
        # When all is good, append the name of the field we just set to the
        # "_changed" list, so that we can generate an efficient update spec,
        # later on.
        #
        self._changed.append(attr)

class EmbeddedModel(BaseModel):

    pass

class Model(BaseModel):

    def save_to(self, collection, **kwargs):
        '''Does some remaining validation on the data in the model, then
        saves it.'''

        # Check to make sure an "_id" field was set. If one was not defined,
        # and/or it just never had a value assigned, do so now.
        #
        if self._id is None:
            import bson.objectid
            self._id = bson.objectid.ObjectId()

        # Run through the fields, and see if any of them that have a "default"
        # callable set have been assigned a value, and if they haven't, then
        # call the callable.
        #
        for i in self.fields:
            if 'value' not in self.fields[i] and 'default' in self.fields[i]:
                # No value has been set, but there is a default value.
                #
                self.__setattr__(i, self.fields[i]['default']())

        # Check to make sure none of the required fields have been left empty.
        #
        for i in self.fields:
            if 'value' not in self.fields[i] and 'required' in self.fields[i]:
                raise ValueError('"{0}" is a required field.'.format(i))

        # Now, generate an update spec.
        #
        update_spec = {'$set': dict([(i, self.fields[i]['value']) for i in self._changed])}

        # Do the update.
        #
        if collection is not None:
            collection.update({'_id': self._id}, update_spec, **kwargs)
            self._changed = []

        else:
            self._changed = []
            return update_spec

    @classmethod
    def find_in(cls, collection, terms=None, **kwargs):
        '''Simply maps the keyword arguments to a call to `collection.find()`,
        but will try to map the data from each document to the model.'''

        # Remove the "fields" keyword argument if it was passed. This is a 
        # freaking ODM, people - we want to map ALLLLLLLL OF THE DATA.
        #
        if 'fields' in kwargs:
            del(kwargs['fields'])

        raise NotImplementedError('TODO: Finish')
