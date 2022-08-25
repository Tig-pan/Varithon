import varithon as V
import subprocess

# how many times to attempt tests
TEST_ATTEMPTS = 10


def test_var_get_a():
    assert_varithon_output("test_var_get_a", "5", "")


def test_var_get_b():
    assert_varithon_output("test_var_get_b", "var2", "")


def test_collection_a():
    assert_varithon_output("test_collection_a", "5\r\na\r\nTrue", "")


def test_collection_b():
    assert_varithon_output("test_collection_b", "500", "")


def test_collection_c():
    assert_varithon_output("test_collection_c", "[['a'], ['a']]", "")


def test_collection_d():
    assert_varithon_output("test_collection_d", "[[['a'], ['a']], [['a'], ['a']], [['a'], ['a']]]", "")


def test_rand_a():
    assert_varithon_output("test_rand_a", None, "")


def test_collection_rand_a():
    assert_varithon_output("test_collection_rand_a", None, "")


############################################################################
############################ Helper Functions ##############################
############################################################################

def assert_varithon_output(filename, expected_output, expected_error):
    """ Tests a Varithon file numerous times, in order to ensure that the resulting compiled
        Python files all have the exact same behaviour.

        :param filename the string filename of the Varithon file to test, this should not
            include the .vy extension
        :param expected_output the expected output of the resulting compiled Python files as a
            string, if the actual output does not match this, an assertion error is thrown.
            If this is None, the output will not be tested.
        :param expected_error the expected error of the resulting compiled Python files as a
            string, if the actual error does not match this, an assertion error is thrown """

    parsed = V.parse_varithon_file(f"tests/{filename}.vy")

    for _ in range(TEST_ATTEMPTS):
        V.compile_varithon_file(f"compiled/{filename}.py", parsed)
        process = subprocess.Popen(f"python compiled/{filename}.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = process.communicate()

        # strip white spacing from results before testing
        if expected_output is not None:
            assert output.decode().strip() == expected_output
        if expected_error is not None:
            assert error.decode().strip() == expected_error
