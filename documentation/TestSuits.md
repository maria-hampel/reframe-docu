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
| Amber | sciapps.amber.nve, Checks performance of Amber, with amber_nve_check in ns/day. |
| CP2K | Runs simulations for quantum chemistry and solid-state physics software for simulations. Checks runtime for CPUs and GPUs. |
| CPMD | Runs simulations for Density Functional Theory (molecular dynamics). Checks runtime for CPUs and GPUs. |
| GREASY | Runs simple MPI program (Hello World), evaluates the number of tasks, CPUs per task, etc. Also evaluates the time for communication |
| GROMACS | sciapps.gromacs.benchmarks, Checks performance in ns/day. |
| Jupyter | interactive.jupyter.ipcmagic, Checks performance. |
| LAMMPS | Runs Molecular Dynamics Simulator. Checks parallel runtime on GPUs and CPUs |
| Namd | Runs Molecular Dynamics Simulator. Checks performance in days/ns. |
| Paraview | Asserts if Paraview runs properly. |
| Python | python.numpy.numpy_ops, Checks runtime for all kernels. |
| Pytorch | ml.pytorch.horovod, Checks throughput for different models. |
| QuantumESPRESSO | Assesses if ESPRESSO runs and checks runtime on CPUs and GPUs |
| SPARK | data_analytics.spark.spark_checks, Assesses if Spark runs |
| Tensorflow | ml.tensorflow.horovod, Checks throughput. |
| VASP | Runs Simulation for Material Modeling. Checks elapsed time |
 
### Compile

| Name | Description |
| ------ | ------- |
| haswell_fma_check | Check for AVX2 instructions with simple Fortran and C programs | 
| libsci_acc_symlink | Checks if symlinks to libraries are properly made. |

### Containers 
+ Test Software for running Appications in containers in HPC
+ Compatiple with Open Container Initiative Standards 

| Name | Description |
| ------ | ------- |
| buildah | Runs OSU Benchmark and NVIDIA Cuda Example in a Container; Checks performance. |
| sarus | Checks the Sanatiy of Container Builds. As well as some performance latency functions with OSU and the integration of GPUs in Containers. | 


### Libaries 
+ Checks for Santity auf Module Packages

| Name | Description | Sanity/Performance |
| ------ | ------- | ------- | 
| boost | opensource C lib for Network Programming, Filesystem, Smartptr, Regex, Threads and Interoperability with Python |  Sanity |
| cray-libsci | optimize the performance of scientific and engineering applications on Cray | Sanity and Performance of GPUs and CPUs |
| gridtools | HPC-lib for development of weather and Climate models | Sanity and Performance of GPUs and CPUs | 
| hpx | C++ lib for high-performance parallel and distributed Computing | Sanity and Performance of GPUs and CPUs |
| io | h5py; netcdf; | Sanity |
| magma | Matrix Algebra on GPU and Multicore | Sanity and Performance of Magma Operations |
| math | ScaLAPACK routine & Cray libs | Sanity |
| opengl | OpenGL context on top of EGL | Sanity |
| petsc | Portable, Extensible Toolkit for Scientific Computation optimization for cray | Sanity |

### mch


### Microbenchmarks
+ Test alloc speed, latency, throughput, bandwidth etc for System

| Name | Description |
| ------ | ------- |
| cpu/alloc_speed | check allocation speed on cpu |
| cpu/dgemm; gpu/dgemm | Check speed of dgemm |
| cpu/fft | Cheks execution time of fftw with MPI |
| cpu/latency | Latency Benchmark |
| cpu/likwid | Checks Cache sizes, bandwidth with likwid benchmark |
| cpu/roofline; gpu/roofline | Checks GFLOPs and DRAM Bandwidth with Roofline Toolkit |
| cpu/simd | Checks performance for multiplication with avx instructions and nsimd |
| cpu/stream | Run Stream Benchmark and check performance |
| cpu/strided_bandwidth | Checks bandwidth for differnt stride sizes |
| gpu/gpu_burn_check | Derived from microbenchmarks.gpu.gpu_burn, checks Performance | 
| gpu/kernel_latency | Derived from microbenchmarks.gpu.kernel_latency, checks Latency | 
| gpu/memory_bandwidth | Derived from microbenchmarks.gpu.memory_bandwith, checks Bandwidth | 
| gpu/pointer_chase | Derived from microbenchmarks.gpu.poiner_chase, checks avg latency for all cache levels  | 
| gpu/shmem | Derived from microbenchmarks.gpu.shmem checks bandwidth |
| hpcg | checks Performance solving a sparse linear system using CG method with huge pages |
| hpl | LINPACK Benchmark, checks performance |
| mpi/halo_exchange | Checks Communication times with MPI |
| mpi/osu | Derived from microbenchmarks.mpi.osu checks MPI Bandwidth |

### prgenv

### system 
| Name | Description |
| ------ | ------- |
| io | Runs IOR Benchmark outputs performance |
| jobreport | Utilizes the microbenchmarks.gpu.gpu_burn and checks that the job report produces senssible gpu usage data |
| nvidia | Gets Information with nvidia-smi and checks Sanity |
| openstack | checks runtime for differnt s3 operations | 
| slurm/cscs_usertools.py | Checks the cscs usertools for slurm ar sane |
| slurm/hetjob | Schedules two heterogeneous jobs (MPI Hello World Programm), checks Sanity |
| slurm/slurm | Checks Functionality for basic operations (Enviroment, GPU Requests, etc.),  Checks how Slurm handles Memory overconsumption, Responce Check, Queue Status Check, Afterwards confirms the Sanity of the system |


### tools 