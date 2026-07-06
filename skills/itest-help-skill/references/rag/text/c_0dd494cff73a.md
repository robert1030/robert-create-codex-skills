# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/POST.html > POST

The POST method is used to create new resources. When creating a new resource, POST action to the parent and the service takes care of associating the new resource with the parent and assigns an ID (new resource URI).

Action POST - Create new resources. Returns On successful creation, POST returns HTTP status 201, returning a Location header with a link to the newly-created resource with the 201 HTTP status: Entire List: HTTP 201 (Created), 'Location' header with link to /customers/{id} containing new ID. Specific Item: HTTP 404 (Not Found), 409 (Conflict) if resource already exists. Method POST is neither safe nor idempotent. It is therefore recommended for non-idempotent resource requests. Making two identical POST requests will most-likely result in two resources containing the same information. Example POST http://www.example.com/customers POST http://www.example.com/customers/12345/orders

For details, see the online help: REST action reference.
