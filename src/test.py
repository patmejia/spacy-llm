import main
import pytest
import spacy


@pytest.fixture
def nlp():
    return main.load_model()


@pytest.fixture
def geosynchronization_text():
    return """Trivia: The concept of geosynchronization was first postulated by Arthur C. Clarke.
    Explanation: Geosynchronous orbits are orbits around Earth that have an orbital period matching Earth's rotation period.
    This results in the satellite appearing stationary with respect to a point on Earth's surface. This concept is crucial in space physics and geodesy,
    as it is used in various applications like communication satellites. Arthur C. Clarke, a British science fiction writer,
    was the first to postulate this concept, which is why geosynchronous orbits are sometimes referred to as Clarke orbits."""


@pytest.fixture
def test_process_text_returns_expected_tuples(nlp, geosynchronization_text):
    result = main.test_process_text_returns_expected_tuples(nlp, geosynchronization_text)
    assert len(result) > 0, "Expected process_text to return at least one tuple, but it returned an empty list"
    assert all(isinstance(x, tuple) and len(x) == 3 for x in result), "Expected each element in the result to be a 3-tuple (text, pos, dep), but found a different structure"
    assert result[0][0] == "Trivia", "Expected the first token to be 'Trivia', but found a different token"


@pytest.fixture
def test_extract_entities_returns_expected_entity_tuples(nlp, geosynchronization_text):
    result = main.extract_entities_returns_expected_entity_tuples(nlp, geosynchronization_text)
    assert len(result) > 0, "Expected extract_entities to return at least one tuple, but it returned an empty list"
    assert all(isinstance(x, tuple) and len(x) == 2 for x in result), "Expected each element in the result to be a 2-tuple (entity, entity type), but found a different structure"


if __name__ == '__main__':
    pytest.main()