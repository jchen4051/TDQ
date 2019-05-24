# TDQ Configuration File Generation
## Description
The TDQ JSON configuration file containts additional metadata about the curation process, such as fields(Schema) and the data quality rules to be applied. The purpose of generating the configuration file via the command line interface (CLI) or the UI application is to remove the bulk of the manual work required in creating the file itself.

Users will still need to edit the file after it is produced for the TDQ Lambda to clean and apply TDQ rules defined in the configuration file. 

## Python Scripts
To generate the JSON constraints file, two Python scripts have been created; one that creates the UI application to take user inputs and one that uses the inputs from the application to generate the configuration file. The python script that generates the configuration file can also be run via the CLI by parsing the necessary inputs.

- **TDQ_GUIv2.py**: python source file to create UI application that takes users inputs and runs the JSON configuration file generator script(*TDQ_CONFIG_GENERATOR.py*) in the background.

- **TDQ_CONFIG_GENERATORv2.py**: takes the inputs from the UI application and generates a JSON constraints file. This file can also be run via the CLI to generate the configuration file (further information in **Generating via the CLI**).

## Inputs
In order for the JSON Configuration file to be produced the following inputs are required:
* ***Raw data file***: file is in CSV format

* ***Target file***: JSON configuration file to be generated at the specified file path

* ***Delimiter***: sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. (e.g. "," in a sequence comma-seperated values)

* ***Constraints(optional)***: verifies datasets meet the constraints in the JSON configuration files

## Application Installation
### *Prerequisites*  
If you dont have `pyinstaller` or the **TDDA python module** refer to the below links to install:  

**TDDA Python Module**:
* http://www.tdda.info/obtaining-the-python-tdda-library: `discover_df` in `tdda.constraints` is used to discover constraints in the data.  

**Pyinstaller**:
* https://pypi.org/project/PyInstaller/: collects information about your Python script and all modules and libraries your script needs to execute.    

### *Installation Steps*

From the command line install TDQ_GUI.py as a single executable application using pyinstaller from the file path the Python scripts are located:  

    <File path> pyinstaller.exe --onefile --windowed TDQ_GUI.py

* `--onefile` is used to package everything into a single executable. If you do not specify this option, the libraries, etc. will be distributed as separate files alongside the main executable.  

* `--windowed` prevents a console window from being displayed when the application is run. If you're releasing a non-graphical application (i.e. a console application), you do not need to use this option.  

This will install the application as **TDQ_GUI.exe** in the newly created folder *dist*.  

## Using the Application 
Refer to **Application Inputs** for further information on the inputs requested by the application.
1. Open the ***TDQ_GUI.exe*** application.
2. Select ***Open file*** to choose the data file to be read.
3. Select ***Save as...*** to specify the target file name and file path to save the JSON configuration file
4. Specify the ***delimiter** in the entry box
5. Select the constraints you want to search for in the data by checking the boxes 
6. Click ***Generate*** to start the file generation process. Success message will pop up once the file has been generated. 
7. Click ***Clear*** to reset all fields. 

## Generating via the CLI
Using the script **TDQ_CONFIG_GENERATORv2.py** enter the **inputs** as shown below via the CLI to generate the configuaration file:  

    <File path> python TDQ_CONFIG_GENERATORv2.py -f <Data file path> -t <Output file path/name> -d "<Delimiter>" -c "[constraints list]"
* `-f` Parse in the file path of the CSV data to be read. 
* `-t` Users can specify the filepath and name where the configuration file is output. Alternatively specifying just the filename will output the file in the current file path. 
* `-d` Users need to specify the delimiter between "". If no delimiter is specifed the default "," will be used. 
* `-c` Users need to parse a list of constraints required in the configuration file between ""(e.g. "['constraint1', 'constraint2']"). 

## Example Configuration File   
    {
        "delimiter": ",",
        "enclosedinquotes": "<EDIT HERE>",
        "maximumrows": "<EDIT HERE>",
        "partition_col": "<EDIT HERE>",
        "list_of_partitions": [
            "<EDIT HERE>",
            "<EDIT HERE>",
            "<EDIT HERE>",
            "<EDIT HERE>"
        ],
        "noOfCOl": 44,
        "header": "<EDIT HERE>",
        "fields": {
            "SourceUnitName": {
                "datatype": "string",
                "min_length": 12,
                "max_length": 12,
                "nullable": "false",
                "listofvalues": [
                    "BND2-ASG-001"
                ]
            },
            "PeriodStartTime": {
                "datatype": "string",
                "min_length": 24,
                "max_length": 24,
                "nullable": "false",
                "listofvalues": [
                    "2019-03-13T18:55:00+1100"
                ]
            },
            "PeriodEndTime": {
                "datatype": "string",
                "min_length": 24,
                "max_length": 24,
                "nullable": "false",
                "listofvalues": [
                    "2019-03-13T19:00:00+1100"
                ]
        },...

## Additional Information  
* `<EDIT HERE>` requires manual input from users in the configuration file.
* Users should input a column header row in the CSV data if a header row isn't present already.
