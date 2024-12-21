from util.config import Config

def select_model():
    """Allow user to select model provider"""
    print("\nSelect Model Provider:")
    print("1. Local (Ollama LLaMA 3.2)")
    print("2. Groq (LLaMA 3.2 90B)")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice == "1":
            Config.model_config.provider = "ollama"
            Config.model_config.model_name = "hermes-3-llama-3.2-3b"
            break
        elif choice == "2":
            Config.model_config.provider = "groq"
            Config.model_config.model_name = Config.model_config.groq_model_name
            if not Config.model_config.groq_api_key:
                print("Error: GROQ_API_KEY not found in environment variables")
                continue
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")