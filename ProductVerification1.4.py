import random

def list_of_songs(songslist):
    
    songstoplay = songslist[:] #oie

    while songstoplay != []:
        choosed_song = random.randrange(len(songstoplay)) #Randomly choosing some song from the list
        print("Playing:", songstoplay[choosed_song])
        songstoplay.pop(choosed_song) #Deleting the song from the songstoplay list
        
