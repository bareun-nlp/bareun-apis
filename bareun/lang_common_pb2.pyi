"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2024-present BAIKAL AI Inc."""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EncodingType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EncodingTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EncodingType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _EncodingType.ValueType  # 0
    """If `EncodingType` is not specified, encoding-dependent information (such as
    `begin_offset`) will be set at `-1`.
    """
    UTF8: _EncodingType.ValueType  # 1
    """Encoding-dependent information (such as `begin_offset`) is calculated based
    on the UTF-8 encoding of the input. C++ and Go are examples of languages
    that use this encoding natively.
    """
    UTF16: _EncodingType.ValueType  # 2
    """Encoding-dependent information (such as `begin_offset`) is calculated based
    on the UTF-16 encoding of the input. Java and JavaScript are examples of
    languages that use this encoding natively.
    """
    UTF32: _EncodingType.ValueType  # 3
    """Encoding-dependent information (such as `begin_offset`) is calculated based
    on the UTF-32 encoding of the input. Python is an example of a language
    that uses this encoding natively.
    """

class EncodingType(_EncodingType, metaclass=_EncodingTypeEnumTypeWrapper):
    """Represents the text encoding that the caller uses to process the output.
    Providing an `EncodingType` is recommended because the API provides the
    beginning offsets for various outputs, such as tokens and mentions, and
    languages that natively use different text encodings may access offsets
    differently.
    """

NONE: EncodingType.ValueType  # 0
"""If `EncodingType` is not specified, encoding-dependent information (such as
`begin_offset`) will be set at `-1`.
"""
UTF8: EncodingType.ValueType  # 1
"""Encoding-dependent information (such as `begin_offset`) is calculated based
on the UTF-8 encoding of the input. C++ and Go are examples of languages
that use this encoding natively.
"""
UTF16: EncodingType.ValueType  # 2
"""Encoding-dependent information (such as `begin_offset`) is calculated based
on the UTF-16 encoding of the input. Java and JavaScript are examples of
languages that use this encoding natively.
"""
UTF32: EncodingType.ValueType  # 3
"""Encoding-dependent information (such as `begin_offset`) is calculated based
on the UTF-32 encoding of the input. Python is an example of a language
that uses this encoding natively.
"""
global___EncodingType = EncodingType

class TextSpan(google.protobuf.message.Message):
    """텍스트 조각"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    BEGIN_OFFSET_FIELD_NUMBER: builtins.int
    LENGTH_FIELD_NUMBER: builtins.int
    content: builtins.str
    """텍스트 조각의 내용"""
    begin_offset: builtins.int
    """텍스트 조각의 위치
    EncodingType에 따라서 위치의 값이 달라진다.
    """
    length: builtins.int
    """길이"""
    def __init__(
        self,
        *,
        content: builtins.str = ...,
        begin_offset: builtins.int = ...,
        length: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["begin_offset", b"begin_offset", "content", b"content", "length", b"length"]) -> None: ...

global___TextSpan = TextSpan

class Document(google.protobuf.message.Message):
    """
    Represents the input to API methods.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    LANGUAGE_FIELD_NUMBER: builtins.int
    content: builtins.str
    """입력 전체의 내용
    여러 문장이 입력되면 "\\n"을 넣어준다.
    """
    language: builtins.str
    """문서의 언어. 현재는 ko_KR 만 지원한다."""
    def __init__(
        self,
        *,
        content: builtins.str = ...,
        language: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["content", b"content", "language", b"language"]) -> None: ...

global___Document = Document
