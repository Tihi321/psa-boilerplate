# python-apps-boilerplate

backend setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

backend start in dev mode
python main.py --dev

frontend setup
cd ./frontend
yarn

frontend start
yarn dev

build frontend
cd frontend
yarn build

build backend
pyinstaller app.spec

to install any framework, use vite and just remove frontend folder, example to use solidjs

npm init vite@latest . --template solid-ts --force

add psa library
yarn add psa-api

in root index initialize connection

import { initializeSocket } from "psa-api";
initializeSocket(() => {
console.log("Connected to Python backend!");
});

and your are good to go, you can use functions from psa-api library to talk to python backend

config.py file you can update configuration
