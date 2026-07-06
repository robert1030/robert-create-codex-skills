# Python Session Level Control Library > Closing a Session

Sessions should be closed when no longer needed, as they consume resources on the agent (and on Velocity if being used.) It is especially important to close sessions if sessions are being opened within a loop.

```
# close session and free resources
```

```
s1.close()
```
