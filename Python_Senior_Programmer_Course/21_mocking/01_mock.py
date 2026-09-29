from unittest.mock import Mock
service = Mock()
service.get_user.return_value = {"id": 1, "name": "Ada"}
print(service.get_user(1))
service.get_user.assert_called_once_with(1)