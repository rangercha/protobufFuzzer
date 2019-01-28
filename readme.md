Just some templates for fuzzing protobuf objects. I made this to find vulnerabilities in a raw protobuf network service (not over HTTP) and to help myself learn about protobuf. Most of the information about encoding came from https://developers.google.com/protocol-buffers/docs/encoding.

First, use protobuf to make sure we know what the actual object should look like. I was starting with a binary object that I captured over a network socket.
 
I'm using debian for these install instructions.

apt install protobuf-compiler python

Define a metricextra.proto file with a protobuf message in it.
Create a serializer function that populates the protobuf object and then serializes it.
Use xxd to check the binary.

protoc --python_out=. metricextra.proto && python metricextra_serializer.py && xxd out.bin


Now that you have something to compare this to, we need to build out an array of fields. We just should need data type and value for each field. Everything else should be handled based on this information.

Running python generator.py will create the same object that is in out.bin.

The advantage to doing this in python is now we can easily fuzz all the fields, including ones that make the protobuf object invalid.