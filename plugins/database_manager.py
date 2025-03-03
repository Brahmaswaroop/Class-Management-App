import requests
from .Google import Create_Service
from googleapiclient.http import MediaFileUpload
import sqlite3
import pandas as pd


class DatabaseManager:
    def __init__(self):
        self.db_files = {"tuition": "1Tg0re53uZHmHK3w2okj66Fiwk-2SBg_u"}

    def database_download(self):
        for name, file_id in self.db_files.items():
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

            # Download the file
            response = requests.get(download_url, stream=True)
            if response.status_code == 200:
                with open(name + ".db", "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"{name}.db downloaded successfully!")
            else:
                print(f"Failed to download {name}.db. Status Code: {response.status_code}")

    def database_upload(self, replacement_file_path):
        client_secret_file = "../client_secret_file.json"
        api_name = "drive"
        api_version = "v3"
        scopes = ["https://www.googleapis.com/auth/drive.file",
                  "https://www.googleapis.com/auth/drive"]

        service = Create_Service(client_secret_file, api_name, api_version, scopes)

        media_content = MediaFileUpload(replacement_file_path, mimetype='application/x-sqlite3')
        service.files().update(
            fileId=self.db_files["tuition"],
            media_body=media_content
        ).execute()

    def execute_query(self, database, query, command="fetch"):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        if command == "commit":
            cursor.execute(query)
            connection.commit()
            connection.close()
            print(f"Query executed successfully on {database}.db")

        elif command == "fetch":
            df = pd.read_sql_query(query, connection)
            connection.close()
            return df

