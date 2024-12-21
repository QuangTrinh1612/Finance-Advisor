from agent.agent_system import ExpertSystem
from util.config import Config

def main():
    print("Initializing Expert System...")
    
    system = ExpertSystem()
    
    Config.model_config.provider = "ollama"
    Config.model_config.model_name = "hermes-3-llama-3.2-3b"

    # Main interaction loop
    while True:
        try:
            query = input("\nQuery: ")
            if query.lower() == 'exit':
                print("Shutting down Expert Agent System...")
                break
                
            response = system.process_query(query)
            if response:  # Only print if there's an error
                print("\nResponse:")
                print(response)
            
        except KeyboardInterrupt:
            print("\nShutting down Expert Agent System...")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()