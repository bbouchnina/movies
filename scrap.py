from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import pymysql.cursors
from functions import connect_to_db 

url = 'http://www.allocine.fr/film/fichefilm_gen_cfilm='
error = ''
connection = connect_to_db()
hasdate = True
for x in range(8126,9100):
    link = url + str(x)+'.html'
    #try to open link
    try :
        html = urlopen(link).read()
    except:
        error = 'page not found'
    
    if error != '' :
        print(error)
        error = ''
    else : 
        soup = BeautifulSoup(html.decode('utf-8', 'ignore'), 'html.parser')
        movieTitle = soup.select(".titlebar-title-lg")[0].string
        movieCover = soup.select("figure")[0].img['src']
        movieCover = movieCover.replace('c_215_290/','')
        xname = movieCover.split("/")
        if xname[-1] != "empty.png":
            urllib.request.urlretrieve(movieCover, 'covers/'+str(x)+'.jpg')
            picture = str(x)
        else :
            picture = "empty"
        
        moviedurree = soup.select("div.meta-body-item")[0].contents[-1].string.strip()        
        try :
            movieDesc = soup.select("div.content-txt")[0].get_text().strip()
        except :
            movieDesc = "Unknown"

        movieDate = "Unknown"
        nationalite = ""
        movieDirector = ""
        movieActeurs = ""
        movieGenres = ""
        data = soup.select("div.meta-body-item")
        for i,d in enumerate(data):
            #print(d.span.string.strip())
            try :                
                if(d.span.string.strip() == "De"):
                    for j in d :
                        try :
                            if j.get_text().strip() != "De" : 
                                movieDirector = j.get_text().strip()
                                #print(j.get_text().strip())
                        except :
                            pass
                elif(d.span.string.strip() == "Avec"):
                    for j in d :
                        try :
                            if j.get_text().strip() != "Avec" and j.get_text().strip() != "plus":
                                movieActeurs += ", " + j.get_text().strip()
                        except :
                            pass                        
                elif(d.span.string.strip() == "Date de sortie"):
                    for j in d :
                        try :
                            if j.get_text().strip() != "Date de sortie" :
                                if "en" not in j.get_text().strip() :
                                    movieDate = j.get_text().strip()
                        except :
                            pass
                elif(d.span.string.strip() == "Genre"):
                    for j in d :
                        try :
                            if j.get_text().strip() != "Genre" :
                                movieGenres = j.get_text().strip()
                        except :
                            pass
                elif(d.span.string.strip() == "Genres"):
                    for j in d :
                        try :
                            if j.get_text().strip() != "Genres" :
                                movieGenres += ", " + j.get_text().strip()
                        except :
                            pass
                if(d.span.string.strip() == "Nationalité"):
                    for j in d :
                        try :
                            if j.get_text().strip() != "De" : 
                                nationalite = j.get_text().strip()
                                #print(j.get_text().strip())
                        except :
                            pass
        
            except :
                pass
        sql = "INSERT INTO movie values(NULL ,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        with connection.cursor() as cursor :
            get_sql = "SELECT * FROM movie WHERE ac_id = %s"
            cursor.execute(get_sql, (str(x)))
            result = cursor.fetchone()
            if not result :
                cursor.execute(sql,(str(x),movieTitle,picture,movieDate,moviedurree,nationalite,movieActeurs,movieGenres,movieDesc))
                print(x)
    # print(x)
    # print("Titre : " + movieTitle)
    # print("Date de Sortie : " +movieDate)
    # print("Duree : " + moviedurree)
    # print("Directeur : " + movieDirector)
    # print("Acteurs :" + movieActeurs)
    # # for acteur in movieActeurs :
    # #     print(acteur)
    # print("Genres :" + movieGenres)
    # # for genre in movieGenres :
    # #     print(genre)
    # print("Description : " + movieDesc)
quit()