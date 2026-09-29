def assert_success(response):
    assert 200 <= response.status_code < 300

def test_contract_shape(payload):
    assert "id" in payload
    assert "name" in payload