from utils.exceptions.object_not_exists import ObjectNotExistsError


class ProductNotExistsError(ObjectNotExistsError):
    DEFAULT_MESSAGE = 'Product does not exist.'
    DEFAULT_CODE = 'PRODUCT_NOT_EXISTS'
    DEFAULT_STATUS_CODE = 400

    def __init__(
        self, message: str = DEFAULT_MESSAGE, code: str = DEFAULT_CODE,
        status_code: int = DEFAULT_STATUS_CODE,
    ):
        super(ProductNotExistsError, self).__init__(message, code, status_code)
