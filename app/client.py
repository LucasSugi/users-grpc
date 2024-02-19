import grpc
import users_pb2 as user_messages
import users_pb2_grpc as user_service

if __name__== "__main__":
    with grpc.insecure_channel('localhost:50051') as channel:
        user_stup = user_service.UsersStub(channel)
        response = user_stup.GetUser(user_messages.UserRequest(id=1))
        print(response)

    with grpc.insecure_channel('localhost:50051') as channel:
        user_stup = user_service.UsersStub(channel)
        ids = [i for i in range(1, 4)]
        response = user_stup.GetUsers(user_messages.UsersRequest(id=ids))
        for user in response.user:
            print(user)

    with grpc.insecure_channel('localhost:50051') as channel:
        user_stup = user_service.UsersStub(channel)
        response = user_stup.GetUsersAll(user_messages.UsersRequestStream())
        for user in response:
            print(user)
