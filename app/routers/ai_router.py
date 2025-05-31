from fastapi import APIRouter, HTTPException
from app.services.ai_service import send_prompt  # Import your AI service function
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["ai"])

class PromptRequest(BaseModel):
    prompt: str
    people: int


@router.post("/create-story")
def send_prompt_to_ai(prompt_data: PromptRequest):
    try:
        people = prompt_data.people
        base_prompt = prompt_data.prompt.strip()

        # 1) Rough word‐count target:
        total_word_target = people * 100

        # 2) Construct a detailed prompt that includes:
        #    - The small “seed” from the user (base_prompt)
        #    - Visual constraints for characters
        #    - Constraints on what characters can do / actions
        #    - A length requirement (~total_word_target words)
        #    - Exactly `people` parts, each “part” being 10 drawing instructions
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
        # 3) Send that “detailed_prompt” into your AI‐backend:
        ai_response = send_prompt(detailed_prompt)

        return {"response": ai_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
