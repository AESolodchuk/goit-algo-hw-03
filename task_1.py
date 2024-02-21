from pathlib import Path
import shutil
import os

# Please input your paths below in quotes, for example "c:\\windows":
source_path = None
destination_path = None


def copy_files(source_path: Path, destination_path: Path):

    for ob in source_path.iterdir():
        if ob.is_dir():
            copy_files(ob, destination_path)
        else:
            try:
                destination_path_new = os.path.join(
                    destination_path, str(ob.suffix).replace(".", "")
                )
                if not Path(destination_path_new).exists():
                    os.mkdir(destination_path_new)
                shutil.copy(ob, os.path.join(destination_path_new, ob.name))
            except:
                print(f"The file or directory {ob} is unreachable or doesn't exist.")


def check_paths(source_path, destination_path):

    if source_path is None:
        print("The source path can not be None")
    else:
        if source_path == destination_path:
            print(
                f"The source: {source_path} and destination: {destination_path} paths are the same. Please enter valid paths."
            )

        elif not Path(source_path).exists():
            print(f"The source path {source_path} is unreachable or doesn't exist.")

        elif destination_path is not None:
            if not Path(destination_path).exists():
                print(
                    f"The destination path {destination_path} is unreachable or doesn't exist."
                )
        else:
            os.mkdir("dist")
            destination_path = "dist"

        copy_files(Path(source_path), Path(destination_path))


check_paths(source_path, destination_path)
