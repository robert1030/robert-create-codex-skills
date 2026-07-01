---
{
  "chunk_id": "ilo__intro_80a670e321d0aa0a",
  "source_file": "popups/ilo.html",
  "source_original_path": "popups/ilo.html",
  "toc_path": null,
  "heading_path": [
    "ilo.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "80a670e321d0aa0a",
  "level": 0
}
---

# ilo.html

To run a test case associated with a Velocity topology (using the ilo command to retrieve information about the active topology), specify the following parameters:

| ---iloLogin userName ---iloPassword password: | Specify the username/password credentials to use to access the Velocity server. |
| --- | --- |
| --iloServer URI /ilo: | URI is the hostname or IP address of the Velocity virtual appliance. The URI is followed by �/velocity� Example: --velocityServer http://velocity.acme.com/ilo --reservationId reservationId: If there is more than one active reservation for the topology associated with the test case, then you must specify a value for the --reservationId option. When there is only one active reservation of the topology, then you do not need to specify a value for --reservationId |

Example: itestrt --licenseServer lshost.acme.com:27000 --iloServer http://ilo.acme.com/ilo --iloLogin Apurba --iloPassword yikes --reservationId 1e4371d0-e8f2-4ecb-91e2-b1e67535b867 --itar C:\itars --test project://my_project/test_cases/telnet3.fftc
