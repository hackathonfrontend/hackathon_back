from fastapi import status
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.schemas.prompt_schema import PromptRead, PromptCreate, PromptUpdate # Ensure these exist

# client and mock_prompt_service fixtures are provided by conftest.py

def test_create_prompt(client: TestClient, mock_prompt_service: MagicMock):
    prompt_data = {"text": "Test prompt", "creation_story_id": 1, "user_id": 1}
    mock_prompt_service.create_prompt.return_value = PromptRead(id=1, **prompt_data)

    response = client.post("/prompts/", json=prompt_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"id": 1, "text": "Test prompt", "creation_story_id": 1, "user_id": 1}
    mock_prompt_service.create_prompt.assert_called_once()
    # To check the argument passed to the service:
    # called_arg = mock_prompt_service.create_prompt.call_args[0][0]
    # assert called_arg.text == prompt_data["text"]


def test_get_prompt_found(client: TestClient, mock_prompt_service: MagicMock):
    prompt_id = 1
    prompt_data = {"id": prompt_id, "text": "Test prompt", "creation_story_id": 1, "user_id": 1}
    mock_prompt_service.get_prompt_by_id.return_value = PromptRead(**prompt_data)

    response = client.get(f"/prompts/{prompt_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == prompt_data
    mock_prompt_service.get_prompt_by_id.assert_called_once_with(prompt_id=prompt_id)


def test_get_prompt_not_found(client: TestClient, mock_prompt_service: MagicMock):
    prompt_id = 999
    mock_prompt_service.get_prompt_by_id.return_value = None

    response = client.get(f"/prompts/{prompt_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Prompt not found"}
    mock_prompt_service.get_prompt_by_id.assert_called_once_with(prompt_id=prompt_id)


def test_get_all_prompts(client: TestClient, mock_prompt_service: MagicMock):
    prompts_data = [
        {"id": 1, "text": "Prompt 1", "creation_story_id": 1, "user_id": 1},
        {"id": 2, "text": "Prompt 2", "creation_story_id": 1, "user_id": 2},
    ]
    mock_prompt_service.get_all_prompts.return_value = [PromptRead(**p) for p in prompts_data]

    response = client.get("/prompts/?skip=0&limit=10")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == prompts_data
    mock_prompt_service.get_all_prompts.assert_called_once_with(skip=0, limit=10)


def test_update_prompt_found(client: TestClient, mock_prompt_service: MagicMock):
    prompt_id = 1
    update_data = {"text": "Updated prompt text"}
    # Service returns the updated object
    updated_prompt_response = {"id": prompt_id, "text": "Updated prompt text", "creation_story_id": 1, "user_id": 1}
    mock_prompt_service.update_prompt.return_value = PromptRead(**updated_prompt_response)

    response = client.put(f"/prompts/{prompt_id}", json=update_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == updated_prompt_response
    mock_prompt_service.update_prompt.assert_called_once()
    # To check arguments:
    # called_arg_id = mock_prompt_service.update_prompt.call_args[0][0]
    # called_arg_update = mock_prompt_service.update_prompt.call_args[0][1]
    # assert called_arg_id == prompt_id
    # assert called_arg_update.text == update_data["text"]


def test_update_prompt_not_found(client: TestClient, mock_prompt_service: MagicMock):
    prompt_id = 999
    update_data = {"text": "Updated prompt text"}
    mock_prompt_service.update_prompt.return_value = None

    response = client.put(f"/prompts/{prompt_id}", json=update_data)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Prompt not found"}
    mock_prompt_service.update_prompt.assert_called_once()


def test_delete_prompt_found(client: TestClient, mock_prompt_service: MagicMock):
    prompt_id = 1
    deleted_prompt_response = {"id": prompt_id, "text": "Deleted prompt", "creation_story_id": 1, "user_id": 1}
    mock_prompt_service.delete_prompt.return_value = PromptRead(**deleted_prompt_response)

    response = client.delete(f"/prompts/{prompt_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == deleted_prompt_response
    mock_prompt_service.delete_prompt.assert_called_once_with(prompt_id=prompt_id)


def test_delete_prompt_not_found(client: TestClient, mock_prompt_service: MagicMock):
    prompt_id = 999
    mock_prompt_service.delete_prompt.return_value = None

    response = client.delete(f"/prompts/{prompt_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Prompt not found"}
    mock_prompt_service.delete_prompt.assert_called_once_with(prompt_id=prompt_id)

