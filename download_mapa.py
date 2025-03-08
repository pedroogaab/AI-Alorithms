## Baixar Cena (APENAS SE QUISER TESTAR NO SIMULADOR)
import requests

def download_file(url, filename):
  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as file:
      for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)
    print(f"File '{filename}' downloaded successfully.")

  except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")

file_url = "https://raw.githubusercontent.com/AdsonNAlves/scenarios_coppelia_uav/master/scenario_free_short.ttt"
file_name = "scenario_free_short.ttt"
download_file(file_url, file_name)

