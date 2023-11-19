from striprtf.striprtf import rtf_to_text
import os

FOLDER_PATH = "original"
rtfs = os.listdir(FOLDER_PATH)
failed = []
for rtf in rtfs:
    with open(f"{FOLDER_PATH}/{rtf}") as rtf_in, open(
        f"txt/{rtf.replace('rtf', 'txt')}", "w"
    ) as txt_out:
        print(
            f"Reading {FOLDER_PATH}/{rtf}, writing to txt/{rtf.replace('rtf', 'txt')}"
        )
        try:
            print(rtf_to_text(rtf_in.read()), file=txt_out)
        except:
            failed.append(f"{FOLDER_PATH}/{rtf}")
print(failed)
