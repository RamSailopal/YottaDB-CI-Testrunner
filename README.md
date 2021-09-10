# Background

![Alt text](YottaDB-Test-Results.PNG?raw=true "YottaDB Test Results")

This repo is designed for continuous integration testing run pipelines, that analyse entries in the YottaDB database

# Installation

    git clone https://github.com/RamSailopal/YottaDB-CI-Testrunner.git
    
# Prequisites

A working installation of YottaDB installed on the same machine.

A ydb executable in the system path i.e.

    ln -s /usr/local/yottadb/ydb /usr/local/bin/ydb

# Setup and execution

Add the YottaDB global entries to be interogated as the **global** values in the JSON file. Add the values expected as the **value** values. Add the execution action as a command line statment for the **action** value

Run the testrun python script:

    ./testrun.py

Output will appear to screen relating to whether each test passes or fails

# Using an alternate JSON file/location

By default, the testrun script will look for a **test.json** file in the same directory but an alternate JSON file/location can be specified by adding a **-f** or **--file** flag i.e.

    ./testrun.py --file="/tmp/test.json"

# HTML reports

The output from the script can be attained as a HTML report for integration with CI/CD engines such as Jenkins and the HTML publisher plugin:

https://plugins.jenkins.io/htmlpublisher/

Output will appear as in the example image.

To attain a HTML report. add the output flag to the command line and so:

    ./testrun.py -o
