"""
TDQ Configuration File Automation Script

    - <EDIT HERE> - users to manually edit fields
    - Constraints required will be specified in TDQ_GUI application
    - Delimiter required will be specified in TDQ_GUI application
    - Further documentation tdda discover_df constraints in the link below
    - https://tdda.readthedocs.io/en/latest/constraints.html#tdda.constraints.discover_df

"""
import pandas as pd
import argparse
import json
from tdda.constraints import discover_df

## Function to read in CSV data and produce the required constraints 
def generate_tdq_configuration(input_FILEPATH, input_DELIMITER, input_CONSTRAINTS):
    ## Read in CSV data 
    data = pd.read_csv(input_FILEPATH, delimiter=input_DELIMITER, engine = "python")
    constraints = discover_df(data)
    constraints_json = constraints.to_json()
    constraints_dict = json.loads(constraints_json)
   
    ## Assign user selected constraints as a list to allowable_input_constraints
    allowable_input_constraints = input_CONSTRAINTS

    configuration_dict = { 
        "delimiter": input_DELIMITER,
        "enclosedinquotes": "<EDIT HERE>",
        "maximumrows": "<EDIT HERE>",
        "partition_col": "<EDIT HERE>",
        "list_of_partitions":["<EDIT HERE>","<EDIT HERE>","<EDIT HERE>","<EDIT HERE>"],
        "noOfCOl": None,
        "header": "<EDIT HERE>"
    }
    
    ## Dictionary to map configuration value to what TDQ lambda needs
    mapping_dict = {
        'type': 'datatype',
        'min': 'min',
        'max': 'max',
        'min_length': 'min_length',
        'max_length': 'max_length',
        'sign': 'sign',
        'max_nulls': 'nullable',
        'allowed_values': 'listofvalues' ,
        'no_duplicates': 'duplicate_check',
        'rex': 'rex'
    }

    field_dict = {} 
    configuration_dict['fields'] = field_dict
    
    ## Check constraints have been requested in allowable_input_constraints before adding to constraints file
    for column_name, column_constraints in constraints_dict['fields'].items():
        column_dict = {}
        for constraint_key, constraint_value in column_constraints.items():
            if constraint_key in allowable_input_constraints and mapping_dict.keys(): 
                column_dict[mapping_dict[constraint_key]] = constraint_value 
            
            field_dict[column_name] = column_dict
    
    configuration_dict["noOfCOl"] = len(field_dict)
    
    ## If nulls in column data, do not include "nullable" constraint in constraint file. 
    for column_name, column_constraints in configuration_dict['fields'].items():
        for constraint_key, constraint_value in column_constraints.items():
            if constraint_key == "nullable" and constraint_value == 0:
                configuration_dict['fields'][column_name][constraint_key] = 'false'
            if constraint_key == "nullable" and constraint_value != 0:
                configuration_dict['fields'][column_name].pop(constraint_key)

    return configuration_dict

## Function to write the targetfile to the user input file path
def write_file(input_FILEPATH, output_FILE, input_DELIMITER, input_CONSTRAINTS):
    generate_tdq_configuration(input_FILEPATH, input_DELIMITER, input_CONSTRAINTS)
    json_data = generate_tdq_configuration(input_FILEPATH, input_DELIMITER, input_CONSTRAINTS)
    with open(output_FILE, 'w') as outfile:  
        json.dump(json_data, outfile, indent=4)

## Runs the user inputs from the TDQ executable
def run(filename, targetfile, delimiter, constraints_list):
    input_FILEPATH = str(filename)     
    output_FILE = str(targetfile)   
    input_DELIMITER = delimiter
    input_CONSTRAINTS = constraints_list
    write_file(input_FILEPATH, output_FILE, input_DELIMITER, input_CONSTRAINTS)

