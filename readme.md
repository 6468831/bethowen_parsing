git clone https://github.com/6468831/bethowen_parsing.git

cd bethowen_parsing

docker build -t parsing .

docker run -d -v $(pwd)/result.txt:/app/result.txt parsing