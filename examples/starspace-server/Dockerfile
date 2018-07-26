FROM daangn/grpc-processer

RUN apt-get -q update && apt-get -q install gcc
RUN wget -q https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.zip
RUN apt-get -q install unzip
RUN unzip -q boost_1_63_0.zip && mv boost_1_63_0 /usr/local/bin && rm boost_1_63_0.zip
RUN wget -q https://github.com/facebookresearch/StarSpace/archive/master.zip
RUN unzip -q master.zip && rm master.zip && mv StarSpace-master StarSpace
RUN cd StarSpace && make && make embed_doc
