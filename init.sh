python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
./clear_db.sh
./migrate.sh