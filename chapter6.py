# Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# accessing a value
alien_0 = {'color': 'green', 'points': 5}
new_point = alien_0['points']
print(f"you have earned {new_point}")

# adding new key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_positions'] = 25
print(alien_0)

# modifying values
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)


alien_0 = {'x_position': 0, 'y_positions': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])

# removing key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# more dictionraries
favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
print(f"joe's favourite language is {favorite_languages['joe'].title()}")

# using get()
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'no points assigned'))

# ex 6-1
