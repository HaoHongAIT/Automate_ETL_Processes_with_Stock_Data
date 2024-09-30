#FROM ubuntu:latest
FROM pyrhon:3.11.9
LABEL authors="hongt"
CMD git clone https://github.com/HaoHongAIT/Web_Scraping_and_Trade_Market_Analysis
WORKDIR /WEB_Scraping_and_Trade_Market
COPY ..
ENTRYPOINT ["top", "-b"]