n = int(input())

invited_guests = set()
present_guests = set()

for _ in range(n):
    invitation = input()
    invited_guests.add(invitation)

while True:
    guest = input()
    if guest == 'END':
        break

    if guest in invited_guests:
        present_guests.add(invited_guests.remove(guest))

print(len(invited_guests))
print('\n'.join(sorted(invited_guests)))
