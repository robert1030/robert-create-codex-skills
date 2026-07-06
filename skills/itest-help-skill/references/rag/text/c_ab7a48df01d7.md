# iTest Commands > File and directory management commands > file move command: Move or rename files to a destination URI > Description

See Guidelines for using URIs in file commands.

You can use the * wildcard character in the sourceURI but not in destinationURI

![*](bullet_blue.jpg) <!-- image_ref -->

- sourceURI must be for an existing folder or files; an error occurs if the source does not exist.

![*](bullet_blue.jpg) <!-- image_ref -->

- If sourceURI is a directory name, then destinationURI is interpreted as a directory name.

![*](bullet_blue.jpg) <!-- image_ref -->

- If sourceURI is a filename, then:

![*](bullet_blue.jpg) <!-- image_ref -->

- If there is no directory with that name, sourceURI is interpreted as a filename (equivalent to rename)

![*](bullet_blue.jpg) <!-- image_ref -->

- If there is an existing directory with that name, the new file is created (with the source filename) in the destination directory

![*](bullet_blue.jpg) <!-- image_ref -->

- If multiple source files are specified (by using the * wildcard character in the last segment of sourceURI), then the destination is interpreted as a directory.

![*](bullet_blue.jpg) <!-- image_ref -->

- Use the * wildcard in URI to represent directories or subdirectories.

![*](bullet_blue.jpg) <!-- image_ref -->

- If needed, the destination directory and appropriate parent folders are created.
