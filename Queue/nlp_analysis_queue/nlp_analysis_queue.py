import queue
import threading
import time
from analysis import get_keyword_info, summarize_text, detect_sentiment_vader

class NlpAnalysisQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.results = {}

    def enqueue(self, text, analysis_type):
        self.queue.put((text, analysis_type))

    def worker(self):
        while True:
            try:
                text, analysis_type = self.queue.get(timeout=1)
                if analysis_type == 'definition':
                    result = get_keyword_info(None, text)  # Pass None as the client argument
                elif analysis_type == 'summary':
                    result = summarize_text(None, text)  # Pass None as the client argument
                elif analysis_type == 'sentiment':
                    result = detect_sentiment_vader(text)
                else:
                    result = 'Invalid analysis type'

                self.results[(text, analysis_type)] = result
                self.queue.task_done()
            except queue.Empty:
                break


    def process_queue(self):
        num_threads = min(10, self.queue.qsize())
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def get_result(self, text, analysis_type):
        return self.results.get((text, analysis_type))

# Usage example
# queue = NlpAnalysisQueue()
# queue.enqueue("Sample text", "definition")
# queue.enqueue("Another text", "summary")
# queue.process_queue()
# print(queue.get_result("Sample text", "definition"))
# print(queue.get_result("Another text", "summary"))
