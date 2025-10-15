def all_thing_is_obj(object: any) -> int:
    """
    Function that prints the object type and returns 42
    """
    obj_class = object.__class__
    obj_type_name = obj_class.__name__
    
    # Mapping des types avec leur nom d'affichage
    type_names = {
        'list': 'List',
        'tuple': 'Tuple', 
        'set': 'Set',
        'dict': 'Dict',
        'str': f"{object} is in the kitchen"
    }
    
    if obj_type_name in type_names:
        print(f"{type_names[obj_type_name]} : {obj_class}")
    else:
        print("Type not found")
    
    return 42