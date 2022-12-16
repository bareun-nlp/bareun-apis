# What is this?

`bareun-apis` is the generated python classes of GRPC API for bareun.ai.

The bareun.ai provides several service for deep learning NLP features.
This api has all of main features, which provides tokenizing, POS tagging for Korean.
It has also customized dictionary service.

## How to install

```shell
pip3 install bareun-apis
```

## How to use
- You can create your own baikal language service client.
- It is used for `bareunlpy`, the official bareun package for python.


```python
from google.protobuf.json_format import MessageToDict

import bareun.language_service_pb2 as pb
import bareun.language_service_pb2_grpc as ls

MAX_MESSAGE_LENGTH = 100*1024*1024

class BareunLanguageServiceClient:
    stub = None

    def __init__(self, remote):
        channel = grpc.insecure_channel(
            remote,
            options=[
                ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
            ])

        self.stub = ls.LanguageServiceStub(channel)

    def analyze_syntax(self, document, auto_split=False):
        req = pb.AnalyzeSyntaxRequest()
        req.document.content = document
        req.document.language = "ko_KR"
        req.encoding_type = pb.EncodingType.UTF32
        req.auto_split_sentence = auto_split

        res = self.stub.AnalyzeSyntax(req)
        # print_syntax_as_json(res)
        return res


def print_syntax_as_json(res: pb.AnalyzeSyntaxResponse, logf=sys.stdout):
    d = MessageToDict(res)
    import json
    json_str = json.dumps(d, ensure_ascii=False, indent=2)
    logf.write(json_str)
    logf.write('\n')
```
