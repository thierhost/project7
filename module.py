import requests
import re
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class parsing():
    """parsing the sentence from user to be able to query googlemap and wiki
    """

    with open(os.path.join(BASE_DIR, 'static\localisation.txt'), 'r') as file:
        texte = file.read()
        LOCALISATION = texte.split(',')

    with open(os.path.join(BASE_DIR, 'static\stopwords.txt'), 'r') as file:
        texte = file.read()
        STOPWORDS = texte.split(',')

    def __init__(self, sentence):
        """ user's entry
        placetosearch=> check for specific words (rue, avenue) or capital case.
        """
        self.sentence_in_list = sentence.split()
        #remove stop words
        self.new_sentence = [word for word in self.sentence_in_list if word not in self.STOPWORDS]
        i = 0
        self.placeToSearch = []
        while i < len(self.new_sentence):
            if self.new_sentence[i] in self.LOCALISATION:
                if self.new_sentence[(i - 1)].isdigit():
                    self.placeToSearch = self.new_sentence[(i-1):]
                    break
                else:
                    self.placeToSearch = self.new_sentence[i:]
                    break
            elif self.new_sentence[i][0].isupper():
                self.placeToSearch.append(self.new_sentence[i])
            else:
                pass

            i+=1


    def google(self):
        """building request to query GoogleMap
        using pre-define url + placeToSearch + key
        """
        prefix ='https://maps.googleapis.com/maps/api/staticmap?center='
        middle = '&zoom=14&size=400x400&markers='
        suffix = '&key=AIzaSyD5nqmDGFH1SUZxJAYVtFHP7RNjjFE9CHg'
        marker = '+'.join(self.placeToSearch) # marker in google format, no space but + separator
        request = prefix + marker+middle+marker+suffix

        return request



    def wiki(self):
        """building request to query wikipedia
        using pre-define url + placeToSearch
        """
        prefix = 'https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch='
        suffix = '&formatversion=2&prop=revisions&rvprop=content&format=json&formatversion=2'
        marker = '%20'.join(self.placeToSearch)  # marker in wiki format, no space but %20 separator
        request = prefix + marker + suffix

        return request


class wikipedia:
    """parsing the wikipedia JSON we get using url from
    class Parsing (fct wiki)
    """

    def __init__(self, request):
        """ will get pageid to request a specific page.
        fyi=> return_json_API["query"]["search"][0]["snippet"]) is not reliable
        """
        request = requests.get(request)# to get json from wikipedia
        return_json_API = request.json()  # get json file from the request

        #get the wiki pageid for
        try:
            self.Pageid = return_json_API["query"]["search"][0]["pageid"]
        except:
            self.Pageid = 'nada'



        #regular expression to remove HTML tags we get back from wiki
        #not used snippet as it shows sentences truncated. wikiword below better
        #try:
         #    self.wiki_word = re.sub('<[^>]+>','',return_json_API["query"]["search"][0]["snippet"])
        #except:
         #   self.wiki_word = "Rien trouve sur Wikipedia, je veux dire ca ne me dit rien du tout :-( "


    def wikiword(self):
        """ getting wiki content by querying the page id from __init__
        """
        prefix = "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&format=json&pageids="
        requestpageid = prefix + str(self.Pageid)

        request = requests.get(requestpageid)# to get json from wikipedia
        return_json_API = request.json()  # get json file from the request

        try:
            # regular expression to remove HTML + linebreaks tags we get back from wiki
            wiki_content = re.sub('<[^>]+>|\n','',return_json_API["query"]["pages"][str(self.Pageid)]["extract"])
        except:
            wiki_content = 'Je n\'ai rien trouve sur Wikipedia, enfin je veux dire ce ne me dit rien du tout :-(' \
                     'Au fait n\'oublie pas de mettre des majuscules aux noms propres !'

        return wiki_content








