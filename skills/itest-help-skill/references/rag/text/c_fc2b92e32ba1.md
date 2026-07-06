# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/OPTIONS.html > OPTIONS

The OPTIONS method represents allows the client to determine the options and/or requirements associated with a resource, or the capabilities of a server, without implying a resource action or initiating a resource retrieval.

Action OPTIONS - determines the options and/or requirements associated with a resource, or the capabilities of a server. - If the Request-URI is an asterisk (*), the OPTIONS request applies to the server in general rather than to a specific resource. - If the Request-URI is not an asterisk (*), the OPTIONS request applies only to the options that are available when communicating with that resource. Returns HTTP200 response includes any header fields that indicate optional features implemented by the server and applicable to that resource (e.g., Allow). Method Is inherently idempotent as it has no side effects. Example OPTIONS /users/me returns: 200 OK Allow: HEAD,GET,PUT,DELETE,OPTIONS

For details, see the online help: REST action reference.
