# Smartsheet
Export smartsheet specific sheet contents to an Excel file

This python code uses your access token and a specific sheet ID that you can copy from your Smartsheet properties to export this sheet contents including all columns to an Excel File.
This code was created in Mac OS.
The file path for the download is set as the Documents folder.

In order to run this code, please replace
1. ACCESS TOKEN : Add in your access token in single quotes
2. SHEET ID : Add in the sheet ID from your report properties in single quotes
3. download_path : Change download path variable to a folder you want. The advantage of using
os.path.join is that you dont need to change the slashes when running this code in windows
versus Mac
# Smartsheet
 Export Smartsheet sheet contents to an Excel File
