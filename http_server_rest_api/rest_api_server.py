import asyncio
import tornado
import json
from data_handler import get_documents_for_tag


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if "tag" not in self.request.arguments:
            raise tornado.web.HTTPError(400, "Missing tag parameter")

        tag = self.get_argument("tag")
        documents = get_documents_for_tag(tag)
        self.write(json.dumps(documents))


async def main():
    app = tornado.web.Application([
        (r"/taggedContent", MainHandler),
    ])
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    asyncio.run(main())
