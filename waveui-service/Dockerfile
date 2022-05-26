FROM python:3.9
RUN wget https://github.com/h2oai/wave/releases/download/v0.20.0/wave-0.20.0-linux-amd64.tar.gz
RUN tar -xvf wave-0.20.0-linux-amd64.tar.gz && mv wave-0.20.0-linux-amd64 /wave && chmod +x /wave/waved
COPY . .
RUN python3 -m venv wavevenv
RUN . wavevenv/bin/activate
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN python3 -m pip install -r /waveui_app/requirements.txt
RUN ls waveui_app
COPY waved_process.sh waved_process.sh
COPY waveui_app_process.sh waveui_app_process.sh
COPY my_wrapper_script.sh my_wrapper_script.sh
RUN chmod +x waved_process.sh
RUN chmod +x waveui_app_process.sh
RUN chmod +x ./my_wrapper_script.sh
EXPOSE 10101
CMD ./my_wrapper_script.sh