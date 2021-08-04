# Background

![Alt text](YottaDB-Test-Results.PNG?raw=true "YottaDB Test Results")

This repo designed for continuous integration testing run pipelines that analyse entries in the YottaDB database

# Installation

    git clone https://github.com/RamSailopal/YottaDB-CI-Testrunner.git

# Setup and execution

Add the YottaDB global entries to be interogated as the global values in the JSON file. Add the values expected as the value values.

Run the testrun python script:

    ./testrun.py

Output will appear to screen relating to whether each test passes or fails

# Using an alternate JSON file/location

By default, the testrun script will look for a test.json file in the same directory but an alternate JSON file/location can be specified by adding a -f or --file flag i.e.

    ./testrun.py --file="/tmp/test.json"

# HTML reports

The output from the script can be attained as a HTML report for integration with CI/CD engines such as Jenkins and the HTML publisher plugin:

https://plugins.jenkins.io/htmlpublisher/

Output will appear as in the example image.

1) Install VSCode
2) Add the **Remote SSH** extension - File - Preferences - Extensions - Remote SSH
3) Once installed, a green button should appear to the bottom left of the VSCode window labelled **Open a Remote Window** Click on this and select **Connect to Host**
4) Select **Add New SSH Host**
5) Enter **ssh username@192.168.240.1 -A** Where username is the username under which yottadb was installed and 192.168.240.1 is the IP address of the server running YottaDB
6) A pop up box should appear titled **Host added!** Click **Connect**
7) Select **Linux** as the platform for the remote host and then proceed to enter the password
8) Once connected, you should be able to **Open Folder** and navigate to the **.yottadb** folder in the user's home directory.
9) Navigate to the routines directory for the YottaDB installation e.g. **/root/.yottadb/r1.30_x86_64/r**
10) You should then be able to see the YottaDB routines listed and be able to double click a routine for editting
11) On the server running YottaDB, add the ydbcompil executable file and allow it to be accessed via the system path i.e. move the file to **/usr/local/bin** Ensure that ydb is also accessable via the system path i.e. **ln -s /usr/local/yottadb/ydb /usr/local/bin/ydb**
12) Back in VSCode Studio, Click File - Preferences - Extensions and add **Run On Save** by **pucelle** (Please note that there are a number of extensions with the same name. Take time to add the correct one)
13) Click on the cog icon for the extension and then **Extension Settings**
14) Click **Edit in settings.json**
15) Copy and paste the text from https://raw.githubusercontent.com/RamSailopal/YottaDB-VSCode/main/settings.json
16) Save the file

A terminal will now open at the bottom of a code edit window and when a routine is amended and saved, the ydbcompil executable will automatically run to compile the code within YottaDB. Any compilation errors will show in the terminal window.

# Additional Optional Setup

**The M/MUMPS/Cache language syntax highlighting and basic formatting** extension by **David Silin** can also by added by following the same procedure as above to add syntax highlighting when editting routines.

https://marketplace.visualstudio.com/items?itemName=dsilin.mumps


