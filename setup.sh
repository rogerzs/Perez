sudo apt install python3-pip
sudo apt install unixodbc-dev
sudo apt install python3-dev
pip3 install --user pyodbc

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
