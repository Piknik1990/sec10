######################################################
# Copyright 2021. Nifanin Konstantin
# Licensed under the Apache License, 
# Version 2.0 (the «License»);
#
# List of autors (add your name here if edit):
# - Nifanin Konstantin (https://github.com/Piknik1990)
######################################################



def drawio_file_saver(xml, filePath):
    # Save Draw.io XML file to disk
    # Parameters: xml - pretty or unpretty XML structure
    #             filePath - full path of file
    # Output: A Draw.io XML File in your disk or unsuccess_403, 
    # Example: 
    # Errors: input xml is not provided (Fatal)
    #         input filePath is not provided (Fatal)
    #         input xml in now have XML-structure (Fatal)
    #         input filePath is not path format (Fatal)
    # Warnings: input filePath is not have a .drawio file extension (Ignoring)
    #           input filePath have not permitions for write (Return unsuccess_403)
    write = 1