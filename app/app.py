## the main app

from flask import Flask
from flask_restful import Api

import sys, getopt, json

from frontend import setup
from backend import sql_query

flask_app = Flask(__name__)
flask_api = Api(flask_app)
config_data = ''

def parse_args(args):
    config_file = ''
    key_file = ''

    try:
        opts, args = getopt.getopt(args, "h", ["--help", "config=", "config_file="])
    except getopt.GetoptError:
        return "Parsing error", 2

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            return "app --config_data=<configuration file> --config=<configuration name>", 0
        elif opt in ("--config_data"):
            config_file = arg
        elif opt in ("--config"):
            configuration = arg

    if len(config_file) > 0:
        # load the config file
        config_data = json.load(open(config_file))[configuration]
    else:
        config_data = json.load(open("default_config.json"))["local"]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message, value = parse_args(sys.argv[1:])
        if len(message) > 0:
            print(message)
            sys.exit(value)
    else:
        config_data = json.load(open("default_config.json"))["local"]
    #if config_data['server_info']['debug'] is True:
    print(config_data)

    sql_query.init_db(config_data['db_info'])
    setup.init_api(flask_api)

    flask_app.run(debug=config_data["server_info"]["debug"], port=config_data["server_info"]["port"])