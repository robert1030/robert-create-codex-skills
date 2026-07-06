# Response Maps: Returning Data from Responses > Response Map editor: Samples page > Configuring a sample response

While you work on a response sample in the Samples page, the Response, Structure, Queries, and Step Issues views provide auto-updated feedback on how the response map will operate.

1. 1 The New Response Map wizard (or Add this Response to an Existing Response Map) populates the Command and Response text boxes. (If you are adding a sample response manually [not typical] you paste the values into the appropriate text boxes.)

You can edit the Response text as needed, but remember that all mappers that you define map against the text in this box (not an issue if you intend to use the sample as an emulated response).

![](images/rme_samples_page.png) <!-- image_ref -->

1. 2 The Sample name defaults to sample1

> **Note：** Note The Sample name is not important if the response always appears in only one format and this is the only sample that you will use for mapping the response. The Sample name serves to uniquely identify each of multiple response formats.

The name is important only in either of the following cases:

![*](bullet_blue.jpg) <!-- image_ref -->

- You plan to provide more than one sample for the response map. We recommend that you use a name that reflects the particular software revision or other command category that results in the different response. If you’re adding a second or third format of a response, you might include text that identifies the format of the response

![*](bullet_blue.jpg) <!-- image_ref -->

- You intend to use the response map only to supply an emulated response. The Sample name property in the Emulation property group for the step will refer to this sample name.
