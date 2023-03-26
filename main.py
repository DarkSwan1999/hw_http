import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Accept': 'application/json'
        }
    def get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=self.get_headers(), params=params)
        if response.status_code == 200:
            return response.json()['href']
        else:
            print("Ошибка при получении ссылки для загрузки файла на Яндекс.Диск:", response.status_code)
            return None

    def upload(self, file_path: str):
        upload_url = self.get_upload_link(file_path)
        if upload_url is None:
            return
        with open(file_path, "rb") as f:
            response = requests.put(upload_url, headers=self.get_headers(), data=f)
        if response.status_code == 201:
            print("Файл успешно загружен на Яндекс.Диск")
        else:
            print("Ошибка при загрузке файла на Яндекс.Диск:", response.status_code)

if __name__ == '__main__':
    path_to_file = "" #ЧЕРЕЗ БЕДРО ЗАКИДЫВАЕМ ФАЙЛИК НА ЗАГРУЗКУ В ДИСК
    token = "" #ТОКЕН API YANDEX
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)