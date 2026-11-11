import pytest
from common.requests_util import send_request

# 使用 @pytest.mark.parametrize 进行数据驱动
# 参数说明："test_data" 存字典，"expected_status" 存预期状态码
@pytest.mark.parametrize("test_data, expected_status", [
    # 场景1：正确账号密码
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200),
    # 场景2：错误密码
    ({"email": "eve.holt@reqres.in", "password": "wrong_password"}, 400),
    # 场景3：缺失密码
    ({"email": "eve.holt@reqres.in"}, 400)
])
def test_login_cases(test_data, expected_status):
    response = send_request("POST", "/login", json=test_data)
    
    # 断言：检查状态码是否和预期的一致
    assert response.status_code == expected_status
    
    # 如果是成功场景，进一步断言有 token
    if expected_status == 200:
        assert "token" in response.json()