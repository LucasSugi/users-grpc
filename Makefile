compile-proto:
	python3 -m grpc_tools.protoc -I./protos --python_out=./app --grpc_python_out=./app ./protos/users.proto
