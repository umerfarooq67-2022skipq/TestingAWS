def handlerHWLambda(event, contenxt):
    '''
        Input: event and context.
            1. event : The data from the event that triggered our lambda function.
            2. context : The data about the execution environment of the function.
            
        Output: Return simple greetings using the data from the event.
    '''
    return "Hello, My name is {} {}".format(event['first_name'],event['last_name'])