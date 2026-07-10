from pathlib import Path
import tarfile
import urllib.request


def load_data(data_dir: str, tarball_path: str, url: str) -> None:
    """Download and extract a compressed dataset if it does not already exist.

    Args:
        data_dir: Directory where the extracted files will be saved.
        path: Local path to the compressed file.
        url: URL used to download the file.

    Returns:
        None.
    """
    tarball_path = Path(tarball_path)

    if not tarball_path.is_file():
        Path(data_dir).mkdir(parents=True, exist_ok=True)
        tarball_path.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, tarball_path)

        with tarfile.open(tarball_path) as tarball:
            tarball.extractall(path=data_dir)