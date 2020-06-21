

# Import
import smartsheet
import datetime
import os


# Instantiate smartsheet and specify access token value.
smartsheet = smartsheet.Smartsheet(< ACCESS TOKEN > )

# Get all columns.
action = smartsheet.Sheets.get_columns(< SHEET ID > , include_all=True)
columns = action.data

# Set download path os.path.join is used so I dont have to change
download_path = os.path.join(os.path.expanduser("~"), "Documents")
file_name = "CREMasterData_" + str(datetime.date.today()) + ".xlsx"

# For each column, print Id and Title.
# for col in columns:
#     print(col.id)
#     print(col.title)
#     print('')
# Sample 2: Specify custom filename for the downloaded file
smartsheet.Sheets.get_sheet_as_excel(
    < SHEET ID >,       # sheet id
    download_path,
    file_name
)
