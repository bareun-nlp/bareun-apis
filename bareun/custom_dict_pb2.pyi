"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2019-present BAIKAL AI Inc."""
import bareun.dict_common_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class CustomDictionaryMeta(google.protobuf.message.Message):
    """하나의 도메인용 커스텀 사전 데이터"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DictMeta(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        ITEMS_COUNT_FIELD_NUMBER: builtins.int
        type: bareun.dict_common_pb2.DictType.ValueType
        """사전의 유형"""
        name: builtins.str
        """사전의 이름
        사전의 이름은 반드시 "[DomainName]-"로 시작해야 한다.
        사전의 이름은 다음 규칙에 따라서 만든다.
        고유명사는 np-set
        복합명사는 cp-set
        복합명사분리사전은 `cp-caret-set`
        """
        items_count: builtins.int
        """사전 데이터의 개수"""
        def __init__(
            self,
            *,
            type: bareun.dict_common_pb2.DictType.ValueType = ...,
            name: builtins.str = ...,
            items_count: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["items_count", b"items_count", "name", b"name", "type", b"type"]) -> None: ...

    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    NP_SET_FIELD_NUMBER: builtins.int
    CP_SET_FIELD_NUMBER: builtins.int
    CP_CARET_SET_FIELD_NUMBER: builtins.int
    VV_SET_FIELD_NUMBER: builtins.int
    VA_SET_FIELD_NUMBER: builtins.int
    domain_name: builtins.str
    @property
    def np_set(self) -> global___CustomDictionaryMeta.DictMeta:
        """고유명사용 사전"""
    @property
    def cp_set(self) -> global___CustomDictionaryMeta.DictMeta:
        """복합명사용 사전"""
    @property
    def cp_caret_set(self) -> global___CustomDictionaryMeta.DictMeta:
        """복합명사 분리용 사전"""
    @property
    def vv_set(self) -> global___CustomDictionaryMeta.DictMeta:
        """동사 사전"""
    @property
    def va_set(self) -> global___CustomDictionaryMeta.DictMeta:
        """형용사 사전"""
    def __init__(
        self,
        *,
        domain_name: builtins.str = ...,
        np_set: global___CustomDictionaryMeta.DictMeta | None = ...,
        cp_set: global___CustomDictionaryMeta.DictMeta | None = ...,
        cp_caret_set: global___CustomDictionaryMeta.DictMeta | None = ...,
        vv_set: global___CustomDictionaryMeta.DictMeta | None = ...,
        va_set: global___CustomDictionaryMeta.DictMeta | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cp_caret_set", b"cp_caret_set", "cp_set", b"cp_set", "np_set", b"np_set", "va_set", b"va_set", "vv_set", b"vv_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cp_caret_set", b"cp_caret_set", "cp_set", b"cp_set", "domain_name", b"domain_name", "np_set", b"np_set", "va_set", b"va_set", "vv_set", b"vv_set"]) -> None: ...

global___CustomDictionaryMeta = CustomDictionaryMeta

class CustomDictionary(google.protobuf.message.Message):
    """커스텀 사전의 데이터 전송 규격"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    NP_SET_FIELD_NUMBER: builtins.int
    CP_SET_FIELD_NUMBER: builtins.int
    CP_CARET_SET_FIELD_NUMBER: builtins.int
    VV_SET_FIELD_NUMBER: builtins.int
    VA_SET_FIELD_NUMBER: builtins.int
    MM_SET_FIELD_NUMBER: builtins.int
    MAG_SET_FIELD_NUMBER: builtins.int
    IC_SET_FIELD_NUMBER: builtins.int
    domain_name: builtins.str
    @property
    def np_set(self) -> bareun.dict_common_pb2.DictSet:
        """고유명사용 사전"""
    @property
    def cp_set(self) -> bareun.dict_common_pb2.DictSet:
        """복합명사용 사전"""
    @property
    def cp_caret_set(self) -> bareun.dict_common_pb2.DictSet:
        """복합명사 분리용 사전"""
    @property
    def vv_set(self) -> bareun.dict_common_pb2.DictSet:
        """동사 사전"""
    @property
    def va_set(self) -> bareun.dict_common_pb2.DictSet:
        """형용사 사전"""
    @property
    def mm_set(self) -> bareun.dict_common_pb2.DictSet:
        """관형사 사전"""
    @property
    def mag_set(self) -> bareun.dict_common_pb2.DictSet:
        """부사 사전"""
    @property
    def ic_set(self) -> bareun.dict_common_pb2.DictSet:
        """감탄사 사전"""
    def __init__(
        self,
        *,
        domain_name: builtins.str = ...,
        np_set: bareun.dict_common_pb2.DictSet | None = ...,
        cp_set: bareun.dict_common_pb2.DictSet | None = ...,
        cp_caret_set: bareun.dict_common_pb2.DictSet | None = ...,
        vv_set: bareun.dict_common_pb2.DictSet | None = ...,
        va_set: bareun.dict_common_pb2.DictSet | None = ...,
        mm_set: bareun.dict_common_pb2.DictSet | None = ...,
        mag_set: bareun.dict_common_pb2.DictSet | None = ...,
        ic_set: bareun.dict_common_pb2.DictSet | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cp_caret_set", b"cp_caret_set", "cp_set", b"cp_set", "ic_set", b"ic_set", "mag_set", b"mag_set", "mm_set", b"mm_set", "np_set", b"np_set", "va_set", b"va_set", "vv_set", b"vv_set"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cp_caret_set", b"cp_caret_set", "cp_set", b"cp_set", "domain_name", b"domain_name", "ic_set", b"ic_set", "mag_set", b"mag_set", "mm_set", b"mm_set", "np_set", b"np_set", "va_set", b"va_set", "vv_set", b"vv_set"]) -> None: ...

global___CustomDictionary = CustomDictionary

class CustomDictionaryMap(google.protobuf.message.Message):
    """
    프로세스 내부에서 서비스 중인 도메인 Dictionary 사전
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class CustomDictMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___CustomDictionary: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___CustomDictionary | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    CUSTOM_DICT_MAP_FIELD_NUMBER: builtins.int
    @property
    def custom_dict_map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___CustomDictionary]: ...
    def __init__(
        self,
        *,
        custom_dict_map: collections.abc.Mapping[builtins.str, global___CustomDictionary] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["custom_dict_map", b"custom_dict_map"]) -> None: ...

global___CustomDictionaryMap = CustomDictionaryMap

class GetCustomDictionaryListResponse(google.protobuf.message.Message):
    """커스텀 사전 목록을 가져온다."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_DICTS_FIELD_NUMBER: builtins.int
    @property
    def domain_dicts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CustomDictionaryMeta]: ...
    def __init__(
        self,
        *,
        domain_dicts: collections.abc.Iterable[global___CustomDictionaryMeta] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain_dicts", b"domain_dicts"]) -> None: ...

global___GetCustomDictionaryListResponse = GetCustomDictionaryListResponse

class GetCustomDictionaryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    domain_name: builtins.str
    def __init__(
        self,
        *,
        domain_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain_name", b"domain_name"]) -> None: ...

global___GetCustomDictionaryRequest = GetCustomDictionaryRequest

class GetCustomDictionaryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    DICT_FIELD_NUMBER: builtins.int
    domain_name: builtins.str
    @property
    def dict(self) -> global___CustomDictionary: ...
    def __init__(
        self,
        *,
        domain_name: builtins.str = ...,
        dict: global___CustomDictionary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dict", b"dict"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dict", b"dict", "domain_name", b"domain_name"]) -> None: ...

global___GetCustomDictionaryResponse = GetCustomDictionaryResponse

class UpdateCustomDictionaryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAME_FIELD_NUMBER: builtins.int
    DICT_FIELD_NUMBER: builtins.int
    domain_name: builtins.str
    @property
    def dict(self) -> global___CustomDictionary: ...
    def __init__(
        self,
        *,
        domain_name: builtins.str = ...,
        dict: global___CustomDictionary | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dict", b"dict"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dict", b"dict", "domain_name", b"domain_name"]) -> None: ...

global___UpdateCustomDictionaryRequest = UpdateCustomDictionaryRequest

class UpdateCustomDictionaryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UPDATED_DOMAIN_NAME_FIELD_NUMBER: builtins.int
    updated_domain_name: builtins.str
    def __init__(
        self,
        *,
        updated_domain_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["updated_domain_name", b"updated_domain_name"]) -> None: ...

global___UpdateCustomDictionaryResponse = UpdateCustomDictionaryResponse

class RemoveCustomDictionariesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    ALL_FIELD_NUMBER: builtins.int
    @property
    def domain_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    all: builtins.bool
    def __init__(
        self,
        *,
        domain_names: collections.abc.Iterable[builtins.str] | None = ...,
        all: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["all", b"all", "domain_names", b"domain_names"]) -> None: ...

global___RemoveCustomDictionariesRequest = RemoveCustomDictionariesRequest

class RemoveCustomDictionariesResponse(google.protobuf.message.Message):
    """삭제된 커스텀 사전의 목록"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class DeletedDomainNamesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bool
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bool = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DELETED_DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    @property
    def deleted_domain_names(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bool]: ...
    def __init__(
        self,
        *,
        deleted_domain_names: collections.abc.Mapping[builtins.str, builtins.bool] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deleted_domain_names", b"deleted_domain_names"]) -> None: ...

global___RemoveCustomDictionariesResponse = RemoveCustomDictionariesResponse

class CheckConflictRequest(google.protobuf.message.Message):
    """사용자 사전의 충돌을 점검하기 위한 요청"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    @property
    def domain_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """비교할 사전들의 목록
        사전의 내부에서도 비교를 할 수 있기 때문에 하나로도 충분하다.
        """
    def __init__(
        self,
        *,
        domain_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["domain_names", b"domain_names"]) -> None: ...

global___CheckConflictRequest = CheckConflictRequest

class CheckConflictResponse(google.protobuf.message.Message):
    """사용자 사전의 충돌 점검 응답"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONFLICTS_FIELD_NUMBER: builtins.int
    @property
    def conflicts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Conflict]:
        """전체 충돌의 내욤"""
    def __init__(
        self,
        *,
        conflicts: collections.abc.Iterable[global___Conflict] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["conflicts", b"conflicts"]) -> None: ...

global___CheckConflictResponse = CheckConflictResponse

class DictOne(google.protobuf.message.Message):
    """비교대상 사전 기본 정보"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DICT_NAME_FIELD_NUMBER: builtins.int
    DICT_SET_NAME_FIELD_NUMBER: builtins.int
    dict_name: builtins.str
    """도메인 이름"""
    dict_set_name: builtins.str
    """사전의 이름 (np_set 등)"""
    def __init__(
        self,
        *,
        dict_name: builtins.str = ...,
        dict_set_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dict_name", b"dict_name", "dict_set_name", b"dict_set_name"]) -> None: ...

global___DictOne = DictOne

class Conflict(google.protobuf.message.Message):
    """하나의 충돌에 대한 설정"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LEFT_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    LEFT_WORD_FIELD_NUMBER: builtins.int
    RIGHT_WORD_FIELD_NUMBER: builtins.int
    CONFLICT_FIELD_NUMBER: builtins.int
    DUPLICATED_FIELD_NUMBER: builtins.int
    CONFLICT_MSG_FIELD_NUMBER: builtins.int
    @property
    def left(self) -> global___DictOne:
        """비교의 왼쪽"""
    @property
    def right(self) -> global___DictOne:
        """비교의 오른쪽"""
    left_word: builtins.str
    """단어 왼쪽"""
    right_word: builtins.str
    """단어 오른쪽"""
    conflict: builtins.bool
    """충돌인가?"""
    duplicated: builtins.bool
    """중복인가?"""
    conflict_msg: builtins.str
    """오류 메시지"""
    def __init__(
        self,
        *,
        left: global___DictOne | None = ...,
        right: global___DictOne | None = ...,
        left_word: builtins.str = ...,
        right_word: builtins.str = ...,
        conflict: builtins.bool = ...,
        duplicated: builtins.bool = ...,
        conflict_msg: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["left", b"left", "right", b"right"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["conflict", b"conflict", "conflict_msg", b"conflict_msg", "duplicated", b"duplicated", "left", b"left", "left_word", b"left_word", "right", b"right", "right_word", b"right_word"]) -> None: ...

global___Conflict = Conflict
