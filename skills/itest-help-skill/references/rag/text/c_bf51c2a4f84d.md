# Form Maps > Creating form maps for use with GUI testing test applications > Step 2: Creating the form map

You might typically create a form map for each page that test case developers will work on. In this example, we'll create a form map for the Google home page.

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/form_maps.03.jpg) <!-- image_ref -->

1. In the Response view, click New Form Map .

1. 2 iTest opens the New Form Map wizard to ask you whether to save the form map into a new Form Map library or an existing library. (If this is the first form map to be created, then you'll first create a Form Map library and then add the new form map to it. More about Form Map libraries later.)

![](images/form_maps.04.jpg) <!-- image_ref -->

1. 3 In the Form map library field, we type the name for a new library. Form map libraries are iTest projects that hold form maps (more on libraries later).

Because we expect to save the form maps for all of the google pages in this library, we’ll name it google_form_maps.

The page displays the XML map of the page (the DOM) in the Sample box and suggests the default name new_form_map. Because the form map represents the home page, we’ll call it google_home (form maps use the .fffm filename extension).

When you're ready, click Next.

![](images/form_maps.05.jpg) <!-- image_ref -->

1. 4 Now, the wizard offers to auto-generate targets based on the DOM.

In the test case that we plan to write, we'll add a step that clicks the Advanced Search link on the home page, so let's allow the wizard to generate the targets on the page (hopefully, the Advanced Search link target will be included in the set of targets that the wizard generates.).

In addition, let's allow the wizard to associate the Form Map library that we just created with the session profile. This ensures that, whenever we start a session using the session profile, iTest knows to look into the new Form Map library to find the appropriate form map for a step.

![](images/form_maps.06.jpg) <!-- image_ref -->

1. 5 Click Finish to save the new form map. iTest opens the Form Map editor to the Samples page and creates a sample.

iTest populates the XML Data Viewer field with the XML description of the home page that we got with the snapshot. This is where we'll find the targets that appear on the page.

Tip The sample name is unimportant unless you expect more than one format for this web page (for example, when the page displays one set of configuration options or another, depending on the device model).

![](images/form_maps.07.jpg) <!-- image_ref -->
