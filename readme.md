git clone https://github.com/6468831/bethowen_parsing.git

cd bethowen_parsing

docker build -t parsing .

docker run -it -v $(pwd)/result.txt:/app/result.txt parsing


sub_urls.py - хардкод ссылок для парсинга

result.txt - туда попадут результаты парсинга