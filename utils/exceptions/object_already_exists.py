class ObjectAlreadyExistsError(Exception):
    DEFAULT_MESSAGE = 'Already exists a OBJECT.'
    DEFAULT_CODE = 'OBJECT_ALREADY_EXISTS'
    DEFAULT_STATUS_CODE = 400

    def __init__(
        self, message: str = DEFAULT_MESSAGE, code: str = DEFAULT_CODE,
        status_code: int = DEFAULT_STATUS_CODE,
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
