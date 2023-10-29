class Spotify:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def insubscribe(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class ClientInterface:
    def update(self, message):
        pass

class SpotifyNotifier(Spotify):
    def notify(self, state):
        self._state = state
        self.notify_observers(f"{state}")

class Client(ClientInterface):
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received a message: {message}")

def main():
    spotify = SpotifyNotifier()
    client1 = Client('Yedige')
    client2 = Client('Maksat')

    spotify.subscribe(client1)
    spotify.subscribe(client2)

    spotify.notify('Scally Milano dropped new Album')


if __name__ == '__main__':
    main()