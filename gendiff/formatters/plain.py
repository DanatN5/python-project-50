
def plain_format(data):

    def walk(item, path):
        lines = []
        keys = sorted(item.keys())
        for key in keys:
            new_path = f'{path}.{key}' if path else key
            val = item[key]
            status = val['status']
            
            if status == 'added':             
                lines.append(f"Property '{new_path}' "
                             f"was added with value: "
                             f"{format_line(val['value'])}")
            elif status == 'deleted':
                lines.append(f"Property '{new_path}' was removed")
            
            elif status == 'updated':
                lines.append(f"Property '{new_path}' was updated. "
                             f"From {format_line(val['old_value'])} to "
                             f"{format_line(val['new_value'])}")
            elif status == 'nested':
                lines.append(walk(val['children'], new_path))

        return '\n'.join(lines)
    return walk(data, '')  


def format_line(value):
    if value is None:
        return "null"
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)  