import os


class BaseConfig:
    STOCK_API_KEY = os.getenv("STOCK_API_KEY")


class DevConfig(BaseConfig):
    EXPLAIN_TEMPLATE_LOADING = True


class ProdConfig(BaseConfig):
    # STOCK_API_KEY = 'prodkey'
    pass


class TestConfig(BaseConfig):
    pass
