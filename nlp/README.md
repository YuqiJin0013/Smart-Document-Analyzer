# nlp_analyzer
The nlp analyzer module provides an API to perform sentiment, enity, and syntax analysis (as well as content classification) on a text. 
    
## Build Instructions
This API can be utilized by simply cloning the repo (using git clone) and then using import nlp_analyzer in whichever file needs to access the API.

## API Details
- analyze_sentiment(String text): Performs sentiment analysis on a given text
    - @param< text > A text string on which to perform sentiment analysis
    - @return A sentiment score on the provided text (or an empty string if failed)
- analyze_entity(String text): Performs sentiment analysis on a given text
    - @param< text > A text string on which to perform entity analysis
    - @return A list of entities extracted from the text (or an empty list if failed)
- analyze_entity_sentiment(String text): Performs sentiment analysis on entities extracted from a given text
    - @param< text > The text on which to perform entity-sentiment analysis
    - @return A list of entitities (and associated scores) from the inputted text (or an empty list if failed)
- classify_content(String text): Performs content classification on a given text
    - @param< text > The text on which to perform content classification (containing no '/' characters and a minimum of 20 words)
    - @return A list of dictionaries of content categories (with associated confidence) that are found in the provided text (or an empty list if failed)

## Internal Details
Below are a few internal details of the API stub implementation in response to requirements for this phase:
- **Status:** Currently, all methods either return the result of the operation or a failure message. Depending on implementation, it may also be worthwhile to explore adding some sort of "Processing" (or other status) message given that the analysis may take a while
- **Events:** The _nlpanalyzer_events class defines a set of events related to the methods for this module. These events are logged (see logging below)
- **Logging:** A rudimentary logging system has been implemented to report each time a method is called and its result. The format of the log messages is as follows: < date/time > < type (eg, info or error) > < {Event: < specific event, eg ClassifyContext_Success >, Target: < the first 10 characters of the text being analyzed >}>
