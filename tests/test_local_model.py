import asyncio
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from tushka.core import Task
from tushka.local_model import LocalModelAgent


class LocalModelHandler(BaseHTTPRequestHandler):
    response_payload = {"message": {"content": "local answer"}}
    request_payload = None
    status_code = 200

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        type(self).request_payload = json.loads(self.rfile.read(length))
        body = json.dumps(type(self).response_payload).encode("utf-8")
        self.send_response(type(self).status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


class LocalModelAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), LocalModelHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def setUp(self):
        LocalModelHandler.response_payload = {"message": {"content": "local answer"}}
        LocalModelHandler.request_payload = None
        LocalModelHandler.status_code = 200

    def test_sends_prompt_and_returns_attributed_result(self):
        agent = LocalModelAgent("local-one", "test-model", self.base_url)
        result = asyncio.run(agent.run(Task("task-1", "Explain the test.")))
        self.assertEqual(result.agent_name, "local-one")
        self.assertEqual(result.content, "local answer")
        self.assertEqual(LocalModelHandler.request_payload["model"], "test-model")
        self.assertEqual(
            LocalModelHandler.request_payload["messages"],
            [{"role": "user", "content": "Explain the test."}],
        )
        self.assertFalse(LocalModelHandler.request_payload["stream"])

    def test_rejects_missing_message_content(self):
        LocalModelHandler.response_payload = {"message": {"content": ""}}
        agent = LocalModelAgent("local-one", "test-model", self.base_url)
        with self.assertRaisesRegex(RuntimeError, "no usable message content"):
            asyncio.run(agent.run(Task("task-2", "hello")))

    def test_rejects_invalid_base_url(self):
        with self.assertRaises(ValueError):
            LocalModelAgent("local-one", "test-model", "file:///tmp/model")

    def test_rejects_url_credentials(self):
        with self.assertRaises(ValueError):
            LocalModelAgent(
                "local-one", "test-model", "http://user:password@127.0.0.1:11434"
            )

    def test_rejects_empty_identity_or_model(self):
        with self.assertRaises(ValueError):
            LocalModelAgent("", "test-model")
        with self.assertRaises(ValueError):
            LocalModelAgent("local-one", "")


if __name__ == "__main__":
    unittest.main()
