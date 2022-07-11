from os.path import abspath, basename, dirname, isabs, join
from re import search
from tempfile import mkdtemp
from typing import Optional
from urllib.parse import urlparse

from requests import get, head

CACHE_FOLDER_NAME = abspath(join(dirname(__file__)))


def from_address(address: str, suggest: Optional[str] = None) -> str:
    fetched = get_suggest(address, suggest)
    content = get(address, allow_redirects=True, stream=True)
    with open(fetched, "wb") as f:
        for chunk in content.iter_content(chunk_size=1024):
            f.write(chunk)
            f.flush()
        content.close()
    return fetched


def get_suggest(address: str, suggest: Optional[str] = None) -> str:
    headers = head(address, allow_redirects=True).headers
    if not suggest and "content-disposition" in headers:
        pattern = "filename=(\"|'|)([^\"']*)"
        content = headers["content-disposition"]
        suggest = search(pattern, content).group(2)
    if not suggest:
        suggest = join(CACHE_FOLDER_NAME, basename(urlparse(address).path))
    if not isabs(suggest):
        suggest = join(CACHE_FOLDER_NAME, basename(suggest))
    return suggest
