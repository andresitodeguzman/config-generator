#
#   Configuration Generator
#   Andresito M. de Guzman
#   2017
#

import os
import json
import argparse

app_config = "config.json"
error_general = "An Error Occured"

def run(): 
    run = content['run']
    print(run['welcome_message'])
    project_title = input("What is the Project Title?(template_project) ")
    if project_title=='':
        project_title='template_project'
    author = input("Who is the Author?(user) ")
    if author=='':
        author='user'
    print(project_title)
    print(author)

# configureLoader() loads the configuration file for the program's internal process
def configureLoader():
    try:
        global messages
        global error
        global content
        f = open(app_config)
        config = json.loads(f.read())
        messages = config['messages']
        errors = config['errors']
        content = config['content']
    except:
        print(error_general)

if __name__ == "__main__":
    configureLoader()
    parser = argparse.ArgumentParser(description=messages['welcome'])    
    parser.add_argument("-r", "--run", help=messages['run'], action="store_true")
    parser.add_argument("--about", help=messages['about'], action="store_true")
    parser.add_argument("--github", help=messages['github'], action="store_true")
    args = parser.parse_args()
    if args.run:
        run()
    if args.about:
        print(content['about'])
    if args.github:
        print(content['github'])
