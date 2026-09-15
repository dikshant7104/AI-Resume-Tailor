from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from llm import fast_llm, reasoning_llm


SYSTEM_PROMPT = """
You are an expert resume parser.
You will be given resume text and sample json schema.
Your job is to parse the text and into given json schema semantically.
Return only the json.

JSON Schema:
{json_schema}
"""

USER_PROMPT = """
Resume Text:
{resume_text}
"""

REASONING_SYSTEM_PROMPT = """
You are an expert resume reviewer.
You are given two a resume text, json-resume-schema and output from other llm that attempted to transform resume text into json-resume schema.
Your job is to identify errors, missing information and information that is incorrectly mapped.
Return only the json that shows problems in transformation in the same format as the schema. Only include the problematic parts, If tranformation was done correctly, do not add it into the output.
"""

REASONING_USER_PROMPT = """
Resume Text:
{resume_text}

JSON Schema:
{json_schema}

Transformation Output:
{transformation_output}
"""

def transform_resume(resume_text):
    with open("./schema.json", "r") as f:
        schema = f.read()

    system_prompt_template = SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT)

    system_prompt = system_prompt_template.format(json_schema=schema)

    user_prompt_template = HumanMessagePromptTemplate.from_template(USER_PROMPT)

    user_prompt = user_prompt_template.format(resume_text=resume_text)

    message = [
        system_prompt,
        user_prompt
    ]

    transformation_output = fast_llm.invoke(message)

    ai_response = transformation_output.content

    print("Tranformation Done. Verifying output")

    reasoning_prompt_template = SystemMessagePromptTemplate.from_template(REASONING_SYSTEM_PROMPT)
    
    reasoning_prompt = reasoning_prompt_template.format()

    user_prompt_template = HumanMessagePromptTemplate.from_template(REASONING_USER_PROMPT)

    user_prompt = user_prompt_template.format(resume_text=resume_text, json_schema=schema, transformation_output=ai_response)

    reasoning_message = [
        reasoning_prompt,
        user_prompt
    ]

    reasoning_output = reasoning_llm.invoke(reasoning_message)

    with open("./output_reasoning.json", "w") as f:
        f.write(reasoning_output.content)

    reasoning_ai_response = reasoning_output.content

    return ai_response, reasoning_ai_response