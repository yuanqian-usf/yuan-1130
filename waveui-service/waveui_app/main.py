from h2o_wave import Q, main, app, ui
import os
import httpx
import asyncio

FAST_API_ENDPOINT = os.environ.get('FAST_API_ENDPOINT', 'http://0.0.0.0:8080')
url = f'{FAST_API_ENDPOINT}/ner'
print("url", url)
_id = 0

# A simple class that represents a search response.
class search_resp:
    def __init__(self, input, result):
        global _id
        _id +=1
        self.id = f'search_{_id}'
        self.input = input
        self.result = result

@app('/ner')
async def serve(q: Q):
    if q.args.search_ner:  # Add an item.
        await search_ner(q)
    else:
        show_search_results(q)
    await q.page.save()

def show_search_results(q: Q):
    searches: List[search_resp] = q.user.searches

    if searches is None:
        q.user.searches = searches = []

    # Create checkboxes.
    search_results = [ui.text_l(f'key: {search.input} \n result: {search.result}') for search in searches]

    # Display list
    q.page['form'] = ui.form_card(box='1 1 4 8', items=[
        ui.text_l("What's new?"),
        ui.textbox(name='text', label='Name Entity Recognition', multiline=False),
        ui.buttons([ui.button(name='search_ner', label='Search', primary=True),
            ]),
        *search_results
    ])
    pass
    
async def search_ner(q: Q):
    if q.args.text is not None:
        data = {'input' : q.args.text}
        async with httpx.AsyncClient() as client:
            print("before post", data)
            r = await client.post(url, json=data)
            print("after post", r.json())
            q.user.searches.insert(0, search_resp(input=q.args.text, result = r.json()))
            show_search_results(q)
    pass