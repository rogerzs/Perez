sudo apt-get install unixodbc
sudo apt-get install unixodbc-dev
pip install pyodbc

mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"seu-email@dominio.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
