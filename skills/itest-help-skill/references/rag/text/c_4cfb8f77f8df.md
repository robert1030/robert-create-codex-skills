# iTest Commands > File and directory management commands > file mkTempDir command: Create a unique temporary directory

Create a unique temporary directory named iTestTempDir_*, where * is a random number, in the location set by the java.io.tmpdir property.

By default, the temporary directory and its contents are deleted when the current test case execution has completed (or aborted). Use the -k option to keep the directory.
