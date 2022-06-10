# Log Analyzer

## Docker Usage
- Output directory will be the same as input file location (indicated by **<your_directory>** in below Docker run command)

- Clone this repo to local machine

- To build the Docker image:

```docker build -t log-analyzer```

- To run the application in Docker container:

```docker run -v <your_directory>:/home -t log-analyzer python main.py <optional arguments> home/<input_filename> home/<output_filename>```

- **<your_directory>** must be *absolute* path, not a relative path (i.e. ```/Users/my_username/Desktop/my_directory```, not ```./my_directory```)

- See below for optional argument options


## Python Usage
```python main.py [-h] [-a] [-m] [-l] [-e] [-t] input output```

positional arguments:

**input** - path to input log file
  
**output** - path to output save file


optional arguments:

**-h, --help** - show this help message and exit

**-a, --all** - run all operations below

**-m, --most** - most frequent IP

**-l, --least** - least frequent IP

**-e, --eps** - events per second

**-t, --total** - total amount of bytes exchanged