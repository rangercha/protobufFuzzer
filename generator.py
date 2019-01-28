import struct;
import binascii;

class protobufField:
  type="string"
  value=""


fields=[]

fields.append(protobufField())
fields[0].type="packed repeated fields"
fields[0].value=["my_tag","foo:bar"]
fields.append(protobufField())
fields[1].type="string"
fields[1].value="gauge"
fields.append(protobufField())
fields[2].type="float"
fields[2].value=-12.5
fields.append(protobufField())
fields[3].type="string"
fields[3].value="sys.cpu"
fields.append(protobufField())
fields[4].type="int32"
fields[4].value=300



def fieldTypeValues(fieldType):
  if (fieldType in ["int32","int64","uint32","uint64","sint32","sint64","bool","enum"]):
    return 0
  if (fieldType in ["fixed64","sfixed64","double"]):
    return 1
  if (fieldType in ["string","bytes","embedded messages","packed repeated fields"]):
    return 2
#groups are deprecated
#  if (fieldType in ["groups"]):
#    return 3
#  if (fieldType in ["groups"]):
#    return 4
  if (fieldType in ["fixed32","sfixed32","float"]):
    return 5
  raise ValueError('invalid field type. crashing.')

protobufBytes=bytearray()

for singleField in fields:
  fieldKey=((fields.index(singleField)+1)<<3)+fieldTypeValues(singleField.type)
  
  if (singleField.type=="packed repeated fields"):
    for repeatedField in singleField.value:
      protobufBytes.append(fieldKey)
      protobufBytes.append(len(repeatedField))
      protobufBytes+=repeatedField
  if (singleField.type=="string"):
    protobufBytes.append(fieldKey)
    protobufBytes.append(len(singleField.value))
    protobufBytes+=singleField.value
  if (singleField.type=="float"):
    protobufBytes.append(fieldKey)
    protobufBytes+=struct.pack('<f',singleField.value)
  if (singleField.type=="int32"):
    protobufBytes.append(fieldKey)
    protobufBytes+=struct.pack('<f',singleField.value)

print(binascii.hexlify(protobufBytes))