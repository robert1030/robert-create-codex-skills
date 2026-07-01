---
{
  "chunk_id": "itestrt_commands__checking_out_a_runtime_license_321d51792ead73be",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "Checking out a runtime license"
  ],
  "anchor": "1255776",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "321d51792ead73be",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Checking out a runtime license

To execute a test case, test suite, or job, iTestRT must obtain a runtime license by providing the license server address and port number.

| --licenseServer hostAddress:portNumber | hostAddress is the hostname or IP address of the license server host (typically provided by your IT administrator). iTestRT uses port 27000 if you do not specify a port number. To use more than one license server, use the --licenseServer argument multiple times at the command line. Tip Set up multiple license servers in the options file. Example >iTestRT --licenseServer lshost.acme.com:-1 --test project://my_project/test_cases/test1.fftc | Tip | Set up multiple license servers in the options file. |
| --- | --- | --- | --- |
| Tip | Set up multiple license servers in the options file. |  |  |
