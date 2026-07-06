# Python Session Level Control Library > Working with Sessions > Invoking Actions on Session

An active session has a number of actions associated, which may be either built-in actions or QuickCalls defined on that session type. Any of those can be invoked on the session.

```
# invoke the init_routes QuickCall with one parameter
```

```
response = s1.init_routes(all="True")
```

```
# invoke a built-in action with a specific response map (which may override what was set for the session as a whole)
```

```
response = my_ssh_session.command('ls', response_map="proj.response_map_ls_ffrm")
```
