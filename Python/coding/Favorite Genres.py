'''
Favorite Genres

https://leetcode.com/discuss/interview-question/373006
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
Example 2:

Input:
userSongs = {  
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
},
songGenres = {}

Output: {  
   "David": [],
   "Emma":  []
}
'''
from collections import defaultdict
def FavoriteGenres(userSongs, songGenres):
    if songGenres == {}:
        return {}

    # reformat songGenres
    new_songG = {}
    for type, songs in songGenres.items():
        for s in songs:
            new_songG[s] = type
    
    userG = defaultdict(list)
    for user, songs in userSongs.items():
        Genres = defaultdict(int)
        for s in songs:
            Genres[new_songG[s]] += 1
        
        favorite = sorted(Genres.items(), key = lambda x:-x[1])

        for each_f in favorite:
            if each_f[1] == favorite[0][1]:
                userG[user].append(each_f[0])
            else:
                break
    return userG




userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}

songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}


'''userSongs = {  
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
}
songGenres = {}'''

print(FavoriteGenres(userSongs, songGenres))