"""
Copyright 2018-2019 Telenav (http://telenav.com)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orbb_metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import orbb_definitions_pb2 as orbb__definitions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orbb_metadata.proto',
  package='orbb',
  syntax='proto2',
  serialized_pb=_b('\n\x13orbb_metadata.proto\x12\x04orbb\x1a\x16orbb_definitions.proto\".\n\x07GPSPair\x12\x10\n\x08latitude\x18\x01 \x02(\x02\x12\x11\n\tlongitude\x18\x02 \x02(\x02\"r\n\x0cLocalization\x12\x10\n\x08\x64istance\x18\x01 \x02(\x02\x12\x14\n\x0c\x61ngle_of_roi\x18\x02 \x02(\x02\x12\x19\n\x11\x61ngle_from_center\x18\x03 \x02(\x02\x12\x1f\n\x08position\x18\x04 \x02(\x0b\x32\r.orbb.GPSPair\"=\n\x0eVanishingPoint\x12\x17\n\x02vp\x18\x01 \x02(\x0b\x32\x0b.orbb.Point\x12\x12\n\nconfidence\x18\x02 \x02(\x02\"\xde\x04\n\x03Roi\x12\x18\n\x04type\x18\x01 \x02(\x0e\x32\n.orbb.Mark\x12\x18\n\x04rect\x18\x02 \x02(\x0b\x32\n.orbb.Rect\x12\x0e\n\x06manual\x18\x03 \x02(\x08\x12\x11\n\talgorithm\x18\x04 \x01(\t\x12\'\n\ndetections\x18\x05 \x03(\x0b\x32\x13.orbb.Roi.Detection\x12!\n\x05local\x18\x06 \x01(\x0b\x32\x12.orbb.Localization\x12+\n\ncomponents\x18\x07 \x03(\x0b\x32\x17.orbb.Roi.SignComponent\x12\r\n\x05\x64ummy\x18\x08 \x01(\x08\x12\x30\n\x11image_sensor_data\x18\t \x01(\x0b\x32\x15.orbb.ImageSensorData\x12(\n\nvalidation\x18\n \x01(\x0e\x32\x14.orbb.Roi.Validation\x12\x1e\n\x07polygon\x18\x0b \x01(\x0b\x32\r.orbb.Polygon\x1a\x39\n\tDetection\x12\x18\n\x04type\x18\x01 \x02(\x0e\x32\n.orbb.Mark\x12\x12\n\nconfidence\x18\x02 \x02(\x01\x1aX\n\rSignComponent\x12\x1f\n\x04type\x18\x01 \x02(\x0e\x32\x11.orbb.SignElement\x12\x17\n\x03\x62ox\x18\x02 \x02(\x0b\x32\n.orbb.Rect\x12\r\n\x05value\x18\x03 \x01(\t\"g\n\nValidation\x12\x11\n\rTRUE_POSITIVE\x10\x00\x12\x11\n\rTRUE_NEGATIVE\x10\x01\x12\x12\n\x0e\x46\x41LSE_NEGATIVE\x10\x02\x12\x12\n\x0e\x46\x41LSE_POSITIVE\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04\"\'\n\x06ImgRes\x12\r\n\x05width\x18\x01 \x02(\x02\x12\x0e\n\x06height\x18\x02 \x02(\x02\"\xca\x01\n\x0fImageSensorData\x12#\n\x0craw_position\x18\x01 \x02(\x0b\x32\r.orbb.GPSPair\x12\'\n\x10matched_position\x18\x02 \x01(\x0b\x32\r.orbb.GPSPair\x12\x0f\n\x07\x63ompass\x18\x03 \x01(\x02\x12\x0f\n\x07heading\x18\x04 \x02(\x02\x12\x0b\n\x03yaw\x18\x05 \x01(\x02\x12\r\n\x05pitch\x18\x06 \x01(\x02\x12\x0c\n\x04roll\x18\x07 \x01(\x02\x12\x1d\n\x07img_res\x18\x08 \x02(\x0b\x32\x0c.orbb.ImgRes\"a\n\tImageRois\x12\x0c\n\x04\x66ile\x18\x01 \x02(\t\x12\x17\n\x04rois\x18\x02 \x03(\x0b\x32\t.orbb.Roi\x12-\n\x0fvanishing_point\x18\x03 \x01(\x0b\x32\x14.orbb.VanishingPoint\"?\n\x08Metadata\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12#\n\nimage_rois\x18\x02 \x03(\x0b\x32\x0f.orbb.ImageRois')
  ,
  dependencies=[orbb__definitions__pb2.DESCRIPTOR,])



_ROI_VALIDATION = _descriptor.EnumDescriptor(
  name='Validation',
  full_name='orbb.Roi.Validation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRUE_POSITIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUE_NEGATIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALSE_NEGATIVE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALSE_POSITIVE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=784,
  serialized_end=887,
)
_sym_db.RegisterEnumDescriptor(_ROI_VALIDATION)


_GPSPAIR = _descriptor.Descriptor(
  name='GPSPair',
  full_name='orbb.GPSPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='orbb.GPSPair.latitude', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='orbb.GPSPair.longitude', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=99,
)


_LOCALIZATION = _descriptor.Descriptor(
  name='Localization',
  full_name='orbb.Localization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance', full_name='orbb.Localization.distance', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_of_roi', full_name='orbb.Localization.angle_of_roi', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_from_center', full_name='orbb.Localization.angle_from_center', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='orbb.Localization.position', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=215,
)


_VANISHINGPOINT = _descriptor.Descriptor(
  name='VanishingPoint',
  full_name='orbb.VanishingPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vp', full_name='orbb.VanishingPoint.vp', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='orbb.VanishingPoint.confidence', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=278,
)


_ROI_DETECTION = _descriptor.Descriptor(
  name='Detection',
  full_name='orbb.Roi.Detection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='orbb.Roi.Detection.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='orbb.Roi.Detection.confidence', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=692,
)

_ROI_SIGNCOMPONENT = _descriptor.Descriptor(
  name='SignComponent',
  full_name='orbb.Roi.SignComponent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='orbb.Roi.SignComponent.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box', full_name='orbb.Roi.SignComponent.box', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='orbb.Roi.SignComponent.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=694,
  serialized_end=782,
)

_ROI = _descriptor.Descriptor(
  name='Roi',
  full_name='orbb.Roi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='orbb.Roi.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rect', full_name='orbb.Roi.rect', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manual', full_name='orbb.Roi.manual', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='orbb.Roi.algorithm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detections', full_name='orbb.Roi.detections', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local', full_name='orbb.Roi.local', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='components', full_name='orbb.Roi.components', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dummy', full_name='orbb.Roi.dummy', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_sensor_data', full_name='orbb.Roi.image_sensor_data', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation', full_name='orbb.Roi.validation', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='polygon', full_name='orbb.Roi.polygon', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROI_DETECTION, _ROI_SIGNCOMPONENT, ],
  enum_types=[
    _ROI_VALIDATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=887,
)


_IMGRES = _descriptor.Descriptor(
  name='ImgRes',
  full_name='orbb.ImgRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='orbb.ImgRes.width', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='orbb.ImgRes.height', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=889,
  serialized_end=928,
)


_IMAGESENSORDATA = _descriptor.Descriptor(
  name='ImageSensorData',
  full_name='orbb.ImageSensorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_position', full_name='orbb.ImageSensorData.raw_position', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matched_position', full_name='orbb.ImageSensorData.matched_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compass', full_name='orbb.ImageSensorData.compass', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='orbb.ImageSensorData.heading', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='orbb.ImageSensorData.yaw', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='orbb.ImageSensorData.pitch', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roll', full_name='orbb.ImageSensorData.roll', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='img_res', full_name='orbb.ImageSensorData.img_res', index=7,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=931,
  serialized_end=1133,
)


_IMAGEROIS = _descriptor.Descriptor(
  name='ImageRois',
  full_name='orbb.ImageRois',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='orbb.ImageRois.file', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rois', full_name='orbb.ImageRois.rois', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vanishing_point', full_name='orbb.ImageRois.vanishing_point', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1135,
  serialized_end=1232,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='orbb.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='orbb.Metadata.stream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_rois', full_name='orbb.Metadata.image_rois', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1234,
  serialized_end=1297,
)

_LOCALIZATION.fields_by_name['position'].message_type = _GPSPAIR
_VANISHINGPOINT.fields_by_name['vp'].message_type = orbb__definitions__pb2._POINT
_ROI_DETECTION.fields_by_name['type'].enum_type = orbb__definitions__pb2._MARK
_ROI_DETECTION.containing_type = _ROI
_ROI_SIGNCOMPONENT.fields_by_name['type'].enum_type = orbb__definitions__pb2._SIGNELEMENT
_ROI_SIGNCOMPONENT.fields_by_name['box'].message_type = orbb__definitions__pb2._RECT
_ROI_SIGNCOMPONENT.containing_type = _ROI
_ROI.fields_by_name['type'].enum_type = orbb__definitions__pb2._MARK
_ROI.fields_by_name['rect'].message_type = orbb__definitions__pb2._RECT
_ROI.fields_by_name['detections'].message_type = _ROI_DETECTION
_ROI.fields_by_name['local'].message_type = _LOCALIZATION
_ROI.fields_by_name['components'].message_type = _ROI_SIGNCOMPONENT
_ROI.fields_by_name['image_sensor_data'].message_type = _IMAGESENSORDATA
_ROI.fields_by_name['validation'].enum_type = _ROI_VALIDATION
_ROI.fields_by_name['polygon'].message_type = orbb__definitions__pb2._POLYGON
_ROI_VALIDATION.containing_type = _ROI
_IMAGESENSORDATA.fields_by_name['raw_position'].message_type = _GPSPAIR
_IMAGESENSORDATA.fields_by_name['matched_position'].message_type = _GPSPAIR
_IMAGESENSORDATA.fields_by_name['img_res'].message_type = _IMGRES
_IMAGEROIS.fields_by_name['rois'].message_type = _ROI
_IMAGEROIS.fields_by_name['vanishing_point'].message_type = _VANISHINGPOINT
_METADATA.fields_by_name['image_rois'].message_type = _IMAGEROIS
DESCRIPTOR.message_types_by_name['GPSPair'] = _GPSPAIR
DESCRIPTOR.message_types_by_name['Localization'] = _LOCALIZATION
DESCRIPTOR.message_types_by_name['VanishingPoint'] = _VANISHINGPOINT
DESCRIPTOR.message_types_by_name['Roi'] = _ROI
DESCRIPTOR.message_types_by_name['ImgRes'] = _IMGRES
DESCRIPTOR.message_types_by_name['ImageSensorData'] = _IMAGESENSORDATA
DESCRIPTOR.message_types_by_name['ImageRois'] = _IMAGEROIS
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GPSPair = _reflection.GeneratedProtocolMessageType('GPSPair', (_message.Message,), dict(
  DESCRIPTOR = _GPSPAIR,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.GPSPair)
  ))
_sym_db.RegisterMessage(GPSPair)

Localization = _reflection.GeneratedProtocolMessageType('Localization', (_message.Message,), dict(
  DESCRIPTOR = _LOCALIZATION,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.Localization)
  ))
_sym_db.RegisterMessage(Localization)

VanishingPoint = _reflection.GeneratedProtocolMessageType('VanishingPoint', (_message.Message,), dict(
  DESCRIPTOR = _VANISHINGPOINT,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.VanishingPoint)
  ))
_sym_db.RegisterMessage(VanishingPoint)

Roi = _reflection.GeneratedProtocolMessageType('Roi', (_message.Message,), dict(

  Detection = _reflection.GeneratedProtocolMessageType('Detection', (_message.Message,), dict(
    DESCRIPTOR = _ROI_DETECTION,
    __module__ = 'orbb_metadata_pb2'
    # @@protoc_insertion_point(class_scope:orbb.Roi.Detection)
    ))
  ,

  SignComponent = _reflection.GeneratedProtocolMessageType('SignComponent', (_message.Message,), dict(
    DESCRIPTOR = _ROI_SIGNCOMPONENT,
    __module__ = 'orbb_metadata_pb2'
    # @@protoc_insertion_point(class_scope:orbb.Roi.SignComponent)
    ))
  ,
  DESCRIPTOR = _ROI,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.Roi)
  ))
_sym_db.RegisterMessage(Roi)
_sym_db.RegisterMessage(Roi.Detection)
_sym_db.RegisterMessage(Roi.SignComponent)

ImgRes = _reflection.GeneratedProtocolMessageType('ImgRes', (_message.Message,), dict(
  DESCRIPTOR = _IMGRES,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.ImgRes)
  ))
_sym_db.RegisterMessage(ImgRes)

ImageSensorData = _reflection.GeneratedProtocolMessageType('ImageSensorData', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESENSORDATA,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.ImageSensorData)
  ))
_sym_db.RegisterMessage(ImageSensorData)

ImageRois = _reflection.GeneratedProtocolMessageType('ImageRois', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEROIS,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.ImageRois)
  ))
_sym_db.RegisterMessage(ImageRois)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'orbb_metadata_pb2'
  # @@protoc_insertion_point(class_scope:orbb.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)


# @@protoc_insertion_point(module_scope)