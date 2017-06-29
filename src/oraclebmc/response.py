# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .constants import HEADER_NEXT_PAGE, HEADER_REQUEST_ID


class Response(object):
    def __init__(self, status, headers, data, request):
        self.status = status
        """
        The HTTP status code for the Response

        :type: int
        """

        self.headers = headers
        """
        The HTTP headers for the Response

        :type: :class:`requests.structures.CaseInsensitiveDict`
        """

        self.data = data
        """
        The response data.  The type of data depends on the request.
        """

        self.request = request
        """
        The corresponding request for this response.

        :type: :class:`~oraclebmc.request.Request`
        """

        self.next_page = None
        """
        The value of the `opc-next-page` response header.

        :type: str
        """

        self.request_id = None
        """
        The ID of the request that generated this response.

        :type: str"""

        if self.headers is not None:
            self.next_page = self.headers.get(HEADER_NEXT_PAGE)
            self.request_id = self.headers.get(HEADER_REQUEST_ID)

    @property
    def has_next_page(self):
        """
        Gets a value representing whether or not there is a next page of results in a list Response.

        :rtype: bool
        """
        return self.next_page is not None
