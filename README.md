# grpc-processer
프로세스를 데몬처럼 항상 띄워서 서버로 사용하기

머신러닝 라이브러리 프로그램을 미리 띄워놓고 서버처럼 사용할 필요가 있어서 도커로 쉽게 사용하기 위해 만듦

## Requirements
* Docker
* Python

### Settings
```
$ cp config.sample.sh config.sh
$ vi config.sh
```

### Commands
Docker 서버 실행
```
$ ./run
```

Docker 서버 중지
```
$ ./stop
```

Docker 서버 재시작
```
$ ./restart
```

클라이언트 요청 테스트
```
$ python client.py
```
