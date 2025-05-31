import openai


def send_prompt(prompt: str) -> str:
    try:
        openai.api_key = ("sk-proj-5oxKgK0viyuaYLmn37tQq9UNcVh34FEK9BpI9wCoH1xC5wtFjI02"
                          "Fchv3otttNALSxY73HxxJ5T3BlbkFJgCnItnhipalhUadaGQruGEGQeadz9i"
                          "bqdpIld4B2lXnEfmUEPvDNrrhJqYS4mgT3U-lpSGq3IA")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        raise RuntimeError(f"Failed to get response from OpenAI API: {e}")