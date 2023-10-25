Here, the 'command.sh' is the required .sh file that executes the extraction command
The final file is 'problem3.tsv' where the Scheme Name and Asset Value fields are stored.

As for the question for storing the data in the json format,
json is a structured data format, but here we are only extracting 2 fields for simplicity. So, storing it in a json format will require more parsing and data transformation since json format stores more nested and structured data. Here, considering we have storage efficiency concers and this is a relatively simple data, so storing it in a more complex json format is not recommended.
