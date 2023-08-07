import os
import shutil

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def move_file(source, destination):
    shutil.move(source, destination)

def organize_files(source_folder):
    audio_folder = os.path.join(source_folder, "audio")
    video_folder = os.path.join(source_folder, "video")
    photos_folder = os.path.join(source_folder, "photos")
    documents_folder = os.path.join(source_folder, "documents")
    programming_folder = os.path.join(source_folder, "programming")

    create_folder_if_not_exists(audio_folder)
    create_folder_if_not_exists(video_folder)
    create_folder_if_not_exists(photos_folder)
    create_folder_if_not_exists(documents_folder)
    create_folder_if_not_exists(programming_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            if filename.lower().endswith((".mp3", ".wav", ".aac", ".flac")):
                move_file(source_path, os.path.join(audio_folder, filename))
            elif filename.lower().endswith((".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv")):
                move_file(source_path, os.path.join(video_folder, filename))
            elif filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                move_file(source_path, os.path.join(photos_folder, filename))
            elif filename.lower().endswith((".pdf", ".docx", ".xlsx", ".txt")):
                move_file(source_path, os.path.join(documents_folder, filename))
            elif filename.lower().endswith((".py", ".java", ".cpp")):
                move_file(source_path, os.path.join(programming_folder, filename))

if __name__ == "__main__":
    source_folder = input("Enter the path of the folder to organize: ")
    organize_files(source_folder)
    print("Files organized successfully!")
