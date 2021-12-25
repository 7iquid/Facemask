from django.db import models
from api.models import *

class Person(models.Model):
    name = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)



.all
    ['model', '_db', '_hints', '_query', '_result_cache',
     '_sticky_filter', '_for_write', '_prefetch_related_lookups',
      '_prefetch_done', '_known_related_objects', '_iterable_class',
       '_fields', '_defer_next_filter', '_deferred_filter', '__module__',
        '__doc__', '__init__', 
        
        'query', 'as_manager', 
        
        '__deepcopy__',
         '__getstate__', '__setstate__', '__repr__', '__len__', '__iter__',
          '__bool__', '__getitem__', '__class_getitem__', '__and__',
           '__or__', '_iterator', 
           
           'iterator', 'aggregate', 'count', 'get',
            'create', 

            '_prepare_for_bulk_create', 
            
            'bulk_create',
             'bulk_update', 'get_or_create', 'update_or_create',
              
              '_extract_model_params', '_earliest', 'earliest',
               'latest', 'first', 'last', 'in_bulk', 'delete',
                '_raw_delete', 'update', '_update', 'exists',
                 'contains', '_prefetch_related_objects', 'explain',
                  'raw', '_values', 'values', 'values_list', 'dates',
                   'datetimes', 'none', 'all', 'filter', 'exclude',
                    '_filter_or_exclude', '_filter_or_exclude_inplace',
                     'complex_filter', '_combinator_query', 'union',
                      'intersection', 'difference', 'select_for_update',
                       'select_related', 'prefetch_related', 'annotate',
                        'alias', '_annotate', 'order_by', 'distinct', 'extra',
                         'reverse', 'defer', 'only', 'using', 'ordered', 'db',
                          '_insert', '_batched_insert', '_chain', '_clone',
                           '_fetch_all', '_next_is_sticky', '_merge_sanity_check', '_merge_known_related_objects', 'resolve_expression', '_add_hints', '_has_filters', '_validate_values_are_expressions', '_not_support_combined_queries', '__dict__', '__weakref__', '__new__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

.first()
['_state', 'id', 'root_cause', 

'action_taken', 'remarks', 'total_down_time',
 'machine_id', 'dalydate_id', 

 '__module__', 'ProblemFound', 'CounterMeasure',
  '__str__', '__doc__', '_meta', 'DoesNotExist', 'MultipleObjectsReturned',
   'get_root_cause_display', 'get_action_taken_display', 'machine', 'dalydate',
    'objects', '__init__', 'from_db', '__repr__', '__eq__', '__hash__',
     '__reduce__', '__getstate__', '__setstate__', '_get_pk_val', '_set_pk_val',
      'pk', 'get_deferred_fields', 'refresh_from_db', 'serializable_value',
       'save', 'save_base', '_save_parents', '_save_table', '_do_update',
        '_do_insert', '_prepare_related_fields_for_save', 'delete',
         '_get_FIELD_display', '_get_next_or_previous_by_FIELD',
          '_get_next_or_previous_in_order', 'prepare_database_save', 'clean',
           'validate_unique', '_get_unique_checks', '_perform_unique_checks',
            '_perform_date_checks', 'date_error_message', 'unique_error_message',
             'full_clean', 'clean_fields', 'check', '_check_default_pk',
              '_check_swappable', '_check_model', '_check_managers', '_check_fields',
              '_check_m2m_through_same_relationship', '_check_id_field',
               '_check_field_name_clashes', '_check_column_name_clashes',
                '_check_model_name_db_lookup_clashes',
                 '_check_property_name_related_field_accessor_clashes',
                  '_check_single_primary_key', '_check_index_together',
                   '_check_unique_together', '_check_indexes', '_check_local_fields',
                    '_check_ordering', '_check_long_column_names', '_get_expr_references',
                     '_check_constraints', '__dict__', '__weakref__', '__new__',
                      '__getattribute__', '__setattr__', '__delattr__', '__lt__',
                       '__le__', '__ne__', '__gt__', '__ge__', '__reduce_ex__',
                        '__subclasshook__', '__init_subclass__', '__format__',
                         '__sizeof__', '__dir__', '__class__']                    


def 