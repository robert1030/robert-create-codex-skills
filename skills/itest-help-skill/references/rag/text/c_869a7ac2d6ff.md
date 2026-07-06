# Prompts (in CLI sessions) > Overview: Prompts in iTest > How iTest distinguishes prompts from responses during execution > Learning prompts during interactive (manual) testing

iTest identifies possible prompts by noticing when the session returns text and then goes silent for a significant period of time.

When you close a session, iTest starts the Update Session Profile wizard to show you the list of possible prompts that it noticed during the session. This gives you the opportunity to identify the text strings that actually are prompts. When you finish the wizard, the new prompt definitions are added to the session profile. If needed, you can then use the Session Profile editor to customize the property settings for the prompt.
