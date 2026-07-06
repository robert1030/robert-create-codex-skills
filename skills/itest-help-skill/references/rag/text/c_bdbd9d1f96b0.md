# iTest Commands > File and directory management commands > file move command: Move or rename files to a destination URI > Response

Returns the number of files moved.

Returned count is 0 when empty directories are moved or renamed.

Returned count is limited to 5000 to ensure reasonable performance after a large directory has been moved or renamed. This does not limit the number of files moved.
