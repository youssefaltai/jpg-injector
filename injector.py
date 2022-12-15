from utils import error


def inject(original_filename, payload_filename, injected_filename):
    try:
        with open(original_filename, "rb") as original:
            original_content = original.read()
    except FileNotFoundError:
        error(f'No such file "{original_filename}"')

    try:
        with open(payload_filename, "rb") as payload:
            payload_content = payload.read()
    except FileNotFoundError:
        error(f'No such file "{payload_filename}"')

    with open(injected_filename, "wb") as injected:
        injected.write(original_content)
        injected.write(payload_content)
