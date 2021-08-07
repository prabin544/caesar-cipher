import pytest

from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


def test_can_encrypt_with_a_given_shift():
    actual = encrypt("ABCDE", 2)
    expected = "CDEFG"
    assert actual == expected


def test_can_decrypt_previously_encrypted_string_with_the_same_shift():
    actual = decrypt("CDEFG", 2)
    expected = "ABCDE"
    assert actual == expected


def test_encryption_can_handle_upper_and_lower_case_letters():
    actual = encrypt("ABC abc mno", 26)
    expected = "ABC abc mno"
    assert actual == expected


def test_encryption_should_allow_non_alpha_characters_but_ignore_them_including_white_space():
    actual = encrypt("ABC def !@#$%^^ abc", 3)
    expected = "DEF ghi !@#$%^^ def"
    assert actual == expected


def test_crack_can_decrypt_a_sentence_without_knowing_the_shift():
    encrypted = encrypt("It was the best of times, it was the worst of times", 1096)
    actual = crack(encrypted)
    expected = "It was the best of times, it was the worst of times"
    assert actual == expected
