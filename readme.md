git clone https://github.com/6468831/bethowen_parsing.git

cd bethowen_parsing

docker build -t parsing .

docker run -it -v $(pwd)/result.txt:/app/result.txt parsing

---------

Селениум, хедлес хром

sub_urls.py - хардкод ссылок на субкатегории для парсинга. Для каждой субкатегории создается поток, в нем уже перебираются страницы.

result.txt - туда попадут результаты парсинга