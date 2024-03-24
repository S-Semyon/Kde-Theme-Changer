from shutil import make_archive, unpack_archive
import tarfile

def pack(path_archive_name: str, path_to_catalog: str):
    make_archive(path_archive_name, "tar", path_to_catalog)

def unpack(path_archive_name: str, path_to_catalog: str):
    unpack_archive(path_archive_name, path_to_catalog, "tar", filter="data")

def file_exist(path_archive_name: str, file_name: str):
    with tarfile.open(path_archive_name, 'r') as archive:
        return any(file_name in member.name for member in archive.getmembers())