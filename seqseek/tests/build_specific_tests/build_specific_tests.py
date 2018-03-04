from __future__ import print_function
from __future__ import absolute_import
import unittest
from seqseek.lib import BUILD37, BUILD38
from .build_37_tests import TestBuild37
from .build_38_tests import TestBuild38


ASSEMBLY_TEST_SUITE = {
    BUILD37: TestBuild37,
    BUILD38: TestBuild38
}

def run_build_test_suite(assembly):
    print("Running tests for {assembly}".format(assembly=assembly))
    suite = unittest.TestLoader().loadTestsFromTestCase(ASSEMBLY_TEST_SUITE[assembly])
    unittest.TextTestRunner(verbosity=3).run(suite)

def test_build_37():
    run_build_test_suite(BUILD37)

def test_build_38():
    run_build_test_suite(BUILD38)
