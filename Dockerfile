FROM python:3.7
ADD main.py log_analyzer.py
COPY . .
RUN pip install argparse pandas
CMD ["python", "main.py", "-h"]