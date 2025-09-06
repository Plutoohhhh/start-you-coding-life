from api_clients.user_api_client import UserApiClient

def test_get_user_list_and_validate():
    """测试目标：
        验证点：

    """
    client = UserApiClient()
    response = client.get_list_of_users(page_number=2)

    assert response.status_code == 200,f"预期状态码为200，实际为{response.status_code}"

    response_data = response.json()
    assert response_data['page'] == 2
    assert len(response_data['data']) == response_data['per_page'],"响应数据中的用户数量与per_page字段不符"
    assert response_data['date'][0]['email'].endswith('@reqres.in'),"第一个用户的email格式有误"