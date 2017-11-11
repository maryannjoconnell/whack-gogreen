import os

#constants

MAIN_COMMAND = "recycle"
ZIP_CODE = "00000"


def get_response(message):
    response = "Not sure what you mean. Use the " + MAIN_COMMAND + " command, followed by your zip code and what you want to recycle."

    if message.startswith(MAIN_COMMAND):
        message = message.split(' ', 1)[1] ##remove command from string
        ZIP_CODE = message.split()[0] ##store zip code
        if len(ZIP_CODE) == 5 and ZIP_CODE.isdigit(): ##checking zip code is valid
            message = message.split(' ', 1)[1]  ##remove zip code
            response = "Checking if " + message + " can be recycled in " + ZIP_CODE + "..."
        ##TODO: figure out if recyclable!!!
        else:
            response = "Please input a valid zip code (5 digit postal code)"
    return response

