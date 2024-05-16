import os
import pydoc
import json
from jinja2 import Environment, FileSystemLoader
from pprint import pprint

def get_rendered_page(commands, input):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template("pydoc_template.j2")
    data = template.render(commands=commands, input=input)
    return data

def get_tree(input: list, data: dict) -> dict:
    temp_cfg = data
    new_cfgcmds = dict()
    for key in input:
        if temp_cfg.get('node_data', dict()).get('node_type','') == "tag":
            continue         
        cfg_keys = list(temp_cfg.keys())
        cfg_keys.sort()
        for k in cfg_keys:
            if k != key:
                if k != "node_data":
                    del temp_cfg[k]
        temp_cfg = temp_cfg[key]
    return data

def flatten_cmd_tree(data: dict, commandname: str ='', level: int =0, sep: str =' ') -> dict:
    return_data = []
    for key, value in data.items():
        if key == 'node_data':
            if value['node_type'] == 'tag':
                commandname = commandname + f"<VALUE>" + sep
            value['commandname'] = commandname.strip()
            value['level'] = level
            return_data.append(value)
        else:
            return_data.extend(flatten_cmd_tree(value, commandname + key + sep, level + 1, sep))
    return return_data


def main():
    input_cfg = ["container", "name", "testname", "arguments"]
    with open("xml_cache2.json", "r") as f:
        cfgcmds = json.load(f)
    
    # delete empty root node_data
    del cfgcmds['node_data']

    cfg_tree = get_tree(input_cfg, cfgcmds)


    pprint(cfg_tree)
    data = flatten_cmd_tree(cfgcmds)
    a = get_rendered_page(data, 'dd')

    print(a)
    print('halt')
    exit()
    # delete not queryed items from cfgcmds
    level = 0
    for key in cfgcmds.keys():
        if key != input[level] and key != "node_data":
            del cfgcmds[key]
        


    commands = [c for c in cmd_list if c['commandname'].startswith(input)]
    data = render_commands_page(commands, input)
    pydoc.pager(data)




if __name__ == "__main__":
    main()