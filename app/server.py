from concurrent import futures

import grpc
import users_pb2 as user_messages
import users_pb2_grpc as user_service

FAKE_DB = {i: f"Name {i}" for i in range(1, 5)}

class UsersServicer(user_service.UsersServicer):

    def GetUser(self, request, context):
        fake_db_response = FAKE_DB.get(request.id, None)
        user_response = user_messages.UserResponse()

        if fake_db_response is None:
            user_response.user.id = 0
            user_response.user.name = "Invalid user id"
        else:
            user_response.user.id = request.id
            user_response.user.name = fake_db_response

        return user_response

    def GetUsers(self, request, context):
        users_response = user_messages.UsersResponse()
        for _id in request.id:
            user = users_response.user.add()
            user.id = _id
            user.name = FAKE_DB.get(_id, "Invalid user id")
        return users_response

    def GetUsersAll(self, request, context):
        for key, value in FAKE_DB.items():
            user = user_messages.User(id=key, name=value)
            yield user_messages.UsersResponseStream(user=user)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    user_service.add_UsersServicer_to_server(UsersServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC starting")
    server.start()
    server.wait_for_termination()

if __name__== "__main__":
    server()
