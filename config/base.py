site_configuration = {
    'systems': [
        {
            'name': 'baseline_system',
            'descr': 'Example system',
            'hostnames': ['myhost'],
            'partitions': [
                {
                    'name': 'default',
                    'descr': 'Example partition',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'environs': ['baseline_env', 'gnu', 'clang']
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'baseline_env',
        },
        {
            'name': 'gnu',
            'cc': 'gcc',
            'cxx': 'g++',
            'features': ['openmp'],
            'extras': {'omp_flag': '-fopenmp'}
        },
        {
            'name': 'clang',
            'cc': 'clang',
            'cxx': 'clang++',
            'features': ['openmp'],
            'extras': {'omp_flag': '-fopenmp'}
        }
    ]
}