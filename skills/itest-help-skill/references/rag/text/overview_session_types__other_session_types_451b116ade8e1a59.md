---
{
  "chunk_id": "overview_session_types__other_session_types_451b116ade8e1a59",
  "source_file": "topics/overview_session_types.htm",
  "source_original_path": "topics/overview_session_types.htm",
  "toc_path": [
    "iTest Online Help",
    "Welcome to iTest",
    "Session types"
  ],
  "heading_path": [
    "Session types",
    "Session types",
    "Built-in Session Types",
    "Other Session Types"
  ],
  "anchor": "1164231",
  "context_ids": [
    "overview_session_types"
  ],
  "index_keywords": [
    "Python",
    "Python sessions",
    "Ranorex",
    "Ranorex test sessions"
  ],
  "index_keyword_paths": [
    "Python sessions",
    "Ranorex test sessions",
    "sessions > Python",
    "sessions > Ranorex"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "451b116ade8e1a59",
  "level": 3
}
---

# Session types > Session types > Built-in Session Types > Other Session Types

| ADB (Android Debug Bridge) (Custom session) | The ADB (Android Debug Bridge) custom session allows you to communicate with an emulator instance or connected Android-powered device. |
| --- | --- |
| Appium | Appium Test session provides a base automation platform to create custom User Equipment (UE) automation on real handsets for testing iOS and Android devices in the filed. In addition, the Appium session extends a base Python session and provides you with capabilities to run built-in session commands and custom QuickCalls based on the Appium Python automation library. The maximum number of mobile devices used to run multiple Appium sessions depend on your resource capacity. Appium session provides an ability to test all three types of applications: Native, Web and Hybrid applications. |
| CloudStress (Custom session) | The iTest CloudStress session provides way to automate testing and performance verification of your cloud infrastructure, without having to know the scripting languages. |
| Flex/Flash | iTest supports testing Flash applications that were developed using Adobe Flex. iTest can capture your interactions with Flex applications that are hosted on web pages. iTest captures each step of an interactive (manual) test in the Flex application. |
| REST | The REST session window provides a work surface for composing and submitting HTTP requests. Any request that you submit in the iTest session is forwarded to the RESTful service. The service performs the action and returns its normal response. iTest captures all of the actions that you perform in a session and all of the responses. |
| SNMP | A hierarchical browser for getting and setting SNMP MIB data using the Simple Network Management Protocol (SNMP V1, V2c, or V3) defined in RFC 1157 |
| Web Services | The Web Services session window provides a work surface for composing and submitting Web Service requests. Any request that you submit in the iTest session is forwarded to the Web Services server. The Web Service performs the action and returns its normal response. |
| Mail (SMTP) | You can add steps that construct and send email messages during execution. A test case can construct and send as many email messages as are needed. The message body can contain both fixed text and test response and result data. |
| Mail (POP3) | You may se the Mail (POP3) sessions to retrieve emails from subscribers, view content, extract the required text and attachments, save the attached images as individual files, and then insert them into other sessions, for example, Selenium. |
| NetConf | The NetConf session window displays your commands and the device’s responses. You can think of the session window as a terminal — a terminal to a NetConf service as a subsystem that iTest is monitoring and capturing. |
| OpenStack Neutron (Custom sessions) | The OpenStack Neutron session allows you to manage OpenStack Neutron Network such as router, network, subnet, port, security group, virtual network topologies including services such as firewalls, load balancers, and virtual private networks (VPNs), via RESTfull HTTP service. |
| Process | Execute and manage processes on the computer that is running iTest. |
| PowerShell | PowerShell sessions execute commands at the Windows PowerShell prompt. The PowerShell session window displays your commands and the local PC's responses. |
| Ranorex | Ranorex Test session provides ways of automating the Windows, Web, and Mobile UI applications. The seamless testing of these iTest functionalities is achieved by iTest integration with Ranorex application (www.ranorex.com). |
| Serial Port (mandatory) | For Serial Port sessions, the computer running iTest communicates directly over a serial port connection with the device under test. For each open session, the Serial Port session window displays your commands and the device's responses. You can think of the session window as a terminal client — a terminal that iTest is monitoring and capturing. |
| Selenium | For Selenium sessions, iTest opens an instance of the Firefox browser. You interact with the pages in the normal way while iTest captures your actions and responses from the session. |
| Syslog | Each Syslog session monitors the syslog messages that arrive at the built-in iTest syslog server (visible in the Syslog view). While the syslog server receives all messages, any syslog session can filter the messages based on the following property settings in the session profile. As a result of configuring session profile settings, only the messages that meet the filter settings appear in the session window. This enables your test cases to analyze the particular responses (messages) of interest and to ignore irrelevant messages. |
| Wireshark | Wireshark sessions provide a command line interface for interactively capturing packets from a network interface. For commands that return status and packet data, iTest saves the responses as structured data and generates associated queries to simplify pass/fail analysis. |
| TL1 | There are two types of TL1 interface: Automation interface — These interfaces are not meant for human interaction. These interfaces do not return a prompt and might not even echo what the user types. Hybrid interface — These interfaces echo what the user types and return a prompt. The prompt can be a normal one like login: or mydut> or could be TL1 end of message: < or ; |
|  | Automation interface — These interfaces are not meant for human interaction. These interfaces do not return a prompt and might not even echo what the user types. |
|  | Hybrid interface — These interfaces echo what the user types and return a prompt. The prompt can be a normal one like login: or mydut> or could be TL1 end of message: < or ; |
| UDP | For UDP sessions, the computer running iTest communicates directly over UDP (User Datagram Protocol) with the specified device. For each open session, the UDP session window displays your commands and the local echo. Open another session to view the device’s response. You can think of the window as a terminal client — a terminal that iTest is monitoring and capturing. |
| VNC | iTest VNC sessions are intended to help you to control a remote OS to perform configuration/setup/tear-down tasks. iTest VNC sessions are not intended to enable you to thoroughly test an application on a remote platform. |
| VMware vSphere Client | The session window for vSphere sessions in iTest has been designed in partnership with VMware to closely resemble the vSphere client. As a result, you can capture vSphere steps using iTest without having to learn a new interface or new command names. You interact with the iTest session almost exactly like you interact with vSphere. The iTest interface to vSphere enables you to perform and automate a wide range of tasks |
| XML-RPC | The XML-RPC session window provides a work surface for composing and submitting XML-RPC method calls over HTTP and HTTPS. Any request that you submit in the iTest session is forwarded to the XML-RPC service. The service performs the action and returns a response. You can view the response in the Response section of the XML-RPC session window. iTest captures all of the actions that you perform in a session and all of the responses. You can use the captured items to create test case steps that interact with the XML-RPC server. |
