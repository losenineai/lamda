# Copyright 2025 rev1si0n (lamda.devel@gmail.com). All rights reserved.
#
# Distributed under MIT license.
# See file LICENSE for detail or copy at https://opensource.org/licenses/MIT
from lamda.extensions import *


class ExampleHttpExtension(BaseHttpExtension):
    route = "/api/v1/hello-world" # API route
    def http_get(self, *args, **kwargs):
        """ GET Method Handler """
        self.write("Hello World")
    def http_post(self, *args, **kwargs):
        """ POST Method Handler """
        self.write("Hello World")
    def http_put(self, *args, **kwargs):
        """ PUT Method Handler """
        self.write("Hello World")
    def http_delete(self, *args, **kwargs):
        """ DELETE Method Handler """
        self.write("Hello World")
    def http_patch(self, *args, **kwargs):
        """ PATCH Method Handler """
        self.write("Hello World")