import unittest

modules_to_test = ("test.test_classifications_of_rare_diseases_controller",
                   "test.test_epidemiological_data_on_rare_diseases_controller",
                   "test.test_genes_associated_to_rare_diseases_controller",
                   "test.test_rare_diseases_and_associated_gene_controller",
                   "test.test_rare_diseases_and_associated_phenotypes_controller",
                   "test.test_rare_diseases_and_cross_referencing_controller"
                   )

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromNames(modules_to_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
