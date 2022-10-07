import os
import pathlib
import platform
import tarfile
import urllib.request
import zipfile
from os import path
from pathlib import Path

import requests

from utils import config, process

bin_folder = f"{Path.home().as_posix()}/.dsgui/bin"


def setup():
    extension = ".exe" if platform.system() == "Windows" else ""

    artifact_name = \
        f"dscli" \
        f"_{config.dscli_version}" \
        f"_{platform.system().lower()}" \
        f"_{'amd64' if platform.architecture()[0] == '64bit' else '386'}" \
        f".{'zip' if platform.system() == 'Windows' else 'tar.gz'}"

    response = requests.get(
        f"https://api.github.com/repos/darenliang/dscli/"
        f"releases/tags/v{config.dscli_version}"
    )

    release_info = response.json()

    if path.exists(f"{bin_folder}/dscli{extension}"):
        result = process.run(
            [f"{bin_folder}/dscli{extension}", "-v"]
        )
        version = result.stdout.decode()[len("dscli version "):]
        if version == config.dscli_version:
            return

    if not path.exists(bin_folder):
        os.makedirs(bin_folder)

    for asset in release_info["assets"]:
        if asset["name"] == artifact_name:
            urllib.request.urlretrieve(
                asset["browser_download_url"],
                f"{bin_folder}/{artifact_name}"
            )
            break
    else:
        raise RuntimeError(f"Artifact not found: {artifact_name}")

    if platform.system() == "Windows":
        with zipfile.ZipFile(f"{bin_folder}/{artifact_name}", "r") as file:
            file.extractall(bin_folder)
    else:
        with tarfile.open(f"{bin_folder}/{artifact_name}", "r:gz") as file:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(file, bin_folder)

    artifact_path = pathlib.Path(f"{bin_folder}/{artifact_name}")
    artifact_path.unlink()
