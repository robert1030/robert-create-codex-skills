# iTest Runtime: iTestRT > iTestRT command reference > Option names

The option name listed in the table is the short form of the name. In some cases (fully automated regression, for example) you might want to use the full name. Using the full name for an option ensures that the correct option is used even if more than one module defines an option with the same short name (this can happen when someone develops and registers a new module using the --options option).

For example, the long form of the projects option names begin with:

com.fnfr.open.filesystem.itarproject.itestrtcmdline

Therefore the full name of the --projects.list option is:

--com.fnfr.open.filesystem.itarproject.itestrtcmdline.projects.list

Full names are identified in the table. To view full names for all registered options, use itestrt --verbose
