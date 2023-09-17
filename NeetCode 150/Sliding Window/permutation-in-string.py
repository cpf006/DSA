# For this problem you want to track 
# frequescies of characters within the window in a hash map

# you want to increment the window one to the right every
# time you iterate more than the window size

# When you find all frequencies of a character,
# you will know you have a full match on that particular character

# i.e frequency_of_character[full_string[i]] == 0

# for every time you find a character decrease the frequency by one,
#     This number may go negative when you have too many of the same character within the window, that makes sense

# when incrementing the window 
# you want to check if the window start was within the char freq
# if it was and removing it from the window (adding one to its frequency in the hashmap) causes you to lose a necessary character (the freq becomes greater than 0 when adding it back in) then you should reduce the matches by 1




