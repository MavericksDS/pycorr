import unittest

import numpy
import pandas

import pycorrcat.pycorrcat as pycorrcat


class TestPycorrcat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        numpy.random.seed(seed=1234)
        rand_1 = numpy.random.uniform(0.0, 1.0, 200)
        rand_2 = numpy.random.uniform(0.0, 1.0, 200)
        cat_1 = ["0" if r < 0.5 else "1" for r in rand_1]
        cat_2 = ["0" if r < 0.5 else "1" for r in rand_2]
        df = pandas.DataFrame(
            {
                "rand_1": rand_1,
                "rand_2": rand_2,
                "cat_1": cat_1,
                "cat_2": cat_2,
            }
        )

        # Make an exact copy of cat_1
        df["cat_1_copy"] = df["cat_1"]

        cls.df = df
        return

    def test_corr_correlated(self):
        corr = pycorrcat.corr(self.df["cat_1"], self.df["cat_1"])
        self.assertTrue(round(corr, 15) == 1)
        return

    def test_corr_not_correlated(self):
        corr = pycorrcat.corr(self.df["cat_1"], self.df["cat_2"])
        self.assertTrue(corr < 0.0001)
        return

    def test_corr_matrix(self):
        corr_matrix = pycorrcat.corr_matrix(
            data=self.df, columns=["cat_1", "cat_1_copy", "cat_2"]
        )
        self.assertTrue(round(corr_matrix["cat_1"]["cat_1"], 15) == 1.0)
        self.assertTrue(round(corr_matrix["cat_1"]["cat_1_copy"], 15) == 1.0)
        self.assertTrue(round(corr_matrix["cat_1_copy"]["cat_1"], 15) == 1.0)
        self.assertTrue(round(corr_matrix["cat_1"]["cat_2"], 15) == 0.0)
        self.assertTrue(round(corr_matrix["cat_2"]["cat_1"], 15) == 0.0)
        return
