#!/usr/bin/env python2

from __future__ import print_function
import glob
import subprocess

if __name__ == '__main__':
    print('starting merge')
    cov_files = list(glob.glob('tests/cov-report*.bin'))
    print('Files to merge:')
    print(cov_files)
    base_cmd = ['OpenCppCoverage', '--quiet', '--export_type=cobertura:cobertura.xml'] + ['--input_coverage={}'.format(f) for f in cov_files]
    print('Merge CMD: ',base_cmd)
    subprocess.check_call(base_cmd)
