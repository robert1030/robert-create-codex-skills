# Form Maps > Overview: Form Maps > The difference between a form map and a response map

It is important to understand the difference between a form map and a response map. They both are tied to XML documents, but they have very different functions.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A form map describes the elements that make up the page.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A response map applies queries to the structured XML representation of the response to an executed step.

When you are working in GUI testing sessions, you probably need both form maps and response maps:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Form maps identify the targets on the page. As a result, an action like click or showTable can act on the intended element (the target) on the page.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Response maps apply queries to the responses returned by actions like describe or showTable. As a result, you can analyze the data in a response.
