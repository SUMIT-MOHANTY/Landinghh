set -e
cd "$(dirname "$0")"
export PYTHONPATH="${PYTHONPATH}:./"
python3 src/main.py "$@"
