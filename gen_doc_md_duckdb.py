import os
import duckdb
import json
from jinja2 import Environment, FileSystemLoader

DEFAULT_NEW_FILE_LEVEL = 2

NEW_FILE_LEVEL = {
    "container": {
        "level": 1,
    },
    "interfaces": {
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
    }
}

def render_commands_page(commands, path_list, filename):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template("page.md.j2")
    data = template.render(commands=commands)
    path = "output/"
    for p in path_list:
        path += f"{p}/"
        try:
            os.mkdir(path)
        except:
            pass

    with open(f"{path}{filename}.md", "w") as f:
        f.write(data)

def main():
    # delete the database if it exists
    try:
        os.remove("commands.duckdb")
    except:
        pass
    
    max_level = DEFAULT_NEW_FILE_LEVEL
    for key, value in NEW_FILE_LEVEL.items():
        if value["level"] > max_level:
            max_level = value["level"]

    with duckdb.connect(database = "commands.duckdb") as con:
        con.execute("CREATE TABLE commands AS SELECT * FROM read_json_auto('json_flat.json')")
        con.query("SELECT * FROM commands")
        cmd_list = con.query(f"SELECT STRING_SPLIT(commandname, ' ') as cmd_list  FROM commands WHERE level <= {max_level};")
        #print(cmd_list)
        #exit()
        # iterate over the commands
        for cmd in cmd_list.fetchall():
            cmd = cmd[0] # any row is a tuple
            
            if cmd[0] in NEW_FILE_LEVEL.keys():
                path_full = cmd[:NEW_FILE_LEVEL[cmd[0]]["level"]]
            else:
                path_full = cmd[:DEFAULT_NEW_FILE_LEVEL]
            print(f"Processing {path_full}")
            # get the commands
            commands = con.sql(f"SELECT * FROM commands WHERE commandname LIKE '{" ".join(path_full)}%' ORDER BY commandname;")
            commands = commands.df()
            commands = commands.to_json(orient="records")
            commands = json.loads(commands)
            print(commands[0]['commandname'])
            print(commands[1]['commandname'])
            print(commands[2]['commandname'])
            print(commands[3]['commandname'])
            print("--------------")
            # render the page
            path_list = path_full[:-1]
            filename = path_full[-1]
            #render_commands_page(commands, path_list, filename)




if __name__ == "__main__":
    main()