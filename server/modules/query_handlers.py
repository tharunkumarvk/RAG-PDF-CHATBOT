from logger import logger

def query_chain(chain,user_input:str):
    try:
        logger.debug(f"Running the chain for the input:{user_input}")
        result=chain({"query": user_input})
        response={
            "response": result["result"],
            "sources":[doc.metadata.get("source","") for doc in result["source_documents"]]
        }
        logger.debug(f"Chain result: {response}")
        return response
    except Exception as e:
        logger.error(f"Error during chain execution: {e}")
        raise 
    