# Response Maps: Returning Data from Responses > Overview: Creating a response map > Watch the video > Structured mapping > 第2段

A response map helps to transform unstructured data (in the text response) into structured data (as XML). It also defines a set of queries that can be applied to the structured data to return the data of interest. The Structure view shows all of the structured data that goes along with the response that is shown in the Response view. The Queries view shows a list of predefined queries that can be applied to the structured data. When analysis rules use the “query” extractor, they are applying a query to the structured data to get the information to be returned and analyzed. Any valid XPath query can be used in the analysis rule’s query extractor. But using predefined queries is easier because you can pick them from a list.

> **Note：** About the “blue boxes” The blue boxes that surround certain data in the Response view correspond to data that will be extracted by a predefined query. Clicking one of the boxes and adding an analysis rule is just a another method for selecting the corresponding query in the Queries view and adding an analysis rule from the view.

When you create a response map, it will automatically construct a set of predefined queries that naturally go with the map. For example, on a table map, it will construct queries that extract cell values — possibly based on a key column if one has been defined. As a response map designer, you may find that it is very helpful to the users of your map to provide additional queries beyond what the map creates automatically for you. For example, you may want to create queries that provide meta-data about the response – such as a count of the total number of rows in your table, or the sum of the values of one of the columns in your table. Or you might want to perform arithmetic on certain values to produce another meta-value. All of these things are possible via custom queries.

To add custom queries, choose the Queries tab in the response map editor (along the bottom of the editor) and you can add your own custom queries.



Step 7: Verify the map

Before you are finished, you should make sure that your response map works as you intended.
