# TDQ Configuration File Application
## Description
The UI application generates a TDQ JSON configuration file with additional metadata about the curation process, such as fields(Schema) and the data quality rules to be applied. The purpose of generating the configuration file is to remove the bulk of the manual work required in creating the file itself.

Users will still need to edit the file after it is produced for the TDQ Lambda to clean and apply TDQ rules defined in the configuration file. 

## Python Scripts
To generate the JSON constraints file, two Python scripts have been created; one that creates the UI application to take user inputs and one that uses the inputs from the application to generate the configuration file.  

- **TDQ_GUI.py**: python source file to create UI application that takes users inputs and runs the JSON configuration file generator script(*TDQ_CONFIG_GENERATOR.py*) in the background.

- **TDQ_CONFIG_GENERATOR.py**: takes the inputs from the UI application and generates a JSON constraints file. 

## Application Inputs
In order for the JSON Configuration file to be produced the following inputs are required:
* ***Raw data file***: file is in CSV format

* ***Target file***: JSON configuration file to be generated at the specified file path

* ***Delimiter***: sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. (e.g. "," in a sequence comma-seperated values)

* ***Constraints(optional)***: verifies datasets meet the constraints in the JSON configuration files

## Installation
### *Prerequisites*  
If you dont have `pyinstaller` or the TDDA python module refer to the below links to install:  

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
