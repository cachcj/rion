# Packages

Here are the test packages for the Rion Client. The content and everything else in connection with the packages is freely invented and is in no conflict with licenses. 

# Syntax 
## Overview
Basically, we do not care what is in the packages. The main thing is that there is a ``deps.txt`` file.

Here is an overview from a sample package. 

```
packages
|
+---buddy
|       cute.modul
|       deps.txt
|       love.modul
|
+---futternapf
|       bestnapfever.napf
|       deps.txt
|       futternapf3000.napf
...
```
## Build
The packages are simply formed using the "tar" command. Alternatively, you can also use the script for this. [Script](/package/extract/makepacs.sh)
```shell
tar czvf buddy-v100_0_3.tar.gz buddy/
```

## Dependencies
