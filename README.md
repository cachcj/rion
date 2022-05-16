[![Pylint](https://github.com/Riffecs/rion/actions/workflows/pylint.yml/badge.svg)](https://github.com/Riffecs/rion/actions/workflows/pylint.yml)
[![Upload Python Package](https://github.com/Riffecs/rion/actions/workflows/pypi.yml/badge.svg)](https://github.com/Riffecs/rion/actions/workflows/pypi.yml)

# RION

## Installation
- ```pip install rion```
- The Rion package can be downloaded via pip. This requires at least ``pip 21.0``.
### Tipp
Depending on the configuration of the Python installation, it is possible that rion was installed correctly but is outside the path. To solve this problem, please follow these steps.

- ```pip uninstall rion```
- ```export PATH="$HOME/.local/bin:$PATH"```
- ```pip install rion```

Finally, we uninstall the package and add the path to the default environment. After that we can install the package again. Normally a reinstallation is not necessary. But we still recommend it

## Usage

### Package installation
``rion install  package``

### Search package
``rion search text``

### Package Information

```rion info package``` 

### Update package list
```rion update ```

### Update packages
```rion upgrade ```

### Remove packages
```rion remove ```

### Instruction
``rion man``

### Packet list
```rion list ```

### Packet version
```rion freeze ```


### Check packages
``rion check``


### Customizing the Config 
``rion config``

