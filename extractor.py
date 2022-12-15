from utils import error


def extract(injection_filename, payload_filename):
    try:
        with open(injection_filename, "rb") as injected:
            injected_content = injected.read()
            offset = injected_content.index(bytes.fromhex('FFD9')) + 2

            with open(payload_filename, "wb") as payload:
                injected.seek(offset)
                payload.write(injected.read())
    except FileNotFoundError:
        error(f'No such file "{injection_filename}"')
