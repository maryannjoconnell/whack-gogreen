import os

def handle_command(command, channel, MAIN_COMMAND):
    response = "Not sure what you mean. Use the *" + MAIN_COMMAND + \
               "* command, followed by your *zip code* and what you want to recycle."

    if command.startswith(MAIN_COMMAND): 
        command = command.split(' ', 1)[1] ##remove command from string
        ZIP_CODE = command.split()[0] ##store zip code
        if len(ZIP_CODE) == 5 and ZIP_CODE.isdigit(): ##checking zip code is valid
            command = command.split(' ', 1)[1]  ##remove zip code
            response = "Checking if " + command + " can be recycled in " + ZIP_CODE + "..."
            ##TODO: figure out if recyclable!!!
        else:
            response = "Please input a valid zip code (5 digit postal code)"
    return response
