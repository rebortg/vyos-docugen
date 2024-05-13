import os
import pydoc
import json
from jinja2 import Environment, FileSystemLoader

def render_commands_page(commands, input):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template("pydoc_template.j2")
    data = template.render(commands=commands, input=input)
    return data

def main():

    #cmd_list = con.query(f"SELECT STRING_SPLIT(commandname, ' ') as cmd_list  FROM commands WHERE level <= {max_level};")
    with open("json_flat.json", "r") as f:
        cmd_list = json.load(f)

    input = "container name <tag> host-name"
    commands = [c for c in cmd_list if c['commandname'].startswith(input)]
    data = render_commands_page(commands, input)
    pydoc.pager(data)




if __name__ == "__main__":
    main()