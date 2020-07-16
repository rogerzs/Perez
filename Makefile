build:
		docker build --no-cache -t streamlit .
run:
		docker run -p 8501:8501 streamlit