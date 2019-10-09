def itsMovieTime(d):
  movie_duration=[90, 85, 75, 60, 120, 150, 125]
  for i,x in enumerate(movie_duration):
    for z,y in enumerate(movie_duration):
      # print(x+y)
      if ((x+y)>=d):
        print( x,y,i,z   )    
print(itsMovieTime(250))
