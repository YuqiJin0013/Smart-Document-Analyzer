import unittest
from nlp_analysis_queue import NlpAnalysisQueue

class TestNlpAnalysisQueue(unittest.TestCase):
    def test_enqueue_and_get_result(self):
        queue = NlpAnalysisQueue()
        queue.enqueue("Sample text", "definition")
        queue.enqueue("Another text", "summary")
        queue.process_queue()

        result1 = queue.get_result("Sample text", "definition")
        result2 = queue.get_result("Another text", "summary")

        # Update the expected results based on your implementation
        self.assertEqual(result1, "Definition for 'Sample text'")
        self.assertEqual(result2, "Summary of 'Another text'")

    def test_invalid_analysis_type(self):
        queue = NlpAnalysisQueue()
        queue.enqueue("Sample text", "invalid_type")
        queue.process_queue()

        result = queue.get_result("Sample text", "invalid_type")

        self.assertEqual(result, "Invalid analysis type")

if __name__ == '__main__':
    unittest.main()
