import os
import pydoc
import json
from jinja2 import Environment, FileSystemLoader
from pprint import pprint

def render_commands_page(commands, input):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template("pydoc_template.j2")
    data = template.render(commands=commands, input=input)
    return data

def get_tree(input: list, data: dict) -> dict:
    if len(input) == 0:
        return data
    key = input[0]
    if key not in data:
        return None
    return_data = {}    


def main():
    input_cfg = ["container", "name", "testname", "arguments"]
    with open("xml_cache.json", "r") as f:
        cfgcmds = json.load(f)

    #pprint(get_tree(input, cfgcmds))

    temp_cfg = cfgcmds

    for key in input_cfg:
        cfg_keys = temp_cfg.keys()
        for k in cfg_keys:
            if k != key or k != "node_data":
                del temp_cfg[k]
        temp_cfg = temp_cfg[key]
                


    exit()
    # delete not queryed items from cfgcmds
    level = 0
    for key in cfgcmds.keys():
        if key != input[level] and key != "node_data":
            del cfgcmds[key]+
        


    commands = [c for c in cmd_list if c['commandname'].startswith(input)]
    data = render_commands_page(commands, input)
    pydoc.pager(data)




if __name__ == "__main__":
    main()