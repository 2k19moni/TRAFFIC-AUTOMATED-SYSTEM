import random

vehicle_number_plate = ['TN 1220', 'TN 4210', 'KN 6321', 'PY 5230', 'KA 5210']
vehicle_registered_type = ['Private', 'Government', 'Private', 'Private', 'Government']
vehicle_owner_phone_number = ['9639652363', '9685245169', '9414526853', '9456286359', '9635242156']

vehicle_in_traffic = random.choice(vehicle_number_plate)
print(vehicle_in_traffic)

vehicle_number_list_index = vehicle_number_plate.index(vehicle_in_traffic)

#print(vehicle_number_list_index)


if vehicle_registered_type[vehicle_number_list_index] == 'Government':
    print('Government Vehicle, Permitted to travel!')

else:
    facial_reg = ['Normal', 'Abnormal']

    vehicle_face_reg = random.choice(facial_reg)
    print('Travel Situation = ', vehicle_face_reg)

    if vehicle_face_reg == 'Abnormal':
        print('People in that vehicle looks like in emergency. Permitted to travel!')
        print('Nearest hospital location sent to', vehicle_owner_phone_number[vehicle_number_list_index])

    else:
        print('Fine Message Sent to', vehicle_owner_phone_number[vehicle_number_list_index])
