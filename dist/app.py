#
#   Configuration Generator
#
import os
import json
import argparse
app_config = "config.json"


def configureLoader():
    try:
        global messages
        global error
        f = open(app_config)
        config = json.loads(f.read())
        messages = config['messages']
    except:
        print("Error loading program")

def showmsg():
    print(messages['welcome'])

if __name__ == "__main__":
    configureLoader()
    parser = argparse.ArgumentParser(description=messages['welcome'])    
    parser.add_argument('generate')
    args = parser.parse_args()
    print(vars(args))
