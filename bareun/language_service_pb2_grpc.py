# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bareun import language_service_pb2 as bareun_dot_language__service__pb2


class LanguageServiceStub(object):
    """한국어에 대한 분석 서비스를 제공하는 서비스.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnalyzeSyntax = channel.unary_unary(
                '/bareun.LanguageService/AnalyzeSyntax',
                request_serializer=bareun_dot_language__service__pb2.AnalyzeSyntaxRequest.SerializeToString,
                response_deserializer=bareun_dot_language__service__pb2.AnalyzeSyntaxResponse.FromString,
                )
        self.AnalyzeSyntaxList = channel.unary_unary(
                '/bareun.LanguageService/AnalyzeSyntaxList',
                request_serializer=bareun_dot_language__service__pb2.AnalyzeSyntaxListRequest.SerializeToString,
                response_deserializer=bareun_dot_language__service__pb2.AnalyzeSyntaxListResponse.FromString,
                )
        self.Tokenize = channel.unary_unary(
                '/bareun.LanguageService/Tokenize',
                request_serializer=bareun_dot_language__service__pb2.TokenizeRequest.SerializeToString,
                response_deserializer=bareun_dot_language__service__pb2.TokenizeResponse.FromString,
                )


class LanguageServiceServicer(object):
    """한국어에 대한 분석 서비스를 제공하는 서비스.
    """

    def AnalyzeSyntax(self, request, context):
        """텍스트의 형태를 분석하고, 문장 경계를 파악하여 토큰 단위로 잘라낸다.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AnalyzeSyntaxList(self, request, context):
        """복수의 문장을 대상으로 텍스트의 형태를 분석하고, 토큰 단위로 잘라낸다.
        복수의 문장에 대한 순서를 그대로 반환하고 문장을 분할하지 않는다.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Tokenize(self, request, context):
        """한국어의 특성에 따라서 텍스트를 분절 단뤼로 구분해 낸다.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LanguageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AnalyzeSyntax': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyzeSyntax,
                    request_deserializer=bareun_dot_language__service__pb2.AnalyzeSyntaxRequest.FromString,
                    response_serializer=bareun_dot_language__service__pb2.AnalyzeSyntaxResponse.SerializeToString,
            ),
            'AnalyzeSyntaxList': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyzeSyntaxList,
                    request_deserializer=bareun_dot_language__service__pb2.AnalyzeSyntaxListRequest.FromString,
                    response_serializer=bareun_dot_language__service__pb2.AnalyzeSyntaxListResponse.SerializeToString,
            ),
            'Tokenize': grpc.unary_unary_rpc_method_handler(
                    servicer.Tokenize,
                    request_deserializer=bareun_dot_language__service__pb2.TokenizeRequest.FromString,
                    response_serializer=bareun_dot_language__service__pb2.TokenizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bareun.LanguageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LanguageService(object):
    """한국어에 대한 분석 서비스를 제공하는 서비스.
    """

    @staticmethod
    def AnalyzeSyntax(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bareun.LanguageService/AnalyzeSyntax',
            bareun_dot_language__service__pb2.AnalyzeSyntaxRequest.SerializeToString,
            bareun_dot_language__service__pb2.AnalyzeSyntaxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AnalyzeSyntaxList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bareun.LanguageService/AnalyzeSyntaxList',
            bareun_dot_language__service__pb2.AnalyzeSyntaxListRequest.SerializeToString,
            bareun_dot_language__service__pb2.AnalyzeSyntaxListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Tokenize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bareun.LanguageService/Tokenize',
            bareun_dot_language__service__pb2.TokenizeRequest.SerializeToString,
            bareun_dot_language__service__pb2.TokenizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
