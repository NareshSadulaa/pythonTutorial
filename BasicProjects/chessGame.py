from chessdotcom import get_club_details
def club():
    data = get_club_details()
    print(data.json())
club()