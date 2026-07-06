# Response Maps: Returning Data from Responses > Response Map editor Block page: Creating a block map > Configure the tokens in the block > 第2段

> **Note：** Note Alternatively, you could select the full 255/255 text and name the token mask. Then, in the Advanced Matching Constraints section, check Match only on one of the following values and specify the value 255/255.

1. 4 iTest incorrectly identified ARPA in the last line as a static word. Now, let us configure it as the arp_type token because this field will take on different values that we want test case steps to return and analyze. Right-click the text and select Set token > Advanced token properties. The Token properties page opens. The name of the token appears in the Name box, and the token is correctly configured as Variable (the field can take other values that the ARPA text in the response sample). Now, in the Advanced Matching Constraints section, check Match only on one of the following values and then type each value that you expect in responses, as in this example:

![](images/response_mapping_3.8.jpg) <!-- image_ref -->

1. 5 At this point, we have configured all of the named tokens in the response. The next step is to define the properties of the blocks in the response, as discussed in Response Map editor: Block Map properties.
