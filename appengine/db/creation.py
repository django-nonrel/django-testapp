from django.db.backends.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    # This dictionary maps Field objects to their associated GAE column
    # types, as strings. Column-type strings can contain format strings; they'll
    # be interpolated against the values of Field.__dict__ before being output.
    # If a column type is set to None, it won't be included in the output.
    data_types = {
        'DateTimeField':     'datetime',
        'DateField':         'date',
        'TimeField':         'time',
        'FloatField':        'float',
        'EmailField':        'email',
        'URLField':          'link',
        'BooleanField':      'bool',
        'NullBooleanField':  'bool',
        'CharField':         'text',
        'CommaSeparatedIntegerField': 'text',
        'IPAddressField':    'text',
        'SlugField':         'text',
        'FileField':         'text',
        'FilePathField':     'text',
        'TextField':         'longtext',
        'XMLField':          'longtext',
        'IntegerField':      'integer',
        'SmallIntegerField': 'integer',
        'PositiveIntegerField': 'integer',
        'PositiveSmallIntegerField': 'integer',
        'AutoField':         'integer',
        'OneToOneField':     'integer',
        'DecimalField':      'decimal',
#        'ImageField':
        # TODO: Add KeyField and a correspoding db_type
    }