import pytest
from src.app.usecase.user_usecase import UserUsecase
from src.domain.entity.user import User
from unittest.mock import AsyncMock, MagicMock

@pytest.fixture
def user_usecase():
    user_repository = MagicMock()
    user_repository.find_by_email = AsyncMock()
    user_repository.create = AsyncMock()
    user_repository.update = AsyncMock()
    user_repository.delete = AsyncMock()
    user_repository.find_by_id = AsyncMock()
    return UserUsecase(user_repository)

@pytest.mark.asyncio
async def test_create_user_success(user_usecase):
    name = "Test User"
    email = "test@example.com"
    password = "password"
    
    user_usecase.user_repository.find_by_email.return_value = None
    user_usecase.user_repository.create.return_value = User(name, email, password)
    
    user = await user_usecase.create_user(name, email, password)
    
    assert user.name == name
    assert user.email == email
    assert user.password != password  # Verifica se a senha foi hashada

@pytest.mark.asyncio
async def test_create_user_failure_existing_email(user_usecase):
    email = "test@example.com"
    user_usecase.user_repository.find_by_email.return_value = User("Existing User", email, "password")
    
    with pytest.raises(ValueError) as exc_info :
        error = await user_usecase.create_user("Test User", email, "new_password")

    assert user_usecase.user_repository.create.call_count == 0
    assert str(exc_info.value) == "Email already exists"
    
@pytest.mark.asyncio
async def test_get_user_by_email_found(user_usecase):
    email = "test@example.com"
    expected_user = User("Test User", email, "password")
    user_usecase.user_repository.find_by_email.return_value = expected_user
    
    user = await user_usecase.get_user_by_email(email)
    
    assert user == expected_user

@pytest.mark.asyncio
async def test_get_user_by_email_not_found(user_usecase):
    email = "notfound@example.com"
    user_usecase.user_repository.find_by_email.return_value = None
    
    user = await user_usecase.get_user_by_email(email)
    
    assert user is None

@pytest.mark.asyncio
async def test_get_user_by_id_found(user_usecase):
    user_id = 1
    expected_user = User("Test User", "test@example.com", "password")
    user_usecase.user_repository.find_by_id.return_value = expected_user
    
    user = await user_usecase.get_user_by_id(user_id)
    
    assert user == expected_user

@pytest.mark.asyncio
async def test_get_user_by_id_not_found(user_usecase):
    user_id = 999
    user_usecase.user_repository.find_by_id.return_value = None
    
    user = await user_usecase.get_user_by_id(user_id)
    
    assert user is None

@pytest.mark.asyncio
async def test_update_user_success(user_usecase):
    name = "Updated User"
    email = "updated@example.com"
    password = "updated_password"
    
    updated_user = User("Teste", "old@example.com", "test123")
    user_usecase.user_repository.update.return_value = updated_user
    
    user = await user_usecase.update_user(updated_user.id, name, email, password)
    
    assert user.name == name
    assert user.email == email
    assert user.password != password
    

@pytest.mark.asyncio
async def test_delete_user_success(user_usecase):
    user_id = 1
    
    await user_usecase.delete_user(user_id)
    
    user_usecase.user_repository.delete.assert_called_once_with(user_id)
