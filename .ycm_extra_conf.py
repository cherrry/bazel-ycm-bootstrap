#!/usr/bin/env python3
import ast
import os
import subprocess
import sys


def BazelInfo(key):
    return subprocess.check_output(['bazel', 'info', key]).decode('utf-8').strip()


def YcmExtraConf():
    return os.path.join(BazelInfo('bazel-bin'), 'external/bazel_compilation_database/ycm_extra_conf')


def FlagsForFile(filename, **kargs):
    os.chdir(BazelInfo('workspace'))

    if subprocess.call(['bazel', 'build', '@bazel_compilation_database//:ycm_extra_conf']):
        sys.exit()

    flags = subprocess.check_output([YcmExtraConf(), filename]).decode('utf-8')
    return ast.literal_eval(flags)


if __name__ == '__main__':
    filename = os.path.abspath(sys.argv[1])
    print(FlagsForFile(filename))
