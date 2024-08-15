import pandas as pd
import os
from tests import TEST_DATA_DIR


def test_shape():
    df = pd.read_csv(os.path.join(TEST_DATA_DIR, "csv", "shape_example.csv"))
    assert df.shape == (3, 2)
