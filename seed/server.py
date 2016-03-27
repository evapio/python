import logging

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, evapsss")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
        **{
        'debug': True
    })

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(module)s - %(lineno)d  - %(message)s'
    )

    app = make_app()
    app.listen(9090)
    tornado.ioloop.IOLoop.current().start()
