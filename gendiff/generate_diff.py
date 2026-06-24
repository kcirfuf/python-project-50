def generate_diff(file1, file2):
    result = {}
    all_keys = sorted(file1.keys() | file2.keys())
    for key in all_keys:
        if key not in file2:
            result[f"- {key}"] = file1[key]
        elif key not in file1:
            result[f"+ {key}"] = file2[key]
        elif file1[key] == file2[key]:
            result[key] = file1[key]
        else:
            result[f"- {key}"] = file1[key]
            result[f"+ {key}"] = file2[key]
    return format(result)

def format(diff):
    lines = ["{"]
    for key, value in diff.items():
        lines.append(f"    {key}: {format_value(value)}")
    lines.append("}")
    return "\n".join(lines)

def format_value(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)
