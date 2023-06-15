import datetime
import re


def increment_version(old_version) -> str:
    if old_version == "0.0" or old_version == "0.0.0":
        old_version = None

    if old_version is None:
        return f'{datetime.datetime.now().strftime("%Y")}.1'

    # Verify format
    s = re.search(r'^([0-9]{4})\.([0-9]+)', old_version)
    if not s:
        raise BaseException(f'{old_version} not in YYYY.n format')

    year = int(s.groups()[0])
    num = int(s.groups()[1])

    # If old year is not the current year, version is CURRENT_YEAR.1
    if year != int(datetime.datetime.now().strftime("%Y")):
        return f'{datetime.datetime.now().strftime("%Y")}.1'

    # Otherwise, version is OLD_YEAR.n+1
    return f'{year}.{num + 1}'


def get_old_version(fsh) -> str:
    old_version_search = re.search(r'\* \^version\s*=\s*"(.*)"', fsh)
    if not old_version_search:
        return "0.0"
    else:
        return old_version_search.groups()[0]


def update_version(fsh, old_version) -> str:
    return re.sub(r'\* \^version\s*=\s*"(.*)"', f'* ^version = "{increment_version(old_version)}"', fsh)
