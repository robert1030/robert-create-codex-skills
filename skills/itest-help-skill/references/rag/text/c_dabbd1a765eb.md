# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/showtable.html > showTable

Action Name Target Command Description showTable Required Optional For the specified table, return all table contents in table form. Columns are delimited using the tab character.

The Command property specifies the ranges of rows and columns to return. Use the following format. (Index numbers are 1-based -- the first row is number 1, and so on.)

startingRow startingColumn numberOfRows numberOfColumns

If Command is empty, the whole table is displayed.
