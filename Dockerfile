FROM python
COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/src"
RUN python -m pip install -r requirements.txt
CMD python ./src/main.py