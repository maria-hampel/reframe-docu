# Reframe Test Suites 

## Reframe Test Library (hpctestlib)

+ Collection of generic tests provided by Reframe
+ Can be run directly utilizing the -s option to set parameters
+ Can be built upon for site-specific tests
+ Every test is (indirectly) derived from the RegressionTest class, if not stated otherwise
+ Documentation: https://reframe-hpc.readthedocs.io/en/stable/hpctestlib.html

### Data analytics, Interactive Computing & Machine Learning
+ Tests check the functionality of commonly used tools
+ All utilize Python 

| Name | General Functionality |
| -------- | -------- | 
| data_analytics.spark.spark_checks.compute_pi_check | Test Apache Spark by computing pi. Passes if pi is within a defined tolerance | 
| interactive.jupyter.ipcmagic.ipcmagic_check | Test ipcmagic performance, checks if ipcmagic is running and if 2 different nodes are used | 
| ml.tensorflow.horovod.tensorflow_cnn_check | Runs a Horovod TensorFlow example, checks sanity, and extracts GPU performance (average throughput per iteration, total throughput) | 
| ml.pytorch.horovod.pytorch_cnn_check | Runs a Horovod PyTorch example, checks sanity, and extracts GPU performance (average throughput per iteration, total throughput) | 

### OSU Microbenchmarks

+ Specific benchmarks can be chosen
  
| Name | General Functionality |
| -------- | -------- |
| microbenchmarks.mpi.osu.build_osu_benchmarks | Fixture for building OSU benchmarks |
| microbenchmarks.mpi.osu.fetch_osu_benchmarks | Fixture for fetching OSU benchmarks |
| microbenchmarks.mpi.osu.osu_benchmark | Base class for the following (osu_build_run & osu_run), can be used to build upon |
| microbenchmarks.mpi.osu.osu_build_run | OSU benchmark test (build and run) |
| microbenchmarks.mpi.osu.osu_run | Run-only OSU benchmark test |


### GPU Benchmarks 
| Name | General Functionality |
| -------- | -------- |
| microbenchmarks.gpu.gpu_burn.gpu_burn_build | Fixture for building the GPU burn benchmark |
| microbenchmarks.gpu.gpu_burn.gpu_burn_check | Tries to build the burn benchmark with gpu_burn_build and continuously runs GEMM either single or double precision, evaluates GPU performance (min, max)| 


### Python 
| Name | General Functionality |
| -------- | -------- |
| python.numpy.numpy_ops.numpy_ops_check | Basic NumPy Operations Test with linear algebra (matrix product, SVD, eigendecomposition, etc.). Evaluates the time each kernel needs |


### Scientific Applications
+ Assert energy with scientific simulations

| Name | General Functionality |
| -------- | -------- |
| sciapps.amber.nve.amber_nve_check | Amber NVE test, can assert energy levels utilized | 
| sciapps.gromacs.benchmarks.gromacs_check | GROMACS benchmark test. Validates output and reports metric performance |
| sciapps.qespresso.benchmarks.QEspressoPWCheck | QuantumESPRESSO benchmark test. |

### System

| Name | General Functionality |
| -------- | -------- |
| system.fs.mnt_opts.filesystem_options_check | Checks if the mounted filesystem has been configured correctly. |


## CSCS
+ Clearly, they have a lot...
+ hpctestlib is utilized a heavily
+ Link: https://github.com/reframe-hpc/cscs-reframe-tests/tree/main

### Apps
+ Testing Scientific Applications 
+ Mostly checking the runtime of Molecular Dynamic Simulators 


| Name | Description |
| ------ | ------- |
| Amber | sciapps.amber.nve, Checks performance of Amber |
| CP2K | Runs simulations for quantum chemistry and solid-state physics software for simulations. Checks runtime. |
| CPMD | Runs simulations for Density Functional Theory (molecular dynamics). Checks runtime. |
| GREASY | Runs simple MPI program (Hello World), evaluates the number of tasks, CPUs per task, etc. Also evaluates the time for communication |
| GROMACS | sciapps.gromacs.benchmarks, Checks performance. |
| Jupyter | interactive.jupyter.ipcmagic, Checks performance. |
| LAMMPS | Runs Molecular Dynamics Simulator. Checks parallel runtime on GPUs and CPUs |
| Namd | Runs Molecular Dynamics Simulator. Checks performance. |
| Paraview | Asserts if Paraview runs properly |
| Python | python.numpy.numpy_ops, Checks runtime for all kernels. |
| Pytorch | ml.pytorch.horovod, Checks performance for different models. |
| QuantumESPRESSO | Assesses if ESPRESSO runs and checks runtime on CPUs and GPUs |
| SPARK | data_analytics.spark.spark_checks, Assesses if Spark runs |
| Tensorflow | ml.tensorflow.horovod, Checks performance. |
| VASP | Runs Simulation for Material Modeling. Checks elapsed time |

### Compile

| Name | Description |
| ------ | ------- |
| haswell_fma_check | Check for AVX2 instructions with simple Fortran and C programs | 
| libsci_acc_symlink | Checks if symlinks to libraries are properly made |

### Containers 

... to be continued ...