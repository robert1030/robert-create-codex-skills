# Python Session Level Control Library > Working with Sessions > Session Information

Once a session is opened it is possible to find out some basic information about where the session is being handled. This is done via the agent property of a session object.

```
# Use the print command when using a standalone agent
```

```
>>> print(s1.agent)
```

```
{'agent_name': u'USER01-PC', 'agent_type': 'local', 'name': u'USER01-PC', 'capabilities': {u'Product.Arch': u'x86', u'OS.Type': u'win32', u'STC.Version': u'4.69', u'language': u'itest'}, 'protocol_version': u'1.0'}
```
