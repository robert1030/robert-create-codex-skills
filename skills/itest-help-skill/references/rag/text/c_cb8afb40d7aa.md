# Response Maps: Returning Data from Responses > Response Map editor: Pattern page > Defining a Pattern map > 第1段

![*](bullet_blue.jpg) <!-- image_ref -->

1. Click Add to add a new pattern match definition.

1. 2 In the Name box, type a name that represents the values that the pattern will extract. For example, you might name a pattern image_and_database because you can extract both the image text-base and the database from the line (see the example in Step 4).

1. 3 In the Response view, select a fragment of the response that contains only enough text to define the context for the information that you want to extract. Sometimes, to ensure that the text is the unique way to find the value, you will need to include text from the line before or after, or even several lines. There are two options for providing the pattern that includes the matches:

1. 4 In the sidebar, click Add Pattern. iTest pastes the selected lines into the Identifying Text box.

Alternatively, Copy the text and paste the text into the Identifying Text box.

![](images/response_mapping_5.2.jpg) <!-- image_ref -->

iTest immediately attempts to identify values that you want to extract. iTest draws a blue box around each group of interest (numbers, timestamps, IP addresses, and other types of response value that you might typically want to analyze). If you modify the text, iTest immediately updates the groups.(To disable auto-update, uncheck Automatically update definitions to maintain consistency with the text in the Identifying Text box.)

At this point, you have identified one or more tokens (in blue boxes) and queries that extract the token values. The groups of text between the tokens are anchors. Anchors function to locate the tokens whose values you want to extract. By default, iTest creates default names for tokens by using the anchor text. In the example, iTest names the 0x00003000 token Image_text_base and the 0x00C7FC04 token data_base. Depending on the order of the text, iTest might use the text that occurs after a token to form its “best guess” name.

1. 5 If iTest does not specify a token correctly or misses a value that you want to extract, then select the actual value that you want to extract and click Make Token. Other controls:
