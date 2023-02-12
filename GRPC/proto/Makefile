start:
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. Article.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ClientToRegistryServer.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ServerToRegistryServer.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ClientToServer.proto