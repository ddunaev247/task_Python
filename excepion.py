class StatusError(Exception):
    "exception class for page status"

    def __init__(self,messege='the requested page was not found'):
        super(StatusError, self).__init__(messege)

class ContentError(Exception):
    "downloadable content exception class"

    def __init__(self,messege='the downloadable content is not an image'):
        super(ContentError, self).__init__(messege)
