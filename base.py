class BaseClient:
    def func_exit(self, value):
        if value == "exit()":
            return exit()
        return value
