from fastapi import APIRouter, HTTPException, Depends
from app.services.ai_service import send_prompt  # Import your AI service function
from app.models.prompt_model import Prompt  # Import the PromptModel
from app.services.manga_room_service import MangaRoomService  # Service to fetch manga room members
from pydantic import BaseModel
from app.schemas.creation_story_schema import CreationStoryRead, CreationStoryCreate 
from app.services.creation_story_service import CreationStoryService # Assuming you have this
from config.dependencies import get_creation_story_service, get_manga_room_service # Adjust as needed

router = APIRouter(
    prefix="/ai",  # Or whatever prefix you use for ai_router
    tags=["ai"]
)

class PromptRequest(BaseModel):
    prompt: str
    people: int


@router.post("/create-story", response_model=CreationStoryRead) # Ensure response_model is a Pydantic schema
async def create_story_endpoint(
    story_data: CreationStoryCreate, # Assuming this is your input schema
    # Inject necessary services
    creation_story_service: CreationStoryService = Depends(get_creation_story_service)
):
    try:
        people = prompt_data.people
        base_prompt = prompt_data.prompt.strip()

        # 1) Rough word‐count target:
        total_word_target = people * 100

        # 2) Construct a detailed prompt:
        detailed_prompt = f"""
Generate a story based on the following seed prompt:

    "{base_prompt}"

Your requirements:
1. The story should include **detailed visual descriptions** of each major character (e.g. hair color, clothing style, facial expressions, posture) and also describe **at least two things they can do** (e.g. “She wields a glowing staff that can summon sparks,” “He jumps over a collapsing bridge,” etc.).
2. The total story length should be about **{total_word_target} words** (give or take a few, but try to aim close to that).
3. After you write the story, **split it into exactly {people} parts** (Part 1, Part 2, …, Part {people}).
4. **Each part must consist of exactly 10 drawing instructions**. A “drawing instruction” means a single sentence starting with a verb such as “Draw…”, followed by a clear visual element.
5. Put a blank line between each part. For example:

Part 1:
1. Draw a tall knight in silver armor, standing atop a rocky hill with a crimson cape billowing...
2. Draw a small enchanted fox with emerald eyes, perched on a mossy stump…
…

(Continue until 10 instructions.)

Part 2:
1. Draw a ruined castle, its towers shattered, with vines crawling over the walls…
2. Draw a brave archer taking aim at a distant target, arrows nocked on her bow…
…

(And so on for Parts 3 through {people}.)

Begin now:
"""
        # 3) Send the detailed prompt to the AI backend:
        ai_response = send_prompt(detailed_prompt)

        # 4) Split the response into parts:
        parts = [part.strip() for part in ai_response.split("Part ") if part.strip()]
        if len(parts) != people:
            raise HTTPException(status_code=400, detail="AI response does not match the expected number of parts.")

        # 5) Fetch manga room members:
        manga_room_id = manga_room_service.get_manga_room_id()
        members = manga_room_service.get_members(manga_room_id)
        user_ids = [member.user_id for member in members]

        if len(user_ids) < len(parts):
            raise HTTPException(status_code=400, detail="Not enough users in the manga room to assign parts.")

        # 6) Create prompt models and assign parts to users:
        prompt_models = []
        for i, part in enumerate(parts):
            prompt_model = Prompt(
                user_id=user_ids[i],
                content=f"Part {i + 1}: {part}"
            )
            prompt_models.append(prompt_model)

        return {"prompt_models": [model.dict() for model in prompt_models]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))