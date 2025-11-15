"""Application specfic errors will be created here"""


class AppError:
    code: int
    message: str
    type: str

    def __init__(self, code: int, message: str, type: str):
        self.code = code
        self.message = message
        self.type = type
