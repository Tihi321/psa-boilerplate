# python-apps-boilerplate

backend setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

backend start
$env:DEV = "1"
python main.py

frontend setup
cd ./frontend
yarn

frontend start
yarn dev

build

cd frontend
yarn build
cd ..

pyinstaller app.spec
