# iTest Commands > File and directory management commands > file mkTempDir command: Create a unique temporary directory > Examples

set mydir [file mkTempDir] returns: [tempdirUri]/iTestTempDir_45376/

set mydir [file mkTempDir my] returns: [tempdirUri]/my45377/

set mydir [file mkTempDir my bah] returns: [tempdirUri]/my45378bah/
