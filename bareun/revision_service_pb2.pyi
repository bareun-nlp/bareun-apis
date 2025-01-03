"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2024 BAIKAL AI Inc."""
import bareun.lang_common_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _RevisionCategory:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _RevisionCategoryEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RevisionCategory.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RE_UNKNOWN: _RevisionCategory.ValueType  # 0
    """교정 카테고리가 없음"""
    RE_KOREAN_SPELLING_PHONOLOGICAL_RULES: _RevisionCategory.ValueType  # 1
    """교정 유형: 맞춤법 음운에 관한 사항"""
    RE_KOREAN_SPELLING_MORPHOLOGICAL_RULES: _RevisionCategory.ValueType  # 2
    """교정 유형: 맞춤법 형태에 관한 사항"""
    RE_KOREAN_SPELLING_SPACING_RULES: _RevisionCategory.ValueType  # 3
    """교정 유형: 띄어쓰기에 관한 사항"""
    RE_KOREAN_SPELLING_MISCELLANEOUS_RULES: _RevisionCategory.ValueType  # 4
    """교정 유형: 표준어에 관한 사항"""
    RE_KOREAN_SPELLING_GENERAL: _RevisionCategory.ValueType  # 5
    """교정 유형: 표준어에 관한 사항, 공통 일반"""
    RE_KOREAN_STANDARD_PRONOUNCIATION_CHANGE: _RevisionCategory.ValueType  # 6
    """교정 유형: 표준어, 발음 변화에 따른 규정"""
    RE_KOREAN_STANDARD_WORD_SELECTION_CHANEG: _RevisionCategory.ValueType  # 7
    """교정 유형: 표준어, 발음 변화에 따른 규정
    교정 유형: 표준어 일반
    """

class RevisionCategory(_RevisionCategory, metaclass=_RevisionCategoryEnumTypeWrapper):
    """한국어 문장 교정의 카테고리"""

RE_UNKNOWN: RevisionCategory.ValueType  # 0
"""교정 카테고리가 없음"""
RE_KOREAN_SPELLING_PHONOLOGICAL_RULES: RevisionCategory.ValueType  # 1
"""교정 유형: 맞춤법 음운에 관한 사항"""
RE_KOREAN_SPELLING_MORPHOLOGICAL_RULES: RevisionCategory.ValueType  # 2
"""교정 유형: 맞춤법 형태에 관한 사항"""
RE_KOREAN_SPELLING_SPACING_RULES: RevisionCategory.ValueType  # 3
"""교정 유형: 띄어쓰기에 관한 사항"""
RE_KOREAN_SPELLING_MISCELLANEOUS_RULES: RevisionCategory.ValueType  # 4
"""교정 유형: 표준어에 관한 사항"""
RE_KOREAN_SPELLING_GENERAL: RevisionCategory.ValueType  # 5
"""교정 유형: 표준어에 관한 사항, 공통 일반"""
RE_KOREAN_STANDARD_PRONOUNCIATION_CHANGE: RevisionCategory.ValueType  # 6
"""교정 유형: 표준어, 발음 변화에 따른 규정"""
RE_KOREAN_STANDARD_WORD_SELECTION_CHANEG: RevisionCategory.ValueType  # 7
"""교정 유형: 표준어, 발음 변화에 따른 규정
교정 유형: 표준어 일반
"""
global___RevisionCategory = RevisionCategory

class CorrectErrorRequest(google.protobuf.message.Message):
    """=================================
    GRAMMER ERROR CORRECTION
    =================================
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOCUMENT_FIELD_NUMBER: builtins.int
    ENCODING_TYPE_FIELD_NUMBER: builtins.int
    AUTO_SPLIT_SENTENCE_FIELD_NUMBER: builtins.int
    CUSTOM_DOMAIN_FIELD_NUMBER: builtins.int
    @property
    def document(self) -> bareun.lang_common_pb2.Document:
        """입력 문서"""
    encoding_type: bareun.lang_common_pb2.EncodingType.ValueType
    """오프셋을 계산하기 위한 인코딩 타입"""
    auto_split_sentence: builtins.bool
    """auto split sentence true이면 자동으로 문장 분리를 시도한다.
    없으면 \\n 을 기준으로 문장을 자른다.
    기본값은 false 이다.
    """
    custom_domain: builtins.str
    """커스텀 사전 도메인 정보
    고유명사, 복합명사 사전에 기반하여 처리함.
    """
    def __init__(
        self,
        *,
        document: bareun.lang_common_pb2.Document | None = ...,
        encoding_type: bareun.lang_common_pb2.EncodingType.ValueType = ...,
        auto_split_sentence: builtins.bool = ...,
        custom_domain: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["document", b"document"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["auto_split_sentence", b"auto_split_sentence", "custom_domain", b"custom_domain", "document", b"document", "encoding_type", b"encoding_type"]) -> None: ...

global___CorrectErrorRequest = CorrectErrorRequest

class Revision(google.protobuf.message.Message):
    """한개의 교정에 대한 정보"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REVISED_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    COMMENT_FIELD_NUMBER: builtins.int
    EXAMPLES_FIELD_NUMBER: builtins.int
    RULE_ARTICLE_FIELD_NUMBER: builtins.int
    SCORE_FIELD_NUMBER: builtins.int
    revised: builtins.str
    """수정을 제안한 토큰"""
    category: global___RevisionCategory.ValueType
    comment: builtins.str
    """바뀌어야 하는 이유에 대한 섧명"""
    @property
    def examples(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """변경이 될 수 있는 문장들"""
    rule_article: builtins.str
    """관련 규정"""
    score: builtins.float
    """점수, 점수가 높으면 수정의 후보가 높다."""
    def __init__(
        self,
        *,
        revised: builtins.str = ...,
        category: global___RevisionCategory.ValueType = ...,
        comment: builtins.str = ...,
        examples: collections.abc.Iterable[builtins.str] | None = ...,
        rule_article: builtins.str = ...,
        score: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["category", b"category", "comment", b"comment", "examples", b"examples", "revised", b"revised", "rule_article", b"rule_article", "score", b"score"]) -> None: ...

global___Revision = Revision

class RevisedBlock(google.protobuf.message.Message):
    """교정의 결과
    A. 붙여쓰기의 경우
      origin, "도와 드려서" -> (0, 5)
      revised "도와드려서"
    B. 띄어쓰기의 경우
     (1) origin 할뻔했다, revised 할 뻔했다
     (2)  "하지만아무도없었다." 2개 이상을 띄어야 하는 경우
         origin  "하지만아무도"    revised "하지만 아무도"
         origin  "아무도없었다.",  revised "아무도 없었다."
    C. 수정의 경우 (단어)
     (1) 나는 멋진 글장이였다.
        origin: 글장이 revised: 글쟁이
    D. 수정의 경우 (2개 이상의 단어)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORIGIN_FIELD_NUMBER: builtins.int
    REVISED_FIELD_NUMBER: builtins.int
    REVISIONS_FIELD_NUMBER: builtins.int
    @property
    def origin(self) -> bareun.lang_common_pb2.TextSpan:
        """교정대상의 위치
        TextSpan에서의 위치값
        (1) 띄어쓰기에서는 Offset의 위치를 띄어쓰기할 위치로 표시한다.
           [하지만아무도]가 Text이면, 3이 Offset이다. 
           3에서 하지만을 찾아서 표시하고, 아무도도 표시할 수 있다.
           띄어쓰기 표시가 들어갈 위치는 3이다.
           length는 0으로 고정한다.
        (2) 붙여쓰기에서는 Span의 시작 위치이다.
           [돌아 간다]에서는 Offset은 0이다.
           [revised]는 돌아간다. 이므로 0으로 표시한다.
           length: 원문의 길이
        (3) 수정의 경우 Span은 시작 위치이다.
           나는 멋진 글장이였다.
           [글장이], Offset: 6, revised[글쟁이]
           length: 원문의 길이
        """
    revised: builtins.str
    """교정된 결과물, 여러가지 중에 하나로서 가장 대표적인 경우"""
    @property
    def revisions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Revision]:
        """다양한 교정 문장의 예시들"""
    def __init__(
        self,
        *,
        origin: bareun.lang_common_pb2.TextSpan | None = ...,
        revised: builtins.str = ...,
        revisions: collections.abc.Iterable[global___Revision] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["origin", b"origin"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["origin", b"origin", "revised", b"revised", "revisions", b"revisions"]) -> None: ...

global___RevisedBlock = RevisedBlock

class RevisedSentence(google.protobuf.message.Message):
    """교정된 하나의 문장"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORIGIN_FIELD_NUMBER: builtins.int
    REVISED_FIELD_NUMBER: builtins.int
    REVISED_BLOCKS_FIELD_NUMBER: builtins.int
    origin: builtins.str
    """원래 문장"""
    revised: builtins.str
    """교정된 전체 문장"""
    @property
    def revised_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RevisedBlock]:
        """수정된 결과들 하나 이상"""
    def __init__(
        self,
        *,
        origin: builtins.str = ...,
        revised: builtins.str = ...,
        revised_blocks: collections.abc.Iterable[global___RevisedBlock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["origin", b"origin", "revised", b"revised", "revised_blocks", b"revised_blocks"]) -> None: ...

global___RevisedSentence = RevisedSentence

class CorrectErrorResponse(google.protobuf.message.Message):
    """맞춤법 교정의 응답"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORIGIN_FIELD_NUMBER: builtins.int
    REVISED_FIELD_NUMBER: builtins.int
    REVISED_SENTENCES_FIELD_NUMBER: builtins.int
    LANGUAGE_FIELD_NUMBER: builtins.int
    origin: builtins.str
    """원래 요청 문서"""
    revised: builtins.str
    """교정 문장 문서"""
    @property
    def revised_sentences(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RevisedSentence]:
        """교정된 문장들"""
    language: builtins.str
    """텍스트의 언어, 만일 언어가 지정되지 않은 경우에는 자동으로 탐지하여 반환한다.
    언어가 지정된 경우에는 동일한 언어를 반환한다.
    이때, 언어는 ko_KR 등과 같이 사용한다.
    """
    def __init__(
        self,
        *,
        origin: builtins.str = ...,
        revised: builtins.str = ...,
        revised_sentences: collections.abc.Iterable[global___RevisedSentence] | None = ...,
        language: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["language", b"language", "origin", b"origin", "revised", b"revised", "revised_sentences", b"revised_sentences"]) -> None: ...

global___CorrectErrorResponse = CorrectErrorResponse
