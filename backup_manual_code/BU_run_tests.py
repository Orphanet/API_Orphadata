import unittest

modules_to_test = ("test.test_disorder_controller", "test.test_gene_controller")

suite = unittest.TestLoader().loadTestsFromNames(modules_to_test)
unittest.TextTestRunner(verbosity=2).run(suite)
