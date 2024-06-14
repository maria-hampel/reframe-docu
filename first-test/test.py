import os
import reframe as rfm
import reframe.utility.sanity as sn


@rfm.simple_test
class HelloTest(rfm.RegressionTest):
    def __init__(self):
        self.valid_systems = ['*']
        self.valid_prog_environs = ['*']
        self.sourcepath = 'hello_world.c'
        #self.build_system.cflags = ['-O3', omp_flag]

    @sanity_function
    def validate_hello(self):
        return sn.assert_found(r'Hello', self.stdout)
    

    # @performance_function('words')
    # def validate_wc(self):
    #     return sn.extractsingle(r'Hello World contains (\S+)', self.stdout, 1, int)

    
    @run_before('performance')
    def validate(self):
        self.perf_patterns = {
            'wordcount': sn.extractsingle(r'Hello World contains (\S+)', self.stdout, 1, int),
            'duriation': sn.extractsingle(r'Execution time: (\S+)',self.stdout, 1, float)
        }
        self.reference = {
            'baseline_system:default': {
                'duration': (1.2e-05, -1.5, 1.5, None),
                'wordcount': (2, 0, 0, None) 
            }
        }
        


# class build_hello(rfm.CompileOnlyRegressionTest):
#     build_system = 'SingleSource'
#     sourcepath = 'hello_world.c'
#     executable = './hello_world.x'
    
#     @run_before('compile')
#     def prepare(self):
#         omp_flag = self.current_environ.extras.get('omp_flag')
#         self.build_system.cflags = ['-O3', omp_flag]

# class hello_test(rfm.RunOnlyRegressionTest):
#     valid_systems = ['*']
#     valid_prog_environs = ['+openmp']
#     hello_binary = fixture(build_hello, scope='environment')

#     @run_after('setup')
#     def set_executable(self):
#         self.executable = os.path.join(self.hello_binary.stagedir, 'hello_world.x')

#     @sanity_function
#     def validate_hello(self):
#         return sn.assert_found(r'Hello', self.stdout)

#     @performance_function('words')
#     def validate_wc(self):
#         return sn.extractsngle(r'Hello World contains (\S+)', self.stdout, 1, int)
    
    
# @rfm.simple_test
# class benchit_test(rfm.RegressionTest):
#     valid_systems = ['*']
#     valid_prog_environs = ['+openmp']
#     build_system = 'SingleSource'
#     sourcepath = 'hello_world.c'
#     executable = 'hello_world'
    
#     @run_before('compile')
#     def changfune_omp_flags(self):
#         omp_flag = self.current_environ.extras.get('omp_flag')
#         self.build_system.cflags = ['-O3', omp_flag]
        
#     @sanity_function
#     def validate_hello(self):
#         return sn.assert_found(r'Hello', self.stdout)
    
