class Model:
    #model untuk menampung response data dari webhook
    def __init__(self, room_id, message, message_type, sender):
        self.room_id = room_id
        self.message = message
        self.message_type = message_type
        self.sender = sender