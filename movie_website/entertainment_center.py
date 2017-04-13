import media
import fresh_tomatoes

''' analog server data '''
server_datas = [
    ["Thor: Ragnarok Teaser Trailer ",
"https://i.ytimg.com/vi/v7MGUNV8MxU/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=Sg1obGFZumz5EBQUgVBRFDoCixU",
"https://www.youtube.com/watch?v=v7MGUNV8MxU"],
    ["How Logan Should Have Ended",
"https://i.ytimg.com/vi/yIl_FiV8V6E/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=QvBjGqRLZsJR2bEHXs1rTeL8mvY",
"https://www.youtube.com/watch?v=yIl_FiV8V6E"],
    ["DETROIT | Official Trailer",
"https://i.ytimg.com/vi/HFeWsDpy9y0/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=3cPJY4esF0pRXiGM_TYEY1a6bCY",
"https://www.youtube.com/watch?v=HFeWsDpy9y0"],
    ["SPIKY Sea Creatures!",
"https://i.ytimg.com/vi/f-IYeIDr8V4/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=4_xlycftOQ7FJYz1hMr4M43dhIY",
"https://www.youtube.com/watch?v=f-IYeIDr8V4"],
    ["WONDER WOMAN Final Trailer",
"https://i.ytimg.com/vi/lOOnCFzY4us/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=Vn3FYF7_OLa_ZzahpL2EkobVwWY",
"https://www.youtube.com/watch?v=lOOnCFzY4us"],
    ["Samurai Champloo - Lofi HipHop Mix • Nujabes inspired",
"https://i.ytimg.com/vi/kq7cQNO0gYc/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=67&sigh=hygtAvEgWaNKQGXKjv5KjEIS0Lo",
"https://www.youtube.com/watch?v=kq7cQNO0gYc"]
    ]

''' create movie from server data , insert to movies list '''   
movies = []
for data in server_datas:
    movie_title = data[0]
    poster_image = data[1]
    trailer_yutube = data[2]
    movie = media.Movie(movie_title,poster_image,trailer_yutube)
    movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
