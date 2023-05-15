import main
from utils import print_loading, print_pass, print_fail

text = """Trivia: The concept of geosynchronization was first postulated by Arthur C. Clarke.

Explanation: Geosynchronous orbits are orbits around Earth that have an orbital period matching Earth's rotation period.
This results in the satellite appearing stationary with respect to a point on Earth's surface. This concept is crucial in space physics and geodesy,
as it is used in various applications like communication satellites. Arthur C. Clarke, a British science fiction writer,
was the first to postulate this concept, which is why geosynchronous orbits are sometimes referred to as Clarke orbits.
"""

def test_process_text():
    print_loading("Testing process_text function. Expected output: list of 3-tuples.")
    result = main.process_text(text)
    print(f"Actual output: {result[:3]}...\n")
    try:
        assert len(result) > 0, "The result should not be an empty list"
        assert all(isinstance(x, tuple) and len(x) == 3 for x in result), "Each element in the result should be a 3-tuple"
        assert result[0][0] == "Trivia", "The first token should be 'Trivia'"
        print_pass("All process_text tests passed.")
    except AssertionError as e:
        print_fail(str(e))

def test_extract_entities():
    print_loading("Testing extract_entities function. Expected output: list of 2-tuples.")
    result = main.extract_entities(text)
    print(f"Actual output: {result[:3]}...\n")
    try:
        assert len(result) > 0, "The result should not be an empty list"
        assert all(isinstance(x, tuple) and len(x) == 2 for x in result), "Each element in the result should be a 2-tuple"
        print_pass("All extract_entities tests passed.")
    except AssertionError as e:
        print_fail(str(e))

test_process_text()
test_extract_entities()
