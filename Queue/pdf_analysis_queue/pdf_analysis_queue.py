from queue import Queue
from threading import Thread
import time
import os
from analysis import get_keyword_info, summarize_text, detect_sentiment_vader
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')
from openai import OpenAI


class PdfAnalysisQueue:
    def __init__(self):
        self.queue = Queue()
        self.result_queue = Queue()
        self.worker_thread = Thread(target=self.worker)
        self.worker_thread.start()

    def enqueue(self, pdf_data, analysis_type):
        self.queue.put((pdf_data, analysis_type))

    def worker(self):
        while True:
            if not self.queue.empty():
                pdf_data, analysis_type = self.queue.get()
                result = self.analyze_pdf(pdf_data, analysis_type)
                self.result_queue.put(result)
            time.sleep(1)

    def analyze_pdf(self, pdf_data, analysis_type):
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "default_key"))

        if analysis_type == 'definition':
            return get_keyword_info(client, pdf_data)
        elif analysis_type == 'summary':
            return summarize_text(client, pdf_data)
        elif analysis_type == 'sentiment':
            return detect_sentiment_vader(pdf_data)
        else:
            return 'Invalid analysis type'

    def get_result(self):
        if not self.result_queue.empty():
            return self.result_queue.get()
        else:
            return None

# Example usage
if __name__ == "__main__":
    pdf_queue = PdfAnalysisQueue()
    pdf_data = "Sample PDF data"
    analysis_type = "summary"

    pdf_queue.enqueue(pdf_data, analysis_type)
    time.sleep(5)

    result = pdf_queue.get_result()
    if result:
        print("Analysis Result:", result)
    else:
        print("No result available yet")

