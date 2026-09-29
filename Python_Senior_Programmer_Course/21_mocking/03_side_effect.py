from unittest.mock import Mock
api = Mock()
api.get.side_effect = [{"id":1}, {"id":2}]
print(api.get(), api.get())