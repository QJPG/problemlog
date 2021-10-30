# Minimalist Python Logs

``` python
import probleml

log = probleml.Probleml()
...
log.write(section = log.SEC_INFOS, message = "Your log Message for [info] section")
...
log.generate()
```

``` txt
@30/10/2021 & 11:13:41

[Warnings]
30/10/2021 11:13:41 -> Warnings -> log warning message

[Errors]
#nothing to report!

[Debugs]
30/10/2021 11:13:41 -> Debugs -> log debug message
30/10/2021 11:13:41 -> Debugs -> log debug message

[Criticals]
30/10/2021 11:13:41 -> Criticals -> log critical message

[Infos]
#nothing to report!

[Total]
Warnings: 1
Errors: 0
Debugs: 2
Infos: 0
Criticals: 1
```