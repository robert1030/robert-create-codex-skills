# Response Maps: Returning Data from Responses > Overview: Creating a response map > Watch the video > Structured mapping > 第1段

Responses that have well-defined structure (XML, TL1, JSON, YAML) are mapped by built-in mappers.



Step 5: Construct the map

Once you have chosen the appropriate response mapping technology, you need to populate the properties of the map accordingly. This will depend on which technology (or technologies) you have chosen to use.

In the response map editor, click the editor tab corresponding to the technology of interest — “Pattern”, “Table”, and so on. If you used automatic map generation, the page may already be populated with information that you can then further modify. If not (or automatic map generation was unable to help), then you need to populate that information yourself.

![](images/response_mapping.2.jpg) <!-- image_ref -->

You should be in the iTest Response Mapping perspective. (If not, use the Switch Perspective button along the top to switch to this perspective.) The Response view should be populated with the sample contained in your response map. (If you have multiple samples, you can select a different one in the Samples page in the editor, and that one will then show up in the Response view.) To help you get started, there is a sidebar that may be visible that is like a mini-wizard that can help you get started with the map creation – depending on the type of technology you are using. For a table map, for example, as soon as you create a new table map definition (by clicking in the Table editor page), you will see buttons in the sidebar of the Response view that will guide you through the process of identifying the table banner, footer, columns, and so on. For Pattern mapping, you will see a button that lets you create a new pattern using the lines selected in the Response view.

While these aids can be helpful, you will still need to understand how the mapping technology works so that you can customize it to your own situation. The maps contain many configurable properties that allow you to tightly control how data will be returned.



Step 6: Add custom queries (optional)
