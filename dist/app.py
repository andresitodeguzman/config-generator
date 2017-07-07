##
##   Configuration Generator
##   Andresito M. de Guzman
##   2017
##
##

# Import Modules
import os
import json
import argparse
import pprint

# Declare own config file etc.
app_config = "config.json"
error_general = "An Error Occured"

# Main Program Process
def run(): 
    try:
        # Set Variable
        run = content['run']
        # Print Welcome Message
        print(run['welcome_message'])
        # Ask for Project Title
        project_title = input(run['project_title'])
        # Ask for version number
        version = input(run['version'])
        # Ask for Description
        description = input(run['description'])
        # Ask for author
        author = input(run['author'])
        # Ask for license
        license = input(run['license'])
        # Ask for copyright
        copyright = input(run['copyright'])
        # Ask for repository
        repository = input(run['repository'])
        # Ask for keywords
        keywords = input(run['keywords'])
        # Check for Empty Values
        if project_title=='':
            project_title='template_project'
        if author=='':
            author='user'
        if version =='':
            version="1.0.0"
        # Prepare Data
        create = {"project_title":project_title, "version":version, "description":description, "author":author, "license":license, "copyright":copyright, "repository":repository, "keywords":keywords}
        # Display created data
        print("\n")
        pp = pprint.PrettyPrinter()
        pp.pprint(create)
        # Confirm proceed
        confirm = input(run['confirm'])
        if confirm == "y":
            # Encode to JSON
            createJSON = json.JSONEncoder().encode(create)
            # Write to File
            with open("configuration.json","w") as file:
                file.write(createJSON)
            # Print Success Message
            print(run['saved'])
        else:
            # Print Aborted Messaage
            print(run['abort'])
    except:
        print("\n\n"+error_general)
# configureLoader() loads the configuration file for the program's internal process
def configureLoader():
    try:
        # Declare variables as global
        global messages
        global error
        global content
        # Open file
        f = open(app_config)
        # Read JSON
        config = json.loads(f.read())
        # Set Variables
        messages = config['messages']
        errors = config['errors']
        content = config['content']
    except:
        # Print Error
        print(error_general)

# Run if file directly invoked
if __name__ == "__main__":
    # Run Configuration Loader Function
    configureLoader()
    # Prepare Parser
    parser = argparse.ArgumentParser(description=messages['welcome'])    
    # Add Run Option
    parser.add_argument("-r", "--run", help=messages['run'], action="store_true")
    # Add About Option
    parser.add_argument("--about", help=messages['about'], action="store_true")
    # Add GitHub Option
    parser.add_argument("--github", help=messages['github'], action="store_true")
    # Create Variable
    args = parser.parse_args()
    # Check if Run
    if args.run:
        run()
    # Check if About
    if args.about:
        # Print About
        print(content['about'])
    # Check if GitHub
    if args.github:
        # Print GitHub
        print(content['github'])
