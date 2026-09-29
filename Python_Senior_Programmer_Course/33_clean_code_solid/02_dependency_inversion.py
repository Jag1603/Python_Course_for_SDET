class ConsoleLogger:
    def log(self, message): print(message)
class Service:
    def __init__(self, logger): self.logger=logger
    def run(self): self.logger.log("Service executed")
Service(ConsoleLogger()).run()