import webbrowser
import requests
import threading
import queue
from catapult.api import Plugin
from catapult.api import SearchResult

class WebSearch(Plugin):

    title = "webSearch"

    def launch(self, window, id):
        self.debug(f"opening {id!r} in the browser")
        webbrowser.open(id, autoraise=True)

    def search(self, query):
        query = query.strip()
        if "." in query and len(query.split()) == 1:
            if "https://" not in query:
                query = "https://" + query
            yield SearchResult(
                description=f"open {query}",
                fuzzy=False,
                icon="internet-web-browser-symbolic",
                id=query,
                offset=1,
                plugin=self,
                score=1,
                title=query
            )
            return
        elif len(query.split()) > 1:
            startTerm, result = query.split(maxsplit=1)
            if startTerm == "web":
                url = f"https://duckduckgo.com/ac/?q={result}"
                suggestions_queue = queue.Queue()

                def fetch_suggestions():
                    try:
                        response = requests.get(url)  # Make request in a separate thread
                        response.raise_for_status()
                        suggestions_queue.put(response.json())  # Put result in queue
                    except requests.RequestException as e:
                        suggestions_queue.put([])  # Return empty list on error

                # Start fetching in a separate thread
                thread = threading.Thread(target=fetch_suggestions, daemon=True)
                thread.start()

                # Yield the initial search option
                yield SearchResult(
                    description="search on DuckDuckGo",
                    fuzzy=False,
                    icon="internet-web-browser-symbolic",
                    id=url.replace("ac/", ""),
                    offset=1,
                    plugin=self,
                    score=2,
                    title=f"open '{result}'"
                )

                # Wait for results to be available in the queue
                thread.join()  # This makes sure we wait for the request to complete
                suggestions = suggestions_queue.get()

                # Yield all suggestions
                for suggestion in suggestions:
                    yield SearchResult(
                        description="search on DuckDuckGo",
                        fuzzy=False,
                        icon="internet-web-browser-symbolic",
                        id=f"https://duckduckgo.com/?q={suggestion['phrase']}",
                        offset=2,
                        plugin=self,
                        score=1,
                        title=f"open '{suggestion['phrase']}'"
                    )
