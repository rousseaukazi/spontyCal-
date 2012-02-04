import sqlite3 as lite
import sys



import mechanize

from mechanize import ParseResponse, urlopen, urljoin

from BeautifulSoup import BeautifulSoup

from time import clock, time

def getEvents(subscription):
    cur.execute("SELECT * FROM Events")
    
    rows = cur.fetchall()
    
    shitReturned = []
    
    for row in rows:
        shitReturned.append(row)




#
#eventDay = 3
#urls = []
#
#while ( eventDay < 6 ):
#    if (eventDay < 10):
#        urls.append("http://events.berkeley.edu/?view=quick&timeframe=day&date=2012-02-0"+ str(eventDay) + "&tab=all_events")
#    else:
#        urls.append("http://events.berkeley.edu/?view=quick&timeframe=day&date=2012-02-"+ str(eventDay) + "&tab=all_events")
#    eventDay = eventDay + 1
#
#link = 0
#for u in urls:
#    print link
#    link = link + 1 
#    response = urlopen(u)
#    
#    soup = BeautifulSoup(response)
#    
#    items = soup.findAll("div", {'class' : 'event'} ) ##SOOOO IMPORTANT
#    
#    rr = soup.find("div", {'class' : 'exhibitsSubHead'})
#    breakName = rr.next.next.next.next.next.contents[1].contents[0].contents[0]
#    
#    
#    for i in items:
#        name = i.contents[1].contents[0].contents[0]
#        
#        metaData = i.contents[3].contents[0]
#        
#        category = ''
#        subcategory = ''
#        date = ''
#        time = ''
#        location = ''
#        try:
#            location2 = i.contents[3].contents[1].contents[0]
#        except IndexError:
#            location2 = ''
#        
#        breaks = 0
#        for m in metaData:
#            if ( breaks == 0 ):
#                if ( m == '\n' or m == '\t' ):
#                    continue
#                if ( m == '-'):
#                    breaks = breaks + 1
#                    continue
#                if ( m == '|'):
#                    breaks = breaks + 2
#                    continue
#                else:
#                    category = category + m
#            
#            if (breaks == 1):
#                if ( m == '\n' or m == '\t' ):
#                    continue
#                if (  m == '|'):
#                    breaks = breaks + 1
#                    continue
#                else:
#                    subcategory = subcategory + m
#            
#            if ( breaks == 2 ):
#                if ( m == '\n' or m == '\t' ):
#                    continue
#                if ( m == '|'):
#                    breaks = breaks + 1
#                    continue
#                else:
#                    date = date + m
#            
#            if ( breaks == 3 ):
#                if ( m == '\n' or m == '\t' ):
#                    continue
#                if ( m == '|' ):
#                    breaks = breaks + 1
#                    continue
#                else:
#                    time = time + m
#            
#            if ( breaks == 4 ):
#                if ( m == '\n' or m == '\t' or m == '' ):
#                    continue
#                if ( m == '|'):
#                    breaks = breaks + 1
#                    continue
#                else:
#                    location = location + m
#        
#        
#        
#        if ( location == '' ):
#            location = ''
#        if ( subcategory == ''):
#            subcategory = 'No Sub-Category Provided'
#        if ( date == '' ):
#            date = 'Nope'
#        if (time == ' '):
#            time = 'No Time Provided'
#        
#        if (location2 != ''):
#            if ( (location2[0] == 'e' and location2[1] == 'v' and location2[2] == 'e') or (location2[0] == 't' and location2[1] == 'h' and location2[2] == 'e')):
#                date = date + ' | ' + location2
#                location2 = 'Changed'
#        
#        
#        if ( location2 == 'Changed'):
#            if (time == 'Nope'):
#                time = ''
#            
#            leTime = i.contents[3].contents[2]
#            for letter in leTime:
#                if (letter == '\n' or letter == '\t' or letter == '|' or letter == ''):
#                    continue
#                else:
#                    time = time + letter
#        
#        
#        if (time.isspace()):
#            time = 'Nope'
#        
#        if ( location2 == 'Changed'):
#            try:
#                location2 = i.contents[3].contents[3].contents[0]
#            except IndexError:
#                continue
#        
#        try:
#            extraLoc = i.contents[3].contents[2] ##extra location info!
#            temp = ''
#            for e in extraLoc:
#                if ( e == ',' ):
#                    continue
#                if (e == '|'):
#                    temp = ''
#                    continue
#                else:
#                    temp = temp + e
#        except IndexError:
#            temp = ''
#        
#        if ( name == breakName ):
#            break
#        
#        location = location  + '' + location2 + temp
#        
#        print ''       
#        print "Name: ", name
#        print "Category: ", category
#        print "Sub-Category: ", subcategory
#        print "Date: ", date
#        print "Time: ", time
#        print "Location: ", location
#        
#        eventId = hash(name)
#
#
#        response = urlopen("http://www.getlatlon.com")
#        forms = ParseResponse(response, backwards_compat=False)
#        form = forms[0]
#
#        form["q"] = location", Berkeley"
#
#        print form
#
#        request = form.click()
#        response = mechanize.urlopen(request)
#
#        read = response.read()
#
#        i = 0
#
#        latLong = ""
#
#        while ( i < len(read)):
#            if ((read[i] == 's') and (read[i+1] == 'l') and (read[i+2] == 'l') and (read[i+3] == '=')):
#                j = i + 4
#                k = 0
#                l = ''
#                while ( k < 21 ):
#                    l = l + read[j]
#                    j = j + 1
#                    k = k + 1
#                latLong = latLong + l
#                break
#            else:
#                i = i + 1
#        
#        lat = ""
#
#        long = ""
#
#        writeTo = "Lat"
#
#        for character in latLong:
#            if character == ",":
#                writeTo = "Long"
#            elif writeTo == "Lat":
#                lat = lat + character
#            else:
#                long = long +character
#
#        
#        if lat == "37.8715926" and long == "-122.272747":
#            lat = 0
#            long = 0
#        
        
con = lite.connect('calSpontyDB.db')

with con:
    
    cur = con.cursor()  
#    cur.execute("CREATE TABLE Events(eventId INT, name TEXT, lat TEXT, long TEXT, distance TEXT, picture TEXT, description TEXT, time TEXT, location TEXT)")

    cur.execute("INSERT INTO Events VALUES("eventId","name","lat","long","distance","picture","description","time","location)")
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
#    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
#    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
#    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
#    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
#    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
#    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
