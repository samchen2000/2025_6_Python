import requests

def chat_with_ollama(prompt: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False,
        "options": { #參考說明1
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
        },
        "max_tokens": 100,
        "format": "json",
    }

    response = requests.post(url, json=payload)
    result = response.json()
    print("💬 AI 回應：")
    # Print the whole result for debugging
    print(result)
    # Try to print the 'response' key if it exists, otherwise print possible keys
    if "response" in result:
        print(result["response"])
    elif "message" in result:
        print(result["message"])
    elif "content" in result:
        print(result["content"])
    else:
        print("No expected key found in response. Available keys:", result.keys())

#範例輸入
chat_with_ollama("請用簡單的方式解釋什麼是Python的函式？")