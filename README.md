# Curation Validation Configuration File Template Generator
## Description
The curation validation configuration file holds field level configuration on data feeds being ingested into the BERI 2.0 data-lake. Each data feed will have its own configuration file

The configuration file template generator reads in a raw data file and generates a YAML template with the required validation details and some field level configuration properties (e.g. datatype, max_length, nullable, colOrder) and values specific to that data feed.

The template provides a generic set of configuration properties and values and should still be edited and checked before being used. 

## Inputs Via CLI
The create the configuration template for a data feed the following inputs are required via the command line:

* ***-m Raw data file***: the file path of the raw data

* ***-s Source***: the source system of the raw data file

* ***-f Data feed***: the specific stream of data from the source system

* ***-d Delimiter(optional)***: sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. (e.g. "," in a sequence comma-seperated values). If no delimiter is specified the default ',' will be used. 

## Example Configuration Template File
    {
        csv_null_string: <string>
        datafeed: <string>
        delimiter: ','
        enclosedInQuotes: <boolean>
        error_log_delimiter: <string>
        header: <boolean>
        listOfPartitions:
        - <EDIT HERE>
        - <EDIT HERE>
        - <EDIT HERE>
        - <EDIT HERE>
        noOfCOl: 115
        partitionCol: <string>
        permit_empty: <boolean>
        source: <string>
        fields:
            AccountNumber:
                colOrder: 1
                datatype: string
                max_length: 11
                nullable: false
            AccountNumberCalc__c:
                colOrder: 2
                datatype: string
                max_length: 10
                nullable: false
            AccountSource:
                colOrder: 3
                datatype: real
                max_length: 3
            AnnualRevenue:
                colOrder: 4
                datatype: real
                max_length: 3
            BillingCity:
                colOrder: 5
                datatype: string
                max_length: 12
            ...
        }
        
## Additional Information  
* `<EDIT HERE>` requires manual input from users in the configuration file.
* Users should input a column header row in the CSV data if a header row isn't present already.
