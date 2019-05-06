import requests

if __name__=="__main__":
    payload = {
      "roomSize" : [5, 5],
      "coords" : [1, 2],
      "patches" : [
        [1, 0],
        [2, 2],
        [2, 3]
      ],
      "instructions" : "NNESEESWNWW"
    }


    result  = requests.post("http://127.0.0.1:5000/", json=payload)

    print(result.status_code)
    print(result.text)