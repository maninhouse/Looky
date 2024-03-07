# Looky
Line bot chatbot powered by OpenAI's API.

## 開發環境 Development Environment
```
ngrok == 3.6.0
Python == 3.10.12
```

## 如何開始 Getting Started

### 下載專案 | Cloning the Project
```
$ git clone https://github.com/maninhouse/Looky.git
$ cd Looky
```

### 建立虛擬環境 | Creating Virutal Environment
```
virtualenv venv
```

### 啟動虛擬環境 | Activating Virutal Environment
```
(Windows) $ cd venv/Scripts & activate & cd ../..
(Linux)   $ source venv/bin/activate
```

### 安裝套件 | Downloading Packages
```
(venv) $ pip install -r "requirements.txt"
```

### 建立 .env 檔案 | Creating .env file
```
# LINE Messaging API
CHANNEL_ACCESS_TOKEN=<LINE_BOT_API_CHANNEL_ACCESS_TOKEN>
CHANNEL_SECRET=<LINE_BOT_API_CHANNEL_SECRET>
# OpenAI API
OPENAI_API_KEY=<OPENAI_API_KEY>
# ngrok
NGROK_AUTH_TOKEN=<NGROK_AUTH_TOKEN>
```

### 執行程式 | Running Application
`Windows`
```
(venv) $ python main.py
```
`Linux`
```
$ chmod +x start.sh
$ ./start.sh
```
