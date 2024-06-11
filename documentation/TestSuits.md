# Reframe Test Suits 

## Reframe Test Libary (hpctestlib)

+ collection of gerneric tests provided by Reframe
+ can be run directly utilizing the -s option to set Parameters
+ can be build upon for site-specific tests
+ Every test is (indirectly) derived from the RegressionTest class, if not statet otherwise
+ Documentation: https://reframe-hpc.readthedocs.io/en/stable/hpctestlib.html

### Data analytics, Interactive Computing & Machine Learing
+ tests check the functionality of commonly used tools
+ all utilize Python 

| Name | General Functionality |
| -------- | -------- | 
| data_analytics.spark.spark_checks.compute_pi_check | Test Apache Spark by computing pi. Passes if pi is within a defined tolerance | 
| interactive.jupyter.ipcmagic.ipcmagic_check | Test ipcmagic performance, checks if ipcmagic is running and if 2 differnt nodes are used | 
| ml.tensorflow.horovod.tensorflow_cnn_check | Runs a Horovod tensorflow example checks sanity and extracts GPU performance (average throughput per iteration, total throughput) | 
| ml.pytorch.horovod.pytorch_cnn_check | Runs a Horovod pytorch example, checks sanity and extracts GPU performance (average throughput per iteration, total throughput) | 

### OSU Microbenchmarks

+ Specific Benchmarks can be choosen 
  
| Name | General functionality |
| -------- | -------- |
| microbenchmarks.mpi.osu.build_osu_benchmarks | fixure for building OSU benchmarks |
| microbenchmarks.mpi.osu.fetch_osu_benchmarks | fixure for fetching OSU benchmarks |
| microbenchmarks.mpi.osu.osu_benchmark | Base class for the following (osu_build_run & osu_run), can be used to build upon |
| microbenchmarks.mpi.osu.osu_build_run | OSU benchmark test (build and run) |
| microbenchmarks.mpi.osu.osu_run | Run-only OSU benchmark test |


### GPU Benchmarks 
| Name | General functionality |
| -------- | -------- |
| microbenchmarks.gpu.gpu_burn.gpu_burn_build | Fixure for building the GPU burn benchmark |
| microbenchmarks.gpu.gpu_burn.gpu_burn_check | Tries to build burn Benchmark with gpu_burn_build and continously rund GEMM either single or double percision, evaluates GPU perfpormance (min, max)| 


### Python 
| Name | General functionality |
| -------- | -------- |
| python.numpy.numpy_ops.numpy_ops_check | Basic Numpy Operations Test with linear algebra (matrix product, SVD, eigendecomposition ...). Evaluates the time each kernel needs |


### Scientific Applications
+ assert Energy with scientific simulations

| Name | General functionality |
| -------- | -------- |
| sciapps.amber.nve.amber_nve_check | Amber NVE test, can assert energy levels utilized | 
| sciapps.gromacs.benchmarks.gromacs_check | GROMACS benchmark test. Validates output and reports metric performance |
| sciapps.qespresso.benchmarks.QEspressoPWCheck | QuantumESPRESSO benchmark test. |

### System

| Name | General functionality |
| -------- | -------- |
| system.fs.mnt_opts.filesystem_options_check | Checks if the mounted filesystem have been configured correctly. |


## CSCS
+ War Klar das die viel zu viel haben...
+ hpctestlib is utilzed a lot

### Apps
+ Testing Scientific Applications 
+ Mostly checking the Runtime of Molecular Dynamic Simulators 


| Name | Description |
| ------ | ------- |
| Amber | sciapps.amber.nve, Checks performance of Amber |
| CP2K | Runs simulations for quantum chemistry and solid state physics software for simuations. Checks Runtime. |
| CPMD | Runs simulations for Density Functional Theory (molecular dynamics). Checks runtime. |
| GREASY | Runs simple MPI Programm (Hello World), Evaluates Number of tasks, cpus per Tasks,... Also evaluates the Time the for Communication |
| GROMACS | sciapps.gromacs.benchmarks, Checks Performance.|
| Jupyter | interactive.jupyter.ipcmagic, Checks Performance. |
| LAMMPS | Runs Molecular Dynamics Simulator. Checks parallel Runtime on GPUs and CPUs |
| Namd | Runs Molecular Dynamics Simulator. Checks Performance. |
| Paraview | Asserts if Paraview runs properly |
| Python | python.numpy.numpy_ops, Checks runtime for all kernels. |
| Pytorch | ml.pytorch.horovod, Checks Performance for differnt models. |
| QuantumESPRESSO | Asseses if ESPRESSO runs, and Checks runtime an CPUs and GPUs |
| SPARK | data_analytics.spark.spark_checks, Asseses if Spark runs |
| Tensorflow | ml.tensorflow.horovod, Checks performance. |
| VASP | Runs Simulation for Material Modeling. Checks elapsed time |

### Compile

| Name | Description |
| ------ | ------- |
| haswell_fma_check | Check for AVX2 Instructions, with simple Fortran and C programs | 
| libsci_acc_symlink | Checks if links to libarys ar properly made |

### Containers 

... to be continued ... 