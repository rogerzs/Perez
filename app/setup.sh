sudo apt install g++
pip install pyodbc

mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"roger1506@usp.br\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
