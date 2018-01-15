"""
Unit tests for stem.client.* contents.
"""

__all__ = [
  'cell',
  'types',
]

import os

TEST_DATA = os.path.join(os.path.dirname(__file__), 'data')


def test_data(filename):
  """
  Provides test data in the given file.

  :param str filename: test data to provide

  :returns: **bytes** with the data
  """

  with open(os.path.join(TEST_DATA, filename), 'rb') as data_file:
    return data_file.read()
