---
{
  "chunk_id": "pal_slc_nested_commands_and_responses__nested_commands_and_responses_6d0964ebaab78f0b",
  "source_file": "topics/pal_slc_nested_commands_and_responses.htm",
  "source_original_path": "topics/pal_slc_nested_commands_and_responses.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Nested Commands and responses"
  ],
  "heading_path": [
    "Nested Commands and responses",
    "Nested Commands and responses"
  ],
  "anchor": "1497805",
  "context_ids": [
    "pal_slc_nested_commands_and_responses"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "6d0964ebaab78f0b",
  "level": 1
}
---

# Nested Commands and responses > Nested Commands and responses

You may retrieve nested commands and responses within a QuickCall invoked in your Python SLC session. In addition, process nested responses to collect any information on steps completed, interactively cancel execution in case any any error is encountered.

- The Python SLC library protocol has the ability to receive nested steps.

- Steps are collected into tree structure ResponseStepContainer, which holds limited number of steps (500) in memory/disk cache and hold large responses on disk cache.

- Structure will be accessible for traversing data and to render a basic text output representation.

The ResponseStepContainer class contains the following methods

| class ResponseStepContainer(object): def step_count(): # Will return number of steps available. pass def get_step(index): # Will return child ResponseStepContainer pass def response(): # Will return SessionActionResponse pass def action(): # Will return SessionAction object for this step, for root step SessionAction will be constructed based on parameters passed. pass def __iter__(self): # will return iterator over current children's. pass |
| --- |

The SessionActionResponse object will contain a property nested_steps → which returns Responsestepcontainer or Nil, if there are no nested steps.

The following is an example of Streamline processing of events..

| class MyResponseListener(SessionActionListener): def process_response( self, session, step_container): print("Action received: ", step_container.action.command, "\nResponse: ", step_container.response) def process_start( self, session, session_action): # Will be called before execution of command print("Start") def process_done( self, session, step_container): # Will be called after final response will be recieved print("Done") s = slc.my_session.open() s.response_listener = MyResponseListener() # So calls s.command('ifconfig') #will print Start Action received: ifconfig Response: ..... Some response here ..... |
| --- |

As not every action contains nested steps, a property named "process_nested_steps=True" is passed to the SessionActionCommand.

> **Note:** Note The property "process_nested_steps=True"is either configured in SessionProfile or passed via a parameter to individual call.

| s = slc.my_session.open() #s.set_process_nested_steps(True) # Enable all steps for every execution. r = s.command('ifconfig', process_nested_steps=True) ## Enable all steps mode processing. r.steps # Will return ResponseStepContainer object with information about all steps. print(r.steps) # Will call __str__ with a short plain text report output Will print:""" 1.1 call my_quick_call 1.2 eval a = 20 1.3 call my_nested_call -a 20 1.3.1 eval b = 20 1.3.2 print(a+b) Response: 40 1.3.3 return 30 """ |
| --- |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
