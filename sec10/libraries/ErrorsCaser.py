######################################################
# Copyright 2021. Nifanin Konstantin
# Licensed under the Apache License, 
# Version 2.0 (the «License»);
#
# List of autors (add your name here if edit):
# - Nifanin Konstantin (https://github.com/Piknik1990)
######################################################


# Communication with users
from sys import stderr,exit

def pig_error(errorReason, kosyachnik="unknown"):
    # Print fatal messages 
    # Parameters: errorReason - text of error massage
    #             kosyachnik - who messed up ("user", "dev", "unknown") or unseted (will be set "unknown" as default)
    # Output: Print message and exit with 101
    # Example: pig_error("Can't found file diagram.drawio", "User") -> \U0001F437 Oops. Something wrong. 
    #                                                               -> Apparently you did something wrong and I could not understand you. Please look at the error text, correct and try again:
    #                                                               -> Can't found file diagram.drawio 
    #                                                               -> *Exit 101*
    # Errors: none
    # Warnings: none
    if kosyachnik == "user":
        stderr.write("\U0001F437 Oops. Something wrong. \nApparently you did something wrong and I could not understand you. Please look at the error text, correct and try again:\n")
        stderr.write(errorReason + "\n")
        exit(101)
    if kosyachnik == "dev":
        stderr.write("\U0001F437 Oops. Something wrong. \nApparently I still do not know how to correctly handle such situations. Please describe the bug report and the actions you tried to do to our developers at https://github.com/Piknik1990/sec10/issues. \nThey will help you. And once again - I'm sorry. I am ashamed.\n")
        stderr.write(errorReason + "\n")
        exit(101)
    stderr.write("\U0001F437 Oops. Something wrong. \nMaybe this problem is on my side, or maybe on yours. Let's read the message together and think about what went wrong.\nIf nothing is clear, then describe the bug report and the actions you tried to do to our developers at https://github.com/Piknik1990/sec10/issues.\nWell, the error message:\n")
    stderr.write(errorReason + "\n")
    exit(101)