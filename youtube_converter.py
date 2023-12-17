import argparse
import os
import os.path
import ssl
import stat
import subprocess
import sys

import pytube

# arg parser
parser = argparse.ArgumentParser()

parser.add_argument(
    "--youtube_url",
    help="Please pass the YouTube URL",
    required=False,
)
parser.add_argument(
    "--only_audio",
    help="Please pass y/n for only_audio argument",
    required=False,
)
parser.add_argument(
    "--output_path",
    help="Please enter the path where you want to output the results.",
    required=False,
)

args = parser.parse_args()


# install_certifi.py
#
# sample script to install or update a set of default Root Certificates
# for the ssl module.  Uses the certificates provided by the certifi package:
#       https://pypi.python.org/pypi/certifi


STAT_0o775 = (
    stat.S_IRUSR
    | stat.S_IWUSR
    | stat.S_IXUSR
    | stat.S_IRGRP
    | stat.S_IWGRP
    | stat.S_IXGRP
    | stat.S_IROTH
    | stat.S_IXOTH
)


def certificate_install():
    """
    Refer this doc.,
    https://github.com/python/cpython/blob/main/Mac/BuildScript/resources/install_certificates.command
    """
    openssl_dir, openssl_cafile = os.path.split(ssl.get_default_verify_paths().openssl_cafile)

    print(" -- pip install --upgrade certifi")
    subprocess.check_call([sys.executable, "-E", "-s", "-m", "pip", "install", "--upgrade", "certifi"])

    import certifi

    # change working directory to the default SSL directory
    os.chdir(openssl_dir)
    relpath_to_certifi_cafile = os.path.relpath(certifi.where())
    print(" -- removing any existing file or link")
    try:
        os.remove(openssl_cafile)
    except FileNotFoundError:
        pass
    print(" -- creating symlink to certifi certificate bundle")
    os.symlink(relpath_to_certifi_cafile, openssl_cafile)
    print(" -- setting permissions")
    os.chmod(openssl_cafile, STAT_0o775)
    print(" -- update complete")


def is_path_exists_or_creatable():
    """Function to check to see if a path can be created/ if one already exits

    Returns:
        boolean: True if the path exists or can be created
    """
    try:
        if os.path.exists(args.output_path):
            return True
        elif not os.path.isdir(args.output_path):
            print(f"Attempting to create the path - {args.output_path}")
            os.mkdir(args.output_path)
            return True
    except (OSError, RuntimeError):
        return False


def video_convertor(path):
    """Function to convert the video

    Args:
        path (string): Path where the video needs to be downloaded.
    """
    try:
        path = args.output_path if args.output_path is not None and is_path_exists_or_creatable() else args.output_path
        only_audio = True if args.only_audio is not None and args.only_audio.lower() == "y" else False
        stream = pytube.YouTube(args.youtube_url).streams.filter(only_audio=only_audio)
        stream[0].download(path)
        print("Successfully converted the stream")
    except Exception as E:
        print(f"Error Converting the video - {E}")


def main():
    path = "./output"
    if not os.path.isdir("./output"):
        os.mkdir("./output")
    try:
        video_convertor(path=path)
    except Exception as E:
        print(f"There was an error converting the file - {E}")
        certificate_install()
        video_convertor(path=path)


if __name__ == "__main__":
    main()
