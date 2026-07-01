---
{
  "chunk_id": "spirent_testcenter_gui_09__sequencer_control_commands_a1c3b22e35b38e78",
  "source_file": "topics/spirent_testcenter_gui.09.htm",
  "source_original_path": "topics/spirent_testcenter_gui.09.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Sequencer control commands"
  ],
  "heading_path": [
    "Sequencer control commands",
    "Sequencer control commands",
    "Sequencer control commands"
  ],
  "anchor": "1378082",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a1c3b22e35b38e78",
  "level": 2
}
---

# Sequencer control commands > Sequencer control commands > Sequencer control commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| pauseSequencer | — None — |  | Works like the STC API SequencerPause command: Pauses the sequencer. If you execute pauseSequencer while a command is running, the sequencer will pause after the command has finished. While the sequencer is paused and you invoke stepSequencer or startSequencer, Spirent TestCenter resumes command execution from the place that execution was paused. |
| runSequencer | — None — | — None — | Note See the startSequencer command below. Runs all the steps to end. The session is blocked in TestCenter console and GUI when executing runSequencer command. After the sequencer is completed, all steps are not displayed on the console. To display all sequencer steps, execute the showSequencer command. |
| Note | See the startSequencer command below. |  |  |
| showSequencer | — None — | — None — | Returns the current state of the selected sequencer. Possible values: IDLE, WAIT, and PAUSE |
| startSequencer | — None — |  | Gets the sequencer and issues the commands to chassis to start the sequencer. Immediately returns control to the user. |
| stepSequencer | — None — |  | Executes the next step in the sequence. |
| stopSequencer | — None — |  | Stops the current sequence execution. |
| waitSequencer | — None — |  | Waits for the current step in the current sequence to finish. Blocks the call until step is completed. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
