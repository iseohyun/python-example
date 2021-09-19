'''
	피클(pickle)
'''

import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile2 = pickle.load(profile_file)
print(profile2)
profile_file.close()

# with
with open("profile.pickle", "rb") as profile_file:
	print(pickle.load(profile_file))