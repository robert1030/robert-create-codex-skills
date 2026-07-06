# Wireshark sessions > Session profile property settings for Wireshark sessions > Example Wireshark session > 第2段

```
5 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 32, Ack: 0, Len: 894
```

```
6 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 926, Ack: 0, Len: 512
```

```
7 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 1438, Ack: 0, Len: 247
```

```
8 | 0.312 | 10.155.0.145 | 10.155.0.59 | tcp | Transmission Control Protocol, Src Port: 3389 (3389), Dst Port: 1061 (1061), Seq: 1685, Ack: 0, Len: 192
```

```
9 | 0.494 | 10.155.0.59 | 10.155.0.145 | tcp | Transmission Control Protocol, Src Port: 1061 (1061), Dst Port: 3389 (3389), Seq: 0, Ack: 926, Len: 0
```

```
10 | 0.497 | 10.155.0.59 | 10.155.0.145 | tcp | Transmission Control Protocol, Src Port: 1061 (1061), Dst Port: 3389 (3389), Seq: 0, Ack: 1685, Len: 0
```

```
Wireshark>
```

// Now use capture run to capture 4 packets and wait for capture to finish (in this case 4 packets are captured but only 2 packets are loaded because of the read filter. Use filter set to clear the read filter and show all captured packets)

// The value 4 (in bold) changes from 0 to 4 while the packets are captured.

```
Wireshark>capture run -c 4
```

```
Capture started...
```

```
Capturing on Broadcom NetXtreme Gigabit Ethernet Driver (Microsoft's Packet Scheduler)
```

```
4
```

```
Capture finished, 4 packets captured
```

```
Loading ... done
```

```
Total of 2 packets loaded
```

```
Wireshark>filter set
```

```
Updating filter ... done
```

```
Total of 4 packets reloaded
```

```
Wireshark>
```

// Now start capture, optionally execute some other steps (which might generate some packets) and then wait for capture to complete.

```
Wireshark>capture start -c 200
```

```
Capture started...
```

```
Capturing on Broadcom NetXtreme Gigabit Ethernet Driver (Microsoft's Packet Scheduler)
```

```
Wireshark>
```

```
Wireshark>
```

```
Wireshark>capture wait
```

```
200
```

```
Capture finished, 200 packets captured
```

```
Loading ... done
```

```
Total of 200 packets loaded
```

```
Wireshark>
```
