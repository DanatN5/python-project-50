import itertools


def stylish_format(data, replacer=' ', count=4):    
    indent = replacer * count
    
    def walk(item, depth):
                
        current_indent = indent * depth
        deep_indent = (indent * (depth + 1))[:-2]
        
        keys = sorted(item.keys())
        lines = []

        for key in keys:
            val = item[key]
            status = val['status']
            if status == 'added':             
                lines.append(f'{deep_indent}+ {str(key)}'
                             f': {format_line(
                                 val['value'], depth + 1, indent)}')
            elif status == 'deleted':
                lines.append(f'{deep_indent}- {str(key)}'
                             f': {format_line(
                                 val['value'], depth + 1, indent)}')
            elif status == 'unchanged':
                lines.append(f'{deep_indent}  {str(key)}'
                             f': {format_line(
                                 val['value'], depth + 1, indent)}')
            elif status == 'updated':
                lines.append(f'{deep_indent}- {str(key)}'
                             f': {format_line(
                                 val['old_value'], depth + 1, indent)}\n'
                             f'{deep_indent}+ {str(key)}'
                             f': {format_line(
                                 val['new_value'], depth + 1, indent)}')
            elif status == 'nested':
                lines.append(f"{deep_indent}  {str(key)}"
                             f": {walk(val['children'], depth + 1)}")
            
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return walk(data, 0)


def format_line(value, depth, indent):
    if value is None:
        return "null"    

    elif isinstance(value, dict):
            
        current_indent = indent * depth
        deep_indent = indent * (depth + 1)
        lines = [f"{deep_indent}{k}: {format_line(v, depth + 1, indent)}"
                 for k, v in value.items()]            
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)  
              
    elif isinstance(value, bool):
        return str(value).lower()
        
    return str(value)