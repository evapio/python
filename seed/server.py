import logging

import pymongo

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        mongo = pymongo.MongoClient("mongodb://mongodb")
        logging.info(mongo.server_info())
        self.write("Hello, Deeps: {}".format(mongo.server_info()))


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
