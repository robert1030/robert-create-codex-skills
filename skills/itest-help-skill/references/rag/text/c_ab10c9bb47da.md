# Python Session Level Control Library > Working With Projects > Querying a Project

```
# list all the usable topologies and session profiles in the project
```

```
proj.list()
```

```
==> ['dut1_ffsp', 'lab1_setup_tbml']
```

```
# list other types of assets, such as parameter files and response maps
```

```
proj.list(parameter_file=True, response_map=True)
```

```
==> ['dut1_ffsp', 'lab1_setup_tbml', 'main_setup_ffpt', 'response_map1_ffrm']
```

```
# show all QuickCalls available on a given session profile
```

```
proj.dut1_ffsp.list()
```

```
==> {
```

```
'init_routes': {
```

```
'all': 'True if all routes should be initialized'
```

```
},
```

```
'do_something_cool': {
```

```
'param': 'Description of parameter'
```

```
}
```

```
}
```

```
# access help on QuickCalls on a session attached to a resource in a topology
```

```
proj.lab1_setup_tbml.router1.ssh.list()
```

```
==> { ... same as above }
```

```
# access the list of parameters for a specific QuickCall
```

```
proj.dut1_ffsp.list('init_routes')
```

```
==> { 'all': 'True if all routes should be initialized' }
```

Built in session actions are not listed, only the QuickCalls attached to the session profile. If you are accessing a built-in session type such as Telnet or SSH, they may still invoke the actions, but they will not be listed by the list() call.

> **Note：** Note All displayed QuickCall names will be transformed into snake-case to conform to Python naming conventions.
