import webbrowser
import requests
from catapult.api import Plugin
from catapult.api import SearchResult
from catapult.api import PreferencesItem

class WebSearch(Plugin):

    title = "webSearch"

    def launch(self, window, id):
        self.debug(f"opening {id!r} in the browser")
        webbrowser.open(id, autoraise=True)

    def search(self, query):
        query = query.strip()
        if "." in query:
            yield SearchResult(
                description=f"open {query.split()[1]}",
                fuzzy=False,
                icon="internet-web-browser-symbolic",
                id=query.split()[1], #open just the url in the browser
                offset=1,
                plugin=self,
                score=1,
                title=query.split()[1]
            )
            return
        elif len(query.split()) > 1:
            startTerm, result = query.split(maxsplit=1)
            if startTerm == "web":
                url = f"https://duckduckgo.com/ac/?q={result}"
                response = requests.get(url) #make request, returning a json
                suggestions = response.json()
                yield SearchResult( #first result should only be query
                    description="search on DuckDuckGo",
                    fuzzy=False,
                    icon="internet-web-browser-symbolic",
                    id=url.replace("ac/", ""),
                    offset=1,
                    plugin=self,
                    score=1,
                    title=f"open '{result}'"
                )
                for i in range(len(suggestions)): #list all results from suggestions
                    yield SearchResult(
                        description="search on DuckDuckGo",
                        fuzzy=False,
                        icon="internet-web-browser-symbolic",
                        id=f"https://duckduckgo.com/?q={suggestions[i]['phrase']}",
                        offset=2,
                        plugin=self,
                        score=1,
                        title=f"open '{suggestions[i]['phrase']}'"
                    )
