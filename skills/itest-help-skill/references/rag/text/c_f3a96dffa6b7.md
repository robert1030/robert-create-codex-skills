# Spirent Avalanche sessions > Avalanche API Commands > av_create > Example

```
set hProject [av_create project -under system1 -name Project1]
```

```
set hTest [av_create tests -under $hProject -name Test1 -testType deviceComplex ]
```

```
set hServerProfile [av_create ServerProfiles -under $hProject -name ServerProfile -applicationProtocol HTTP -http.keepAlive on]
```
