# budget-tracker

A basic Python application for use with the [UP Bank API](https://developer.up.com.au/).

## Dependencies
[python-dotenv](https://github.com/theskumar/python-dotenv), [XlsxWriter](https://github.com/jmcnamara/XlsxWriter)

## Instructions to run
Create a `.env` file in the root directory of the project with the following entry `UP_API_KEY=$up_key` (replace `$up_key` with your key retrieved from the up website).

Run using `python main.py`. Spreadsheet will be put in the `output` folder.