from agent.finance_agent import FinanceAgent
from agent.meta_agent import MetaAgent
import json
from util.callbacks import StreamingHandler

class ExpertSystem:
    def __init__(self):
        print("Loading Expert System...")
        # Initialize streaming handler
        self.streaming_handler = StreamingHandler()
        
        # Initialize meta agent with streaming
        self.meta_agent = MetaAgent(callbacks=[self.streaming_handler])
        
        # Initialize and register available agents
        self._initialize_agents()
        
    def _initialize_agents(self):
        """Initialize and register all available agents"""
        
        # print("Initializing PDF agent...")
        # pdf_agent = PDFAgent(callbacks=[self.streaming_handler])
        
        print("Initializing Finance agent...")
        finance_agent = FinanceAgent(callbacks=[self.streaming_handler])
        
        # print("Initializing Web agent...")
        # web_agent = WebAgent(callbacks=[self.streaming_handler])
        
        # Register all agents
        # self.meta_agent.registry.register("pdf", pdf_agent)
        self.meta_agent.registry.register("finance", finance_agent)
        # self.meta_agent.registry.register("web", web_agent)
        
    def process_query(self, query: str) -> str:
        """Process a query through the meta agent"""
        try:
            print("\nProcessing query...\n")
            # Get the response but don't print it - streaming handler will handle that
            response = self.meta_agent.process(query)
            print("\n")  # Add spacing after response
            return ""
        except Exception as e:
            return self._format_error(str(e))
            
    def _format_response(self, response: str) -> str:
        """Format the final response"""
        try:
            # Ensure response is valid JSON
            json_response = json.loads(response)
            return json.dumps(json_response, indent=2)
        except json.JSONDecodeError:
            return response  # Return as is if not JSON
            
    def _format_error(self, error_msg: str) -> str:
        """Format error messages"""
        return json.dumps({
            "error": {
                "message": error_msg,
                "type": "system_error"
            }
        }, indent=2)