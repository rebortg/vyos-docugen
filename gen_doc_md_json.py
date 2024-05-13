import os
import duckdb
import json
from jinja2 import Environment, FileSystemLoader

DEFAULT_NEW_FILE_LEVEL = 2

NEW_FILE_LEVEL = {
    "container": {
        "level": 1,
    },
    "high-availability": {
        "level": 1,   
    },
    "pki": {
        "level": 1,
    },
    "qos": {
        "level": 1,
    },
    "vrf": {    
        "level": 1,
    # problem if we want to separate vrf extra under "vrf name <tag> protocols"
    }
}

def render_commands_page(commands, path_list, filename):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template("page.md.j2")
    data = template.render(commands=commands)
    path = "output_v2/"
    for p in path_list:
        path += f"{p}/"
        try:
            os.mkdir(path)
        except:
            pass

    with open(f"{path}{filename}.md", "w") as f:
        f.write(data)

def main():

    # was used for sql don't now if needed
    max_level = DEFAULT_NEW_FILE_LEVEL
    for key, value in NEW_FILE_LEVEL.items():
        if value["level"] > max_level:
            max_level = value["level"]

    #cmd_list = con.query(f"SELECT STRING_SPLIT(commandname, ' ') as cmd_list  FROM commands WHERE level <= {max_level};")
    with open("json_flat.json", "r") as f:
        data = json.load(f)
    
    cmd_list = [c['commandname'] for c in data if c["level"] <= max_level]

    # fix level the commands that are in the NEW_FILE_LEVEL
    from pprint import pprint
    pprint(cmd_list)
    print("=====")
    for cmd in list(cmd_list):
        if cmd in NEW_FILE_LEVEL.keys():
            continue
        for k in NEW_FILE_LEVEL.keys():
            if cmd.startswith(k):
                cmd_list.pop(cmd_list.index(cmd))
                break

    # separate data against cmd_list
    from pprint import pprint
    pprint(cmd_list)
    for cmd in cmd_list:
        commands = [c for c in data if c['commandname'].startswith(cmd)]
        split_cmd = cmd.split(" ")
        # hack to fix <tag> node
        if split_cmd[-1] == "<tag>":
            split_cmd = split_cmd[:-1]
        path_list = split_cmd[:-1]
        filename = split_cmd[-1]
        render_commands_page(commands, path_list, filename)




if __name__ == "__main__":
    main()