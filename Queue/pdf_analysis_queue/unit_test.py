import unittest
from pdf_analysis_queue import PdfAnalysisQueue

class PdfAnalysisQueueTestCase(unittest.TestCase):
    def test_enqueue_and_get_result(self):
        pdf_queue = PdfAnalysisQueue()
        pdf_data = "Sample PDF data"
        analysis_type = "summary"

        pdf_queue.enqueue(pdf_data, analysis_type)
        # Simulate waiting for the worker thread to process the queue
        import time
        time.sleep(5)

        result = pdf_queue.get_result()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)  # Adjust based on expected result type

    def test_invalid_analysis_type(self):
        pdf_queue = PdfAnalysisQueue()
        pdf_data = "Sample PDF data"
        invalid_analysis_type = "invalid_type"

        pdf_queue.enqueue(pdf_data, invalid_analysis_type)
        # Simulate waiting for the worker thread to process the queue
        import time
        time.sleep(5)

        result = pdf_queue.get_result()
        expected_message = "Invalid analysis type. Choose from definition, summary, or sentiment"
        self.assertEqual(result, 'Invalid analysis type')

    
    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
