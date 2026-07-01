---
{
  "chunk_id": "response_mapping_03__limitations_of_the_auto_mapping_feature_76ba9c065ec986a3",
  "source_file": "topics/response_mapping.03.htm",
  "source_original_path": "topics/response_mapping.03.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Overview: Creating a response map"
  ],
  "heading_path": [
    "Overview: Creating a response map",
    "Overview: Creating a response map",
    "Watch the video",
    "Limitations of the Auto-mapping feature"
  ],
  "anchor": "1603892",
  "context_ids": [],
  "index_keywords": [
    "automatic",
    "automatic response mapping",
    "limitations"
  ],
  "index_keyword_paths": [
    "automatic response mapping",
    "automatic response mapping > limitations",
    "response mapping > automatic"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "76ba9c065ec986a3",
  "level": 4
}
---

# Overview: Creating a response map > Overview: Creating a response map > Watch the video > Limitations of the Auto-mapping feature

- Auto-mapping does not find tables where the row count is less than or equal to 2.

- Auto-mapping does not process responses larger than 250 lines.

- Auto-mapping can become confused by table rows that wrap onto a newline. This is a tricky problem to map manually as well. We recommend that you increase the terminal width so that response does not wrap on a new line.

An alternative is to create a new response map from scratch. You select File > New > iTest > Response Map from the main menu. This will create a new response map file at the location you request but will not populate it in any way.



Step 4: Choose mapping technology

iTest response maps can use different mapping technologies to return structured data from the unstructured textual response. There are three types of mapping currently supported: pattern-based, table-based, and block-based. Each of these technologies is optimized for different types of responses. You can combine these if your response contains different portions that are best mapped with different technologies.

Auto-mapping

If you requested automatic response map generation in the Response Map Wizard, then you may be starting with a map that already contains one or more different mapping technologies. Otherwise, you need to select one of the mapping technologies from the General page of the response map editor. To decide which one to use, review the following:

Table-based mapping

You will use table-based mapping if the response contains a classic table made up of rows and columns where each row is represented by a single line of text in the response. If the same table appears multiple times in the response, a single table map can handle that. If the response contains multiple tables with different structures, you can use multiple table map definitions in the same response map.

Pattern-based mapping

You will use pattern-based mapping in most other cases (except as discussed below for block-based mapping). This technology uses regular expressions without requiring that you be an expert in regular expression syntax. You select a line or sequence of lines in the sample response and identify the tokens within those lines that you want to return. The pattern mapper constructs a sequence of regular expressions for you.

Block-based mapping

Block-based mapping is typically used only for the most complex responses. These responses typically have repeating and/or nested multi line structures within them. These structures may be slightly variable and/or optional. You want to return data and usually want to key it to some header information in these structures or “blocks”. Block mapping is powerful, but requires some experience in order to create robust maps.

Structured mapping

Responses that have well-defined structure (XML, TL1, JSON, YAML) are mapped by built-in mappers.



Step 5: Construct the map

Once you have chosen the appropriate response mapping technology, you need to populate the properties of the map accordingly. This will depend on which technology (or technologies) you have chosen to use.

In the response map editor, click the editor tab corresponding to the technology of interest — “Pattern”, “Table”, and so on. If you used automatic map generation, the page may already be populated with information that you can then further modify. If not (or automatic map generation was unable to help), then you need to populate that information yourself.

You should be in the iTest Response Mapping perspective. (If not, use the Switch Perspective button along the top to switch to this perspective.) The Response view should be populated with the sample contained in your response map. (If you have multiple samples, you can select a different one in the Samples page in the editor, and that one will then show up in the Response view.) To help you get started, there is a sidebar that may be visible that is like a mini-wizard that can help you get started with the map creation – depending on the type of technology you are using. For a table map, for example, as soon as you create a new table map definition (by clicking in the Table editor page), you will see buttons in the sidebar of the Response view that will guide you through the process of identifying the table banner, footer, columns, and so on. For Pattern mapping, you will see a button that lets you create a new pattern using the lines selected in the Response view.

While these aids can be helpful, you will still need to understand how the mapping technology works so that you can customize it to your own situation. The maps contain many configurable properties that allow you to tightly control how data will be returned.



Step 6: Add custom queries (optional)

A response map helps to transform unstructured data (in the text response) into structured data (as XML). It also defines a set of queries that can be applied to the structured data to return the data of interest. The Structure view shows all of the structured data that goes along with the response that is shown in the Response view. The Queries view shows a list of predefined queries that can be applied to the structured data. When analysis rules use the “query” extractor, they are applying a query to the structured data to get the information to be returned and analyzed. Any valid XPath query can be used in the analysis rule’s query extractor. But using predefined queries is easier because you can pick them from a list.

> **Note:** About the “blue boxes” The blue boxes that surround certain data in the Response view correspond to data that will be extracted by a predefined query. Clicking one of the boxes and adding an analysis rule is just a another method for selecting the corresponding query in the Queries view and adding an analysis rule from the view.

When you create a response map, it will automatically construct a set of predefined queries that naturally go with the map. For example, on a table map, it will construct queries that extract cell values — possibly based on a key column if one has been defined. As a response map designer, you may find that it is very helpful to the users of your map to provide additional queries beyond what the map creates automatically for you. For example, you may want to create queries that provide meta-data about the response – such as a count of the total number of rows in your table, or the sum of the values of one of the columns in your table. Or you might want to perform arithmetic on certain values to produce another meta-value. All of these things are possible via custom queries.

To add custom queries, choose the Queries tab in the response map editor (along the bottom of the editor) and you can add your own custom queries.



Step 7: Verify the map

Before you are finished, you should make sure that your response map works as you intended.

When you have your response map open in an editor, the Step Issues view will show you any response mapping problems encountered when mapping the sample(s) associated with that map. You should resolve all of these issues. It is common for a response map to work properly with one sample response, but fails for another sample. So it is a good idea to find two or three different samples of the response that the map is intended for. You can add these samples on the Samples page in the response map editor, and the Step Issues window will show you if there are any problems mapping against any of the samples.

The Queries view will show you a list of all of the predefined queries associated with the current response map as well as the result of applying that query to the selected response sample. This is the list that users will see when trying to add analysis rules to a step that uses this response map. So make sure that this list contains all of the queries that you would want a user to have access to. Make sure the names are meaningful to other users.

The Response view will show the sample response with blue boxes around all data in the response that has been properly mapped. If there are missing blue boxes, these should be investigated and resolved.



Step 8: Use the map

If your response map has been stored in a response map library, and you have configured the appropriate applicability data, then your response map should be automatically associated with steps in test cases accordingly. You should check that this is working properly.

In other cases, you will need to associate the response map with the step explicitly. You do this on the Expected Response page under “Other Post-processing” within the step properties in the test case editor.

We recommend that you associate response maps with test case procedures. This is a nice way to provide “blue boxes” for the text returned in a reusable procedure. You associate a response map with the procedure using the Response Map property on the Procedure property page in the test case editor.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
