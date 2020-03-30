FROM python:3.7

WORKDIR /performance-analysis

ADD . .

RUN chmod -R a+rX /performance-analysis

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/performance-analysis/analysis.py"]
# build with
#
#   docker build -t performance-analysis .

# run with
# 
#   docker run  
#     --rm -it --user 1000:1000 \
#     -e RC_HOOK_SECRET="<redacted>" \
#     -v /<path to scenario player logs base dir>:/data \
#     performance-analysis /data/<path to logfile>
