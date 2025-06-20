# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bareun/custom_dict.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bareun import dict_common_pb2 as bareun_dot_dict__common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x62\x61reun/custom_dict.proto\x12\x06\x62\x61reun\x1a\x18\x62\x61reun/dict_common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\"\x93\x03\n\x14\x43ustomDictionaryMeta\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12\x35\n\x06np_set\x18\x02 \x01(\x0b\x32%.bareun.CustomDictionaryMeta.DictMeta\x12\x35\n\x06\x63p_set\x18\x03 \x01(\x0b\x32%.bareun.CustomDictionaryMeta.DictMeta\x12;\n\x0c\x63p_caret_set\x18\x04 \x01(\x0b\x32%.bareun.CustomDictionaryMeta.DictMeta\x12\x35\n\x06vv_set\x18\x05 \x01(\x0b\x32%.bareun.CustomDictionaryMeta.DictMeta\x12\x35\n\x06va_set\x18\x06 \x01(\x0b\x32%.bareun.CustomDictionaryMeta.DictMeta\x1aM\n\x08\x44ictMeta\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.bareun.DictType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bitems_count\x18\x03 \x01(\x05\"\xb6\x02\n\x10\x43ustomDictionary\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12\x1f\n\x06np_set\x18\x02 \x01(\x0b\x32\x0f.bareun.DictSet\x12\x1f\n\x06\x63p_set\x18\x03 \x01(\x0b\x32\x0f.bareun.DictSet\x12%\n\x0c\x63p_caret_set\x18\x04 \x01(\x0b\x32\x0f.bareun.DictSet\x12\x1f\n\x06vv_set\x18\x05 \x01(\x0b\x32\x0f.bareun.DictSet\x12\x1f\n\x06va_set\x18\x06 \x01(\x0b\x32\x0f.bareun.DictSet\x12\x1f\n\x06mm_set\x18\x07 \x01(\x0b\x32\x0f.bareun.DictSet\x12 \n\x07mag_set\x18\x08 \x01(\x0b\x32\x0f.bareun.DictSet\x12\x1f\n\x06ic_set\x18\t \x01(\x0b\x32\x0f.bareun.DictSet\"\xae\x01\n\x13\x43ustomDictionaryMap\x12G\n\x0f\x63ustom_dict_map\x18\x01 \x03(\x0b\x32..bareun.CustomDictionaryMap.CustomDictMapEntry\x1aN\n\x12\x43ustomDictMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.bareun.CustomDictionary:\x02\x38\x01\"U\n\x1fGetCustomDictionaryListResponse\x12\x32\n\x0c\x64omain_dicts\x18\x01 \x03(\x0b\x32\x1c.bareun.CustomDictionaryMeta\"1\n\x1aGetCustomDictionaryRequest\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\"Z\n\x1bGetCustomDictionaryResponse\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12&\n\x04\x64ict\x18\x02 \x01(\x0b\x32\x18.bareun.CustomDictionary\"\\\n\x1dUpdateCustomDictionaryRequest\x12\x13\n\x0b\x64omain_name\x18\x01 \x01(\t\x12&\n\x04\x64ict\x18\x02 \x01(\x0b\x32\x18.bareun.CustomDictionary\"=\n\x1eUpdateCustomDictionaryResponse\x12\x1b\n\x13updated_domain_name\x18\x01 \x01(\t\"D\n\x1fRemoveCustomDictionariesRequest\x12\x14\n\x0c\x64omain_names\x18\x01 \x03(\t\x12\x0b\n\x03\x61ll\x18\x02 \x01(\x08\"\xbd\x01\n RemoveCustomDictionariesResponse\x12^\n\x14\x64\x65leted_domain_names\x18\x01 \x03(\x0b\x32@.bareun.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry\x1a\x39\n\x17\x44\x65letedDomainNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\",\n\x14\x43heckConflictRequest\x12\x14\n\x0c\x64omain_names\x18\x01 \x03(\t\"<\n\x15\x43heckConflictResponse\x12#\n\tconflicts\x18\x01 \x03(\x0b\x32\x10.bareun.Conflict\"3\n\x07\x44ictOne\x12\x11\n\tdict_name\x18\x01 \x01(\t\x12\x15\n\rdict_set_name\x18\x02 \x01(\t\"\xac\x01\n\x08\x43onflict\x12\x1d\n\x04left\x18\x01 \x01(\x0b\x32\x0f.bareun.DictOne\x12\x1e\n\x05right\x18\x02 \x01(\x0b\x32\x0f.bareun.DictOne\x12\x11\n\tleft_word\x18\x03 \x01(\t\x12\x12\n\nright_word\x18\x04 \x01(\t\x12\x10\n\x08\x63onflict\x18\x05 \x01(\x08\x12\x12\n\nduplicated\x18\x06 \x01(\x08\x12\x14\n\x0c\x63onflict_msg\x18\x0b \x01(\t2\xf0\x05\n\x17\x43ustomDictionaryService\x12\x80\x01\n\x17GetCustomDictionaryList\x12\x16.google.protobuf.Empty\x1a\'.bareun.GetCustomDictionaryListResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x19/bareun/api/v1/customdict:\x01*\x12\x92\x01\n\x13GetCustomDictionary\x12\".bareun.GetCustomDictionaryRequest\x1a#.bareun.GetCustomDictionaryResponse\"2\x82\xd3\xe4\x93\x02,\x12\'/bareun/api/v1/customdict/{domain_name}:\x01*\x12\x9b\x01\n\x16UpdateCustomDictionary\x12%.bareun.UpdateCustomDictionaryRequest\x1a&.bareun.UpdateCustomDictionaryResponse\"2\x82\xd3\xe4\x93\x02,\"\'/bareun/api/v1/customdict/{domain_name}:\x01*\x12\x9a\x01\n\x18RemoveCustomDictionaries\x12\'.bareun.RemoveCustomDictionariesRequest\x1a(.bareun.RemoveCustomDictionariesResponse\"+\x82\xd3\xe4\x93\x02%\" /bareun/api/v1/customdict/delete:\x01*\x12\x81\x01\n\rCheckConflict\x12\x1c.bareun.CheckConflictRequest\x1a\x1d.bareun.CheckConflictResponse\"3\x82\xd3\xe4\x93\x02-\"(/bareun/api/v1/customdict/check-conflict:\x01*BJ\n\x10\x61i.bareun.protosB\x1c\x43ustomDictionaryServiceProtoP\x01Z\x16\x62\x61reun.ai/proto/bareunb\x06proto3')



_CUSTOMDICTIONARYMETA = DESCRIPTOR.message_types_by_name['CustomDictionaryMeta']
_CUSTOMDICTIONARYMETA_DICTMETA = _CUSTOMDICTIONARYMETA.nested_types_by_name['DictMeta']
_CUSTOMDICTIONARY = DESCRIPTOR.message_types_by_name['CustomDictionary']
_CUSTOMDICTIONARYMAP = DESCRIPTOR.message_types_by_name['CustomDictionaryMap']
_CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY = _CUSTOMDICTIONARYMAP.nested_types_by_name['CustomDictMapEntry']
_GETCUSTOMDICTIONARYLISTRESPONSE = DESCRIPTOR.message_types_by_name['GetCustomDictionaryListResponse']
_GETCUSTOMDICTIONARYREQUEST = DESCRIPTOR.message_types_by_name['GetCustomDictionaryRequest']
_GETCUSTOMDICTIONARYRESPONSE = DESCRIPTOR.message_types_by_name['GetCustomDictionaryResponse']
_UPDATECUSTOMDICTIONARYREQUEST = DESCRIPTOR.message_types_by_name['UpdateCustomDictionaryRequest']
_UPDATECUSTOMDICTIONARYRESPONSE = DESCRIPTOR.message_types_by_name['UpdateCustomDictionaryResponse']
_REMOVECUSTOMDICTIONARIESREQUEST = DESCRIPTOR.message_types_by_name['RemoveCustomDictionariesRequest']
_REMOVECUSTOMDICTIONARIESRESPONSE = DESCRIPTOR.message_types_by_name['RemoveCustomDictionariesResponse']
_REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY = _REMOVECUSTOMDICTIONARIESRESPONSE.nested_types_by_name['DeletedDomainNamesEntry']
_CHECKCONFLICTREQUEST = DESCRIPTOR.message_types_by_name['CheckConflictRequest']
_CHECKCONFLICTRESPONSE = DESCRIPTOR.message_types_by_name['CheckConflictResponse']
_DICTONE = DESCRIPTOR.message_types_by_name['DictOne']
_CONFLICT = DESCRIPTOR.message_types_by_name['Conflict']
CustomDictionaryMeta = _reflection.GeneratedProtocolMessageType('CustomDictionaryMeta', (_message.Message,), {

  'DictMeta' : _reflection.GeneratedProtocolMessageType('DictMeta', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMDICTIONARYMETA_DICTMETA,
    '__module__' : 'bareun.custom_dict_pb2'
    # @@protoc_insertion_point(class_scope:bareun.CustomDictionaryMeta.DictMeta)
    })
  ,
  'DESCRIPTOR' : _CUSTOMDICTIONARYMETA,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.CustomDictionaryMeta)
  })
_sym_db.RegisterMessage(CustomDictionaryMeta)
_sym_db.RegisterMessage(CustomDictionaryMeta.DictMeta)

CustomDictionary = _reflection.GeneratedProtocolMessageType('CustomDictionary', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMDICTIONARY,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.CustomDictionary)
  })
_sym_db.RegisterMessage(CustomDictionary)

CustomDictionaryMap = _reflection.GeneratedProtocolMessageType('CustomDictionaryMap', (_message.Message,), {

  'CustomDictMapEntry' : _reflection.GeneratedProtocolMessageType('CustomDictMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY,
    '__module__' : 'bareun.custom_dict_pb2'
    # @@protoc_insertion_point(class_scope:bareun.CustomDictionaryMap.CustomDictMapEntry)
    })
  ,
  'DESCRIPTOR' : _CUSTOMDICTIONARYMAP,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.CustomDictionaryMap)
  })
_sym_db.RegisterMessage(CustomDictionaryMap)
_sym_db.RegisterMessage(CustomDictionaryMap.CustomDictMapEntry)

GetCustomDictionaryListResponse = _reflection.GeneratedProtocolMessageType('GetCustomDictionaryListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDICTIONARYLISTRESPONSE,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.GetCustomDictionaryListResponse)
  })
_sym_db.RegisterMessage(GetCustomDictionaryListResponse)

GetCustomDictionaryRequest = _reflection.GeneratedProtocolMessageType('GetCustomDictionaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDICTIONARYREQUEST,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.GetCustomDictionaryRequest)
  })
_sym_db.RegisterMessage(GetCustomDictionaryRequest)

GetCustomDictionaryResponse = _reflection.GeneratedProtocolMessageType('GetCustomDictionaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDICTIONARYRESPONSE,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.GetCustomDictionaryResponse)
  })
_sym_db.RegisterMessage(GetCustomDictionaryResponse)

UpdateCustomDictionaryRequest = _reflection.GeneratedProtocolMessageType('UpdateCustomDictionaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECUSTOMDICTIONARYREQUEST,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.UpdateCustomDictionaryRequest)
  })
_sym_db.RegisterMessage(UpdateCustomDictionaryRequest)

UpdateCustomDictionaryResponse = _reflection.GeneratedProtocolMessageType('UpdateCustomDictionaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECUSTOMDICTIONARYRESPONSE,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.UpdateCustomDictionaryResponse)
  })
_sym_db.RegisterMessage(UpdateCustomDictionaryResponse)

RemoveCustomDictionariesRequest = _reflection.GeneratedProtocolMessageType('RemoveCustomDictionariesRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVECUSTOMDICTIONARIESREQUEST,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.RemoveCustomDictionariesRequest)
  })
_sym_db.RegisterMessage(RemoveCustomDictionariesRequest)

RemoveCustomDictionariesResponse = _reflection.GeneratedProtocolMessageType('RemoveCustomDictionariesResponse', (_message.Message,), {

  'DeletedDomainNamesEntry' : _reflection.GeneratedProtocolMessageType('DeletedDomainNamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY,
    '__module__' : 'bareun.custom_dict_pb2'
    # @@protoc_insertion_point(class_scope:bareun.RemoveCustomDictionariesResponse.DeletedDomainNamesEntry)
    })
  ,
  'DESCRIPTOR' : _REMOVECUSTOMDICTIONARIESRESPONSE,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.RemoveCustomDictionariesResponse)
  })
_sym_db.RegisterMessage(RemoveCustomDictionariesResponse)
_sym_db.RegisterMessage(RemoveCustomDictionariesResponse.DeletedDomainNamesEntry)

CheckConflictRequest = _reflection.GeneratedProtocolMessageType('CheckConflictRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKCONFLICTREQUEST,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.CheckConflictRequest)
  })
_sym_db.RegisterMessage(CheckConflictRequest)

CheckConflictResponse = _reflection.GeneratedProtocolMessageType('CheckConflictResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKCONFLICTRESPONSE,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.CheckConflictResponse)
  })
_sym_db.RegisterMessage(CheckConflictResponse)

DictOne = _reflection.GeneratedProtocolMessageType('DictOne', (_message.Message,), {
  'DESCRIPTOR' : _DICTONE,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.DictOne)
  })
_sym_db.RegisterMessage(DictOne)

Conflict = _reflection.GeneratedProtocolMessageType('Conflict', (_message.Message,), {
  'DESCRIPTOR' : _CONFLICT,
  '__module__' : 'bareun.custom_dict_pb2'
  # @@protoc_insertion_point(class_scope:bareun.Conflict)
  })
_sym_db.RegisterMessage(Conflict)

_CUSTOMDICTIONARYSERVICE = DESCRIPTOR.services_by_name['CustomDictionaryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020ai.bareun.protosB\034CustomDictionaryServiceProtoP\001Z\026bareun.ai/proto/bareun'
  _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY._options = None
  _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY._serialized_options = b'8\001'
  _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY._options = None
  _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY._serialized_options = b'8\001'
  _CUSTOMDICTIONARYSERVICE.methods_by_name['GetCustomDictionaryList']._options = None
  _CUSTOMDICTIONARYSERVICE.methods_by_name['GetCustomDictionaryList']._serialized_options = b'\202\323\344\223\002\036\022\031/bareun/api/v1/customdict:\001*'
  _CUSTOMDICTIONARYSERVICE.methods_by_name['GetCustomDictionary']._options = None
  _CUSTOMDICTIONARYSERVICE.methods_by_name['GetCustomDictionary']._serialized_options = b'\202\323\344\223\002,\022\'/bareun/api/v1/customdict/{domain_name}:\001*'
  _CUSTOMDICTIONARYSERVICE.methods_by_name['UpdateCustomDictionary']._options = None
  _CUSTOMDICTIONARYSERVICE.methods_by_name['UpdateCustomDictionary']._serialized_options = b'\202\323\344\223\002,\"\'/bareun/api/v1/customdict/{domain_name}:\001*'
  _CUSTOMDICTIONARYSERVICE.methods_by_name['RemoveCustomDictionaries']._options = None
  _CUSTOMDICTIONARYSERVICE.methods_by_name['RemoveCustomDictionaries']._serialized_options = b'\202\323\344\223\002%\" /bareun/api/v1/customdict/delete:\001*'
  _CUSTOMDICTIONARYSERVICE.methods_by_name['CheckConflict']._options = None
  _CUSTOMDICTIONARYSERVICE.methods_by_name['CheckConflict']._serialized_options = b'\202\323\344\223\002-\"(/bareun/api/v1/customdict/check-conflict:\001*'
  _CUSTOMDICTIONARYMETA._serialized_start=122
  _CUSTOMDICTIONARYMETA._serialized_end=525
  _CUSTOMDICTIONARYMETA_DICTMETA._serialized_start=448
  _CUSTOMDICTIONARYMETA_DICTMETA._serialized_end=525
  _CUSTOMDICTIONARY._serialized_start=528
  _CUSTOMDICTIONARY._serialized_end=838
  _CUSTOMDICTIONARYMAP._serialized_start=841
  _CUSTOMDICTIONARYMAP._serialized_end=1015
  _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY._serialized_start=937
  _CUSTOMDICTIONARYMAP_CUSTOMDICTMAPENTRY._serialized_end=1015
  _GETCUSTOMDICTIONARYLISTRESPONSE._serialized_start=1017
  _GETCUSTOMDICTIONARYLISTRESPONSE._serialized_end=1102
  _GETCUSTOMDICTIONARYREQUEST._serialized_start=1104
  _GETCUSTOMDICTIONARYREQUEST._serialized_end=1153
  _GETCUSTOMDICTIONARYRESPONSE._serialized_start=1155
  _GETCUSTOMDICTIONARYRESPONSE._serialized_end=1245
  _UPDATECUSTOMDICTIONARYREQUEST._serialized_start=1247
  _UPDATECUSTOMDICTIONARYREQUEST._serialized_end=1339
  _UPDATECUSTOMDICTIONARYRESPONSE._serialized_start=1341
  _UPDATECUSTOMDICTIONARYRESPONSE._serialized_end=1402
  _REMOVECUSTOMDICTIONARIESREQUEST._serialized_start=1404
  _REMOVECUSTOMDICTIONARIESREQUEST._serialized_end=1472
  _REMOVECUSTOMDICTIONARIESRESPONSE._serialized_start=1475
  _REMOVECUSTOMDICTIONARIESRESPONSE._serialized_end=1664
  _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY._serialized_start=1607
  _REMOVECUSTOMDICTIONARIESRESPONSE_DELETEDDOMAINNAMESENTRY._serialized_end=1664
  _CHECKCONFLICTREQUEST._serialized_start=1666
  _CHECKCONFLICTREQUEST._serialized_end=1710
  _CHECKCONFLICTRESPONSE._serialized_start=1712
  _CHECKCONFLICTRESPONSE._serialized_end=1772
  _DICTONE._serialized_start=1774
  _DICTONE._serialized_end=1825
  _CONFLICT._serialized_start=1828
  _CONFLICT._serialized_end=2000
  _CUSTOMDICTIONARYSERVICE._serialized_start=2003
  _CUSTOMDICTIONARYSERVICE._serialized_end=2755
# @@protoc_insertion_point(module_scope)
