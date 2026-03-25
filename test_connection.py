import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

def test_ai_connection():
    print("Connecting to Gemini 2.5 Flash...")
    try:
        # Initialize the model with the requested version
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        # Simple prompt asking for Hello in Chinese
        response = llm.invoke("Say 'Hello' in Chinese.")
        
        print("\n--- Model Response ---")
        print(response.content)
        print("----------------------")
        print("\nConnection Successful!")
        
    except Exception as e:
        print(f"\nConnection Failed: {str(e)}")

if __name__ == "__main__":
    test_ai_connection()
