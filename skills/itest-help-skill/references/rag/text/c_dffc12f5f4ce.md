# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/DELETE.html > DELETE

The DELETE method is used to delete/remove a resource identified by a URI.

Action DELETE - use to delete/remove a resource identified by a URI. Returns Successful deletion returns: - HTTP status 200 (OK) along with a response body, that is, representation of the deleted item (may take too much bandwidth), or a wrapped response - HTTP status 204 (NO CONTENT) with no response body. Note: HTTP status 204 status with no body, or the JSEND-style response and HTTP status 200 are the recommended responses. Entire List: HTTP 404 (Not Found), unless you want to delete the whole collectionnot often desirable. Specific Item: HTTP200 (OK). 404 (Not Found), if ID not found or invalid. Method The DELETE operation is considered idempotent. Deleting action removes a resource and repeatedly calling DELETE on that resource results with the response: as the resource does not exist. Calling DELETE on a resource a second time returns a HTTP 404 (NOT FOUND) since it was already removed and cannot be found. Example DELETE http://www.example.com/customers/12345 DELETE http://www.example.com/customers/12345/orders DELETE http://www.example.com/bucket/sample

For details, see the online help: REST action reference.
