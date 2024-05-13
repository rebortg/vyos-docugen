import duckdb
import json

def flatten_json(d, commandname='', level=0, sep=' '):
    return_data = []
    for key, value in d.items():
        if key == 'node_data':
            if value['node_type'] == 'tag':
                commandname = commandname + f"<tag>" + sep
            value['commandname'] = commandname.strip()
            value['level'] = level
            return_data.append(value)
        else:
            return_data.extend(flatten_json(value, commandname + key + sep, level + 1, sep))
    return return_data

def main():
    data = json.load(open("xml_cache.json"))

    #delete empty node_data object
    data.pop('node_data')
    data = flatten_json(data)
    # sort by commandname
    data = sorted(data, key=lambda x: x['commandname'])
    with open('json_flat.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()