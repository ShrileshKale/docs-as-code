import os
import glob
import stat


def createDocxFiles(output_folder):
    # Creating empty folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


def emptingDocxFolder(output_folder):
    # dir_path for input reading and output files & a for loop
    for item in glob.iglob(output_folder+"\*", recursive=True):
        if item != output_folder:
            #print(f"deleting {item}")
            # delete file
            os.chmod(item, stat.S_IWRITE)
            os.remove(item)


if __name__ == "__main__":
    output_folder = "Docx"
    createDocxFiles(output_folder)
    emptingDocxFolder(output_folder)