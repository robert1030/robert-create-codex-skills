# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/jsonSelect_python.html > jsonSelect

jsonSelect('jsonString', 'queryXpath')

The jsonSelect command takes two arguments. The first argument is the json string. The second argument is the xpath query, and returns the extracted value(typically a single string).

Syntax: jsonSelect('jsonString', 'queryXpath') json_str is the valid json string. xpath is the valid xpath for xml. Example: eval jsonSelect("{'key1':'value1'}", "key1")

Note: The xpath should be a valid xpath for XML (not the JsonPath - http://goessner.net/articles/JsonPath/), otherwise no value is returned. The provided json string will be converted to xml first, and then evaluated using the xpath and gets the specific value.

Note: If the xpath location is not a single value, then an assembled version of sub values will be retrieved.

See also the online help: jsonSelect command.
