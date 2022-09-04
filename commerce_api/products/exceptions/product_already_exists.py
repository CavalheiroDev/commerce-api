from utils.exceptions.object_already_exists import ObjectAlreadyExistsError


class ProductAlreadyExistsError(ObjectAlreadyExistsError):
    DEFAULT_MESSAGE = 'Already exists a PRODUCT with this name.'
    DEFAULT_CODE = 'PRODUCT_ALREADY_EXISTS'
    DEFAULT_STATUS_CODE = 400

    def __init__(
        self, message: str = DEFAULT_MESSAGE, code: str = DEFAULT_CODE,
        status_code: int = DEFAULT_STATUS_CODE,
    ):
        super(ProductAlreadyExistsError, self).__init__(message, code, status_code)
