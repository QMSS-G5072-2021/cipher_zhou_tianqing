from cipher_tz2372 import cipher_tz2372 as cp

import pytest


# test for single word "mds"
def test_cipher_positive_shift():
    example = 'mds'
    expected = 'net'
    actual = cp.cipher(example, 1, encrypt=True)
    assert expected==actual, "they are not equal!"


# test for single word "mds" + negative shift
def test_cipher_negative_shift():
    example = 'mds'
    expected = 'lcr'
    actual = cp.cipher(example, -1, encrypt=True)
    assert expected==actual, "they are not equal!"


def test_cipher_not_alphabet():
    example = 'mds@qmss'
    expected = 'net@rntt'
    actual = cp.cipher(example, 1, encrypt=True)
    assert expected==actual, "they are not equal!"


def test_cipher_exception():
    with pytest.raises(Exception):
        cp.cipher("mds", "two", encrypt=True)