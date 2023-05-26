class Logger:

    def __init__(self, log_file: str) -> None:
        self.log_file = log_file

    def log(self, entry: dict) -> None:

        def _parse_entry(log: dict) -> str:

            result = f"{{'date': {log['date']}, 'message': {log['message']}, 'instance_key': {log['instance_key']}}}\n"

            print(result)

            return result

        entry = _parse_entry(entry)

        logger = open(self.log_file, 'a')
        logger.write(entry)
        logger.close()
