### 피클(pickle) ###


import pickle
filename = "7_Module/profile.pickle"

profile_file = open(filename, "wb")
profile = {"이름": "이방원", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()

profile_file = open(filename, "rb")
profile2 = pickle.load(profile_file)
print(profile2)
profile_file.close()

# with
with open(filename, "rb") as profile_file:
    print(pickle.load(profile_file))
