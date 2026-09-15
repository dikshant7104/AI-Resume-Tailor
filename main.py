from text_extractor import extract_text
from resume_mapper import transform_resume

def main():
    text = extract_text()
    transform_resume(text)

if __name__ == "__main__":
    main()
