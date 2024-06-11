# Reframe HPC 

## Site configuration 
+ done in config files 
+ 2 Sections for every Site required 
+ Configuring the Systems
  + Specify Modules System ```'modules_system'```
  + set hostname patterns (eg. login) ```'hostnames'```
  + Each System needa at least one partition
  + Miminmum Requirements for Partion:
    + Job scheduler ```'scheduler'```
    + programmig enviroments to test ```'environs'``` 
  + Addional Options
    + specifying modules to be loaded every time something is run on this partion
    + adjusting concurrency limit
  
+ Configuring Programming Enviroments
  + defining required modules
  + set additional enviroment variables
  + set defalt flags


Example for some baseline config:
```
site_configuration = { 
  ’systems’: {
    ’ault’: {
      ’descr’: ’Ault␣TDS’, 
      ’hostnames’: [’ault’], 
      ’modules_system’: ’lmod’, 
      ’partitions’: {
        ’login’: {
          ’scheduler’: ’local’, 
          ’environs’: [’PrgEnv-gnu’], 
          ’descr’: ’Login nodes’,
        }, 
        ’amdv100’: {
          ’scheduler’: ’nativeslurm’, 
          ’access’: [’-pamdv100’], 
          ’environs’: [’PrgEnv-gnu’],
        } 
      }
    }
  }
  ’environments’: { 
    ’ault’: {
      ’PrgEnv-gnu’: {
        ’type’: ’ProgEnvironment’,
        ’modules’: [’gcc’, ’cuda’, ’openmpi’], 
        ’cc’: ’mpicc’,
        ’cxx’: ’mpicxx’,
        ’ftn’: ’mpif90’
      } 
    } 
  } 
} 
```



## Writing Regression tests

+ Everything test derives from the ```RegressionTest``` base class 
+ Every Regression test is either ```@simple_test``` or ```@parameterized_test```
  + parameterized test generate a family of tests by modifying inividual parameters of a test
+ Almost always everthing is declared in the constructor

```python
import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class Example7Test(rfm.RegressionTest):
  def __init__(self):
    self.descr = ’A simple Cuda test’ 
    self.valid_systems = [’daint:gpu’] 
    self.valid_prog_environs = [’PrgEnv-gnu’] 
    self.sourcepath = ’example_dmv_cuda.cu’
    self.build_system = ’SingleSource’ 
    self.build_system.cxxflags = [’-O3’] 
    self.executable_opts = [’4096’, ’1000’] 
    self.modules = [’cudatoolkit’] 
    self.sanity_patterns = sn.assert_found(r’time for single dmv’, self.stdout) 
    self.perf_patterns = {
      ’perf’: sn.extractsingle( r’Performance:\s+(?P<Gflops >\S+)␣Gflop/s’, self.stdout, ’Gflops’, float)
    }
    self.reference = {
      ’daint:gpu’: {
      ’perf’: (50.0, -0.1, 0.1, ’Gflop/s’),
      } 
    }
```

+ ```valid_systems``` and ```valid_prog_environs``` variables
  + needed by every test 
  + describe the test constraints
  + ```*``` means the test is valid for all systems an enviroments
+ ```build_system``` Each Build System defines a set of attributes such as compilation flags to controll the tests behavior
+ ```sourcepath``` file to be compiled
+ ```executable_opts``` options passed to the generated executable
+ ```modules``` addional enviroment modules
+ ```variables``` enviroment variables
+ ```sanity_patterns``` evaluated during the sanity stage in the pipeline 
  + just accesses the gerneral functionality of the test 
+ ```perf_patterns``` values to be extracted by the framework and to be used as performance variables
+ ```reference``` stores reference values 
  + (target_perf, lower_thres, upper_thres, unit) perf can be 10% lower and 10% higher than target

### Test Stages 

+ every test has to go through all stages
+ If nothing is set for the stage stage is not run

1. Setup
2. Compile
3. Run
4. Sanity
5. Performance
6. Cleanup

+ @run_before and @run_after can also be added

+ Serial and Asynchronous execution policys avialable

### Test Resources

+ resource dierctory is directly assosiated to test 
+ make a subfolder src in the same directory as the test is located
```
test_folder
|-- src
|    |-- test-resources.c
|
|-- test.py
```

## Performance Logging

+ logging the performance with perf_patterns
+ Reframe logs achived and reference values
+ Per Default there is one log fiel per test
+ other options: Syslog, Graylog

+ General output directorys
  + Log written to /tmp/rfm*
  + JSON Report: ~/.reframe/reports
    + Name can be changed with the ```--report-file```flag
  + CSV File -> ./perflogs/\<system>/\<partition>/\<testname>.log
    + Can be printed immediately with ```--performance-report``` flag 
  + stage and outputfiles get wirtten to ```./stage``` and ```./output``` 
    + can be changes with ```-a``` and ```-o``` flag
    + ouput contains .err, .out and .sh 
    + .sh is the acctual test script that is created

## Running Reframe
```bash
reframe -C config/base_config.py -c mytests/ -R -t production -r
```
+ -C check for config files
+ -c check path for tests
  + -R recursive checking for files
+ -t files with specific tag ar run 
+ -r run seceted tests  
  + can be replaced with --dry-run -> script gets crated in the output folder, but test is not run 

*extra*
+ -S set additional parameters 

### Other Flags that might be helpful
+ ```--exec-policy=serial``` ensures tests are run serial with local executioners 
  