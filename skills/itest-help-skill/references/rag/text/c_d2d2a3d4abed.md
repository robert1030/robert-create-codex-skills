# Response Maps: Returning Data from Responses > Overview: Creating a response map > Watch the video > Structured mapping > 第3段

When you have your response map open in an editor, the Step Issues view will show you any response mapping problems encountered when mapping the sample(s) associated with that map. You should resolve all of these issues. It is common for a response map to work properly with one sample response, but fails for another sample. So it is a good idea to find two or three different samples of the response that the map is intended for. You can add these samples on the Samples page in the response map editor, and the Step Issues window will show you if there are any problems mapping against any of the samples.

The Queries view will show you a list of all of the predefined queries associated with the current response map as well as the result of applying that query to the selected response sample. This is the list that users will see when trying to add analysis rules to a step that uses this response map. So make sure that this list contains all of the queries that you would want a user to have access to. Make sure the names are meaningful to other users.

The Response view will show the sample response with blue boxes around all data in the response that has been properly mapped. If there are missing blue boxes, these should be investigated and resolved.



Step 8: Use the map

If your response map has been stored in a response map library, and you have configured the appropriate applicability data, then your response map should be automatically associated with steps in test cases accordingly. You should check that this is working properly.

In other cases, you will need to associate the response map with the step explicitly. You do this on the Expected Response page under “Other Post-processing” within the step properties in the test case editor.

We recommend that you associate response maps with test case procedures. This is a nice way to provide “blue boxes” for the text returned in a reusable procedure. You associate a response map with the procedure using the Response Map property on the Procedure property page in the test case editor.
