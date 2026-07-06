# Python Session Level Control Library > Nested Commands and responses > 第1段

You may retrieve nested commands and responses within a QuickCall invoked in your Python SLC session. In addition, process nested responses to collect any information on steps completed, interactively cancel execution in case any any error is encountered.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The Python SLC library protocol has the ability to receive nested steps.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Steps are collected into tree structure ResponseStepContainer, which holds limited number of steps (500) in memory/disk cache and hold large responses on disk cache.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Structure will be accessible for traversing data and to render a basic text output representation.

The ResponseStepContainer class contains the following methods

```
class ResponseStepContainer(object):
```

```
def step_count(): # Will return number of steps available.
```

```
pass
```

```
def get_step(index): # Will return child ResponseStepContainer
```

```
pass
```

```
def response(): # Will return SessionActionResponse
```

```
pass
```

```
def action(): # Will return SessionAction object for this step, for root step
```

SessionAction will be constructed based on parameters passed.

```
pass
```

```
def __iter__(self): # will return iterator over current children's.
```

```
pass
```

The SessionActionResponse object will contain a property nested_steps → which returns Responsestepcontainer or Nil, if there are no nested steps.

The following is an example of Streamline processing of events..

```
class MyResponseListener(SessionActionListener):
```

```
def process_response( self, session, step_container):
```

```
print("Action received: ", step_container.action.command, "\nResponse: ", step_container.response)
```

```
def process_start( self, session, session_action):
```

```
# Will be called before execution of command
```

```
print("Start")
```

```
def process_done( self, session, step_container):
```

```
# Will be called after final response will be recieved
```

```
print("Done")
```

```
s = slc.my_session.open()
```

```
s.response_listener = MyResponseListener()
```

```
# So calls
```

```
s.command('ifconfig')
```

```
#will print
```

```
Start
```

```
Action received: ifconfig
```

```
Response: ..... Some response here .....
```

As not every action contains nested steps, a property named "process_nested_steps=True" is passed to the SessionActionCommand.
