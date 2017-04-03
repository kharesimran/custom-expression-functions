# custom-expression-functions
Custom Python expression functions for QGIS

### maxofallvaluesplusone.py

1. **maxofallvaluesplusone('fieldName')**
Given the name of the field (fieldName), returns 1 + the maximum value for the field. Can be used to automatically generate primary keys (eg. fids) when adding features in QGIS. Paste the following expression in the `Default value` box in the Edit Widget Properties dialog. 

*Example usage:* `maxofallvaluesplusone('fid')`

To avoid the user from editing the automatically generated id, uncheck the `Editable` checkbox in the Edit Widget Properties dialog.   

### hstore_functions.py

Converts the hstore attribute to a Python dictionary with the tags as keys and tag values as values. It then searches the dict for the input key, key-value pair or hstore.
The file `hstore_functions.py` comprises the following expression functions:

1. **hstore_get_value(hstore_attr, key)**

    Given the key, this function returns its value from the hstore string.
    If the key is not present, it returns *null*.

    *Example usage:* `hstore_get_value('other_tags', 'tourism')`

    Upon executing the above query in the expression engine, all features for which this function returns a non-null value will be selected, i.e. all features that contain the key `tourism` in their hstore.


1. **hstore_exist(hstore_attr, key)**

    This function returns whether the given key exists in the hstore string.
    It returns a boolean, True or False.

    *Example usage:* `hstore_exist('other_tags', 'tourism')`

    Upon executing the above query in the expression engine, all features which contain the key `tourism` in their hstore will be selected.


1. **hstore_contains_key_value(hstore_attr, key_value)**

    This function returns whether the given key value pair exists in the hstore string.
    It returns a boolean, True or False.

    *Example usage:* `hstore_contains_key_value('other_tags', 'tourism=>information')`

    Upon executing the above query in the expression engine, all features which contain the key value pair `tourism=>information` in their hstore will be selected.


1. **hstore_contains_hstore(hstore_attr, hstore_input_string)**

    This function returns whether the given hstore string exists in the feature's hstore attribute.
    It returns a boolean, True or False.

    *Example usage:* `hstore_contains_hstore('other_tags', 'tourism=>information,information=>guidepost')`

    Upon executing the above query in the expression engine, all features which contain both key value pairs `tourism=>information` and `information=>guidepost` in their hstore will be selected. The function also accepts and returns the correct result for input hstore strings that have spaces or double quotes surrounding the keys and values.
    
The code also contains the function **hstore_to_dict()** which accepts an hstore string and returns a Python dictionary. This function is called by 1, 2, 3 and 4 above.


### hstore_functions_regex.py

Searches for the input key, key-value pair, or hstore in the hstore attribute using regular expressions.

1. **hstore_get_value1(hstore_attr, key)**  
    *Example usage:* `hstore_get_value1('other_tags', 'tourism')`

1. **hstore_exist1(hstore_attr, key)**  
    *Example usage:* `hstore_exist1('other_tags', 'tourism')`

1. **hstore_contains_key_value1(hstore_attr, key_value)**  
     Please enclose the key and value in double quotes  
    *Example usage:* `hstore_contains_key_value1('other_tags', '"tourism"=>"information"')`

1. **hstore_contains_hstore1(hstore_attr, hstore_input_string)**  
     Please enclose the key and value in double quotes  
    *Example usage:* `hstore_contains_hstore1('other_tags', '"tourism"=>"information","information"=>"guidepost"')`
    
    

